from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class HealthStatus:
    fps: float
    track_count: int
    status: str

    def as_dict(self) -> dict:
        return asdict(self)


def evaluate_health(fps: float, track_count: int, minimum_fps: float = 10.0) -> HealthStatus:
    """Return a small runtime health summary for diagnostics."""
    if fps <= 0:
        status = "NO_DATA"
    elif fps < minimum_fps:
        status = "DEGRADED"
    else:
        status = "OK"

    return HealthStatus(
        fps=round(float(fps), 2),
        track_count=int(track_count),
        status=status,
    )
