---
name: scrum-backlog-refinement
description: Refine Product Backlog items to ready state. Use when PBIs need clarification, acceptance criteria, or splitting per INVEST principles.
---

# Backlog Refinement

## Prerequisites Check

First, verify these exist (create if missing):
- [ ] Product Goal defined in `scrum.ts`
- [ ] At least one PBI in Product Backlog
- [ ] Definition of Done configured

## Refinement Process

For each `draft` or `refining` PBI:

### 1. Information Gathering
- Explore codebase for relevant context
- Identify technical dependencies
- Understand current implementation state

### 2. Acceptance Criteria
- Propose executable verification commands
- Each criterion must have a `verification` command that can be run

### 3. INVEST Check

| Principle | Question |
|-----------|----------|
| Independent | Can this be reprioritized freely? |
| Negotiable | Is implementation approach flexible? |
| Valuable | Is user benefit clear? |
| Estimable | Do we have all needed information? |
| Small | Would splitting lose value? |
| Testable | Do we have verification commands? |

### 4. Splitting (if needed)

**Best Practices:**
- Extract high-value features first
- Create skeleton/dummy implementation story for big features
- Keep original PBI in `refining` if still large

**Anti-patterns to avoid:**
- Dependency-only PBIs
- Interface-only PBIs
- Test-only PBIs (TDD handles this in subtasks)

### 5. Status Update

- All checks pass → `status: "ready"`
- Human judgment needed → document questions, keep `status: "refining"`

## Output

Update `scrum.ts` with:
- Refined acceptance criteria
- Updated status
- Any new PBIs from splitting

## When Human Input Needed

Document questions and keep status as `refining`:
- Domain expertise required
- Business priority unclear
- Technical feasibility uncertain
