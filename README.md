# 🤖 AI Coding Orchestrator + Superpowers + MCP

> **Ship complex features and surgical bug fixes in a SINGLE prompt across Claude Code, Cursor, Windsurf, and Aider.**
> An agentic workflow combining interactive requirement intake, `spec.md` contract gates, `caveman` token compression, dynamic multi-model tier routing, **obra/superpowers** TDD & Worktree methodology, and **Playwright & Chrome DevTools MCP** automated browser testing.

---

## 🌟 Key Features

* **Multi-Tool Native Support**: Works seamlessly across **Claude Code Terminal & Desktop** (`.claude/`), **Cursor** (`.cursorrules` & `.cursor/rules/`), **Windsurf** (`.windsurfrules`), and **Aider / Copilot** (`CONVENTIONS.md`).
* **Superpowers TDD & Worktree Engine**:
  * **Strict TDD Cycle**: Mandates RED ➔ GREEN ➔ REFACTOR cycles. Automatically deletes implementation code written prior to writing a failing test.
  * **Git Worktree Isolation**: Spawns clean `.claude/worktrees/task-N` branches to keep your main development branch untouched.
  * **Systematic Debugging**: Enforces a 4-phase root-cause analysis before making speculative edits.
* **Automated Browser Verification (Playwright & Chrome DevTools MCP)**:
  * Uses **Playwright MCP** (`@playwright/mcp`) for DOM snapshots, visual assertions, and user interactions.
  * Uses **Chrome DevTools MCP** (`@modelcontextprotocol/server-chrome-devtools`) to inspect live console logs, network payloads, and HTTP status codes before declaring a fix complete.
* **Spec Gate Approval (`spec.md`)**: Generates a pre-coding specification and **halts execution** for your explicit approval before modifying production code.
* **Dynamic Model Tier Routing**: Automatically detects your available API models and routes fast tasks (file searches, log traces) to cheap models (Haiku/Flash/GPT-4o-mini) and surgical edits to premium models (Sonnet/Opus/GPT-4o), reducing costs by ~70%.
* **Safe-Merge Setup**: The installer safely appends orchestrator rules to existing `.cursorrules` or `.claude/CLAUDE.md` files without overwriting existing project rules.
* **Live Inspection Dashboard (`http://localhost:8080`)**: Zero-dependency Python server visualizing pipeline steps, active model tiers, spec status, handoff state, and token analytics.

---

## 🚀 Installation & Setup

### 1. Quick Setup for This Repository

No `chmod` or executable permissions required. Simply run the universal Python setup script:

```bash
python3 setup_orchestrator.py
```

### 2. Using in Other Projects / Existing Codebases

To add this orchestrator and Superpowers framework to any of your existing projects (Java, React, Python, Go, Node.js, etc.):

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Dave-1/Dev_orchestrator.git
   ```
2. **Navigate to your existing project directory** and run the installer:
   ```bash
   cd /path/to/your-existing-project
   python3 /path/to/Dev_orchestrator/setup_orchestrator.py
   ```
3. **Start coding** with your preferred AI tool:
   ```bash
   claude        # For Claude Code
   cursor .      # For Cursor
   windsurf .    # For Windsurf
   ```

---

## 💻 Daily Usage

Launch your preferred AI tool in terminal or desktop and prompt naturally—the orchestrator automatically executes behind the scenes:

```text
Fix the checkout button error on the /checkout page when discountCode is null.
```

### What Happens Automatically:
1. **Intake & Auto-Extract**: Prompts for target environment, credentials/env file path, context, screenshot path, and target file pinpointing.
2. **Worktree & Spec Gate**: Spawns an isolated git worktree, writes `.claude/spec.md`, and **pauses for your approval**.
3. **Pre-Implementation Verification**: Runs baseline tests and checks Oracle/Staging status before editing code.
4. **TDD Surgical Edit**: Writes a failing test (`RED`), applies minimal surgical edits (`GREEN`), and cleans code (`REFACTOR`).
5. **MCP Browser & Console Verification**: QA Agent uses Playwright MCP and Chrome DevTools MCP to verify live DOM state, console errors, and HTTP status codes.
6. **Isolated Review & QA**: Reviewer sub-agent verifies code quality against standards before issuing a GO decision.
7. **Handoff**: Writes `.claude/handoff.md` and updates the live Python dashboard.

---

## 📂 Project Structure

```text
.
├── setup_orchestrator.py            # Universal Python installer (safe-merge)
├── setup-orchestrator.sh            # Shell launcher script
├── README.md                        # Project documentation
├── .cursorrules                     # Cursor rules (auto-generated)
├── .windsurfrules                  # Windsurf rules (auto-generated)
├── CONVENTIONS.md                   # Aider / Copilot rules (auto-generated)
└── .claude/
    ├── CLAUDE.md                    # Core orchestrator initialization rules
    ├── mcp.json                     # Playwright & Chrome DevTools MCP config
    ├── spec.md                      # Auto-generated plan & contract gate
    ├── handoff.md                   # Multi-session continuity log
    ├── screenshots/                 # Folder for visual error screenshots
    ├── dashboard.py                 # Live inspection HTTP server
    ├── rules/
    │   └── coding-standards.md      # Externalized coding conventions
    ├── skills/
    │   ├── tdd-cycle.md             # Superpowers TDD engine
    │   ├── worktree-isolation.md    # Superpowers git worktree manager
    │   ├── systematic-debugging.md  # Superpowers 4-phase root cause debugger
    │   ├── mcp-browser-verification.md # Playwright & Chrome DevTools MCP testing
    │   ├── intake-auto-parser.md    # Interactive intake & keyword extractor
    │   ├── spec-generator.md        # Plan phase explorer & user approval gate
    │   ├── pre-verify-oracle.md     # Baseline code & Oracle regression checker
    │   ├── surgical-implementer.md  # Model tier router & browser logger
    │   ├── preference-bias-eval.md  # Preference bias elimination (Reviewer & QA)
    │   └── session-handoff.md       # Automatic handoff log writer
    └── agents/
        ├── implementer.md           # Primary coding agent
        ├── reviewer.md              # Isolated code reviewer
        └── qa-agent.md              # Independent QA tester
```

---

## 📊 Token Usage & Cost Savings

| Optimization Mechanism | Token / Cost Impact |
| :--- | :--- |
| **Caveman Compression** | ~55% reduction in inter-agent communication tokens |
| **Dynamic Tiered Routing** | ~70% reduction in API costs (Fast models for log/trace tasks) |
| **Context Window Capping (35%)** | Prevents quadratic token expansion and context degradation |
| **Isolated Sub-Agent Contexts** | Eliminates 30k+ tokens of bloated chat history per turn |
| **Total Combined Savings** | **~65%–80% reduction in total token spend vs. standard chat** |

---

## 🛡️ License

MIT License. Feel free to fork and adapt for your team's workflow!
