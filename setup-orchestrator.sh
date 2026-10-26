#!/usr/bin/env bash
# ==============================================================================
# Claude Code Agent Orchestrator Setup Script
# Automatically creates the .claude/ directory layout, rules, skills, agents,
# and initial template files for zero-keyword automated orchestration.
# ==============================================================================

set -e

echo "🚀 Setting up Claude Code Agent Orchestrator structure..."

# 1. Create directory structure
mkdir -p .claude/rules
mkdir -p .claude/skills
mkdir -p .claude/agents
mkdir -p .claude/screenshots

# 2. Master Config: CLAUDE.md
cat << 'EOF' > CLAUDE.md
# Master Claude Code Orchestrator Rules

## Operating Principles
1. **Zero User Keywords Required**: The pipeline executes all sub-skills automatically behind the scenes.
2. **Context Window Limit**: Monitor token usage continuously. At 35% context capacity, write progress to `.claude/handoff.md` and restart session.
3. **Spec Gate First**: Never write implementation code until `.claude/spec.md` is generated and approved by the user.
4. **Pre-Implementation Verification**: Verify current code state and run baseline regression checks *before* editing code. Inform the user of findings first.
5. **Preference-Bias Elimination**: Main coding agent MUST NOT review or QA its own code. Deploy isolated sub-agents.

## Automated Execution Pipeline
1. **Intake & Auto-Extract**: Run `.claude/skills/intake-auto-parser.md`. Prompt user for missing env, credentials file, context, screenshot path, and pinpointed files. Extract all technical keywords and criteria automatically.
2. **Plan & Spec Approval Gate**: Run `.claude/skills/spec-generator.md`. Generate `.claude/spec.md`. Pause execution for explicit user verification.
3. **Pre-Implementation Verification**: Run `.claude/skills/pre-verify-oracle.md`. Check clean tree against Oracle URL. Report findings to user.
4. **Surgical Implementation**: Run `.claude/skills/surgical-implementer.md`. Use fast model for logs, smart model for surgical code edits. Validate live in browser with console logs.
5. **Isolated Review & QA**: Run `.claude/skills/preference-bias-eval.md`. Launch isolated `reviewer.md` and `qa-agent.md`.
6. **Session Handoff**: Run `.claude/skills/session-handoff.md`. Write `.claude/handoff.md`.
EOF

# 3. Externalized Coding Rules
cat << 'EOF' > .claude/rules/coding-standards.md
# Coding & Architecture Standards

## General Guidelines
- Keep modifications minimal and strictly targeted to specified issue boundaries.
- Never add unrequested third-party dependencies or libraries.
- Maintain existing code style, naming conventions, and file structures.
- Do not modify public API signatures without explicit requirement in spec.md.
- Never modify or remove failing unit tests simply to make a build pass; address the root cause.
EOF

# 4. Skill: Intake & Auto Parser
cat << 'EOF' > .claude/skills/intake-auto-parser.md
# Skill: Intake & Automated Keyword Extractor

## Interactive Intake Checklist
If any of these 5 inputs are missing from the prompt, pause and request them:
1. **Target Environment**: Local dev command, Staging URL, or Oracle production URL.
2. **Credentials File Path**: Path to `.env`, `credentials.json`, or API keys.
3. **Issue/Feature Context**: Problem summary or user story.
4. **Screenshot Path**: Image path inside `.claude/screenshots/`.
5. **Pinpointed Files/Folders**: Exact target files, components, or API routes.

## Automated Parsing Protocol (No Manual Keywords From User)
- Inspect provided screenshots and target files.
- Automatically extract UI selectors, component names, props, state handlers, error stack traces, and API endpoints.
- Derive explicit **Acceptance/Done Criteria** automatically.
- Write extracted parameters into `.claude/spec.md`.
EOF

# 5. Skill: Spec Generator & Approval Gate
cat << 'EOF' > .claude/skills/spec-generator.md
# Skill: Spec Generator & Approval Gate

## Execution Protocol
1. Perform pre-coding exploration:
   - Bug Fix: Reproduce live in browser, add console trace logs, identify root cause in `spike.md`.
   - Feature: Inspect target components, state transitions, click handlers, and API calls to build a Knowledge Graph.
2. Generate `.claude/spec.md` with:
   - Target environment & credentials verification status.
   - In-scope target files vs. out-of-scope files.
   - Automatically derived Acceptance Criteria.
   - Verification guardrails (no new libraries, no public API changes, no editing tests to pass).
3. **HALT EXECUTION**: Present `.claude/spec.md` to the user and request explicit confirmation before writing any implementation code.
EOF

# 6. Skill: Pre-Verify Oracle
cat << 'EOF' > .claude/skills/pre-verify-oracle.md
# Skill: Pre-Implementation Oracle Verification

## Execution Protocol
1. Connect to the designated Oracle (Staging server, Main branch, or Production URL).
2. Run baseline test suites and inspect browser console outputs on the clean codebase.
3. **Inform User**: Provide a clear report to the user summarizing:
   - Baseline code health and test status.
   - Staging/Oracle comparison status.
   - Confirmed root cause trace location before any edits are made.
EOF

# 7. Skill: Surgical Implementer
cat << 'EOF' > .claude/skills/surgical-implementer.md
# Skill: Surgical Implementer

## Execution Rules
1. **Model Tier Allocation**:
   - Fast Tier (Haiku): Codebase searching, log placement, trace gathering.
   - Smart Tier (Sonnet/Opus): Surgical code edits.
2. **Surgical Boundaries**:
   - Touch ONLY target files explicitly listed in `.claude/spec.md`.
   - No unrequested libraries, no altering public APIs, no suppressing errors.
   - Do not edit failing tests just to make them pass.
3. **Live Browser Verification**:
   - Add console logs to verify every state change live in browser.
   - Assume nothing; do not reason from theory.
   - Capture visual proof (screenshot/recording) of expected behavior.
EOF

# 8. Skill: Preference-Bias Evaluation
cat << 'EOF' > .claude/skills/preference-bias-eval.md
# Skill: Isolated Review & QA

## Execution Protocol
1. **Isolated Code Review**:
   - Launch `.claude/agents/reviewer.md` in a fresh agent context.
   - Review code diff against `.claude/rules/coding-standards.md`.
   - Record review learnings in `review-learnings.md`.
2. **Independent QA Clearance**:
   - Launch `.claude/agents/qa-agent.md` in a fresh agent context.
   - Test edge cases, console logs, and Acceptance Criteria.
   - Issue a definitive **GO** or **NO-GO** decision.
   - Record QA learnings in `qa-learnings.md`.
EOF

# 9. Skill: Session Handoff
cat << 'EOF' > .claude/skills/session-handoff.md
# Skill: Session Handoff

## Execution Protocol
At session end or when context usage approaches 35% capacity, generate `.claude/handoff.md`:

```markdown
# Session Handoff Log

## 1. Goal & Context
- **Task**: [Bug Fix / Feature Name]
- **Environment**: [Local / Staging / Oracle]
- **Spec Gate**: [Approved / Pending]

## 2. Completed Work
- [x] Automated intake & spec.md generated
- [x] Baseline code & Oracle regression checks reported to user

## 3. Pending Implementation Tasks
- [ ] Surgical edit in target files
- [ ] Isolated code review via reviewer.md
- [ ] Independent QA Go/No-Go clearance

## 4. Key Learnings
- **Traces & Discoveries**: [Key learnings captured during execution]

## 5. Resume Command
`claude "Resume session using .claude/handoff.md"`
```
EOF

# 10. Agent: Implementer
cat << 'EOF' > .claude/agents/implementer.md
# Agent: Surgical Implementer

You are the primary coding agent.
1. Read `.claude/spec.md` and modify ONLY the specified target files.
2. Do not introduce refactors outside the assigned problem scope.
3. Insert console logs and verify behavior live in the browser environment.
EOF

# 11. Agent: Reviewer
cat << 'EOF' > .claude/agents/reviewer.md
# Agent: Independent Code Reviewer

You are an isolated code reviewer.
1. Inspect git diff of recent changes.
2. Verify diff against `.claude/rules/coding-standards.md`.
3. Ensure surgical scope: zero unrequested libraries, no altered public APIs, no altered tests.
EOF

# 12. Agent: QA Agent
cat << 'EOF' > .claude/agents/qa-agent.md
# Agent: Quality Assurance Tester

You are an independent QA tester operating in a clean context.
1. Run all test suites and check console outputs.
2. Test acceptance criteria defined in `.claude/spec.md`.
3. Issue a formal GO or NO-GO decision.
EOF

# 13. Initial spec.md Template
cat << 'EOF' > .claude/spec.md
# Specification & Contract (.claude/spec.md)

## Status: UNINITIALIZED
Run orchestrator intake to populate specifications.
EOF

# 14. Initial handoff.md Template
cat << 'EOF' > .claude/handoff.md
# Session Handoff Log (.claude/handoff.md)

## Status: NO ACTIVE SESSION
EOF

echo "✅ Claude Code Orchestrator successfully set up!"
echo "📁 Structure created under .claude/ and CLAUDE.md"
