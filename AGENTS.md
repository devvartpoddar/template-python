# AGENTS.md

Index, not a rulebook. If something needs more than a pointer, it lives in the file it belongs to.

## Setup

    uv sync --all-extras

## Run

    uv run pytest
    uv run ruff check .
    uv run ruff format --check .

## Where things live

- `src/app/` — package code. Rename `app` once, to your project's name; update `pyproject.toml` and this file to match.
- `src/app/config.py` — the only place paths and `.env` loading happen. Import from it, don't hardcode paths.
- `data/` — raw input data, gitignored, immutable once written. Never edit in place.
- `notebooks/` — exploration only. No logic that doesn't also live in `src/`.
- `outputs/` — small sample artifacts, committed on purpose.
- `docs/GOTCHAS.md` — the quirk ledger. Read it before you re-debug something old. Add to it when you hit something new.

## Before opening a PR

Read `.github/pull_request_template.md`, fill every section for real, then pass it with `--body-file`:

    gh pr create --body-file /tmp/pr-body.md

Do not invent your own PR body — the web UI auto-fills the template, `gh pr create --body "..."` does not. Any new gotcha found while doing this work goes into `docs/GOTCHAS.md` in the same PR.
