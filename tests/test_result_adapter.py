from src.result_adapter import track_states_from_result


class FakeTensor:
    def __init__(self, values):
        self.values = values

    def cpu(self):
        return self

    def tolist(self):
        return self.values


class FakeBoxes:
    id = FakeTensor([7])
    xyxy = FakeTensor([[10.0, 20.0, 30.0, 40.0]])
    conf = FakeTensor([0.91])
    cls = FakeTensor([2])


class FakeResult:
    boxes = FakeBoxes()
    names = {2: "uav"}


def test_track_states_from_result_marks_selected_track():
    states = track_states_from_result(FakeResult(), selected_track_id=7)

    assert len(states) == 1
    assert states[0].track_id == 7
    assert states[0].class_name == "uav"
    assert states[0].locked is True
    assert states[0].bbox_xyxy == (10.0, 20.0, 30.0, 40.0)


def test_track_states_from_result_without_boxes():
    class EmptyResult:
        boxes = None

    assert track_states_from_result(EmptyResult()) == []
