# Automated Interceptor Drone Guidance & Perception System

![CI](https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system/actions/workflows/ci.yml/badge.svg)

A public, portfolio-safe representation of the **computer-vision and software-integration work** I performed on an automated interceptor-drone project.

My work focused on the perception and integration layers: live camera processing, custom YOLO detection, multi-object tracking, track-state handling, **perception-layer target locking**, **automated interception pipeline integration**, edge-AI inference, performance measurement, and clean software boundaries for the wider autonomous UAV stack.

> This repository does not publish Vayuron proprietary source code, private datasets, model weights, credentials, flight-controller commands, navigation/control laws, actuation logic, or operational interception behavior.

## My contribution

- Built real-time object-detection pipelines for aerial imagery using YOLO, PyTorch, and OpenCV.
- Integrated ByteTrack for persistent multi-object tracking across live video frames.
- Implemented reusable track-state structures for IDs, classes, confidence scores, and bounding boxes.
- Developed a perception-layer target-locking workflow that maintains selected-track / lock-state metadata across frames.
- Exposed target-lock state through a clean software interface for visualization, telemetry, and wider autonomous-system integration.
- Contributed to the **automated interception pipeline** by connecting camera perception, detection, tracking, target-state handling, and target-locking components through modular software interfaces.
- Structured perception outputs so downstream autonomy components could consume stable state data without depending directly on raw detector outputs.
- Kept perception, integration interfaces, and vehicle-control implementation separated so modules remained testable and maintainable.
- Worked with NVIDIA Jetson-class edge hardware for low-latency onboard inference.
- Added validation utilities and CI so the public implementation can be inspected like a real engineering project.

## Automated Interception Pipeline

The professional system used a modular interception pipeline in which multiple software components were connected through clear interfaces.

At a high level, the public-facing portion covers:

- live camera / video acquisition
- real-time object detection
- multi-object tracking with persistent IDs
- target-state representation
- perception-layer target locking
- telemetry and visualization outputs
- software handoff to the wider autonomous UAV stack

The public repository demonstrates the **perception and software-integration side of that pipeline only**. It intentionally excludes proprietary guidance algorithms, flight-control commands, navigation/control laws, actuation logic, and operational interception behavior.

## Target-Locking System

The target-locking code in this public repository is deliberately limited to **manual selected-track state and visualization**.

It demonstrates:

- maintaining a selected track ID across frames
- reporting whether the selected track is currently visible
- attaching lock-state metadata to a tracked-object representation
- exposing that state through a serializable perception interface
- keeping lock-state handling independent from vehicle-control logic

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

## Source code

| Path | Purpose |
|---|---|
| `src/camera.py` | Webcam / video / network-stream frame acquisition wrapper |
| `src/detect.py` | Real-time YOLO inference |
| `src/track.py` | YOLO + ByteTrack tracking with explicit selected-track visualization |
| `src/pipeline.py` | Integrated public perception pipeline |
| `src/target_state.py` | Typed tracked-object state |
| `src/lock_state.py` | Manual perception-layer lock-state manager |
| `src/result_adapter.py` | Converts model/tracker results into stable track-state objects |
| `src/interfaces.py` | Serializable perception snapshot contract |
| `src/metrics.py` | Rolling FPS / latency metrics |
| `src/health.py` | Runtime health/status evaluation |
| `src/config.py` | YAML configuration loading and validation |
| `scripts/benchmark.py` | Reproducible inference benchmark |
| `tests/` | Unit tests for state, interfaces, metrics, health, and utilities |
| `models/README.md` | Model-artifact policy |
| `docs/` | Architecture, verification, performance, and code-tour notes |

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Detection:

```powershell
python src/detect.py --source 0 --show
```

Tracking:

```powershell
python src/track.py --source 0 --show
```

Public integrated pipeline with a manually selected track ID:

```powershell
python src/pipeline.py --source 0 --selected-track-id 7 --show --emit-json
```

Use a local model without committing the weight file:

```powershell
python src/pipeline.py --model path\to\model.pt --source path\to\video.mp4 --show
```

Run tests:

```powershell
pytest -q
```

Run a benchmark:

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
