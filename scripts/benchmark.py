from __future__ import annotations

import argparse
import json
import statistics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Measure YOLO inference latency.")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", required=True)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--device", default=None)
    parser.add_argument("--max-frames", type=int, default=300)
    parser.add_argument("--json", action="store_true", help="Emit benchmark results as JSON.")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    from ultralytics import YOLO

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
    ordered = sorted(samples)
    p95_ms = ordered[max(0, int(len(ordered) * 0.95) - 1)]
    approx_fps = 1000.0 / mean_ms

    payload = {
        "frames_measured": len(samples),
        "mean_inference_ms": round(mean_ms, 3),
        "p95_inference_ms": round(p95_ms, 3),
        "approx_inference_fps": round(approx_fps, 2),
        "model": args.model,
        "image_size": args.imgsz,
        "device": args.device,
    }

    if args.json:
        print(json.dumps(payload, separators=(",", ":")))
        return

    print(f"Frames measured : {payload['frames_measured']}")
    print(f"Mean inference  : {payload['mean_inference_ms']:.3f} ms")
    print(f"P95 inference   : {payload['p95_inference_ms']:.3f} ms")
    print(f"Approx. FPS     : {payload['approx_inference_fps']:.2f}")


if __name__ == "__main__":
    main()
