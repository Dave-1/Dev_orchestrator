#!/usr/bin/env python3
"""
Claude Code Orchestrator Pure Python Installer (Zero chmod required)
"""

import os
import json
from pathlib import Path

CLAUDE_DIR = Path(".claude")

def setup():
    # 1. Create directory layout
    (CLAUDE_DIR / "skills").mkdir(parents=True, exist_ok=True)
    (CLAUDE_DIR / "agents").mkdir(parents=True, exist_ok=True)
    (CLAUDE_DIR / "rules").mkdir(parents=True, exist_ok=True)
    (CLAUDE_DIR / "screenshots").mkdir(parents=True, exist_ok=True)

    # 2. Write CLAUDE.md
    claude_md = """# Master Claude Code Orchestrator Rules

## Operating Principles
1. Zero User Keywords Required: The pipeline executes sub-skills automatically.
2. Context Budget: At 35% memory limit, compact context into `.claude/handoff.md`.
3. Spec Gate First: Never write code until `.claude/spec.md` is generated and approved by user.
4. Pre-Verification: Run baseline checks and report findings to user before editing code.
5. Preference-Bias Elimination: Use isolated reviewer and QA agents.

## Automated Execution Pipeline
1. Intake & Auto-Extract -> .claude/skills/intake-auto-parser.md
2. Plan & Spec Approval Gate -> .claude/skills/spec-generator.md
3. Pre-Implementation Verification -> .claude/skills/pre-verify-oracle.md
4. Surgical Implementation -> .claude/skills/surgical-implementer.md
5. Isolated Review & QA -> .claude/skills/preference-bias-eval.md
6. Session Handoff -> .claude/skills/session-handoff.md
"""
    (CLAUDE_DIR / "CLAUDE.md").write_text(claude_md)

    # 3. Write default spec.md & handoff.md
    (CLAUDE_DIR / "spec.md").write_text("# Spec Plan\nStatus: PENDING USER APPROVAL\n")
    (CLAUDE_DIR / "handoff.md").write_text("# Session Handoff Log\nStatus: Active\n")

    # 4. Write initial state.json
    state = {
        "status": "Initialized",
        "environment": "Local Dev",
        "total_savings_pct": "~65%",
        "caveman_savings_pct": "-55%",
        "routing_savings_pct": "-70% Cost",
        "context_pct": 10,
        "tokens_used": 0,
        "tokens_saved": 0
    }
    (CLAUDE_DIR / "state.json").write_text(json.dumps(state, indent=2))

    print("✅ Claude Code Orchestrator successfully initialized in .claude/!")
    print("🚀 Run dashboard anytime using: python3 .claude/dashboard.py")

if __name__ == "__main__":
    setup()
