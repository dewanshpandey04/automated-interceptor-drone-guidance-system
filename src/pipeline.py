from __future__ import annotations

import argparse
import json
import time
from typing import Any

from src.config import load_config
from src.health import evaluate_health
from src.interfaces import PerceptionSnapshot
from src.lock_state import TargetLockState
from src.metrics import RuntimeMetrics
from src.result_adapter import track_states_from_result
from src.utils import parse_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Detection, tracking, selected-track state, and perception telemetry."
    )
    parser.add_argument("--config", default=None, help="Optional YAML runtime configuration.")
    parser.add_argument("--model", default=None)
    parser.add_argument("--source", default=None)
    parser.add_argument("--tracker", default=None)
    parser.add_argument("--conf", type=float, default=None)
    parser.add_argument("--imgsz", type=int, default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--selected-track-id", type=int, default=None)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--emit-json", action="store_true")
    return parser


def _section(config: dict[str, Any], name: str) -> dict[str, Any]:
    value = config.get(name, {})
    return value if isinstance(value, dict) else {}


def main() -> None:
    args = build_parser().parse_args()
    config = load_config(args.config) if args.config else {}

    camera = _section(config, "camera")
    detection = _section(config, "detection")
    tracking = _section(config, "tracking")

    model_path = args.model or detection.get("model", "yolo11n.pt")
    source = parse_source(args.source if args.source is not None else camera.get("source", 0))
    tracker = args.tracker or tracking.get("tracker", "bytetrack.yaml")
    conf = args.conf if args.conf is not None else float(detection.get("confidence_threshold", 0.35))
    imgsz = args.imgsz if args.imgsz is not None else int(detection.get("image_size", 640))

    from ultralytics import YOLO

    cv2 = None
    if args.show:
        import cv2 as cv2_module

        cv2 = cv2_module

    model = YOLO(model_path)
    lock = TargetLockState()
    metrics = RuntimeMetrics(window=60)

    if args.selected_track_id is not None:
        lock.select(args.selected_track_id)

    results = model.track(
        source=source,
        tracker=tracker,
        persist=True,
        conf=conf,
        imgsz=imgsz,
        device=args.device,
        stream=True,
        verbose=False,
    )

    previous = time.perf_counter()

    for frame_id, result in enumerate(results, start=1):
        now = time.perf_counter()
        metrics.add_frame_time_ms((now - previous) * 1000.0)
        previous = now

        track_ids: list[int] = []
        if result.boxes is not None and result.boxes.id is not None:
            track_ids = [int(v) for v in result.boxes.id.cpu().tolist()]

        lock.update_visible_tracks(track_ids)
        states = track_states_from_result(result, lock.selected_track_id)
        health = evaluate_health(metrics.fps, len(states))

        snapshot = PerceptionSnapshot(
            frame_id=frame_id,
            captured_at=time.time(),
            fps=metrics.fps,
            tracks=states,
            selected_track_id=lock.selected_track_id,
        )

        if args.emit_json:
            payload = {
                "perception": snapshot.as_dict(),
                "lock": lock.as_dict(),
                "health": health.as_dict(),
            }
            print(json.dumps(payload, separators=(",", ":")))

        if args.show:
            frame = result.plot()
            cv2.putText(
                frame,
                f"FPS {metrics.fps:.1f} | Tracks {len(states)} | Health {health.status}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )
            if lock.selected_track_id is not None:
                cv2.putText(
                    frame,
                    f"Selected track: {lock.selected_track_id} | {lock.status}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )
            cv2.imshow("Perception Pipeline", frame)
            if cv2.waitKey(1) & 0xFF in (27, ord("q")):
                break

    if cv2 is not None:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
