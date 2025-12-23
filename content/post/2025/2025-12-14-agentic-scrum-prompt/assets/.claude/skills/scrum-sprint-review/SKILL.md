---
name: scrum-sprint-review
description: Verify Sprint increment against Definition of Done and acceptance criteria. Determines if Sprint is accepted or needs rework.
---

# Sprint Review

## Prerequisites

- All subtasks have `status: "completed"`
- Sprint has `status: "in_progress"`

## Review Process

### 1. Run Definition of Done Checks

Execute each check in `definition_of_done.checks`:

```bash
# Example checks
cargo test
cargo clippy -- -D warnings
cargo check
```

Record results for each check.

### 2. Run Acceptance Criteria Verification

For the Sprint's PBI, execute each `acceptance_criteria.verification` command.

### 3. Determine Outcome

**All Passed:**
- Set `sprint.status = "done"`
- Set PBI `status = "done"`
- Sprint is complete, proceed to Retrospective

**Some Failed:**

Evaluate severity:

| Severity | Action |
|----------|--------|
| Minor fix possible | Add subtask, keep `status: "in_progress"` |
| Sprint Goal at risk | Report to Product Owner for scope decision |
| Goal impossible | Consider Sprint cancellation |

### 4. Handle Failures

**For minor fixes:**
```typescript
subtasks: [
  ...existingSubtasks,
  {
    test: "Fix: <description of the fix>",
    implementation: "<what needs to be fixed>",
    type: "behavioral",
    status: "pending",
    commits: [],
    notes: ["Added during Sprint Review to address: <issue>"]
  }
]
```

**For scope reduction:**
- Consult Product Owner
- May split PBI and return part to backlog
- Document decision in sprint notes

**For cancellation:**
- Set `sprint.status = "cancelled"`
- Return PBI to Product Backlog
- Document reason in Retrospective

## Output

Update `scrum.ts` with:
- Sprint status (`done`, `in_progress`, or `cancelled`)
- PBI status (if done)
- Any new subtasks (if fixes needed)
- Move to `completed` array if done

## Report Format

```
Sprint Review Results
=====================
Sprint: #N - <Goal>
PBI: <ID> - <Story summary>

Definition of Done:
  ✓ Test合格
  ✓ Lint合格
  ✗ 型チェック - <error details>

Acceptance Criteria:
  ✓ <criterion 1>
  ✓ <criterion 2>

Decision: <ACCEPTED / NEEDS_REWORK / CANCELLED>
```
