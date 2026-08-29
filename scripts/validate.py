#!/usr/bin/env python3
"""Validate the public QArborBench-v0.1 payload using the standard library."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABSOLUTE_PATH = re.compile(r"(?:/mnt/|/home/|[A-Za-z]:\\\\)")
INTERNAL_STAGE = re.compile(
    r"\b(?:Goal[ _-]?[A-D]|C(?:[0-9]|1[0-3])|qualification|HM1|HM2|mechanism[ _-]?smoke)\b",
    re.IGNORECASE,
)
EXPECTED_CELL_IDS = {
    "bike-sharing-demand",
    "hull-tactical-market-prediction",
    "jpx-tokyo-stock-exchange-prediction",
    "optiver-trading-at-the-close",
    "recruit-restaurant-visitor-forecasting",
    "walmart-store-sales",
    "web-traffic-time-series-forecasting",
}
DENY_DIRS = {
    "data",
    "artifacts",
    "sessions",
    "attempts",
    "ledgers",
    "papers",
    "workspaces",
    ".venv",
}


def main() -> int:
    registry = json.loads((ROOT / "benchmark/registry.json").read_text())
    summary = json.loads((ROOT / "results/summary.json").read_text())
    protocol = json.loads((ROOT / "protocol/protocol.json").read_text())

    assert registry["name"] == "QArborBench"
    assert registry["coverage"] == {
        "registered_cells": 7,
        "executed_cells": 7,
        "deferred_cells": 0,
        "task_families": 5,
        "primary_evidence_regimes": 3,
    }
    assert len(registry["cells"]) == 7
    assert len(summary["cells"]) == 7
    assert summary["primary_outcomes"]["q_arbor_vs_flat"] == {
        "wins": 4,
        "losses": 3,
        "no_result": 0,
    }
    assert protocol["admissibility"]["heterogeneous_metrics_aggregated"] is False

    registry_ids = {cell["cell_id"] for cell in registry["cells"]}
    summary_ids = {cell["cell_id"] for cell in summary["cells"]}
    assert registry_ids == summary_ids == EXPECTED_CELL_IDS
    assert {path.stem for path in (ROOT / "tasks").glob("*.md")} == EXPECTED_CELL_IDS
    for cell in registry["cells"]:
        source_url = cell["original_source_url"]
        assert source_url.startswith("https://www.kaggle.com/competitions/")
        task_card = ROOT / cell["task_card"]
        assert task_card.is_file()
        assert source_url in task_card.read_text(encoding="utf-8")

    for path in ROOT.rglob("*"):
        if path.is_dir():
            assert path.name not in DENY_DIRS
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".cff", ".py"}:
            text = path.read_text(encoding="utf-8")
            assert not ABSOLUTE_PATH.search(text), path
            assert not INTERNAL_STAGE.search(text), path

    print("QArborBench public payload: PASS")
    print("7 complete contracts; no restricted directories or local paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
