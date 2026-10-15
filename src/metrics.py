from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from statistics import mean


@dataclass
class RuntimeMetrics:
    """Rolling runtime statistics independent from the model implementation."""

    window: int = 60
    _frame_times_ms: deque[float] = field(default_factory=deque)

    def add_frame_time_ms(self, value: float) -> None:
        self._frame_times_ms.append(float(value))
        while len(self._frame_times_ms) > self.window:
            self._frame_times_ms.popleft()

    @property
    def mean_frame_time_ms(self) -> float:
        return mean(self._frame_times_ms) if self._frame_times_ms else 0.0

    @property
    def fps(self) -> float:
        value = self.mean_frame_time_ms
        return 1000.0 / value if value > 0 else 0.0

    def snapshot(self) -> dict:
        return {
            "samples": len(self._frame_times_ms),
            "mean_frame_time_ms": round(self.mean_frame_time_ms, 3),
            "fps": round(self.fps, 2),
        }
