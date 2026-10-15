# Verification

## Automated quality gates

GitHub Actions runs the following checks on Python 3.10, 3.11, and 3.12:

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m pytest -q
```

## Unit-test coverage

The test suite validates:

- webcam/source parsing
- configuration schema validation
- bounding-box geometry helpers
- explicit selected-track visibility
- target-state serialization
- Ultralytics-result normalization using lightweight test doubles
- perception-snapshot serialization
- rolling performance metrics
- runtime health-state evaluation

## Performance verification

Use `scripts/benchmark.py` to record:

- measured frame count
- mean inference latency
- p95 inference latency
- approximate inference FPS
- model
- image size
- compute device

Performance comparisons should state the model format, input size, precision, hardware, and source pipeline.
