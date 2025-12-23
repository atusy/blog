---
name: scrum-sprint-planning
description: Plan a new Sprint by selecting a ready PBI, defining Sprint Goal, and breaking down into TDD subtasks.
---

# Sprint Planning

## Input Requirements

- At least one PBI with `status: "ready"` in Product Backlog
- No active Sprint (or previous Sprint is `done`/`cancelled`)

## Planning Process

### 1. Select PBI
- Choose the top `ready` item from Product Backlog
- This becomes the Sprint's single PBI (1 Sprint = 1 PBI)

### 2. Define Sprint Goal
- Derive from the PBI's `benefit` field
- Should be a clear, achievable outcome statement
- Example: "Users can log in with their email and password"

### 3. Break Down into Subtasks

Each subtask represents one TDD cycle:

```typescript
{
  test: "Description of what the test verifies",
  implementation: "Description of the implementation",
  type: "behavioral" | "structural",
  status: "pending",
  commits: [],
  notes: []
}
```

**Subtask Guidelines:**
- Each subtask = one test + its implementation
- Order subtasks by dependency (earlier ones first)
- Mark as `structural` if it's pure refactoring
- Mark as `behavioral` if it changes observable behavior

### 4. Update Dashboard

Set in `scrum.ts`:
```typescript
sprint: {
  number: <increment from last>,
  pbi_id: "<selected PBI id>",
  goal: "<sprint goal>",
  status: "in_progress",
  subtasks: [...]
}
```

## Output

- Sprint is configured and ready for execution
- First subtask is ready to begin (status: "pending")
- PBI remains in backlog with status: "ready" until Sprint Review

## Validation

Before completing planning:
- [ ] Sprint Goal is clear and measurable
- [ ] All subtasks have both `test` and `implementation` descriptions
- [ ] Subtasks are ordered by dependency
- [ ] Dashboard is updated
