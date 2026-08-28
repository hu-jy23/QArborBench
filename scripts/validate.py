#!/usr/bin/env python3
"""Validate the public QArborBench-v0.1 payload using the standard library."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABSOLUTE_PATH = re.compile(r"(?:/mnt/|[A-Za-z]:\\\\)")
DENY_DIRS = {"data", "artifacts", "sessions", "attempts", "ledgers", ".venv"}


def main() -> int:
    registry = json.loads((ROOT / "benchmark/registry.json").read_text())
    summary = json.loads((ROOT / "results/summary.json").read_text())
    protocol = json.loads((ROOT / "protocol/protocol.json").read_text())

    assert registry["name"] == "QArborBench"
    assert registry["coverage"] == {
        "registered_cells": 12,
        "executed_cells": 9,
        "deferred_cells": 3,
        "task_families": 5,
        "evidence_regimes": 4,
    }
    assert len(registry["cells"]) == 12
    assert len(summary["cells"]) == 12
    assert summary["primary_outcomes"]["q_arbor_vs_flat"] == {
        "wins": 4,
        "losses": 4,
        "no_result": 1,
    }
    assert protocol["admissibility"]["heterogeneous_metrics_aggregated"] is False

    registry_ids = {cell["cell_id"] for cell in registry["cells"]}
    summary_ids = {cell["cell_id"] for cell in summary["cells"]}
    assert registry_ids == summary_ids
    for cell in registry["cells"]:
        assert (ROOT / cell["task_card"]).is_file()

    for path in ROOT.rglob("*"):
        if path.is_dir():
            assert path.name not in DENY_DIRS
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".cff", ".py"}:
            text = path.read_text(encoding="utf-8")
            assert not ABSOLUTE_PATH.search(text), path

    print("QArborBench public payload: PASS")
    print("12 contracts; 9 executed; 3 deferred; no restricted directories or local paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
