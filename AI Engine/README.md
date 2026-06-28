# Estimated Token Consumption: 4000
# Agent Development Kit (ADK)

A template for building AI agent systems following layered framework best practices.

## Overview

The ADK provides:
- **CLAUDE.md**: Agent instructions with layered guidance (dos/donts, commands, safety).
- **Skills**: Modular rules for style learning, code quality, and MCP gatekeeping.
- **Hooks**: Pre-tool hooks, token optimizers, and guardrails in `core/hook_manager.py`.
- **Subagents**: Reviewer and tester classes in `core/subagent_manager.py` with anti-recursion.

## Structure

- `CLAUDE.md`: Root instructions.
- `.claude/CLAUDE.md`: Nested instructions.
- `skills/`: Markdown files with rules.
- `core/`: Python modules.
- `tests/`: Unit tests.
- `.github/workflows/`: CI.

## Usage

1. Copy `adk/` to your project.
2. Customize CLAUDE.md for your needs.
3. Run tests: `pytest`.
4. Extend skills or core modules.

## Running Tests

```bash
pip install -r requirements.txt
pytest
```

## Extending the ADK

- Add new skills in `skills/`.
- Implement hooks in `core/hook_manager.py`.
- Create subagents in `core/subagent_manager.py`.

## Troubleshooting

- Tests fail: Check Python version (3.11+).
- Hooks not working: Verify context parameters.