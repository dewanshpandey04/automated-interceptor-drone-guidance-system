from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TargetLockState:
    """Perception-layer selected-track state.

    The public project keeps selection explicit/manual and does not issue
    vehicle-control or navigation commands.
    """

    selected_track_id: int | None = None
    visible: bool = False

    def select(self, track_id: int) -> None:
        self.selected_track_id = int(track_id)
        self.visible = False

    def clear(self) -> None:
        self.selected_track_id = None
        self.visible = False

    def update_visible_tracks(self, track_ids: list[int]) -> None:
        if self.selected_track_id is None:
            self.visible = False
            return
        self.visible = self.selected_track_id in {int(v) for v in track_ids}

    @property
    def status(self) -> str:
        if self.selected_track_id is None:
            return "UNSELECTED"
        return "LOCKED" if self.visible else "NOT_VISIBLE"

    def as_dict(self) -> dict:
        return {
            "selected_track_id": self.selected_track_id,
            "visible": self.visible,
            "status": self.status,
        }
