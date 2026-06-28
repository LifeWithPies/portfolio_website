# Estimated Token Consumption: 1200
# style_learner.md - Style Learning Rules for Agents

## Actionable Rules
- Learn coding styles from provided examples by analyzing patterns in indentation, naming, and structure.
- Adapt to project-specific conventions by scanning existing codebases.
- Apply consistent style across generated code.

## Examples
- Example: Use snake_case for Python variables, CamelCase for classes.
- Trigger: When generating Python code, ensure PEP 8 compliance.

## Semantic Triggers
- Keywords: "style", "format", "convention"
- Context: Code generation tasks

## Dos and Don'ts
- DO: Enforce consistent indentation (4 spaces).
- DON'T: Mix tabs and spaces.

## File-Scoped Commands
- Run `autopep8 <file>` for formatting.