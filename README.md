# Automated Interception — AI Perception & Tracking

**Python · YOLO · ByteTrack · OpenCV · Pytest**

Public, inspectable computer-vision components from an automated-interception research portfolio: object detection, multi-object tracking, explicit selected-track lock state, structured perception output, and runtime diagnostics.

**Scope:** This repository implements perception and software interfaces, **not** autonomous interception guidance, vehicle control, or actuation. Proprietary company code, trained weights, and private datasets are excluded.

## Quick start

Python 3.10+:

```bash
git clone https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system.git
cd automated-interceptor-drone-guidance-system
python -m venv .venv
python -m pip install -r requirements.txt
python -m src.detect --source 0 --show
```

Activate the virtual environment before installing dependencies on your OS. The default Ultralytics model may download on first use.

## Run

| Command | Purpose |
| --- | --- |
| `python -m src.detect --source 0 --show` | Webcam detection |
| `python -m src.track --source 0 --show` | Detection and ByteTrack tracking |
| `python -m src.pipeline --source 0 --show --emit-json` | Tracking, health metrics, and JSON perception output |
| `python -m src.pipeline --source 0 --selected-track-id 7 --show` | Display state for an explicitly selected track ID |
| `python scripts/benchmark.py --model yolo11n.pt --source video.mp4` | Measure inference latency |

The selected-track state indicates whether a user-specified track ID is visible; it is not autonomous target selection.

## Code map

| Location | Responsibility |
| --- | --- |
| [`src/detect.py`](src/detect.py), [`src/track.py`](src/track.py) | YOLO detection and tracking entry points |
| [`src/pipeline.py`](src/pipeline.py) | Perception output and diagnostics |
| [`src/lock_state.py`](src/lock_state.py), [`src/target_state.py`](src/target_state.py) | Selected-track status and typed track records |
| [`src/result_adapter.py`](src/result_adapter.py), [`src/interfaces.py`](src/interfaces.py) | Normalized results and serializable snapshots |
| [`src/config.py`](src/config.py), [`config/`](config/) | Runtime configuration |
| [`tests/`](tests/), [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Tests and automated checks |

## Verify

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
ruff check .
```

## Documentation

[Architecture](docs/architecture.md) · [Code tour](docs/code-tour.md) · [Verification](docs/verification.md) · [Performance](docs/performance.md) · [Public scope](docs/public-scope.md)

Historical project accuracy and FPS claims are discussed in [performance notes](docs/performance.md); they are not independently reproduced by the public repository.

**Author:** [Dewansh Pandey](https://github.com/dewanshpandey04)
