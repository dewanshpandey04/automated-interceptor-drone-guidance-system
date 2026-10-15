# Automated Interceptor Drone Guidance & Perception System

A public, portfolio-safe representation of the **computer-vision and software-integration work** I performed on an automated interceptor-drone project.

My work focused on the perception stack: live camera processing, custom YOLO detection, multi-object tracking, track-state handling, target-selection/lock-state visualization, edge-AI inference, performance measurement, and integration boundaries for the wider autonomous UAV software stack.

> This repository does not publish Vayuron proprietary source code, private datasets, model weights, credentials, flight-controller commands, navigation/control laws, or operational interception logic.

## My contribution

- Built real-time object-detection pipelines for aerial imagery using YOLO, PyTorch, and OpenCV.
- Integrated ByteTrack for persistent multi-object tracking across live video frames.
- Implemented reusable track-state structures for IDs, classes, confidence scores, and bounding boxes.
- Added target-selection / lock-state visualization at the perception layer without exposing vehicle-control logic.
- Structured the vision stack into testable modules for detection, tracking, state handling, configuration, metrics, and benchmarking.
- Worked with NVIDIA Jetson-class edge hardware for low-latency onboard inference.
- Added validation utilities and CI so the public implementation can be inspected like a real engineering project.

## Professional project results

The following figures describe the original professional project work and are **not claimed as reproducible from the public repository**, because the private dataset, trained model artifacts, and production hardware configuration are intentionally excluded.

| Result | Professional project |
|---|---:|
| Training dataset | ~18,000 aerial images |
| Detector performance | mAP50 above 0.92 on custom aerial detectors |
| Jetson Orin NX inference | 70+ FPS in the project configuration |
| Live edge inference | 50+ FPS on optimized live-camera pipelines |

## Technical stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · CUDA · NVIDIA Jetson · Edge AI**

## Repository structure

| Path | Purpose |
|---|---|
| `src/detect.py` | Real-time YOLO inference |
| `src/track.py` | YOLO + ByteTrack live tracking |
| `src/target_state.py` | Typed tracked-object state model |
| `src/metrics.py` | Runtime FPS / latency metrics |
| `src/config.py` | Configuration loading and validation |
| `config/` | Public-safe runtime configuration |
| `scripts/benchmark.py` | Reproducible inference benchmark utility |
| `tests/` | Unit tests for public modules |
| `docs/` | Architecture, verification, results, and code-tour notes |
| `.github/workflows/` | Automated CI checks |

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run detection:

```powershell
python src/detect.py --source 0 --show
```

Run multi-object tracking:

```powershell
python src/track.py --source 0 --show
```

Use a local custom model without committing the weight file:

```powershell
python src/track.py --model path\to\model.pt --source path\to\video.mp4 --show
```

Run unit tests:

```powershell
pytest -q
```

Run a local benchmark:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

## Engineering documentation

- [System architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Performance and results](docs/performance.md)
- [Verification approach](docs/verification.md)
- [Public / proprietary boundary](docs/public-scope.md)

## Branch strategy

- `main` — stable recruiter-facing portfolio version
- `develop` — development and integration work
- `docs` — documentation-focused changes

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems
