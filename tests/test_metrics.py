from src.metrics import RuntimeMetrics


def test_runtime_metrics_snapshot():
    metrics = RuntimeMetrics(window=3)
    metrics.add_frame_time_ms(20)
    metrics.add_frame_time_ms(20)
    snapshot = metrics.snapshot()
    assert snapshot["samples"] == 2
    assert snapshot["mean_frame_time_ms"] == 20.0
    assert snapshot["fps"] == 50.0


def test_runtime_metrics_window():
    metrics = RuntimeMetrics(window=2)
    metrics.add_frame_time_ms(10)
    metrics.add_frame_time_ms(20)
    metrics.add_frame_time_ms(30)
    assert metrics.snapshot()["samples"] == 2
    assert metrics.snapshot()["mean_frame_time_ms"] == 25.0
