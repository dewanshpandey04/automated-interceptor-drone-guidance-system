# System Architecture

The public repository represents the **perception and software-integration layer** of the original project. The production system contained additional proprietary autonomous-system components that are intentionally not published here.

## Component model

| Component | Responsibility | Public implementation |
|---|---|---|
| Frame source | Webcam, video, or network-stream acquisition | Yes |
| Detection | Class, confidence, and bounding-box inference | Yes |
| Multi-object tracking | Persistent identity across frames | Yes |
| Result adapter | Convert model-specific results into stable state objects | Yes |
| Track state | Typed per-track metadata | Yes |
| Lock state | Explicit/manual selected-track state and visibility status | Yes, state/visualization only |
| Perception snapshot | Serializable frame-level integration contract | Yes |
| Runtime metrics | FPS and frame-time measurement | Yes |
| Health diagnostics | Basic runtime status | Yes |
| Configuration | External model/source/runtime settings | Yes |
| Autonomous-stack handoff | Public software interface boundary | Interface only |
| Flight control / navigation | Guidance, actuation, control laws | No |
| Operational interception behavior | Production interception implementation | No |

## Public processing sequence

1. A webcam, video, or stream source produces frames.
2. YOLO produces class/confidence/bounding-box detections.
3. ByteTrack maintains persistent IDs.
4. The result adapter converts tracker output to typed `TrackState` records.
5. An explicitly selected track ID can be represented by the public lock-state module.
6. Metrics and health information are generated independently.
7. State can be serialized for visualization or telemetry through the perception interface.

## Design decisions

**Separation of concerns.** Acquisition, inference, tracking, state representation, selected-track state, metrics, and interfaces are separate modules.

**Explicit public selection.** The portfolio code does not automatically choose an object for interception. Selected-track state is supplied explicitly for visualization and interface testing.

**Model independence.** Scripts accept a runtime model path rather than embedding a private model artifact.

**Safe integration boundary.** The repository stops at perception metadata and interface contracts. It does not publish control, navigation, or operational interception code.

**Reproducible measurement.** Benchmarks report timing for the exact model, source, and hardware used by the reviewer.

## Deployment context

The professional project used NVIDIA Jetson hardware for edge inference. Hardware-specific optimizations, production-trained weights, private camera configuration, and proprietary deployment settings are excluded.
