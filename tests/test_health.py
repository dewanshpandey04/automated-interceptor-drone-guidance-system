from src.health import evaluate_health


def test_health_ok():
    status = evaluate_health(42.0, 3, minimum_fps=10.0)
    assert status.status == "OK"
    assert status.track_count == 3


def test_health_degraded():
    assert evaluate_health(7.0, 1, minimum_fps=10.0).status == "DEGRADED"


def test_health_no_data():
    assert evaluate_health(0.0, 0).status == "NO_DATA"
