# Automated Interceptor Drone Guidance & Perception System

Public, portfolio-safe reconstruction of the **perception and software-integration layers** of an automated interceptor-drone project I worked on.

The original engineering work included real-time aerial object detection, multi-object tracking, target-state handling, target-locking workflows, live camera processing, edge-AI inference, and integration with an autonomous UAV software stack.

> **IP / safety note:** this repository does **not** contain Vayuron proprietary source code, private datasets, credentials, flight-controller commands, navigation/control laws, or operational interception/engagement logic. It demonstrates the computer-vision and software-engineering work with public tooling and safe demo interfaces.

## What this repository demonstrates

- Real-time YOLO object detection
- ByteTrack multi-object tracking
- Persistent track IDs and track-state representation
- Target-lock **visualization/state management only**
- Live webcam, video, and network-stream input
- FPS and inference-latency measurement
- Modular perception-to-autonomous-system interface design
- Edge-AI deployment structure for NVIDIA Jetson-class hardware
- Unit tests and validation utilities

## Tech stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · CUDA · NVIDIA Jetson · Edge AI**

## High-level architecture

```text
Camera / Video / Stream
          |
          v
    Frame Acquisition
          |
          v
     YOLO Detector
          |
          v
   ByteTrack Tracker
          |
          v
 Track State / Lock State
          |
          v
 Perception Interface Layer
      /             \
     v               v
Telemetry / HUD   Autonomous-System API
```

See [docs/architecture.md](docs/architecture.md) for the public-safe architecture.

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

Use your own local model without committing weights:

```powershell
python src/track.py --model path\to\model.pt --source path\to\video.mp4 --show
```

## Repository layout

```text
config/                  Public configuration template
docs/                    Architecture and verification notes
scripts/                 Benchmark utilities
src/                     Detection, tracking, state and utilities
tests/                   Unit tests
.github/workflows/       CI
```

## Branches

- `main` — stable portfolio version
- `develop` — development/integration branch
- `docs` — documentation-focused branch

## Engineering context

This public repository is designed so a recruiter or engineer can inspect how the perception stack is organized, how detection/tracking outputs are represented, how components are tested, and how performance is measured—without exposing company IP.

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems
