"""Inventory checks for the SERE documentation skeleton.

These tests do not validate physics, autonomy, or integration.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "LICENSE",
    "docs/ARCHITECTURE.md",
    "docs/CLAIM_STATUS.md",
    "docs/CONSTITUTIONAL_SAFETY.md",
    "docs/PHYSICS.md",
    "docs/WORKFLOW.md",
    "seem/README.md",
    "cft/README.md",
    "security/README.md",
    "blockchain/README.md",
    "gdextension/README.md",
    "godot/README.md",
    "storage/README.md",
    "scripts/README.md",
)


def test_required_docs_exist():
    missing = [rel for rel in REQUIRED if not (ROOT / rel).is_file()]
    assert missing == []


def test_claim_cap_is_research():
    text = (ROOT / "docs" / "CLAIM_STATUS.md").read_text(encoding="utf-8")
    assert "RESEARCH" in text
    assert "≤ 1" in text
    assert "Not claimed" in text
