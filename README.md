# Automated Interceptor Drone Guidance & Perception System

![CI](https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system/actions/workflows/ci.yml/badge.svg)

## Overview

Reference implementation of the **perception and software-integration layer** used in an automated interceptor UAV system.

The repository focuses on real-time camera ingestion, YOLO-based object detection, ByteTrack multi-object tracking, target-state representation, explicit target-lock state, runtime diagnostics, and clean interfaces between perception and the wider autonomous system.

Production guidance, control, navigation, actuation, proprietary model artifacts, private datasets, and confidential deployment configuration are not included.

## Key capabilities

- Real-time YOLO object detection
- ByteTrack multi-object tracking
- Persistent track IDs
- Typed target-state representation
- Explicit/manual selected-track lock state
- JSON perception metadata output
- FPS and runtime-health monitoring
- Webcam, video, and network-stream input
- Configurable model/source/runtime settings
- Unit tests and GitHub Actions CI
- Reproducible inference benchmarking

## Automated interception pipeline

The perception side of the system is organized as independent stages:

1. frame acquisition
2. object detection
3. multi-object tracking
4. target-state normalization
5. selected-track / lock-state management
6. telemetry and visualization output
7. interface handoff to the wider autonomous UAV stack

This separation keeps detection, tracking, state handling, diagnostics, and integration testable as independent modules.

## Target-locking subsystem

The target-locking implementation in this repository is limited to **perception-layer state management**.

It supports:

- selecting a track ID explicitly
- maintaining the selected ID across frames
- reporting whether the selected track is currently visible
- marking the corresponding `TrackState` as locked
- exposing lock state through a serializable interface

It does not contain autonomous target-selection logic, flight-control commands, navigation laws, or actuation code.

## Project results

The original project work included:

| Metric | Result |
|---|---:|
| Training dataset | ~18,000 aerial images |
| Custom detector | mAP50 > 0.92 |
| Jetson Orin NX inference | 70+ FPS |
| Optimized live-camera pipeline | 50+ FPS |

These results refer to the original project configuration. The private dataset, production weights, and exact deployment configuration are not distributed with this repository.

## Tech stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · CUDA · NVIDIA Jetson · Edge AI**

## Repository structure

| Path | Purpose |
|---|---|
| `src/camera.py` | Frame acquisition |
| `src/detect.py` | YOLO detection entry point |
| `src/track.py` | YOLO + ByteTrack tracking |
| `src/pipeline.py` | Integrated perception pipeline |
| `src/target_state.py` | Typed tracked-object state |
| `src/lock_state.py` | Selected-track lock-state manager |
| `src/result_adapter.py` | Tracker-result normalization |
| `src/interfaces.py` | Serializable perception snapshot |
| `src/metrics.py` | Rolling FPS / latency metrics |
| `src/health.py` | Runtime health evaluation |
| `src/config.py` | YAML configuration loader |
| `scripts/benchmark.py` | Inference benchmark |
| `tests/` | Unit tests |
| `docs/` | Architecture and engineering notes |

## Installation

```powershell
git clone https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system.git
cd automated-interceptor-drone-guidance-system

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

Detection:

```powershell
python src/detect.py --source 0 --show
```

Tracking:

```powershell
python src/track.py --source 0 --show
```

Integrated perception pipeline with an explicitly selected track:

```powershell
python src/pipeline.py --source 0 --selected-track-id 7 --show --emit-json
```

Custom local model:

```powershell
python src/pipeline.py --model path\to\model.pt --source path\to\video.mp4 --show
```

## Testing

```powershell
pytest -q
```

## Benchmarking

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

## Documentation

- [Architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Performance](docs/performance.md)
- [Verification](docs/verification.md)
- [Repository scope](docs/public-scope.md)

## Branches

- `main` — stable branch
- `develop` — development and integration
- `docs` — documentation work

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems  
[LinkedIn](https://www.linkedin.com/in/dewansh-pandey-9b564a317) · [GitHub](https://github.com/dewanshpandey04)
