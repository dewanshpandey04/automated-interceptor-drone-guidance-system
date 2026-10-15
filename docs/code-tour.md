# Code Tour

## `src/detect.py`

Command-line entry point for real-time YOLO inference. Model path, source, confidence threshold, image size, compute device, and display/save behavior are runtime arguments.

## `src/track.py`

Runs YOLO with ByteTrack and exposes persistent track IDs. An optional explicit track ID can be used to visualize selected-track visibility.

## `src/pipeline.py`

Integrates detection, tracking, normalized state, selected-track state, rolling metrics, runtime health, JSON metadata output, and visualization.

## `src/camera.py`

Provides a small frame-source abstraction for webcam, file, or network video input.

## `src/target_state.py`

Defines the typed `TrackState` model used by downstream perception code.

## `src/lock_state.py`

Maintains the explicitly selected track ID and reports whether it is visible in the current frame.

## `src/result_adapter.py`

Converts Ultralytics tracking results into stable `TrackState` objects so higher-level modules are not coupled directly to framework-specific result structures.

## `src/interfaces.py`

Defines `PerceptionSnapshot`, a serializable frame-level contract containing timestamp, FPS, selected-track ID, and tracked-object state.

## `src/metrics.py`

Maintains a rolling window of frame times and exposes mean frame time and approximate FPS.

## `src/health.py`

Maps runtime FPS and visible-track count to a small diagnostic health state.

## `src/config.py`

Loads and validates the YAML runtime configuration schema.

## `scripts/benchmark.py`

Collects model inference timings and reports mean latency, p95 latency, and approximate inference FPS.

## `tests/`

Covers parsing, configuration validation, target state, selected-track state, result normalization, interfaces, runtime health, and performance metrics.

## Design intent

The source tree separates inference, tracking, state models, diagnostics, configuration, and integration contracts so reusable logic can be tested independently from GPU inference.
