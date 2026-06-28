# Estimated Token Consumption: 2000
# CLAUDE.md - Agent Development Kit Instructions

## Basic Instructions
This is the Agent Development Kit (ADK), a template for building AI agent systems. Follow these instructions deterministically for all interactions within the adk/ workspace.

## Transparency
Always be transparent about your actions, reasoning, and limitations. Explain decisions clearly.

## Anti-Hallucination
If you don't know something, say "I don't know" instead of guessing or fabricating information.

## Output Protocol
For large outputs (code blocks >50 lines, complex data structures, or multi-file changes), write them to separate files instead of outputting directly in responses.

## Workspace Scope Rules
- Operate only within the adk/ directory and its subdirectories.
- Do not access or modify files outside adk/.
- Assume adk/ is the root for all relative paths.

## Dos and Don'ts
- DO: Use type hints and docstrings in all Python code.
- DO: Write comprehensive unit tests with PyTest.
- DO: Follow PEP 8 style guidelines.
- DON'T: Use external APIs without explicit permission.
- DON'T: Modify core files without tests passing.
- DON'T: Assume dependencies beyond requirements.txt.

## File-Scoped Commands
- For Python files: Run `python -m py_compile <file>` for syntax check.
- For tests: Run `pytest <test_file>` to validate.
- For linting: Run `flake8 <file>` if available.

## Safety and Permissions
- No destructive operations without confirmation.
- Block shell commands that could harm the system.
- Only use tools explicitly allowed.

## Project Structure Hints
- core/: Core modules like hook_manager.py, subagent_manager.py
- skills/: Markdown files with rules for style, quality, gatekeeping
- tests/: Unit tests for core modules
- .github/workflows/: CI configuration

## Use Concrete Examples
- Example: For hooks, see core/hook_manager.py
- Avoid legacy patterns; follow current best practices.

## API Docs References
- Refer to Python standard library docs for built-ins.
- For external libs, check requirements.txt.

## PR Checklist
- Code compiles without errors.
- Tests pass.
- Documentation updated.
- No security vulnerabilities.

## When Stuck, Plan First
If unsure, propose a plan instead of guessing.

## Optional Test First Mode
For new features, write tests before implementation.