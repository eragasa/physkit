"""Repository-layout conformance for the Project Koios component package."""

from __future__ import annotations

import json
from pathlib import Path


def test__repository_layout__uses_projectkoios_namespace() -> None:
    root: Path = Path(__file__).resolve().parents[2]
    pyproject_text: str = (root / "pyproject.toml").read_text(encoding="utf-8")

    assert 'name = "projectkoios-physkit"' in pyproject_text
    assert 'package-dir = { "" = "src/python" }' in pyproject_text
    assert 'where = ["src/python"]' in pyproject_text
    assert "namespaces = true" in pyproject_text
    package_root = root / "src/python/projectkoios/physkit"
    assert (package_root / "__init__.py").is_file()
    assert not tuple(package_root.rglob("*.ipynb"))
    assert not (root / "src/python/projectkoios/__init__.py").exists()
    assert not (root / "src/physkit").exists()
    assert (root / "tests/projectkoios/physkit").is_dir()
    assert not (root / "tests/physkit").exists()
    assert (root / "notebooks/qm/piab1d").is_dir()
    assert (root / "notebooks/qm/piab2d").is_dir()
    assert (root / "notebooks/qm/piab3d").is_dir()
    assert (root / "notebooks/qm/piab1d/piab1d.ipynb").is_file()
    assert (root / "notebooks/qm/piab2d/tise/analytical/piab2d.ipynb").is_file()
    assert (root / "notebooks/qm/piab2d/tdse/numerical").is_dir()
    assert (root / "notebooks/qm/piab3d/piab3d.ipynb").is_file()
    assert not (root / "notebooks/quantum-mechanics").exists()


def test__repository_notebooks__are_valid_json_documents() -> None:
    root = Path(__file__).resolve().parents[2]
    notebook_paths = tuple(sorted((root / "notebooks").rglob("*.ipynb")))

    assert notebook_paths
    for notebook_path in notebook_paths:
        json.loads(notebook_path.read_text(encoding="utf-8"))
