# 🤖 Claude Code Superpowers Orchestrator

> **Ship complex features and surgical bug fixes in a SINGLE prompt.**
> An agentic workflow for **Claude Code Terminal & Desktop** combining Matt Pocock's `grill-me` & `handoff` skills, `caveman` token compression, `ponytail` multi-model routing, and embedded software engineering methodology from [obra/superpowers](https://github.com/obra/superpowers).

---

## 🌟 Key Features

* **Zero-Keyword Interactive Intake**: Automatically extracts technical keywords, props, API routes, and acceptance criteria from your inputs and screenshots—no manual prompt keywords required.
* **Superpowers TDD & Worktree Engine**:
  * **Strict TDD Cycle**: Mandates RED ➔ GREEN ➔ REFACTOR cycles. Automatically deletes implementation code written prior to writing a failing test.
  * **Git Worktree Isolation**: Spawns clean `.claude/worktrees/task-N` branches to keep your main development branch untouched.
  * **Systematic Debugging**: Enforces a 4-phase root-cause analysis before making speculative edits.
* **Spec Gate Approval (`spec.md`)**: Generates a pre-coding specification and **halts execution** for your explicit approval before modifying production code.
* **Baseline & Oracle Regression Checks**: Compares clean codebase state against Staging/Production Oracles and reports findings before coding.
* **Ponytail Multi-Model Tier Routing**: Allocates fast models (Haiku) for log traces and file mapping, reserving premium models (Sonnet/Opus) for surgical edits (~70% cost reduction).
* **Caveman Token Compression**: Strips conversational filler from inter-agent communication (~55% token reduction).
* **Preference-Bias Elimination**: Deploys independent Reviewer and QA sub-agents in isolated context windows.
* **Automatic Session Handoff (`handoff.md`)**: Automatically summarizes progress and generates session resume commands when context usage reaches ~35%.
* **Live Inspection Dashboard (`http://localhost:8080`)**: Zero-dependency Python server visualizing pipeline steps, active model tiers, spec status, handoff state, and token analytics.

---

## 🚀 Quick Start (Zero Permission Setup)

No `chmod` or executable permissions required. Simply run the Python installer in your repository root:

```bash
python3 setup_orchestrator.py
```

### Start the Live Dashboard

In a terminal tab, launch the inspection dashboard:

```bash
python3 .claude/dashboard.py
```

Open **`http://localhost:8080`** in your browser to monitor real-time execution flows and token savings.

---

## 💻 Daily Usage

Launch Claude Code in your terminal or desktop:

```bash
claude
```

Prompt naturally—the orchestrator automatically executes behind the scenes:

```text
Fix the checkout button error on the /checkout page.
```

### What Happens Automatically:
1. **Intake**: Prompts for target environment, credentials/env file path, context, screenshot path, and target file pinpointing.
2. **Worktree & Spec Gate**: Spawns an isolated git worktree, writes `.claude/spec.md`, and **pauses for your approval**.
3. **Verification**: Compares clean tree against Oracle/Staging and **reports baseline findings to you**.
4. **TDD Surgical Edit**: Writes a failing test, applies surgical edits, and validates live in the browser using console logs.
5. **Review & QA**: Isolated Reviewer and QA sub-agents verify code quality and issue a Go/No-Go decision.
6. **Handoff**: Writes `.claude/handoff.md` and updates the live Python dashboard.

---

## 📂 Project Structure

```text
.
├── setup_orchestrator.py         # Universal Python installer
├── setup-orchestrator.sh         # Shell installer
├── README.md                    # Documentation
└── .claude/
    ├── CLAUDE.md                # Core orchestrator initialization rules
    ├── spec.md                  # Auto-generated plan & contract gate
    ├── handoff.md               # Multi-session continuity log
    ├── screenshots/             # Folder for visual error screenshots
    ├── dashboard.py             # Live inspection HTTP server
    ├── rules/
    │   └── coding-standards.md # Externalized coding conventions
    ├── skills/
    │   ├── tdd-cycle.md        # Superpowers TDD engine
    │   ├── worktree-isolation.md # Superpowers git worktree manager
    │   ├── systematic-debugging.md # Superpowers 4-phase root cause debugger
    │   ├── intake-auto-parser.md # Interactive intake & keyword extractor
    │   ├── spec-generator.md    # Plan phase explorer & user approval gate
    │   ├── pre-verify-oracle.md # Baseline code & Oracle regression checker
    │   ├── surgical-implementer.md # Model tier router & browser logger
    │   ├── preference-bias-eval.md # Preference bias elimination (Reviewer & QA)
    │   └── session-handoff.md   # Automatic handoff log writer
    └── agents/
        ├── implementer.md       # Primary coding agent
        ├── reviewer.md          # Isolated code reviewer
        └── qa-agent.md          # Independent QA tester
```

---

## 📊 Token Usage & Savings

| Optimization Mechanism | Token / Cost Impact |
| :--- | :--- |
| **Caveman Compression** | ~55% reduction in inter-agent communication tokens |
| **Ponytail Tiered Routing** | ~70% reduction in API costs (Haiku for exploration) |
| **Context Window Capping (35%)** | Prevents quadratic token expansion and context degradation |
| **Total Combined Savings** | **~65% reduction in total token spend vs. standard prompts** |

---

## 🛡️ License

MIT License. Feel free to fork and adapt for your team's workflow!
