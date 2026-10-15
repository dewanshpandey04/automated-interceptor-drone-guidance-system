from __future__ import annotations

from dataclasses import dataclass, field

from .target_state import TrackState


@dataclass
class PerceptionSnapshot:
    """Serializable output contract for visualization/telemetry integration."""

    frame_id: int
    captured_at: float
    fps: float
    tracks: list[TrackState] = field(default_factory=list)
    selected_track_id: int | None = None

    def as_dict(self) -> dict:
        return {
            "frame_id": int(self.frame_id),
            "captured_at": float(self.captured_at),
            "fps": round(float(self.fps), 2),
            "selected_track_id": self.selected_track_id,
            "tracks": [track.as_dict() for track in self.tracks],
        }
