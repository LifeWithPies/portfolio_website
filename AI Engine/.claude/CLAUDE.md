# Estimated Token Consumption: 1500
# CLAUDE.md - Nested Agent Instructions for .claude/

## Basic Instructions
This CLAUDE.md applies specifically to the .claude/ subdirectory within the ADK. It inherits all rules from the root CLAUDE.md but adds nested-specific guidance.

## Transparency
Maintain full transparency in all operations within .claude/.

## Anti-Hallucination
Strictly adhere to "I don't know" for any unknowns.

## Output Protocol
Use file outputs for large content, storing in .claude/ if appropriate.

## Workspace Scope Rules
Limited to .claude/ subdirectory. Do not affect parent adk/ files.

## Dos and Don'ts
- DO: Keep instructions concise and focused on agent behavior.
- DON'T: Include executable code; this is for guidance only.

## File-Scoped Commands
- For Markdown: Use `markdownlint <file>` if available.

## Safety and Permissions
- Read-only operations preferred; no modifications without review.

## Project Structure Hints
- This directory holds agent-specific instructions.

## Use Concrete Examples
- Reference root CLAUDE.md for examples.

## When Stuck, Plan First
Always plan before acting.