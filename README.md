# template-python

Project scaffold for new Python work — one template for both data-analysis and infra-development projects. See `AGENTS.md` for how to run things and `docs/GOTCHAS.md` for accumulated lessons.

## Using this template

1. GitHub → **Use this template** → create a new repository (not fork, not clone).
2. New repo's Settings → General → tick **"Automatically delete head branches"**. The one setting that actually matters; not carried over by the template.
3. Rename `src/app/` to your project's package name; update the name in `pyproject.toml` and `AGENTS.md`.
4. `uv sync --all-extras`
5. Infra project rather than data-analysis? Delete `data/`, `notebooks/`, and `outputs/` — they won't be used.
6. Copy `.env.example` to `.env` and fill in real values. `.env` is gitignored; `.env.example` is not.

## Layout

- `src/app/config.py` — resolves `PROJECT_ROOT`, `DATA_DIR`, `OUTPUT_DIR` and loads `.env`. Every script imports from here instead of hardcoding paths.
- `data/` — raw, immutable input data. Gitignored except `.gitkeep`.
- `notebooks/` — exploration only, no logic that doesn't also live in `src/`. Strip cell outputs before committing.
- `outputs/` — small sample artifacts that *do* get committed.
- `docs/GOTCHAS.md` — symptom → cause → rule. Add to it whenever a quirk bites.
