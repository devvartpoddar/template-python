import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env_file(PROJECT_ROOT / ".env")

# Honors the existing /workspace/data/<project>/ convention so heavy data never touches git.
DATA_DIR = Path(os.environ.get("PROJECT_DATA_DIR", PROJECT_ROOT / "data"))
OUTPUT_DIR = PROJECT_ROOT / "outputs"
