# Code Tour

This page is intended for reviewers who want to understand the repository quickly.

## `src/camera.py`

Wraps webcam, recorded-video, and network-stream input behind a small frame-packet interface.

## `src/detect.py`

Command-line entry point for real-time YOLO inference. The model path, source, confidence threshold, image size, device, and display/save behavior are runtime arguments.

## `src/track.py`

Runs YOLO with ByteTrack and exposes persistent IDs. Selected-track visualization is explicit/manual; the public code does not perform autonomous target selection.

## `src/pipeline.py`

Combines detection, ByteTrack tracking, selected-track state, JSON metadata output, and visualization into one public-safe perception demo.

## `src/target_state.py`

Defines a typed tracked-object state so downstream code does not depend directly on Ultralytics result objects.

## `src/lock_state.py`

Maintains perception-layer selected-track state and reports whether that explicitly selected ID is visible in the current frame.

## `src/result_adapter.py`

Converts Ultralytics tracker results into stable `TrackState` objects.

## `src/interfaces.py`

Defines a serializable `PerceptionSnapshot` contract for visualization, telemetry, or other non-control integration layers.

## `src/metrics.py`

Implements rolling FPS and frame-time metrics independently from the inference engine.

## `src/health.py`

Produces a small runtime health status from FPS and visible-track counts.

## `src/config.py`

Loads and validates the public YAML configuration template.

## `scripts/benchmark.py`

Measures model inference timing for the exact model/source/device chosen by the reviewer.

## `tests/`

Contains pure-Python unit tests for parsing, geometry, selected-track state, track serialization, interfaces, runtime health, and performance metrics.

## Why the repository is structured this way

The goal is to show production-oriented habits: small modules, explicit data contracts, configuration outside source, tests for reusable logic, and a documented boundary between public perception code and private production integration.
