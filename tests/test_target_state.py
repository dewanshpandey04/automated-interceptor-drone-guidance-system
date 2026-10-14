from src.target_state import TrackState


def test_track_state_schema():
    state = TrackState(
        track_id=4,
        class_name="uav",
        confidence=0.91321,
        bbox_xyxy=(10.0, 20.0, 30.0, 40.0),
        locked=True,
    )
    payload = state.as_dict()
    assert payload["track_id"] == 4
    assert payload["class_name"] == "uav"
    assert payload["confidence"] == 0.9132
    assert payload["locked"] is True
