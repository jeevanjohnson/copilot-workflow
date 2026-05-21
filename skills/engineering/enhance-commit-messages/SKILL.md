---
name: enhance-commit-messages
description: 'Enhance rough commit messages into professional, informational Conventional Commits format. Use when you want to convert informal commit thoughts into well-structured, semantic commit messages that accurately describe code changes.'
argument-hint: 'Your rough commit message (e.g., "fixed bug in login" or "updated deps")'
---

# Enhance Commit Messages

Transform your rough, informal commit message drafts into professional, semantically accurate Conventional Commits format by analyzing the actual code changes.

## When to Use

- You've written a rough commit message but want it refined
- You want to ensure your message accurately reflects the git diff
- You need Conventional Commits format (feat, fix, refactor, etc.)
- You want to add context, scope, or breaking change descriptions where appropriate

## Prerequisites

Your changes must be staged or unstaged in a git repository. The skill will read the diff to understand what changed.

## Procedure

### Step 1: Examine Unstaged Changes
Provide your rough commit message. The skill will:
- Read the git diff of unstaged changes in the current repository
- Analyze file paths, code modifications, and impact scope
- Identify the category of change (feature, fix, refactor, chore, docs, style, test, perf)

### Step 2: Determine Conventional Commit Type
Based on the diff analysis, identify the appropriate type:

| Type | When to Use |
|------|------------|
| **feat** | New feature or functionality added |
| **fix** | Bug fix or error correction |
| **refactor** | Code restructuring without changing behavior |
| **perf** | Performance improvements |
| **docs** | Documentation changes only |
| **style** | Code style, formatting (no logic change) |
| **test** | Test additions or modifications |
| **chore** | Dependency updates, build config, tooling |
| **ci** | CI/CD configuration changes |

### Step 3: Extract Scope
Identify the area of the codebase affected:
- If targeting a specific module or feature: `feat(auth): add login with oauth`
- If cross-cutting or broad impact: omit scope or use `*`
- If unclear, ask the user for clarification

### Step 4: Write the Subject Line
Conventional Commits format:
```
<type>(<scope>): <subject>
```

Guidelines for the subject:
- Start with lowercase verb (past tense or imperative, e.g., "add", "fix", "update")
- Be specific and descriptive (not vague: ✓ "add email validation" vs ✗ "update code")
- Keep under 50 characters if possible
- No period at the end

### Step 5: Add Body (if needed)
For complex changes, add a blank line followed by a detailed body:
```
<type>(<scope>): <subject>

<body explanation>
```

Use the body to explain:
- *Why* the change was made (motivation, problem solved)
- *What* specific changes were made (if not obvious from subject)
- Impact on other parts of the system
- Any dependencies or related issues

### Step 6: Flag Breaking Changes
If the change breaks backward compatibility, add a footer:
```
BREAKING CHANGE: description of what broke and migration path
```

## Output Format

Provide a single, complete commit message as the output:

```
<final commit message>
```

The message should be comprehensive and self-contained, even if it results in a longer body. If the changes involve multiple concerns, incorporate them into one message with a detailed body explaining all aspects.

## Example Workflow

**User input:** "fixed login bug and updated stuff"

**Your analysis:**
- Diff shows: Bug fix in auth module + dependency updates
- Types detected: `fix` (primary change) with related dependency updates
- Approach: Combine into one comprehensive commit since updates support the main fix

**Output:**
```
fix(auth): resolve token expiration and update dependencies

Prevent JWT token from expiring unexpectedly during active sessions
by adjusting token refresh interval from 1 hour to 30 minutes.

Also updates lodash from 4.17.20 to 4.17.21 to include security fixes
required for this auth flow refactor.
```

## Tips for Better Results

1. **Analyze the diff thoroughly** — don't guess the scope; verify from file paths
2. **Prioritize clarity** — the commit message should be understandable to someone unfamiliar with the code
3. **Be comprehensive** — when changes are related, combine them into one commit with a detailed body explaining all aspects
4. **Use the body effectively** — separate logical concerns with paragraphs in the body rather than splitting into multiple commits
5. **Ask for clarification** — if the diff is ambiguous or contradicts the user's message
6. **Consider context** — check for related issues or PRs if mentioned
