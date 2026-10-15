# Performance and Professional Project Results

## Original professional project

The resume-backed professional work reported:

- custom YOLO detectors trained on an aerial dataset of approximately **18,000 images**
- **mAP50 above 0.92** on custom aerial detectors
- **70+ FPS** on NVIDIA Jetson Orin NX in the project configuration
- **50+ FPS** low-latency inference on live UAV camera feeds

These figures belong to the original project environment.

## Why the public repository does not reproduce those numbers automatically

The public repository intentionally excludes:

- private training data
- production-trained weights
- exact camera/decoder configuration
- internal optimization settings
- proprietary source
- production hardware configuration files

For that reason, public users should benchmark their own selected model and hardware using:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

## Reporting rule

Only compare FPS or latency values when model format, input size, device, precision, and source pipeline are stated. This avoids misleading performance claims.
