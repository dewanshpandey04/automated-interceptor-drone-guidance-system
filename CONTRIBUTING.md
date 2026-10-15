# Contributing

Contributions are welcome for bug fixes, tests, documentation, portability, configuration, and performance tooling.

## Development setup

```powershell
git clone https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system.git
cd automated-interceptor-drone-guidance-system

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Install `requirements.txt` as well when running the YOLO/OpenCV entry points locally.

## Quality checks

Before opening a pull request, run:

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m pytest -q
```

## Workflow

1. Branch from `develop`.
2. Use a focused name such as `feature/...`, `fix/...`, or `docs/...`.
3. Keep each change scoped to one problem.
4. Add or update tests when reusable logic changes.
5. Run the local quality checks.
6. Open a pull request into `develop` and describe the change and validation performed.

## Code guidelines

- Support Python 3.10+.
- Prefer small modules with a single responsibility.
- Use type hints for reusable interfaces and data structures.
- Keep model paths, sources, thresholds, and devices configurable.
- Keep model-specific result objects behind adapter boundaries.
- Do not commit generated outputs, model weights, datasets, credentials, or confidential configuration.

## Branches

- `main` — stable branch
- `develop` — active development and integration
- `docs` — documentation work
