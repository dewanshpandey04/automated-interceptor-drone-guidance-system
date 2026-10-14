from __future__ import annotations

from typing import Sequence


def parse_source(value: str):
    """Convert a numeric webcam source such as '0' to int."""
    value = value.strip()
    return int(value) if value.isdigit() else value


def box_center(box: Sequence[float]) -> tuple[float, float]:
    x1, y1, x2, y2 = box
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


def nearest_track_to_center(
    track_ids: Sequence[int],
    boxes_xyxy: Sequence[Sequence[float]],
    frame_width: int,
    frame_height: int,
) -> int | None:
    """Return the visible track nearest image center for HUD/demo visualization.

    This is not vehicle guidance logic.
    """
    if not track_ids or not boxes_xyxy:
        return None

    center_x = frame_width / 2.0
    center_y = frame_height / 2.0
    best_id = None
    best_distance = None

    for track_id, box in zip(track_ids, boxes_xyxy):
        x, y = box_center(box)
        distance = (x - center_x) ** 2 + (y - center_y) ** 2
        if best_distance is None or distance < best_distance:
            best_id = int(track_id)
            best_distance = distance

    return best_id
