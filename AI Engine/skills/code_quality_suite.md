# Estimated Token Consumption: 1300
# code_quality_suite.md - Code Quality Rules for Agents

## Actionable Rules
- Ensure code has proper error handling, logging, and validation.
- Maintain high test coverage (>80%).
- Use static analysis tools like pylint or flake8.

## Examples
- Example: Add try-except blocks around risky operations.
- Trigger: Before committing code, run quality checks.

## Semantic Triggers
- Keywords: "quality", "lint", "test"
- Context: Code review or generation

## Dos and Don'ts
- DO: Write docstrings for all functions.
- DON'T: Ignore linter warnings.

## File-Scoped Commands
- Run `pylint <file>` for quality check.