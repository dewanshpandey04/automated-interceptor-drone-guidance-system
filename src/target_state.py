from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrackState:
    """Small public data model for a tracked object's visible state."""

    track_id: int
    class_name: str
    confidence: float
    bbox_xyxy: tuple[float, float, float, float]
    locked: bool = False

    def as_dict(self) -> dict:
        return {
            "track_id": self.track_id,
            "class_name": self.class_name,
            "confidence": round(float(self.confidence), 4),
            "bbox_xyxy": list(self.bbox_xyxy),
            "locked": self.locked,
        }
