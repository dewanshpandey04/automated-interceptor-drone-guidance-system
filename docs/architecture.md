# System Architecture

The public repository represents the **perception and software-integration layer** of the original project. The production system contained additional proprietary autonomous-system components that are intentionally not published here.

## Component model

| Component | Responsibility | Public implementation |
|---|---|---|
| Video input | Accept webcam, recorded video, or network-stream sources | Yes |
| Detection | Produce class, confidence, and bounding-box outputs | Yes |
| Multi-object tracking | Associate detections over time and maintain IDs | Yes |
| Track state | Normalize per-track metadata for downstream consumers | Yes |
| Selection / lock state | Maintain a perception-layer selected-track state for visualization | Yes, visualization/state only |
| Runtime metrics | Measure FPS and inference timing | Yes |
| Configuration | Externalize model/source/runtime settings | Yes |
| Perception interface | Define the boundary to the larger autonomous stack | Interface only |
| Flight control / navigation | Vehicle guidance, actuation, control laws | No |
| Operational interception logic | Production decision / engagement implementation | No |

## Data contract

Detection and tracking outputs are normalized into small Python data structures before downstream use. This keeps the vision model implementation separate from UI, telemetry, and integration code.

A typical tracked-object record contains:

- persistent track ID
- class label
- confidence score
- bounding box coordinates
- optional selected / lock-state flag

## Design decisions

**Separation of concerns.** Detection, tracking, state representation, configuration, and metrics live in separate modules so they can be tested independently.

**Model independence.** Public scripts accept an Ultralytics model path at runtime rather than hard-coding a private model artifact.

**Source independence.** Webcam indices, file paths, and network-style stream sources share the same command-line interface.

**Safe integration boundary.** The public project stops at the perception interface and does not publish vehicle-control or operational interception implementation.

**Reproducible measurement.** The benchmark utility reports timing for the exact model, source, and hardware selected by the user rather than embedding unverified performance claims.

## Deployment context

The professional project used NVIDIA Jetson hardware for edge inference. Hardware-specific optimizations, trained model weights, production camera configuration, and private deployment settings are excluded from the public repository.
