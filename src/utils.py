from __future__ import annotations

from typing import Sequence


def parse_source(value: str | int) -> int | str:
    """Normalize webcam indexes while preserving file paths and URLs."""
    if isinstance(value, int):
        return value
    text = str(value).strip()
    return int(text) if text.isdigit() else text


def box_center(box: Sequence[float]) -> tuple[float, float]:
    x1, y1, x2, y2 = box
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


def contains_track(track_ids: Sequence[int], selected_track_id: int | None) -> bool:
    """Return whether an explicitly selected track is currently visible."""
    if selected_track_id is None:
        return False
    selected = int(selected_track_id)
    return any(int(track_id) == selected for track_id in track_ids)
