from __future__ import annotations

import argparse

from src.utils import parse_source


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Real-time YOLO detection.")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", default="0", help="Webcam index, image/video path, or stream URL.")
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--device", default=None)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--save", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    from ultralytics import YOLO

    cv2 = None
    if args.show:
        import cv2 as cv2_module

        cv2 = cv2_module

    model = YOLO(args.model)
    results = model.predict(
        source=parse_source(args.source),
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        stream=True,
        save=args.save,
        verbose=False,
    )

    for result in results:
        if not args.show:
            continue

        frame = result.plot()
        cv2.imshow("Perception - Detection", frame)
        if cv2.waitKey(1) & 0xFF in (27, ord("q")):
            break

    if cv2 is not None:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
