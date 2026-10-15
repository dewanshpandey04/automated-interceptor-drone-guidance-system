from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a YAML config and perform lightweight public-demo validation."""
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(config_path)

    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}

    if not isinstance(data, dict):
        raise ValueError("Configuration root must be a mapping.")

    required = {"project", "camera", "detection", "tracking"}
    missing = sorted(required.difference(data))
    if missing:
        raise ValueError(f"Missing config sections: {', '.join(missing)}")

    return data
