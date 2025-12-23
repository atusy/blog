---
name: scrum-init
description: Initialize a new scrum.ts dashboard file with type definitions and empty data structure. Use when starting Agentic Scrum in a new project.
---

# Initialize Scrum Dashboard

Creates a new `scrum.ts` file with the complete type definitions and an empty dashboard ready for use.

## Usage

Run this skill when:
- Starting Agentic Scrum in a new project
- No `scrum.ts` exists yet
- Need to reset to a clean state

## Process

1. Check if `scrum.ts` already exists
   - If exists, ask user for confirmation before overwriting
2. Create `scrum.ts` with full template
3. Prompt user to define Product Goal

## Template

The generated file includes:
- All type definitions (read-only section)
- Empty dashboard structure
- JSON output for `deno run scrum.ts | jq` compatibility

## After Initialization

Guide user through:
1. Define Product Goal (statement + success metrics)
2. Create first PBI in draft status
3. Run Backlog Refinement to get PBI to ready

## Validation

After creation, verify with:
```bash
deno check scrum.ts
```
