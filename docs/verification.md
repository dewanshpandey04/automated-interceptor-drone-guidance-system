# Verification Notes

The public project is structured around checks that demonstrate software quality without exposing proprietary data.

## Functional checks

- numeric webcam inputs are parsed correctly
- bounding-box centers are computed deterministically
- visible-track selection is stable for known inputs
- track-state objects serialize to a predictable schema
- detector/tracker scripts accept file, webcam, and stream-style sources

## Performance checks

Use `scripts/benchmark.py` on hardware you control to record:

- mean inference latency
- p95 inference latency
- approximate inference FPS
- model name
- image size
- device

Do not present benchmark numbers as production results unless they were measured on the stated hardware and configuration.
