from pathlib import Path

from app.config import DATA_DIR, OUTPUT_DIR, PROJECT_ROOT


def test_project_root_exists():
    assert PROJECT_ROOT.is_dir()


def test_data_and_output_dirs_are_paths():
    assert isinstance(DATA_DIR, Path)
    assert isinstance(OUTPUT_DIR, Path)
    assert OUTPUT_DIR == PROJECT_ROOT / "outputs"
