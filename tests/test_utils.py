from src.utils import box_center, contains_track, parse_source


def test_parse_source_numeric():
    assert parse_source("0") == 0


def test_box_center():
    assert box_center([0, 0, 10, 20]) == (5.0, 10.0)


def test_contains_track():
    assert contains_track([3, 7], 7) is True
    assert contains_track([3, 7], 5) is False
    assert contains_track([3, 7], None) is False
