from __future__ import annotations

import argparse
import time

import cv2
from ultralytics import YOLO

from utils import nearest_track_to_center, parse_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="YOLO + ByteTrack tracking demo.")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", default="0")
    parser.add_argument("--tracker", default="bytetrack.yaml")
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--device", default=None)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--save", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    model = YOLO(args.model)

    results = model.track(
        source=parse_source(args.source),
        tracker=args.tracker,
        persist=True,
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        stream=True,
        save=args.save,
        verbose=False,
    )

    previous = time.perf_counter()

    for result in results:
        now = time.perf_counter()
        fps = 1.0 / max(now - previous, 1e-9)
        previous = now

        frame = result.plot()
        track_ids: list[int] = []
        boxes: list[list[float]] = []

        if result.boxes is not None:
            if result.boxes.id is not None:
                track_ids = [int(v) for v in result.boxes.id.cpu().tolist()]
            if result.boxes.xyxy is not None:
                boxes = result.boxes.xyxy.cpu().tolist()

        visual_lock_id = nearest_track_to_center(
            track_ids, boxes, frame.shape[1], frame.shape[0]
        )

        cv2.putText(
            frame,
            f"FPS {fps:.1f} | Tracks {len(track_ids)}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        if visual_lock_id is not None:
            cv2.putText(
                frame,
                f"Selected track: {visual_lock_id}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

        if args.show:
            cv2.imshow("Perception - Tracking", frame)
            if cv2.waitKey(1) & 0xFF in (27, ord("q")):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
