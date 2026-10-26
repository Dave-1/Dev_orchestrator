# AI Coding Orchestrator + Superpowers + Playwright & Chrome DevTools MCP

> An open-source, multi-tool AI software engineering orchestrator. Enforces interactive requirements intake, **Playwright MCP** & **Chrome DevTools MCP** live browser verification, **Superpowers TDD** test-driven execution, **Git worktree isolation**, and **preference-bias elimination** across Claude Code, Cursor, Windsurf, Aider, and Copilot CLI.

---

## 🌟 Key Features

* 🎭 **Playwright MCP & Chrome DevTools MCP Live Verification**: Automatically tests UI interactions, element snapshots, console errors, and HTTP network payloads in a live browser before issuing QA clearance.
* ⚡ **Task-Based Dynamic Model Routing**:
  * **Fast Tier** (*Haiku / GPT-4o-mini / Flash*): High-speed file searching, console log tracing, and intake parsing.
  * **Smart Tier** (*Sonnet / GPT-4o*): TDD unit test creation, surgical edits, systematic debugging, and QA analysis.
  * **Reasoning Tier** (*Opus / o1 / DeepSeek R1*): Architectural escalation if Smart Tier fails twice.
  * *Auto-Collapse*: Automatically runs seamlessly if a user has access to only a single model.
* 🛡️ **Superpowers TDD Protocol**: Enforces strict **RED ➔ GREEN ➔ REFACTOR** cycles. Requires a failing test *before* implementation code is touched.
* 🌲 **Git Worktree Isolation**: Executes all code edits in an isolated task branch (`.claude/worktrees/task`), keeping main branches clean.
* 🛑 **Spec Approval Gate**: Auto-generates `.claude/spec.md` and halts execution for explicit user confirmation before any code is modified.
* 🧩 **Multi-Tool Native Compatibility**: Safely merges rules into **Claude Code** (`.claude/CLAUDE.md`), **Cursor** (`.cursorrules`), **Windsurf** (`.windsurfrules`), and **Aider / Copilot** (`CONVENTIONS.md`).
* 📊 **Live Browser Inspection Dashboard**: Lightweight Python HTTP dashboard at `http://localhost:8080` displaying live pipeline steps, model routing, token savings (~65%), `spec.md`, and `handoff.md`.

---

## 🚀 Quick Start (1 Command)

No `chmod` or special execution permissions required. Run inside any project repository:

```bash
python3 setup_orchestrator.py
```

### Starting the Live Inspection Dashboard

```bash
python3 .claude/dashboard.py
```
Open **`http://localhost:8080`** in your browser to view live execution metrics.

---

## 🔄 Automated Execution Pipeline

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Intake & Auto-Extract (`intake-auto-parser.md`)                                    │
│    • Prompts for env, credentials file, context, screenshots, and target files.       │
│    • Auto-derives components, API routes, and acceptance criteria.                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Git Worktree Isolation (`worktree-isolation.md`)                                   │
│    • Spawns clean `.claude/worktrees/task-1` branch automatically.                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Spec & Design Approval Gate (`spec-generator.md` & `brainstorming.md`)              │
│    • Writes `.claude/spec.md` and HALTS execution until user approves.                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. Pre-Implementation Verification (`pre-verify-oracle.md` & `systematic-debugging.md`) │
│    • Compares clean codebase against Oracle/Staging and reports baseline state.        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 5. TDD Surgical Implementation (`tdd-cycle.md` & `surgical-implementer.md`)            │
│    • Writes failing test ➔ Minimal surgical code ➔ Live browser console validation.   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 6. Playwright & Chrome DevTools MCP Verification (`mcp-browser-verification.md`)       │
│    • Executes automated end-to-end clicks, DOM assertions, console error checks,       │
│      and API network payload validation using Playwright MCP & Chrome DevTools MCP.    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 7. Preference-Bias Elimination (`preference-bias-eval.md`)                             │
│    • Launches isolated Reviewer & QA subagents for final GO/NO-GO clearance.           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 8. Automatic Session Handoff (`session-handoff.md`)                                    │
│    • Writes `.claude/handoff.md` and syncs with Python inspection dashboard.          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔌 Model Context Protocol (MCP) Integration

The setup script automatically configures `.claude/mcp.json` with Playwright and Chrome DevTools MCP servers:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-chrome-devtools"]
    }
  }
}
```

---

## 📁 Repository Structure

```text
.
├── setup_orchestrator.py             # Universal Python installer (Safe-merge + Multi-Tool)
├── setup-orchestrator.sh             # Shell launcher script
├── README.md                         # Project documentation
└── .claude/
    ├── CLAUDE.md                     # Master orchestrator instructions
    ├── mcp.json                      # Playwright & Chrome DevTools MCP config
    ├── spec.md                       # Auto-generated contract & plan gate
    ├── handoff.md                    # Auto-generated session log
    ├── dashboard.py                  # Live HTTP inspection dashboard
    ├── rules/
    │   └── coding-standards.md       # Architecture & lint rules
    ├── skills/
    │   ├── mcp-browser-verification.md
    │   ├── brainstorming.md
    │   ├── tdd-cycle.md
    │   ├── worktree-isolation.md
    │   ├── systematic-debugging.md
    │   ├── intake-auto-parser.md
    │   ├── spec-generator.md
    │   ├── pre-verify-oracle.md
    │   ├── surgical-implementer.md
    │   ├── preference-bias-eval.md
    │   └── session-handoff.md
    └── agents/
        ├── implementer.md            # Surgical coding agent
        ├── reviewer.md               # Isolated code review agent
        └── qa-agent.md               # Independent QA agent (Playwright + Chrome DevTools)
```

---

## 📄 License

MIT License. Free for open-source and commercial use.
