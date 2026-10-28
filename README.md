# 🤖 DevOrchestrator

> **Ship complex features and surgical bug fixes in a SINGLE prompt using `/DevOrchestrator`.**
> An agentic workflow for **Claude Code, Cursor, Windsurf, and Aider/Copilot** combining requirement intake, TDD cycles, `spec.md` contract approval, `handoff.md` state persistence, Harness² continuous browser testing, and embedded software engineering skills from [obra/superpowers](https://github.com/obra/superpowers).

---

## 🌟 Key Features

* **Single Keyword Invocation (`/DevOrchestrator`)**: Scoped exclusively to `/DevOrchestrator <prompt>` so it won't conflict with other installed plugins.
* **Harness² Engine**: Automates unit test suites and connects Playwright MCP (`@playwright/mcp`) & Chrome DevTools MCP (`@modelcontextprotocol/server-chrome-devtools`) to inspect real-time DOM states, network HTTP payloads, and browser console logs.
* **Superpowers TDD & Worktree Engine**:
  * **Strict TDD Cycle**: Mandates RED ➔ GREEN ➔ REFACTOR cycles. Deletes implementation code written prior to writing a failing test.
  * **Git Worktree Isolation**: Spawns clean `.claude/worktrees/task-N` branches to keep main development branches clean.
  * **Systematic Debugging**: Enforces a 4-phase root-cause investigation before making speculative edits.
* **Spec Gate Approval (`spec.md`)**: Generates pre-coding contract and **halts execution** for your explicit confirmation before modifying code.
* **Dynamic Model Allocation**: Routes light tasks (logs, file search) to fast models (Haiku/Flash) and surgical edits to smart models (Sonnet/Opus).
* **Multi-Tool Native Support**: Configures `.claude/CLAUDE.md`, `.cursorrules`, `.windsurfrules`, and `CONVENTIONS.md` with safe-merge appending.
* **Live Inspection Dashboard (`http://localhost:8080`)**: Zero-dependency Python server visualizing pipeline steps, spec status, handoff state, and token analytics.

---

## 🚀 Quick Start & Installation

No `chmod` or special permissions required. Simply run the Python setup script:

```bash
python3 setup_orchestrator.py
```

### Using in Other Projects / Existing Codebases
1. Clone this repository:
   ```bash
   git clone https://github.com/Dave-1/Dev_orchestrator.git
   ```

2. Run the installer inside your existing project directory:
   ```bash
   cd /path/to/your-project
   python3 /path/to/Dev_orchestrator/setup_orchestrator.py
   ```

3. Launch your preferred AI tool and invoke using `/DevOrchestrator`:
   ```bash
   claude                   # Type: /DevOrchestrator Fix checkout button
   cursor .                 # Type: /DevOrchestrator Fix checkout button
   windsurf .               # Type: /DevOrchestrator Fix checkout button
   ```

---

## 💻 Usage & Command

In **Claude Code**, use the slash command:

```bash
/DevOrchestrator Fix NullPointerException in UserPaymentController when discountCode is null.
```

In **Cursor**, **Windsurf**, or **Aider**, prefix your prompt with `/DevOrchestrator`:

```text
/DevOrchestrator Add dark mode toggle to navigation header
```

---

## 📂 Project Structure

```text
.
├── setup_orchestrator.py         # Universal installer script
├── setup-orchestrator.sh         # Shell launcher script
├── README.md                        # Documentation
└── .claude/
    ├── CLAUDE.md                    # Core orchestrator initialization rules
    ├── mcp.json                     # Playwright & Chrome DevTools MCP servers
    ├── commands/
    │   └── DevOrchestrator.md      # Dedicated /DevOrchestrator slash command
    ├── spec.md                      # Auto-generated spec approval gate
    ├── handoff.md                   # Multi-session continuity log
    ├── dashboard.py                 # Live inspection HTTP server
    ├── rules/
    │   └── coding-standards.md      # Coding conventions
    ├── skills/
    │   ├── harness.md               # Harness² testing engine
    │   ├── mcp-browser-verification.md # Playwright & Chrome DevTools MCP assertions
    │   ├── tdd-cycle.md             # Superpowers TDD engine
    │   ├── worktree-isolation.md    # Superpowers git worktree manager
    │   ├── systematic-debugging.md  # Superpowers 4-phase root cause debugger
    │   ├── intake-auto-parser.md    # Interactive requirement intake
    │   ├── spec-generator.md        # Spec generator & approval gate
    │   ├── pre-verify-oracle.md     # Baseline code checker
    │   ├── surgical-implementer.md  # Dynamic tier router
    │   ├── preference-bias-eval.md  # Isolated reviewer & QA agents
    │   └── session-handoff.md       # Automatic handoff log writer
    └── agents/
        ├── implementer.md           # Primary coding agent
        ├── reviewer.md              # Isolated code reviewer
        └── qa-agent.md              # Independent QA tester
```

---

## 🛡️ License

MIT License.
