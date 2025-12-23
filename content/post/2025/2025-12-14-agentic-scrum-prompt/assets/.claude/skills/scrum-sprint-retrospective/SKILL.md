---
name: scrum-sprint-retrospective
description: Facilitate Sprint Retrospective using 5-phase structure. Identifies improvements and executes immediate actions.
---

# Sprint Retrospective

## 5-Phase Structure

### Phase 1: Set the Stage

Review previous Retrospective's improvement actions:
- Check `status: "active"` actions from previous sprint
- Evaluate their effectiveness
- Update status to `completed` or `abandoned` with outcome notes

### Phase 2: Gather Data

Analyze the Sprint:
- What went well?
- What was problematic?
- What impediments were encountered?

Sources to review:
- Commit history for the Sprint
- Subtask notes
- Any blocked periods

### Phase 3: Generate Insights

- Identify root causes of problems
- Look for patterns across sprints
- Consider systemic vs. one-off issues

### Phase 4: Decide What to Do

Select 1-2 improvement actions.

For each action, determine `timing`:

| Timing | When to Use | Example |
|--------|-------------|---------|
| `immediate` | Non-production code, single logical change | Update CLAUDE.md, add skill |
| `sprint` | Process improvement needing TDD | Add test helper |
| `product` | Feature addition | New capability |

**Immediate Action Constraints:**
- No production code changes
- Single logical change (one commit can revert)

**Action Archetypes:**

| Category | Examples | Typical Timing |
|----------|----------|----------------|
| Prompt adjustment | Skills, CLAUDE.md, slash commands | immediate |
| Process adjustment | scrum.ts notes, DoD update | immediate |
| Tool/Environment | MCP server, hooks | immediate |
| Documentation | ADR, code standards | sprint |
| Code quality | Test helpers, utilities | sprint/product |
| Automation | Slash commands for repetitive tasks | sprint/product |

### Phase 5: Close

1. **Execute immediate actions** right now
   - Make the change
   - Commit with appropriate message
   - Update action `status: "completed"`

2. **Queue sprint actions** as subtasks for next sprint

3. **Queue product actions** as new PBIs in backlog

4. **Update dashboard** with new retrospective entry

## Dashboard Compaction Check

After Retrospective, check dashboard size:

```bash
wc -l scrum.ts
```

If > 300 lines, prune:
- Keep only 2-3 most recent completed sprints
- Remove completed/abandoned improvements from old retrospectives
- Remove done PBIs from backlog

Never exceed 600 lines.

## Output

Update `scrum.ts` with:
```typescript
retrospectives: [
  {
    sprint: <number>,
    improvements: [
      {
        action: "<description>",
        timing: "immediate" | "sprint" | "product",
        status: "active" | "completed" | "abandoned",
        outcome: "<result or null>"
      }
    ]
  },
  ...previousRetrospectives
]
```
