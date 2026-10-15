# Automated Interceptor Drone Guidance & Perception System

![CI](https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system/actions/workflows/ci.yml/badge.svg)

Real-time **computer-vision and perception software** for aerial object detection, multi-object tracking, target-state handling, selected-track lock state, runtime diagnostics, and edge-AI deployment.

**Python · PyTorch · YOLO · OpenCV · ByteTrack · CUDA · NVIDIA Jetson · GitHub Actions**

## Engineering highlights

- YOLO-based real-time aerial object detection
- ByteTrack persistent multi-object tracking
- Typed `TrackState` data model that decouples application code from model-specific results
- Explicit perception-layer selected-track / lock-state handling
- Serializable frame-level perception snapshots for telemetry and integration
- Rolling FPS and frame-time metrics
- Runtime health-state evaluation
- Webcam, recorded-video, and network-stream inputs
- CLI and YAML-driven runtime configuration
- Unit-tested reusable logic
- Automated syntax, lint, CLI-smoke, and test checks on Python 3.10, 3.11, and 3.12
- Human-readable and JSON inference benchmarking output

## System architecture

The perception pipeline is separated into independent stages:

1. **Video input** — webcam, file, or network stream
2. **Detection** — YOLO class, confidence, and bounding-box inference
3. **Tracking** — ByteTrack persistent track IDs
4. **State normalization** — model results converted into typed `TrackState` records
5. **Selected-track state** — explicit track ID visibility and lock-state management
6. **Diagnostics** — FPS, frame-time, and runtime health
7. **Output interface** — JSON-serializable perception snapshots for visualization and telemetry

The repository intentionally stops at the perception/software-interface boundary. Proprietary flight-control, navigation, actuation, production model weights, private datasets, and confidential deployment configuration are not distributed here.

## Target-locking subsystem

The target-locking code is limited to **perception-layer state management**. It supports explicit track selection, selected-ID persistence across frames, visibility status, and lock-state serialization.

It does not implement autonomous target selection, navigation/control laws, flight-controller commands, or actuation.

## Measured project results

The original project work included the following measured results:

| Metric | Result |
|---|---:|
| Training dataset | ~18,000 aerial images |
| Custom detector | mAP50 > 0.92 |
| Jetson Orin NX inference | 70+ FPS |
| Optimized live-camera pipeline | 50+ FPS |

These results refer to the original project environment. The production dataset, trained weights, hardware-specific optimization settings, and exact deployment configuration are not included in this repository.

## Repository structure

| Path | Responsibility |
|---|---|
| `src/detect.py` | YOLO detection entry point |
| `src/track.py` | YOLO + ByteTrack tracking |
| `src/pipeline.py` | Integrated perception, lock-state, metrics, and JSON output |
| `src/camera.py` | Frame-source abstraction |
| `src/target_state.py` | Typed tracked-object state |
| `src/lock_state.py` | Selected-track lock-state manager |
| `src/result_adapter.py` | Ultralytics result normalization |
| `src/interfaces.py` | Serializable perception snapshot |
| `src/metrics.py` | Rolling frame-time and FPS metrics |
| `src/health.py` | Runtime health evaluation |
| `src/config.py` | YAML configuration validation |
| `config/` | Example runtime configuration |
| `scripts/benchmark.py` | Inference benchmark utility |
| `tests/` | Unit tests |
| `docs/` | Architecture, verification, performance, and scope notes |
| `pyproject.toml` | Test and lint configuration |

## Setup

```powershell
git clone https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system.git
cd automated-interceptor-drone-guidance-system

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For development and repository quality checks:

```powershell
pip install -r requirements-dev.txt
```

> NVIDIA Jetson deployments may require the JetPack-compatible PyTorch build provided for the target platform.

## Usage

Detection:

```powershell
python -m src.detect --source 0 --show
```

Multi-object tracking:

```powershell
python -m src.track --source 0 --show
```

Integrated perception pipeline with an explicitly selected track ID:

```powershell
python -m src.pipeline --source 0 --selected-track-id 7 --show --emit-json
```

Run from the example YAML configuration:

```powershell
python -m src.pipeline --config config\config.example.yaml --show
```

CLI values such as `--model`, `--source`, `--conf`, and `--imgsz` override the corresponding config values when supplied.

Local custom model:

```powershell
python -m src.pipeline --model path\to\model.pt --source path\to\video.mp4 --show
```

## Quality checks

Run the same lightweight checks used by GitHub Actions:

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m src.detect --help
python -m src.track --help
python -m src.pipeline --help
python -m pytest -q
```

CI runs these checks on **Python 3.10, 3.11, and 3.12**.

## Benchmarking

Human-readable output:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

Machine-readable output:

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4 --json
```

The benchmark reports measured frames, mean inference latency, p95 inference latency, and approximate inference FPS. Performance comparisons should state the model, input size, precision, hardware, and video pipeline.

## Documentation

- [Architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Performance](docs/performance.md)
- [Verification](docs/verification.md)
- [Repository scope](docs/public-scope.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Branches

- `main` — stable branch
- `develop` — development and integration
- `docs` — documentation work

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems  
[LinkedIn](https://www.linkedin.com/in/dewansh-pandey-9b564a317) · [GitHub](https://github.com/dewanshpandey04)
