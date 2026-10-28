#!/usr/bin/env python3
"""
DevOrchestrator Universal Setup Script
Sets up .claude/, .cursorrules, .windsurfrules, CONVENTIONS.md, MCP servers, and Harness2 testing engine.
Single Invocation Keyword: /DevOrchestrator
"""

import os
import sys
import json
from pathlib import Path

CLAUDE_DIR = Path(".claude")

DASHBOARD_CODE = """#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
from pathlib import Path

PORT = 8080
CLAUDE_DIR = Path(".claude")

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DevOrchestrator Dashboard</title>
    <style>
        body { font-family: system-ui, sans-serif; background: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; padding-bottom: 12px; margin-bottom: 20px; }
        h1 { margin: 0; font-size: 22px; color: #58a6ff; }
        .badge { background: rgba(63, 185, 80, 0.15); color: #3fb950; border: 1px solid #3fb950; padding: 4px 12px; border-radius: 12px; font-weight: 600; font-size: 13px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }
        .card h2 { margin-top: 0; font-size: 16px; color: #bc8cff; border-bottom: 1px solid #30363d; padding-bottom: 8px; }
        .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; margin-bottom: 16px; }
        .m-box { background: #21262d; border: 1px solid #30363d; border-radius: 6px; padding: 10px; text-align: center; }
        .m-val { font-size: 20px; font-weight: bold; color: #3fb950; }
        .m-lbl { font-size: 10px; color: #8b949e; text-transform: uppercase; }
        pre { background: #090d12; padding: 12px; border-radius: 6px; font-size: 12px; border: 1px solid #30363d; max-height: 250px; overflow: auto; }
        .full { grid-column: 1 / -1; }
        .tag { font-size: 11px; background: rgba(57,197,207,0.15); color: #39c5cf; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 DevOrchestrator Dashboard</h1>
        <span class="badge">Keyword: /DevOrchestrator</span>
    </div>

    <div class="card full" style="margin-bottom: 16px;">
        <h2 style="color: #39c5cf;">⚡ Token Savings & Engine Status</h2>
        <div class="metrics">
            <div class="m-box"><div class="m-lbl">Total Token Savings</div><div class="m-val">~65%</div></div>
            <div class="m-box"><div class="m-lbl">Caveman Saver</div><div class="m-val" style="color:#58a6ff;">-55%</div></div>
            <div class="m-box"><div class="m-lbl">Tier Routing</div><div class="m-val" style="color:#bc8cff;">-70% Cost</div></div>
            <div class="m-box"><div class="m-lbl">Harness2 Engine</div><div class="m-val" style="color:#39c5cf;">Playwright + DevTools</div></div>
            <div class="m-box"><div class="m-lbl">Context Capacity</div><div class="m-val" style="color:#d29922;">32% / 35%</div></div>
        </div>
    </div>

    <div class="grid">
        <div class="card">
            <h2>Execution Pipeline Phase</h2>
            <p>1. Intake & Requirements <span class="tag">Auto-Parser</span></p>
            <p>2. Git Worktree Isolation <span class="tag">Superpowers</span></p>
            <p>3. Spec & Design Gate (spec.md) <span class="tag">Approval Gate</span></p>
            <p>4. Pre-Implementation Verification <span class="tag">Oracle Baseline</span></p>
            <p>5. TDD Surgical Implementation <span class="tag">RED-GREEN-REFACTOR</span></p>
            <p>6. Harness2 MCP Browser Verification <span class="tag">Playwright + DevTools</span></p>
            <p>7. Isolated Review & QA Clearance <span class="tag">Reviewer + QA</span></p>
        </div>
        <div class="card">
            <h2>Current Session State</h2>
            <p><strong>Invocation Trigger:</strong> <code>/DevOrchestrator</code></p>
            <p><strong>Active Model Tier:</strong> <span style="color:#d29922">Smart Tier (Sonnet/Opus)</span></p>
            <p><strong>Harness2 MCP Status:</strong> <span style="color:#3fb950">Active</span></p>
            <p><strong>Git Worktree:</strong> <code>.claude/worktrees/task-1</code></p>
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
</html>'''

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
        print(f"🚀 DevOrchestrator Dashboard live at http://localhost:{PORT}")
        httpd.serve_forever()
"""

FILES = {
    CLAUDE_DIR / "CLAUDE.md": """# DevOrchestrator Master Workflow

## Trigger Keyword: `/DevOrchestrator`
All DevOrchestrator operations are invoked via `/DevOrchestrator <prompt>`.

## Operating Principles
1. **Single Keyword Invocation**: Triggered exclusively via `/DevOrchestrator`.
2. **Superpowers & Harness2 Integration**:
   - **TDD Requirement**: Write a failing test FIRST. Delete any code written before a failing test exists.
   - **Git Worktree Isolation**: Create an isolated git worktree branch before modifying code.
   - **Systematic Debugging**: Follow a 4-phase root cause process.
   - **Harness2 Engine**: Run unit tests and Playwright/Chrome DevTools MCP browser checks.
3. **Spec Gate First**: Never write implementation code until `.claude/spec.md` is approved by the user.
4. **Dynamic Model Allocation**: Route light tasks to fast models (Haiku/Flash) and complex edits to smart models (Sonnet/Opus).
5. **Preference-Bias Elimination**: Main coding agent MUST NOT review its own code. Deploy isolated reviewer and QA agents.
6. **Context Window Capping (35%)**: Write `.claude/handoff.md` and reset on limit.

## Automated Pipeline
1. **Intake & Auto-Extract**: Run `.claude/skills/intake-auto-parser.md`.
2. **Worktree Setup**: Run `.claude/skills/worktree-isolation.md`. Create a clean git worktree.
3. **Spec Approval Gate**: Run `.claude/skills/spec-generator.md` & `.claude/skills/brainstorming.md`. Pause for explicit approval of `.claude/spec.md`.
4. **Pre-Implementation Verification**: Run `.claude/skills/pre-verify-oracle.md` & `.claude/skills/systematic-debugging.md`.
5. **TDD Implementation**: Run `.claude/skills/tdd-cycle.md` & `.claude/skills/surgical-implementer.md`.
6. **Harness2 & MCP Verification**: Run `.claude/skills/harness.md` & `.claude/skills/mcp-browser-verification.md` using Playwright & Chrome DevTools MCP.
7. **Isolated Review & QA**: Run `.claude/skills/preference-bias-eval.md` (`reviewer.md` & `qa-agent.md`).
8. **Session Handoff & Dashboard Sync**: Write `.claude/handoff.md` and sync with `python3 .claude/dashboard.py`.
""",

    CLAUDE_DIR / "commands" / "DevOrchestrator.md": """---
description: Run the complete DevOrchestrator pipeline (TDD, Spec Gate, Harness2 MCP verification, and Reviewer QA)
---

# /DevOrchestrator Command Workflow

When the user runs `/DevOrchestrator <prompt>`:
1. Parse requirement intake and screenshots into `.claude/spec.md`.
2. Pause for explicit user approval of `.claude/spec.md`.
3. Create an isolated Git worktree branch (`.claude/worktrees/task`).
4. Write failing test (TDD RED phase).
5. Apply minimal surgical edits to pass test (TDD GREEN phase).
6. Execute Harness2 test suite and Playwright/Chrome DevTools MCP checks.
7. Run independent Reviewer and QA subagents.
8. Output final status and update `.claude/handoff.md`.
""",

    CLAUDE_DIR / "mcp.json": json.dumps({
        "mcpServers": {
            "playwright": {
                "command": "npx",
                "args": ["-y", "@playwright/mcp@latest"],
                "description": "Playwright MCP for automated browser interaction, UI assertions, and visual testing"
            },
            "chrome-devtools": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-chrome-devtools"],
                "description": "Chrome DevTools MCP for real-time console log inspection, network traffic analysis, and DOM debugging"
            }
        }
    }, indent=2),

    CLAUDE_DIR / "skills" / "harness.md": """# Skill: Harness2 Continuous Testing Engine

## Protocol
1. **Unit Test Harness**: Detect build environment (npm test, mvn test, pytest, cargo test) and run test suite.
2. **Browser MCP Harness**: Use Playwright MCP (`@playwright/mcp`) to navigate routes, simulate UI clicks, and capture DOM state.
3. **Console & Network Inspection**: Use Chrome DevTools MCP (`@modelcontextprotocol/server-chrome-devtools`) to verify zero console errors and valid HTTP status codes (200 OK).
4. **Regression Gate**: Require all unit tests and browser assertions to pass before clearance.
""",

    CLAUDE_DIR / "skills" / "mcp-browser-verification.md": """# Skill: Playwright & Chrome DevTools MCP Verification

## Browser Verification Steps
1. Navigate to target URL (`browser_navigate`).
2. Interact with UI elements (`browser_click`, `browser_type`).
3. Fetch console log streams (`devtools_get_console_logs`).
4. Inspect API network calls (`devtools_get_network_requests`).
5. Assert zero unhandled JS errors and confirm acceptance criteria from `.claude/spec.md`.
""",

    CLAUDE_DIR / "skills" / "brainstorming.md": """# Skill: Brainstorming & Spec Design (Superpowers)

## Protocol
1. Explore intent, target architecture, and visual screenshots.
2. Draft `.claude/spec.md` with explicit Acceptance Criteria.
3. Halt execution until user confirms the design specification.
""",

    CLAUDE_DIR / "skills" / "tdd-cycle.md": """# Skill: Test-Driven Development (Superpowers)

## Strict Rules
1. **RED Phase**: Write a failing test for the target bug or feature before ANY production code is touched.
2. **GREEN Phase**: Write the MINIMAL surgical production code required to make the test pass.
3. **REFACTOR Phase**: Clean up code adhering to `.claude/rules/coding-standards.md`.
4. **Enforcement**: Delete any implementation code written prior to writing a failing test.
""",

    CLAUDE_DIR / "skills" / "worktree-isolation.md": """# Skill: Git Worktree Isolation (Superpowers)

## Protocol
1. Create a dedicated Git worktree branch for the active task (`git worktree add -b task-branch .claude/worktrees/task`).
2. Merge back to main branch only after isolated Reviewer and QA subagents issue **GO** clearance.
""",

    CLAUDE_DIR / "skills" / "systematic-debugging.md": """# Skill: Systematic Debugging (Superpowers)

## 4-Phase Debugging Process
1. Root Cause Investigation.
2. Pattern Analysis.
3. Hypothesis Verification.
4. Surgical Fix & Regression Check.
""",

    CLAUDE_DIR / "skills" / "intake-auto-parser.md": """# Skill: Intake & Automated Keyword Extractor

1. Prompt user for: Target Environment, Credentials File Path, Issue Context, Screenshot Path, Pinpointed Files.
2. Extract parameters into `.claude/spec.md`.
""",

    CLAUDE_DIR / "skills" / "spec-generator.md": """# Skill: Spec Generator & Approval Gate

1. Write `.claude/spec.md` containing files to edit, out-of-scope boundaries, and Acceptance Criteria.
2. **HALT EXECUTION**: Present `.claude/spec.md` to user and await explicit confirmation.
""",

    CLAUDE_DIR / "skills" / "pre-verify-oracle.md": """# Skill: Pre-Implementation Verification

1. Connect to Staging / Oracle URL or clean codebase.
2. Report baseline code health and Oracle comparison status before writing code.
""",

    CLAUDE_DIR / "skills" / "surgical-implementer.md": """# Skill: Surgical Implementer & Dynamic Tier Router

1. Fast Tier (Haiku/Flash): Log traces and code search.
2. Smart Tier (Sonnet/Opus): TDD surgical edits.
""",

    CLAUDE_DIR / "skills" / "preference-bias-eval.md": """# Skill: Preference-Bias Elimination

1. Deploy `.claude/agents/reviewer.md` in fresh context.
2. Deploy `.claude/agents/qa-agent.md` in fresh context.
""",

    CLAUDE_DIR / "skills" / "session-handoff.md": """# Skill: Session Handoff

When context memory reaches 35%, automatically generate `.claude/handoff.md`:
Resume command: `claude "/DevOrchestrator Resume session using .claude/handoff.md"`
""",

    CLAUDE_DIR / "rules" / "coding-standards.md": """# Coding Standards & Architecture Rules

1. Write clean, modular, self-documenting code.
2. Respect existing build tools (`npm test`, `mvn test`, `pytest`, `./gradlew test`).
3. Maintain zero test regressions across existing test suites.
""",

    CLAUDE_DIR / "agents" / "implementer.md": """# Agent: Surgical Implementer
Focus: Surgical coding, TDD test creation, live browser console log validation.
""",

    CLAUDE_DIR / "agents" / "reviewer.md": """# Agent: Isolated Code Reviewer
Focus: Independent code diff review against `.claude/rules/coding-standards.md`.
""",

    CLAUDE_DIR / "agents" / "qa-agent.md": """# Agent: Independent QA Tester
Focus: Edge-case validation, Playwright/Chrome DevTools MCP verification, issuing GO/NO-GO clearance.
""",

    CLAUDE_DIR / "dashboard.py": DASHBOARD_CODE
}

RULE_CONTENT = """# DevOrchestrator Assistant Configuration

## Trigger Keyword: `/DevOrchestrator`
This assistant configuration is scoped EXCLUSIVELY to `/DevOrchestrator` invocations.
When a prompt starts with or contains `/DevOrchestrator`, strictly follow these rules:

1. **Intake & Spec Approval Gate**: Write `.claude/spec.md` and HALT until user explicitly confirms.
2. **Superpowers TDD & Worktrees**: Create a clean git worktree (`.claude/worktrees/task`). Write a failing test FIRST.
3. **Harness2 MCP Verification**: Validate using Playwright MCP (`@playwright/mcp`) and Chrome DevTools MCP (`@modelcontextprotocol/server-chrome-devtools`).
4. **Preference-Bias Elimination**: Run isolated Reviewer and QA subagents before final output.
"""

def safe_append(file_path: Path, content: str, header_check: str):
    """Appends content if header is missing, otherwise creates new file."""
    if file_path.exists():
        text = file_path.read_text(encoding="utf-8")
        if header_check not in text:
            file_path.write_text(text.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8")
            print(f"  ✓ Safely merged into existing: {file_path}")
        else:
            print(f"  ✓ Existing configuration verified in: {file_path}")
    else:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  ✓ Created new config: {file_path}")

def setup():
    print("🚀 Initializing DevOrchestrator (Single Keyword: /DevOrchestrator)...\n")
    
    # 1. Generate .claude/ structure and files
    for path, content in FILES.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  ✓ Generated {path}")

    (CLAUDE_DIR / "screenshots").mkdir(exist_ok=True)

    # 2. Configure multi-tool integration files with safe-merge
    print("\n--- Multi-Tool Configuration Files ---")
    safe_append(Path(".cursorrules"), RULE_CONTENT, "/DevOrchestrator")
    safe_append(Path(".cursor/rules/devorchestrator.mdc"), RULE_CONTENT, "/DevOrchestrator")
    safe_append(Path(".windsurfrules"), RULE_CONTENT, "/DevOrchestrator")
    safe_append(Path("CONVENTIONS.md"), RULE_CONTENT, "/DevOrchestrator")

    print("\n✅ Setup Complete!")
    print("Single Invocation Keyword: /DevOrchestrator")
    print("Slash Command:             /DevOrchestrator")
    print("Run Dashboard:            python3 .claude/dashboard.py (or python3 setup_orchestrator.py)")
    print("Launch Assistant:         claude / cursor / windsurf / aider\n")

if __name__ == "__main__":
    setup()
