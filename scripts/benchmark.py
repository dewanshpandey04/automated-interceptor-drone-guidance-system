from __future__ import annotations

import argparse
import statistics

from ultralytics import YOLO


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure YOLO inference latency.")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", required=True)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--device", default=None)
    parser.add_argument("--max-frames", type=int, default=300)
    args = parser.parse_args()

    model = YOLO(args.model)
    samples: list[float] = []

    results = model.predict(
        source=args.source,
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        stream=True,
        verbose=False,
    )

    for index, result in enumerate(results, start=1):
        inference_ms = (result.speed or {}).get("inference")
        if inference_ms is not None:
            samples.append(float(inference_ms))
        if index >= args.max_frames:
            break

    if not samples:
        raise SystemExit("No timing data produced.")

    mean_ms = statistics.mean(samples)
    p95_ms = sorted(samples)[max(0, int(len(samples) * 0.95) - 1)]

    print(f"Frames measured : {len(samples)}")
    print(f"Mean inference  : {mean_ms:.2f} ms")
    print(f"P95 inference   : {p95_ms:.2f} ms")
    print(f"Approx. FPS     : {1000.0 / mean_ms:.2f}")


if __name__ == "__main__":
    main()
