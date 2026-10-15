# Project evidence and implementation map

This portfolio repository demonstrates **perception and tracking software** related to GOBABYGO research. It does not publish operational interception guidance, vehicle control, or proprietary system integration.

| Work area | Public evidence | Verification |
| --- | --- | --- |
| Detection entry point | [`src/detect.py`](../src/detect.py) | CLI `python -m src.detect --help` |
| Multi-object tracking | [`src/track.py`](../src/track.py), [`src/result_adapter.py`](../src/result_adapter.py) | [Adapter tests](../tests/test_result_adapter.py) |
| Explicitly selected track status | [`src/lock_state.py`](../src/lock_state.py), [`src/target_state.py`](../src/target_state.py) | [Lock-state tests](../tests/test_lock_state.py) |
| Structured perception telemetry | [`src/interfaces.py`](../src/interfaces.py), [`src/pipeline.py`](../src/pipeline.py) | [Interface tests](../tests/test_interfaces.py) |
| Runtime diagnostics | [`src/metrics.py`](../src/metrics.py), [`src/health.py`](../src/health.py) | [Metrics](../tests/test_metrics.py) and [health tests](../tests/test_health.py) |
| Code quality and reproducibility | [`scripts/benchmark.py`](../scripts/benchmark.py), [CI](../.github/workflows/ci.yml) | Run `python -m pytest -q` and `ruff check .` |

## What this does not prove

- The selected-track state is an **explicit/manual track-ID selection**, not autonomous target selection.
- This repository does **not** implement or demonstrate autonomous flight, interception trajectories, actuation, or weapon integration.
- Original GOBABYGO, VTOL AI, and private detection-model code and trained weights are not included.
- Historical accuracy and FPS claims are not reproduced by this public repository; see [performance notes](performance.md).

## Reproduce the public portion

Follow the [quick start](../README.md#quick-start), run unit tests, then use an authorized test video to exercise the detection and tracking entry points. Publish performance numbers only alongside the exact hardware, model, resolution, input source, and measurement method.
