from src.utils import box_center, nearest_track_to_center, parse_source


def test_parse_source_numeric():
    assert parse_source("0") == 0


def test_box_center():
    assert box_center([0, 0, 10, 20]) == (5.0, 10.0)


def test_nearest_track_to_center():
    ids = [3, 7]
    boxes = [[0, 0, 20, 20], [45, 45, 55, 55]]
    assert nearest_track_to_center(ids, boxes, 100, 100) == 7
