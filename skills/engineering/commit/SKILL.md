---
name: commit
description: >
  Polish rough commit messages into professional, tightly-formatted Conventional Commits 
  with max 2-sentence bodies and optional notes/warnings section. Trigger with `/commit` 
  followed by an optional rough commit message. If no message is provided, generates one from scratch 
  by analyzing changes. Safely retrieves git diffs without executing modifying commands. Ensures consistent 
  `type(scope): description` format. DO NOT trigger for general git questions, commit history review, 
  or rebasing help — this is specifically for polishing individual commit messages into shape.
---

# Commit Message Pro

Transform your rough, informal commit message drafts into professional Conventional Commits with strict discipline: max 2 sentences, clean `type(scope): subject` format, and optional notes for TODOs and known issues. Safely analyzes actual changes from git diffs.

## Purpose

This skill transforms rough, informal commit messages into professional Conventional Commits 
with discipline and consistency. It produces commits that are scannable, informative, and follow 
a strict format: `type(scope): description` with max 2 sentences, plus an optional notes section 
for TODOs, known issues, or future fixes. Safely analyzes changes without executing modifying git commands.

## Core Workflow

### Step 1: Capture Input and Determine Mode

**If user provided a rough commit message:**
- Note it as an "anchor" — it tells you what the user *thinks* they changed
- Use this as context to guide your analysis and final message
- Your job: refine it into the proper format while respecting their intent

**If user provided no message:**
- You'll generate the commit message entirely from the diff
- Analyze the changes and create both type, scope, and subject from scratch
- Ask clarifying questions if the diff is ambiguous

### Step 2: Safely Get the Diff

Execute `git diff` (for unstaged changes) or `git diff --cached` (for staged changes) to retrieve 
the actual changes. Read-only operation only — never execute any commands that modify state.

### Step 3: Analyze Changes

Read the diff and extract:
- **Files changed**: Which files were modified?
- **Type of change**: Is this a feature, fix, refactor, docs update, etc.?
- **Scope**: What module or feature is affected? (Use the file path or module name as a hint)
- **Impact**: Is this breaking? Does it affect multiple systems?

### Step 4: Determine Commit Type

Select from this table:

| Type | When | Example |
|------|------|---------|
| `feat` | New feature or capability | `feat(auth): add oauth login` |
| `fix` | Bug fix | `fix(parser): handle null values` |
| `refactor` | Restructure without behavior change | `refactor(api): simplify response mapping` |
| `perf` | Performance improvement | `perf(db): optimize query with index` |
| `docs` | Documentation only | `docs(readme): update setup instructions` |
| `style` | Formatting, no logic change | `style(linter): enforce consistent spacing` |
| `test` | Test additions/changes | `test(auth): add oauth edge cases` |
| `chore` | Dependency, tooling, build config | `chore(deps): update lodash to 4.17.21` |
| `ci` | CI/CD pipeline changes | `ci(github): add linting to workflow` |

### Step 5: Extract Scope

Identify the affected area:
- If changes are localized to one module: use that module name (e.g., `auth`, `parser`, `db`)
- If changes span multiple areas: use the primary affected area, or omit scope if truly cross-cutting
- When unsure, ask the user: "What would you call the main area this touches?"

### Step 6: Write Subject (Max 2 Sentences)

Format: `<type>(<scope>): <sentence 1>. <sentence 2>.`

Rules:
- Start with an imperative verb (add, fix, update, remove, simplify, etc.)
- **Sentence 1**: What changed (be specific)
- **Sentence 2** (optional): Why or what it enables (the impact or benefit)
- Each sentence lowercase, no period after the last one — periods only between sentences
- Total: max 2 sentences

Examples:
- ✓ `fix(auth): resolve token expiration bug. Refresh tokens now persist across sessions.`
- ✓ `feat(api): add batch endpoint for bulk operations.`
- ✗ `fix(auth): Fixed the token thing` (vague, wrong tense)
- ✗ `feat(api): Add batch endpoint for bulk operations. This is a new feature. It allows users to send multiple requests at once.` (too many sentences)

### Step 7: Output Commit Message (Code Block Only)

Output ONLY the commit message in code blocks, nothing else:
```
<type>(<scope>): <sentence 1>. <sentence 2>.
```

That's it — no explanation, no analysis, just the message in the code block.

### Step 8: Ask About Notes (Optional)

After outputting the commit, ask the user: **"Would you like to add notes (TODOs, known issues, or future fixes)?"**

Only if they say yes, then provide the notes section:
```
Notes:
- [TODO] Add error handling for edge case X
- [KNOWN ISSUE] Performance degrades with large datasets (needs optimization in next sprint)
- [FUTURE] Plan to refactor this module in v2.0
```

## Rules & Constraints

**Hard Rules (Never Break These):**

1. **Safe git diff execution only** — The skill may execute `git diff` or `git diff --cached` 
   to retrieve unstaged or staged changes. NEVER execute any commands that modify state 
   (git add, git commit, git reset, etc.). Read-only diff inspection only.

2. **Max 2 sentences in subject — NEVER exceed** — This is non-negotiable. The output commit message 
   is ALWAYS exactly 1-2 sentences. If a change is complex and needs more explanation, ask the user 
   if they want notes after outputting the commit.

3. **Always use `type(scope): subject` format** — The format must be consistent. Every commit 
   must follow Conventional Commits structure.

4. **Use imperative voice in subject** — "Add", "fix", "refactor", not "Added", "fixed", "refactored".

5. **Ask if ambiguous** — If the diff is unclear, contradicts the user's intent, or could fit 
   multiple commit types, ask clarifying questions. Never guess.

6. **Notes are opt-in and separate** — Always output the commit message first in code blocks. 
   Then ask the user: "Would you like to add notes?" Only provide notes if they say yes. 
   Never auto-include notes without asking.

7. **Respect user intent as anchor** — If the user provided a rough message, let it guide your 
   interpretation. Don't override their intent unless the diff clearly shows something different.

## Examples

### Example 1: User Provides Rough Message (Feature)

**Input:**
```
/commit added new auth system
```

**Diff analysis:** (Skill executes `git diff`)
- Files changed: `src/auth/oauth.ts`, `src/auth/strategies.ts`, `tests/auth.test.ts`
- New exports, classes, test coverage added
- No breaking changes to existing API

**Output:**
```
feat(auth): add oauth authentication strategy. Supports Google and GitHub login with session persistence.
```

**Then ask:** Would you like to add notes (TODOs, known issues, or future fixes)?

---

### Example 2: User Provides No Message (Bug Fix with Notes)

**Input:**
```
/commit
```
User then describes: "I fixed a memory leak and found another issue but ran out of time."

**Diff analysis:** (Skill executes `git diff`)
- Files changed: `src/memory/cache.ts`
- Event listeners now properly cleaned up on teardown
- Added TODO comment about similar leak in nearby module

**First output:**
```
fix(memory): prevent cache event listener leak on teardown. Listeners now unsubscribe during cleanup.
```

**Then ask:** Would you like to add notes (TODOs, known issues, or future fixes)?

**If yes, provide notes:**
```
Notes:
- [TODO] Audit similar patterns in notification module
```

---

### Example 3: Complex Multi-File Change (Refactor)

**Input:**
```
/commit refactored request handler
```

**Diff analysis:** (Skill executes `git diff`)
- Files: `src/handlers/request.ts`, `src/middleware/auth.ts`, `src/utils/errors.ts`
- Extracted common error handling logic
- No behavior change to external API

**Output:**
```
refactor(handlers): extract error handling middleware. Centralizes error responses across auth and request layers.
```

**Then ask:** Would you like to add notes (TODOs, known issues, or future fixes)?

---

### Example 4: Dependency Update (Chore)

**Input:**
```
/commit
```
User: "Just bumped lodash."

**Diff analysis:** (Skill executes `git diff`)
- `package.json`: lodash 4.17.20 → 4.17.21
- Changelog shows: security patches, no breaking changes

**Output:**
```
chore(deps): update lodash to 4.17.21. Includes security fixes for prototype pollution.
```

**Then ask:** Would you like to add notes (TODOs, known issues, or future fixes)?

## Edge Cases

### Scenario: Diff is Ambiguous or Contradicts User's Message

**What happens:** The diff shows something different from what the user claimed.

**How to handle:**
- Call this out explicitly: "Your message says X, but the diff shows Y. Which is accurate?"
- Don't guess — ask for clarification before proceeding
- Use the diff as ground truth if they can't decide

### Scenario: Multiple Distinct Changes in One Diff

**What happens:** The diff includes a feature *and* a bug fix *and* a dependency update.

**How to handle:**
- If changes are tightly related (e.g., fix depends on the new feature): combine into one commit 
  with the primary type, explain dependencies in notes
- If changes are unrelated: suggest splitting into separate commits, but still provide a solid 
  commit message for the primary change
- Ask: "Are these changes related, or should they be in separate commits?"

### Scenario: User Provides Empty or Trivial Diff

**What happens:** `git diff` returns nothing, or only whitespace changes.

**How to handle:**
- Confirm with the user: "I don't see meaningful changes in the diff. Did you stage your changes? 
  Try `git diff --cached` or describe what you changed."
- Don't fabricate a commit message for nothing

### Scenario: Diff is Massive or Affects Many Files

**What happens:** 50+ files changed, unclear what the primary change is.

**How to handle:**
- Ask for context: "This is a large change. What's the main goal or feature?"
- Use the user's intent as the anchor
- Type/scope should reflect the primary purpose, not every affected file

### Scenario: Notes Section Would Be Very Long

**What happens:** User mentions many TODOs, known issues, or caveats.

**How to handle:**
- Keep notes concise and grouped by category (TODO, KNOWN ISSUE, FUTURE)
- If notes exceed 3-4 items, ask: "Should some of these be separate issues/tickets instead?"
- Notes are meant to capture quick callouts, not full documentation
