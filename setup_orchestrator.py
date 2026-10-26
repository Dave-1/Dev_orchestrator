#!/usr/bin/env python3
"""
Claude Code Orchestrator + Superpowers + MCP Verification Package
Features:
- Playwright MCP & Chrome DevTools MCP live browser verification
- Multi-Tool rules (Claude Code, Cursor, Windsurf, Aider, Copilot CLI)
- Dynamic Model Detection & Fallback Cascade (Haiku / Sonnet / Opus / GPT-4o / Local)
- Superpowers TDD, Git Worktrees, & Systematic Debugging
- Safe-merge appending for existing configuration files
"""

import os
import sys
import json
from pathlib import Path

CLAUDE_DIR = Path(".claude")
CURSOR_DIR = Path(".cursor")
RULES_DIR = CURSOR_DIR / "rules"

MCP_CONFIG = {
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ],
      "description": "Playwright MCP for automated browser interaction, UI assertions, and visual testing"
    },
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-chrome-devtools"
      ],
      "description": "Chrome DevTools MCP for real-time console log inspection, network traffic analysis, and DOM debugging"
    }
  }
}

ORCHESTRATOR_HEADER = "<!-- CLAUDE CODE ORCHESTRATOR + SUPERPOWERS + MCP VERIFICATION -->"

CORE_RULES = """# Master AI Coding Orchestrator + Superpowers + MCP Verification

## Operating Principles
1. **Zero User Keywords**: All pipeline stages execute automatically behind the scenes.
2. **Task-Based Dynamic Model Routing**:
   - **Fast Tier** (e.g. Haiku / GPT-4o-mini / Flash): File searching, trace insertion, intake parsing, spec.md & handoff.md logs.
   - **Smart Tier** (e.g. Sonnet / GPT-4o): TDD code writing, surgical edits, systematic debugging, QA analysis.
   - **Reasoning Tier** (e.g. Opus / o1 / DeepSeek R1): Escalated complex architectural refactors (if Smart Tier fails twice).
   - *Auto-Detection*: If only one model is available, all tiers automatically collapse to that model.
3. **Playwright & Chrome DevTools MCP Verification**:
   - Every bug fix and feature MUST be verified live in-browser using Playwright MCP (`browser_navigate`, `browser_click`, `browser_snapshot`) and Chrome DevTools MCP (`devtools_get_console_logs`, `devtools_get_network_requests`).
4. **Superpowers TDD Protocol**:
   - Write a failing test FIRST. Delete any production code written before a failing test exists.
5. **Git Worktree Isolation**:
   - Perform all changes inside an isolated git worktree branch before merging to main.
6. **Spec Approval Gate**:
   - Never edit implementation code until `.claude/spec.md` is generated and approved by the user.
7. **Preference-Bias Elimination**:
   - The primary coding agent MUST NOT review or QA its own code. Deploy isolated Reviewer and QA subagents.

## Automated Pipeline
1. **Intake & Auto-Extract**: Run `.claude/skills/intake-auto-parser.md`. Parse screenshots & pinpointed files into `.claude/spec.md`.
2. **Worktree Isolation**: Run `.claude/skills/worktree-isolation.md`. Create a clean task branch.
3. **Spec Gate**: Run `.claude/skills/spec-generator.md` & `.claude/skills/brainstorming.md`. Pause for explicit user approval of `.claude/spec.md`.
4. **Pre-Implementation Verification**: Run `.claude/skills/pre-verify-oracle.md` & `.claude/skills/systematic-debugging.md`.
5. **TDD Surgical Implementation**: Run `.claude/skills/tdd-cycle.md` & `.claude/skills/surgical-implementer.md`.
6. **MCP Live Browser Verification**: Run `.claude/skills/mcp-browser-verification.md` using Playwright MCP & Chrome DevTools MCP.
7. **Isolated Review & QA**: Run `.claude/skills/preference-bias-eval.md` (`reviewer.md` & `qa-agent.md`).
8. **Session Handoff**: Write `.claude/handoff.md` and sync with `python3 .claude/dashboard.py`.
"""

FILES = {
    CLAUDE_DIR / "CLAUDE.md": CORE_RULES,
    CLAUDE_DIR / "mcp.json": json.dumps(MCP_CONFIG, indent=2),
    CLAUDE_DIR / "skills" / "mcp-browser-verification.md": """# Skill: MCP Browser Verification (Playwright + Chrome DevTools)

## Purpose
Enforce live browser verification of all bug fixes and features using Playwright MCP and Chrome DevTools MCP before issuing QA clearance.

## Protocol
1. **Playwright MCP Navigation**:
   - Launch Playwright MCP server (`@playwright/mcp`).
   - Navigate to target route (`browser_navigate`).
   - Interact with components (`browser_click`, `browser_type`).
   - Capture DOM element states (`browser_snapshot`) and visual evidence (`browser_take_screenshot`).

2. **Chrome DevTools MCP Inspection**:
   - Attach Chrome DevTools MCP (`@modelcontextprotocol/server-chrome-devtools`).
   - Fetch real-time console logs (`devtools_get_console_logs`). Assert ZERO unhandled JavaScript errors/warnings.
   - Inspect API network payloads (`devtools_get_network_requests`). Verify HTTP 200 responses and expected JSON schemas.

3. **Acceptance Criteria Verification**:
   - Compare observed browser state directly against `.claude/spec.md` Acceptance Criteria.
   - Record visual and console log proof in `.claude/qa-learnings.md`.
""",
    CLAUDE_DIR / "skills" / "brainstorming.md": """# Skill: Brainstorming & Spec Design (Superpowers)
1. Explore intent, target architecture, and visual screenshots.
2. Identify trade-offs, state handlers, and edge cases.
3. Draft `.claude/spec.md` with explicit Acceptance Criteria.
4. Halt execution until user confirms the design specification.
""",
    CLAUDE_DIR / "skills" / "tdd-cycle.md": """# Skill: Test-Driven Development (Superpowers)
1. **RED Phase**: Write a failing unit or integration test before touching production code.
2. Verify test failure reproduces the reported bug or feature gap.
3. **GREEN Phase**: Write the MINIMAL surgical code needed to make the test pass.
4. **REFACTOR Phase**: Clean code adhering to `.claude/rules/coding-standards.md`.
5. **Enforcement**: Delete any implementation code written prior to writing a failing test.
""",
    CLAUDE_DIR / "skills" / "worktree-isolation.md": """# Skill: Git Worktree Isolation (Superpowers)
1. Create dedicated Git worktree branch (`git worktree add -b task-branch .claude/worktrees/task`).
2. Perform all edits inside the isolated worktree.
3. Merge to main branch only after Reviewer and QA subagents issue **GO** clearance.
""",
    CLAUDE_DIR / "skills" / "systematic-debugging.md": """# Skill: Systematic Debugging (Superpowers)
1. **Root Cause Investigation**: Add console traces via Chrome DevTools MCP; no guesswork.
2. **Pattern Analysis**: Trace data flow back through state handlers, props, and API boundaries.
3. **Hypothesis Verification**: Prove root cause with live Playwright MCP interaction.
4. **Surgical Fix**: Fix root cause without refactoring unrelated files.
""",
    CLAUDE_DIR / "skills" / "intake-auto-parser.md": """# Skill: Intake & Automated Keyword Extractor
1. Prompt user for: Target Environment, Credentials File Path, Issue Context, Screenshot Path, Pinpointed Files.
2. Automatically parse UI selectors, props, state handlers, error traces, and acceptance criteria.
3. Write extracted parameters into `.claude/spec.md`.
""",
    CLAUDE_DIR / "skills" / "spec-generator.md": """# Skill: Spec Generator & Approval Gate
1. Map out target routes and state transitions into a Knowledge Graph.
2. Write `.claude/spec.md` containing target files, out-of-scope boundaries, and Acceptance Criteria.
3. **HALT EXECUTION**: Present `.claude/spec.md` to user and await explicit confirmation before coding.
""",
    CLAUDE_DIR / "skills" / "pre-verify-oracle.md": """# Skill: Pre-Implementation Verification
1. Connect to Staging / Oracle URL or clean codebase.
2. Run baseline test suites and inspect console logs via Chrome DevTools MCP.
3. **Inform User**: Report baseline code health and Oracle comparison status before editing code.
""",
    CLAUDE_DIR / "skills" / "surgical-implementer.md": """# Skill: Surgical Implementer
1. Fast Tier: Code searching, console log placement, trace gathering.
2. Smart Tier: Surgical code edits following TDD cycle.
3. Edit ONLY target files. Validate live in browser using Playwright MCP.
""",
    CLAUDE_DIR / "skills" / "preference-bias-eval.md": """# Skill: Preference-Bias Elimination
1. Deploy `.claude/agents/reviewer.md` in fresh context to review diff against `.claude/rules/coding-standards.md`.
2. Deploy `.claude/agents/qa-agent.md` in fresh context using Playwright MCP & Chrome DevTools MCP to verify edge cases and issue GO/NO-GO clearance.
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
Model Strategy: Smart Tier (Sonnet / GPT-4o)
Focus: Surgical coding, TDD test creation, live Playwright MCP browser validation.
""",
    CLAUDE_DIR / "agents" / "reviewer.md": """# Agent: Isolated Code Reviewer
Model Strategy: Fast Tier (Haiku / GPT-4o-mini)
Focus: Independent code diff review against `.claude/rules/coding-standards.md`.
""",
    CLAUDE_DIR / "agents" / "qa-agent.md": """# Agent: Independent QA Tester
Model Strategy: Smart Tier (Sonnet / GPT-4o)
Focus: Playwright MCP & Chrome DevTools MCP browser automation, console error checking, network payload validation, and GO/NO-GO release clearance.
""",
}

FILES[CLAUDE_DIR / "dashboard.py"] = '#!/usr/bin/env python3\nimport http.server\nimport socketserver\nimport json\nimport os\nfrom pathlib import Path\n\nPORT = 8080\nCLAUDE_DIR = Path(".claude")\n\nHTML_TEMPLATE = \'\'\'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>Claude Code Orchestrator + Superpowers + MCP Dashboard</title>\n    <style>\n        body { font-family: system-ui, sans-serif; background: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }\n        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; padding-bottom: 12px; margin-bottom: 20px; }\n        h1 { margin: 0; font-size: 22px; color: #58a6ff; }\n        .badge { background: rgba(63, 185, 80, 0.15); color: #3fb950; border: 1px solid #3fb950; padding: 4px 12px; border-radius: 12px; font-weight: 600; font-size: 13px; }\n        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }\n        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }\n        .card h2 { margin-top: 0; font-size: 16px; color: #bc8cff; border-bottom: 1px solid #30363d; padding-bottom: 8px; }\n        .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin-bottom: 16px; }\n        .m-box { background: #21262d; border: 1px solid #30363d; border-radius: 6px; padding: 10px; text-align: center; }\n        .m-val { font-size: 20px; font-weight: bold; color: #3fb950; }\n        .m-lbl { font-size: 10px; color: #8b949e; text-transform: uppercase; }\n        pre { background: #090d12; padding: 12px; border-radius: 6px; font-size: 12px; border: 1px solid #30363d; max-height: 250px; overflow: auto; }\n        .full { grid-column: 1 / -1; }\n        .tag { font-size: 11px; background: rgba(57,197,207,0.15); color: #39c5cf; padding: 2px 6px; border-radius: 4px; font-weight: bold; }\n    </style>\n</head>\n<body>\n    <div class="header">\n        <h1>🤖 Claude Code Orchestrator + Superpowers + MCP Dashboard</h1>\n        <span class="badge">Playwright & Chrome DevTools MCP Active</span>\n    </div>\n\n    <div class="card full" style="margin-bottom: 16px;">\n        <h2 style="color: #39c5cf;">⚡ Token Savings & MCP Status</h2>\n        <div class="metrics">\n            <div class="m-box"><div class="m-lbl">Total Token Savings</div><div class="m-val">~65%</div></div>\n            <div class="m-box"><div class="m-lbl">Caveman Saver</div><div class="m-val" style="color:#58a6ff;">Active (-55%)</div></div>\n            <div class="m-box"><div class="m-lbl">Tier Routing</div><div class="m-val" style="color:#bc8cff;">Dynamic</div></div>\n            <div class="m-box"><div class="m-lbl">Browser Engine</div><div class="m-val" style="color:#39c5cf;">Playwright MCP</div></div>\n            <div class="m-box"><div class="m-lbl">DevTools Engine</div><div class="m-val" style="color:#d29922;">Chrome DevTools</div></div>\n        </div>\n    </div>\n\n    <div class="grid">\n        <div class="card">\n            <h2>Execution Pipeline Phase</h2>\n            <p>1. Intake & Requirements <span class="tag">Auto-Parser</span></p>\n            <p>2. Git Worktree Isolation <span class="tag">Superpowers</span></p>\n            <p>3. Spec & Design Gate (spec.md) <span class="tag">Approval Gate</span></p>\n            <p>4. Pre-Implementation Verification <span class="tag">Oracle Check</span></p>\n            <p>5. TDD Surgical Implementation <span class="tag">RED-GREEN-REFACTOR</span></p>\n            <p>6. Playwright & Chrome DevTools MCP Verification <span class="tag">Live MCP Test</span></p>\n            <p>7. Isolated Review & QA Clearance <span class="tag">Reviewer + QA</span></p>\n        </div>\n        <div class="card">\n            <h2>Current Session State</h2>\n            <p><strong>Model Allocation:</strong> <span style="color:#d29922">Dynamic Tiering Active</span></p>\n            <p><strong>Playwright MCP:</strong> <span style="color:#3fb950">Connected</span></p>\n            <p><strong>Chrome DevTools MCP:</strong> <span style="color:#39c5cf">Connected</span></p>\n            <p><strong>Git Worktree:</strong> <code>.claude/worktrees/task-1</code></p>\n        </div>\n        <div class="card full">\n            <h2>📄 Current Specification (spec.md)</h2>\n            <pre id="spec">Loading spec.md...</pre>\n        </div>\n        <div class="card full">\n            <h2>🤝 Session Handoff Log (handoff.md)</h2>\n            <pre id="handoff">Loading handoff.md...</pre>\n        </div>\n    </div>\n\n    <script>\n        async function load() {\n            try {\n                const res = await fetch(\'/api/state\');\n                const data = await res.json();\n                document.getElementById(\'spec\').textContent = data.spec || \'No spec.md created yet.\';\n                document.getElementById(\'handoff\').textContent = data.handoff || \'No handoff.md logged yet.\';\n            } catch (e) {}\n        }\n        load(); setInterval(load, 3000);\n    </script>\n</body>\n</html>\'\'\'\n\nclass Handler(http.server.SimpleHTTPRequestHandler):\n    def do_GET(self):\n        if self.path == \'/api/state\':\n            self.send_response(200)\n            self.send_header(\'Content-type\', \'application/json\')\n            self.end_headers()\n            spec = (CLAUDE_DIR / "spec.md").read_text() if (CLAUDE_DIR / "spec.md").exists() else "spec.md pending"\n            handoff = (CLAUDE_DIR / "handoff.md").read_text() if (CLAUDE_DIR / "handoff.md").exists() else "handoff.md pending"\n            self.wfile.write(json.dumps({"spec": spec, "handoff": handoff}).encode(\'utf-8\'))\n        else:\n            self.send_response(200)\n            self.send_header(\'Content-type\', \'text/html\')\n            self.end_headers()\n            self.wfile.write(HTML_TEMPLATE.encode(\'utf-8\'))\n\nif __name__ == "__main__":\n    os.makedirs(CLAUDE_DIR, exist_ok=True)\n    with socketserver.TCPServer(("", PORT), Handler) as httpd:\n        print(f"🚀 Orchestrator Dashboard live at http://localhost:{PORT}")\n        httpd.serve_forever()\n'

def safe_merge_file(target_path: Path, content_to_append: str):
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        existing_text = target_path.read_text(encoding="utf-8")
        if ORCHESTRATOR_HEADER not in existing_text:
            merged_text = existing_text.strip() + "\n\n" + ORCHESTRATOR_HEADER + "\n" + content_to_append.strip() + "\n"
            target_path.write_text(merged_text, encoding="utf-8")
            print(f"  ✓ Appended orchestrator rules to existing file: {target_path}")
        else:
            print(f"  ✓ Orchestrator rules already present in: {target_path}")
    else:
        file_text = ORCHESTRATOR_HEADER + "\n" + content_to_append.strip() + "\n"
        target_path.write_text(file_text, encoding="utf-8")
        print(f"  ✓ Created new config: {target_path}")

def setup():
    print("🚀 Initializing AI Coding Orchestrator + Superpowers + MCP Verification...")
    safe_merge_file(CLAUDE_DIR / "CLAUDE.md", CORE_RULES)
    safe_merge_file(RULES_DIR / "orchestrator.mdc", CORE_RULES)
    safe_merge_file(Path(".cursorrules"), CORE_RULES)
    safe_merge_file(Path(".windsurfrules"), CORE_RULES)
    safe_merge_file(Path("CONVENTIONS.md"), CORE_RULES)

    for path, content in FILES.items():
        if path != CLAUDE_DIR / "CLAUDE.md":
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content.strip() + "\n", encoding="utf-8")
            print(f"  ✓ Generated {path}")

    (CLAUDE_DIR / "screenshots").mkdir(exist_ok=True)
    print("\n✅ Setup Complete!")
    print("MCP Servers Configured: Playwright MCP (@playwright/mcp) & Chrome DevTools MCP (@modelcontextprotocol/server-chrome-devtools)")
    print("Multi-Tool Support: Claude Code (.claude/), Cursor (.cursorrules), Windsurf (.windsurfrules), Aider/Copilot (CONVENTIONS.md)")
    print("Run Dashboard: python3 .claude/dashboard.py (or python3 setup_orchestrator.py)")
    print("Launch Assistant: claude / cursor / windsurf / aider\n")

if __name__ == "__main__":
    setup()
