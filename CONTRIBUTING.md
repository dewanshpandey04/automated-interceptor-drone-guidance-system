# Contributing

Contributions are welcome for bug fixes, tests, documentation, portability, and performance tooling.

## Development setup

```powershell
git clone https://github.com/dewanshpandey04/automated-interceptor-drone-guidance-system.git
cd automated-interceptor-drone-guidance-system

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the test suite before submitting changes:

```powershell
pytest -q
```

## Workflow

1. Create a branch from `develop`.
2. Use a clear branch name such as `feature/...`, `fix/...`, or `docs/...`.
3. Keep each change focused on one problem.
4. Add or update tests when changing reusable logic.
5. Run the test suite locally.
6. Open a pull request into `develop` with a short description of the change and validation performed.

## Code guidelines

- Target Python 3.11 or newer.
- Prefer small modules with clear responsibilities.
- Add type hints for reusable interfaces and data structures.
- Keep model paths, camera sources, and runtime settings configurable.
- Avoid committing generated outputs, model weights, datasets, or credentials.

## Repository boundaries

Do not commit proprietary source code, private datasets, camera credentials, production model weights, internal network details, or confidential deployment configuration.

## Branches

- `main` — stable branch
- `develop` — active development and integration
- `docs` — documentation work
