# System Architecture

The repository implements the perception and software-interface portion of an aerial autonomous-system stack.

## Component model

| Component | Responsibility |
|---|---|
| Video source | Webcam, recorded video, or network stream |
| Detector | Class, confidence, and bounding-box inference |
| Multi-object tracker | Persistent object identity across frames |
| Result adapter | Normalize model-specific results |
| Track state | Typed ID, class, confidence, box, and selected-state metadata |
| Selected-track state | Explicit selected ID and visibility status |
| Perception snapshot | Serializable frame-level output contract |
| Runtime metrics | Rolling frame-time and FPS measurement |
| Health diagnostics | Basic runtime state derived from FPS and track count |
| Configuration | External runtime settings and schema validation |
| Integration boundary | Perception metadata exposed to visualization/telemetry consumers |

## Processing sequence

1. A source provides frames from a webcam, file, or network stream.
2. YOLO produces detections.
3. ByteTrack associates detections and maintains persistent IDs.
4. The result adapter converts tracker output into `TrackState` records.
5. The selected-track module checks whether an explicitly supplied ID is visible.
6. Runtime metrics and health status are updated.
7. A `PerceptionSnapshot` is emitted for JSON, visualization, or telemetry use.

## Design decisions

**Framework isolation.** Application state is represented with project-owned dataclasses rather than passing Ultralytics result objects throughout the codebase.

**Explicit selected-track state.** Track selection is supplied as an input; the repository does not implement autonomous target selection.

**Independent diagnostics.** Metrics and health logic are testable without loading a model or GPU runtime.

**Configurable inference.** Model path, input source, thresholds, image size, and compute device are runtime parameters.

**Measured performance.** Benchmark output is generated from the selected model, source, and device rather than hard-coded into the application.

## Scope boundary

Production flight-control, navigation, actuation, proprietary model artifacts, private datasets, and confidential deployment configuration are outside this repository. See [Repository Scope](public-scope.md).
