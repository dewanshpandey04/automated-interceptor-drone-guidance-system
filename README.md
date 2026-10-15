# Automated Interceptor Drone Guidance & Perception System

![CI](https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system/actions/workflows/ci.yml/badge.svg)

A public, portfolio-safe representation of the **computer-vision, target-state, trajectory-integration, and software-integration work** I performed on an automated interceptor-drone project.

My work focused on the perception stack: live camera processing, custom YOLO detection, multi-object tracking, track-state handling, **perception-layer target locking**, **automated trajectory-planning integration**, edge-AI inference, performance measurement, and integration boundaries for the wider autonomous UAV software stack.

> This repository does not publish Vayuron proprietary source code, private datasets, model weights, credentials, flight-controller commands, navigation/control laws, proprietary trajectory-generation algorithms, or operational interception logic.

## My contribution

- Built real-time object-detection pipelines for aerial imagery using YOLO, PyTorch, and OpenCV.
- Integrated ByteTrack for persistent multi-object tracking across live video frames.
- Implemented reusable track-state structures for IDs, classes, confidence scores, and bounding boxes.
- Developed a perception-layer target-locking workflow that maintains selected-track / lock-state metadata across frames.
- Exposed target-lock state through a clean software interface for visualization, telemetry, and integration with the wider autonomous system.
- Worked on the software handoff between target-state estimation and the autonomous trajectory-generation / path-planning layer.
- Structured perception outputs so downstream autonomy modules could consume stable target-state data without depending directly on raw detector outputs.
- Kept perception, trajectory-integration interfaces, and vehicle-control implementation separated so modules remained testable and maintainable.
- Structured the vision stack into testable modules for detection, tracking, state handling, configuration, metrics, and benchmarking.
- Worked with NVIDIA Jetson-class edge hardware for low-latency onboard inference.
- Added validation utilities and CI so the public implementation can be inspected like a real engineering project.

## Target-Locking System

The target-locking work sat inside the **perception layer** of the project.

Its software responsibilities included:

- maintaining a selected target's identity using the active tracking state
- carrying selected-track / lock-state metadata across consecutive video frames
- keeping target-state information separate from raw detector outputs
- presenting lock status to visualization / telemetry layers
- providing a defined perception interface for the larger autonomous software stack

## Automated Trajectory Integration

The wider professional system also included an **automated trajectory-planning layer**. My portfolio describes the integration at a high level:

- target-state estimation was prepared in a stable, reusable software representation
- selected-track state was exposed to downstream autonomy modules
- the perception-to-autonomy interface separated computer-vision outputs from trajectory-generation and vehicle-control code
- trajectory-related processing was treated as a distinct subsystem so perception, planning, and control could be developed and tested independently

The public repository intentionally stops at this software boundary. It does **not** contain proprietary trajectory algorithms, flight-control commands, navigation/control laws, actuation logic, or operational interception behavior.

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
| `src/target_state.py` | Typed tracked-object and lock-state representation |
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
[LinkedIn](https://www.linkedin.com/in/dewansh-pandey-9b564a317) · [GitHub](https://github.com/dewanshpandey04)
