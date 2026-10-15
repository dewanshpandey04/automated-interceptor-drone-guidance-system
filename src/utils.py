from __future__ import annotations

from typing import Sequence


def parse_source(value: str):
    """Convert a numeric webcam source such as '0' to int."""
    value = value.strip()
    return int(value) if value.isdigit() else value


def box_center(box: Sequence[float]) -> tuple[float, float]:
    x1, y1, x2, y2 = box
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


def contains_track(track_ids: Sequence[int], selected_track_id: int | None) -> bool:
    """Return whether an explicitly selected track is currently visible."""
    if selected_track_id is None:
        return False
    return int(selected_track_id) in {int(v) for v in track_ids}
