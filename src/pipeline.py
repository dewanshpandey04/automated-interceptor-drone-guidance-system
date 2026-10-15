from __future__ import annotations

import argparse
import json
import time

import cv2
from ultralytics import YOLO

from lock_state import TargetLockState
from result_adapter import track_states_from_result
from utils import parse_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Public-safe perception pipeline: detection, tracking, and lock-state visualization."
    )
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", default="0")
    parser.add_argument("--tracker", default="bytetrack.yaml")
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--device", default=None)
    parser.add_argument("--selected-track-id", type=int, default=None)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--emit-json", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    model = YOLO(args.model)
    lock = TargetLockState()

    if args.selected_track_id is not None:
        lock.select(args.selected_track_id)

    results = model.track(
        source=parse_source(args.source),
        tracker=args.tracker,
        persist=True,
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        stream=True,
        verbose=False,
    )

    previous = time.perf_counter()

    for result in results:
        now = time.perf_counter()
        fps = 1.0 / max(now - previous, 1e-9)
        previous = now

        track_ids = []
        if result.boxes is not None and result.boxes.id is not None:
            track_ids = [int(v) for v in result.boxes.id.cpu().tolist()]

        lock.update_visible_tracks(track_ids)
        states = track_states_from_result(result, lock.selected_track_id)

        if args.emit_json:
            payload = {
                "fps": round(fps, 2),
                "lock": lock.as_dict(),
                "tracks": [state.as_dict() for state in states],
            }
            print(json.dumps(payload, separators=(",", ":")))

        if args.show:
            frame = result.plot()
            cv2.putText(
                frame,
                f"FPS {fps:.1f} | Tracks {len(states)} | Lock {lock.status}",
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
                    f"Selected track: {lock.selected_track_id}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )
            cv2.imshow("Public Perception Pipeline", frame)
            if cv2.waitKey(1) & 0xFF in (27, ord("q")):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
