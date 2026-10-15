from __future__ import annotations

from .target_state import TrackState


def track_states_from_result(result, selected_track_id: int | None = None) -> list[TrackState]:
    """Convert an Ultralytics result into the repository's stable TrackState model."""
    boxes = getattr(result, "boxes", None)
    if boxes is None or boxes.id is None:
        return []

    ids = [int(v) for v in boxes.id.cpu().tolist()]
    xyxy = boxes.xyxy.cpu().tolist()
    conf = boxes.conf.cpu().tolist() if boxes.conf is not None else [0.0] * len(ids)
    classes = boxes.cls.cpu().tolist() if boxes.cls is not None else [-1] * len(ids)
    names = getattr(result, "names", {}) or {}

    states: list[TrackState] = []
    for track_id, cls_id, confidence, box in zip(ids, classes, conf, xyxy):
        class_name = str(names.get(int(cls_id), int(cls_id)))
        states.append(
            TrackState(
                track_id=track_id,
                class_name=class_name,
                confidence=float(confidence),
                bbox_xyxy=tuple(float(v) for v in box),
                locked=(track_id == selected_track_id),
            )
        )
    return states
