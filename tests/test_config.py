import pytest

from src.config import load_config


def test_load_config_accepts_required_sections(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text(
        """
project: {}
camera: {}
detection: {}
tracking: {}
""".strip(),
        encoding="utf-8",
    )

    data = load_config(path)
    assert set(data) >= {"project", "camera", "detection", "tracking"}


def test_load_config_rejects_missing_sections(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("project: {}", encoding="utf-8")

    with pytest.raises(ValueError, match="Missing config sections"):
        load_config(path)
