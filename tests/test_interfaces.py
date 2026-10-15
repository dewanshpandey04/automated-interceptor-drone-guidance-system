from src.interfaces import PerceptionSnapshot
from src.target_state import TrackState


def test_snapshot_serialization():
    snapshot = PerceptionSnapshot(
        frame_id=12,
        captured_at=123.5,
        fps=49.987,
        selected_track_id=8,
        tracks=[
            TrackState(
                track_id=8,
                class_name="uav",
                confidence=0.91,
                bbox_xyxy=(1.0, 2.0, 3.0, 4.0),
                locked=True,
            )
        ],
    )
    payload = snapshot.as_dict()
    assert payload["frame_id"] == 12
    assert payload["fps"] == 49.99
    assert payload["selected_track_id"] == 8
    assert payload["tracks"][0]["locked"] is True
