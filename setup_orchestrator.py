#!/usr/bin/env python3
"""
Claude Code Orchestrator + Superpowers Setup Script (v3)
Option B: Embedded Skill Inheritance
Bundles Superpowers' TDD, Git Worktree Isolation, Brainstorming/Spec Design,
and Systematic Debugging directly into .claude/skills/ with ZERO external dependencies.
"""

import os
import sys
from pathlib import Path

CLAUDE_DIR = Path(".claude")

FILES = {
    CLAUDE_DIR / "CLAUDE.md": """# Claude Code Master Orchestrator + Superpowers

## Operating Principles
1. **Zero User Keywords**: All skills execute automatically behind the scenes.
2. **Superpowers Core Rules**:
   - **TDD Requirement**: Write a failing test FIRST. Delete any code written before a failing test exists.
   - **Git Worktree Isolation**: Create an isolated git worktree branch before modifying code.
   - **Systematic Debugging**: Follow a strict 4-phase root cause process. Never fix by guesswork.
3. **Spec Gate First**: Never write implementation code until `.claude/spec.md` is approved by the user.
4. **Pre-Implementation Verification**: Verify baseline tests and Oracle regressions before editing. Report findings to user.
5. **Preference-Bias Elimination**: Main coding agent MUST NOT review its own code. Deploy isolated reviewer and QA agents.
6. **Context Limit**: Keep memory under 35%. Write `.claude/handoff.md` and reset on limit.

## Automated Pipeline
1. **Intake & Auto-Extract**: Run `.claude/skills/intake-auto-parser.md`. Collect env, credentials file, context, screenshot path, target files.
2. **Worktree Setup**: Run `.claude/skills/worktree-isolation.md`. Create a clean git worktree.
3. **Spec Approval Gate**: Run `.claude/skills/spec-generator.md` & `.claude/skills/brainstorming.md`. Pause for explicit user approval of `.claude/spec.md`.
4. **Pre-Implementation Verification**: Run `.claude/skills/pre-verify-oracle.md` & `.claude/skills/systematic-debugging.md`. Report findings to user.
5. **TDD Implementation**: Run `.claude/skills/tdd-cycle.md` & `.claude/skills/surgical-implementer.md`. Write failing test -> write minimal code to pass -> refactor.
6. **Isolated Review & QA**: Run `.claude/skills/preference-bias-eval.md` (`reviewer.md` & `qa-agent.md`).
7. **Session Handoff & Dashboard Sync**: Write `.claude/handoff.md` and sync with `python3 .claude/dashboard.py`.
""",

    CLAUDE_DIR / "skills" / "brainstorming.md": """# Skill: Brainstorming & Spec Design (Superpowers)

## Protocol
1. Explore intent, target architecture, and visual screenshots.
2. Identify trade-offs, state handlers, and edge cases.
3. Draft `.claude/spec.md` with explicit Acceptance Criteria.
4. Halt execution until user confirms the design specification.
""",

    CLAUDE_DIR / "skills" / "tdd-cycle.md": """# Skill: Test-Driven Development (Superpowers)

## Strict Rules
1. **RED Phase**: Write a failing test for the target bug or feature before ANY production code is touched.
2. Verify test failure reproduces the reported bug or missing feature.
3. **GREEN Phase**: Write the MINIMAL surgical production code required to make the test pass.
4. **REFACTOR Phase**: Clean up code adhering to `.claude/rules/coding-standards.md`.
5. **Enforcement**: Delete any implementation code written prior to writing a failing test.
""",

    CLAUDE_DIR / "skills" / "worktree-isolation.md": """# Skill: Git Worktree Isolation (Superpowers)

## Protocol
1. Create a dedicated Git worktree branch for the active task (`git worktree add -b task-branch .claude/worktrees/task`).
2. Run all exploration, tests, and surgical code edits inside the isolated worktree.
3. Merge back to main branch only after isolated Reviewer and QA subagents issue **GO** clearance.
""",

    CLAUDE_DIR / "skills" / "systematic-debugging.md": """# Skill: Systematic Debugging (Superpowers)

## 4-Phase Debugging Process
1. **Root Cause Investigation**: Add console traces; do NOT guess or apply speculative fixes.
2. **Pattern Analysis**: Trace data flow back through state handlers, props, and API boundaries.
3. **Hypothesis Verification**: Prove root cause by reproducing live in browser with log evidence.
4. **Surgical Fix & Regression Check**: Fix root cause without refactoring unrelated code.
""",

    CLAUDE_DIR / "skills" / "intake-auto-parser.md": """# Skill: Intake & Automated Keyword Extractor

1. Prompt user for: Target Environment, Credentials File Path, Issue Context, Screenshot Path, Pinpointed Files.
2. Automatically parse UI selectors, props, state handlers, error traces, and acceptance criteria.
3. Write extracted parameters into `.claude/spec.md` in Caveman compressed syntax.
""",

    CLAUDE_DIR / "skills" / "spec-generator.md": """# Skill: Spec Generator & Approval Gate

1. Map out target routes and state transitions into a Knowledge Graph.
2. Write `.claude/spec.md` containing files to edit, out-of-scope boundaries, and Acceptance Criteria.
3. **HALT EXECUTION**: Present `.claude/spec.md` to user and await explicit confirmation before coding.
""",

    CLAUDE_DIR / "skills" / "pre-verify-oracle.md": """# Skill: Pre-Implementation Verification

1. Connect to Staging / Oracle URL or clean codebase.
2. Run baseline test suites and trace logs.
3. **Inform User**: Report baseline code health and Oracle comparison status before writing code.
""",

    CLAUDE_DIR / "skills" / "surgical-implementer.md": """# Skill: Surgical Implementer

1. Fast Tier (Haiku): Code searching, console log placement, trace gathering.
2. Smart Tier (Sonnet/Opus): Surgical code edits following TDD cycle.
3. Edit ONLY target files. Validate live in browser with console log proof.
""",

    CLAUDE_DIR / "skills" / "preference-bias-eval.md": """# Skill: Preference-Bias Elimination

1. Deploy `.claude/agents/reviewer.md` in fresh context to review diff against `.claude/rules/coding-standards.md`.
2. Deploy `.claude/agents/qa-agent.md` in fresh context to test edge cases and issue GO/NO-GO clearance.
""",

    CLAUDE_DIR / "skills" / "session-handoff.md": """# Skill: Session Handoff

When context memory reaches 35%, automatically generate `.claude/handoff.md`:
- Completed tasks
- Pending implementation steps
- Accumulated trace learnings
- Exact resume command: `claude "Resume session using .claude/handoff.md"`
""",

    CLAUDE_DIR / "rules" / "coding-standards.md": """# Coding Standards & Architecture Rules

1. Write clean, modular, self-documenting code.
2. Never add unrequested third-party packages or modify public API signatures without spec approval.
3. Maintain zero test regressions across existing test suites.
""",

    CLAUDE_DIR / "agents" / "implementer.md": """# Agent: Surgical Implementer
Focus: Surgical coding, TDD test creation, live browser console log validation.
""",

    CLAUDE_DIR / "agents" / "reviewer.md": """# Agent: Isolated Code Reviewer
Focus: Independent code diff review against `.claude/rules/coding-standards.md`.
""",

    CLAUDE_DIR / "agents" / "qa-agent.md": """# Agent: Independent QA Tester
Focus: Edge-case validation, browser verification, and issuing GO/NO-GO clearance.
""",

    CLAUDE_DIR / "dashboard.py": """#!/usr/bin/env python3
\"\"\"
Claude Code Orchestrator Dashboard (v3 + Superpowers)
Running on http://localhost:8080
\"\"\"
import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 8080
CLAUDE_DIR = Path(".claude")

HTML_TEMPLATE = \"\"\"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Claude Code Orchestrator + Superpowers Dashboard</title>
    <style>
        :root {
            --bg: #0d1117; --card: #161b22; --border: #30363d;
            --blue: #58a6ff; --green: #3fb950; --yellow: #d29922; --purple: #bc8cff; --cyan: #39c5cf;
        }
        body { font-family: system-ui, sans-serif; background: var(--bg); color: #c9d1d9; margin: 0; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 12px; margin-bottom: 20px; }
        h1 { margin: 0; font-size: 22px; color: var(--blue); }
        .badge { background: rgba(63, 185, 80, 0.15); color: var(--green); border: 1px solid var(--green); padding: 4px 12px; border-radius: 12px; font-weight: 600; font-size: 13px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; }
        .card h2 { margin-top: 0; font-size: 16px; color: var(--purple); border-bottom: 1px solid var(--border); padding-bottom: 8px; }
        .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin-bottom: 16px; }
        .m-box { background: #21262d; border: 1px solid var(--border); border-radius: 6px; padding: 10px; text-align: center; }
        .m-val { font-size: 20px; font-weight: bold; color: var(--green); }
        .m-lbl { font-size: 10px; color: #8b949e; text-transform: uppercase; }
        pre { background: #090d12; padding: 12px; border-radius: 6px; font-size: 12px; border: 1px solid var(--border); max-height: 250px; overflow: auto; }
        .full { grid-column: 1 / -1; }
        .tag { font-size: 11px; background: rgba(57,197,207,0.15); color: var(--cyan); padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 Claude Code Orchestrator + Superpowers Dashboard</h1>
        <span class="badge">Superpowers Active (TDD + Worktrees)</span>
    </div>

    <div class="card full" style="margin-bottom: 16px;">
        <h2 style="color: var(--cyan);">⚡ Token Savings & Superpowers Status</h2>
        <div class="metrics">
            <div class="m-box"><div class="m-lbl">Total Token Savings</div><div class="m-val">~65%</div></div>
            <div class="m-box"><div class="m-lbl">Caveman Saver</div><div class="m-val" style="color:var(--blue);">-55%</div></div>
            <div class="m-box"><div class="m-lbl">Tier Routing</div><div class="m-val" style="color:var(--purple);">-70% Cost</div></div>
            <div class="m-box"><div class="m-lbl">Superpowers Engine</div><div class="m-val" style="color:var(--cyan);">TDD + Worktree</div></div>
            <div class="m-box"><div class="m-lbl">Context Capacity</div><div class="m-val" style="color:var(--yellow);">32% / 35%</div></div>
        </div>
    </div>

    <div class="grid">
        <div class="card">
            <h2>Execution Pipeline Phase</h2>
            <p>1. Intake & Requirements <span class="tag">Auto-Parser</span></p>
            <p>2. Git Worktree Isolation <span class="tag">Superpowers</span></p>
            <p>3. Spec & Design Gate (spec.md) <span class="tag">Approval Gate</span></p>
            <p>4. Pre-Implementation Oracle Verification <span class="tag">Baseline Check</span></p>
            <p>5. TDD Surgical Implementation <span class="tag">RED-GREEN-REFACTOR</span></p>
            <p>6. Isolated Review & QA Clearance <span class="tag">Reviewer + QA</span></p>
        </div>
        <div class="card">
            <h2>Current Session State</h2>
            <p><strong>Active Model Tier:</strong> <span style="color:var(--yellow)">Smart Tier (Sonnet/Opus)</span></p>
            <p><strong>TDD Status:</strong> <span style="color:var(--green)">Failing Test Created</span></p>
            <p><strong>Git Worktree:</strong> <code>.claude/worktrees/task-1</code></p>
            <p><strong>Credentials File:</strong> <code>.env.local</code></p>
        </div>
        <div class="card full">
            <h2>📄 Current Specification (spec.md)</h2>
            <pre id="spec">Loading spec.md...</pre>
        </div>
        <div class="card full">
            <h2>🤝 Session Handoff Log (handoff.md)</h2>
            <pre id="handoff">Loading handoff.md...</pre>
        </div>
    </div>

    <script>
        async function load() {
            try {
                const res = await fetch('/api/state');
                const data = await res.json();
                document.getElementById('spec').textContent = data.spec || 'No spec.md created yet.';
                document.getElementById('handoff').textContent = data.handoff || 'No handoff.md logged yet.';
            } catch (e) {}
        }
        load(); setInterval(load, 3000);
    </script>
</body>
</html>
\"\"\"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/state':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            spec = (CLAUDE_DIR / "spec.md").read_text() if (CLAUDE_DIR / "spec.md").exists() else "spec.md pending"
            handoff = (CLAUDE_DIR / "handoff.md").read_text() if (CLAUDE_DIR / "handoff.md").exists() else "handoff.md pending"
            self.wfile.write(json.dumps({"spec": spec, "handoff": handoff}).encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode('utf-8'))

if __name__ == "__main__":
    os.makedirs(CLAUDE_DIR, exist_ok=True)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Orchestrator + Superpowers Dashboard live at http://localhost:{PORT}")
        httpd.serve_forever()
"""
}

def setup():
    print("🚀 Initializing Claude Code Orchestrator + Superpowers (Option B)...")
    for path, content in FILES.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  ✓ Generated {path}")
    
    (CLAUDE_DIR / "screenshots").mkdir(exist_ok=True)
    print("\n✅ Setup Complete!")
    print("Run Dashboard: python3 .claude/dashboard.py")
    print("Launch Claude:  claude\n")

if __name__ == "__main__":
    setup()
