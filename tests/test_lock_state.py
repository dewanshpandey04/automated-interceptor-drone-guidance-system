from src.lock_state import TargetLockState


def test_lock_state_visibility():
    state = TargetLockState()
    state.select(7)
    state.update_visible_tracks([3, 7, 9])
    assert state.status == "LOCKED"
    assert state.visible is True


def test_lock_state_not_visible():
    state = TargetLockState()
    state.select(7)
    state.update_visible_tracks([3, 9])
    assert state.status == "NOT_VISIBLE"


def test_lock_state_clear():
    state = TargetLockState(selected_track_id=4, visible=True)
    state.clear()
    assert state.status == "UNSELECTED"
    assert state.selected_track_id is None
