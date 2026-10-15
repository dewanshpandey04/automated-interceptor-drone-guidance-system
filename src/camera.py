from __future__ import annotations

from dataclasses import dataclass
from time import time
from typing import Any


@dataclass(frozen=True)
class FramePacket:
    frame_id: int
    captured_at: float
    frame: Any


class CameraSource:
    """Small OpenCV source wrapper for webcam, file, or network stream."""

    def __init__(self, source):
        import cv2

        self._cv2 = cv2
        self._capture = cv2.VideoCapture(source)
        if not self._capture.isOpened():
            raise RuntimeError(f"Unable to open video source: {source}")
        self._frame_id = 0

    def read(self) -> FramePacket | None:
        ok, frame = self._capture.read()
        if not ok:
            return None
        self._frame_id += 1
        return FramePacket(
            frame_id=self._frame_id,
            captured_at=time(),
            frame=frame,
        )

    def close(self) -> None:
        self._capture.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
