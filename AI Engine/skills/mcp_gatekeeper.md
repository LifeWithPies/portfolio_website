# Estimated Token Consumption: 1100
# mcp_gatekeeper.md - MCP Gatekeeping Rules for Agents

## Actionable Rules
- Validate MCP calls against local data availability.
- Block external MCP if local index exists.
- Optimize token usage in MCP interactions.

## Examples
- Example: Check local workspace before calling external MCP.
- Trigger: On tool use requests.

## Semantic Triggers
- Keywords: "MCP", "external", "gatekeep"
- Context: Tool invocation

## Dos and Don'ts
- DO: Prioritize local data.
- DON'T: Make unnecessary external calls.

## File-Scoped Commands
- No specific commands; integrated in hooks.