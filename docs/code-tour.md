# Code Tour

This page is intended for reviewers who want to understand the repository quickly.

## `src/detect.py`

Command-line entry point for real-time YOLO inference. The model path, source, confidence threshold, image size, device, and display/save behavior are runtime arguments.

## `src/track.py`

Runs YOLO with ByteTrack and extracts persistent IDs and boxes. The public implementation includes selected-track visualization only; it does not contain vehicle-control or guidance logic.

## `src/target_state.py`

Defines a small typed track-state object so downstream code does not depend directly on Ultralytics result objects.

## `src/metrics.py`

Implements rolling FPS and frame-time metrics independently from the inference engine. This makes performance reporting testable without requiring a GPU.

## `src/config.py`

Loads and validates the public YAML configuration template.

## `scripts/benchmark.py`

Measures model inference timing for the exact model/source/device chosen by the reviewer.

## `tests/`

Contains pure-Python unit tests for input parsing, box geometry, track selection, state serialization, and runtime metrics.

## Why the repository is structured this way

The goal is to show production-oriented habits: small modules, explicit data contracts, configuration outside source, tests for reusable logic, and a documented boundary between public perception code and private production integration.
