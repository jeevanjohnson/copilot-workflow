---
name: skill-builder
description: >
  Collaboratively build a new SKILL.md file from scratch through a back-and-forth loop, or extract
  a skill from an existing conversation and refine it together. Use this skill whenever the user wants
  to create, build, write, or improve a Claude skill or SKILL.md file. Trigger phrases include:
  "build a skill", "make a skill", "write a SKILL.md", "help me create a skill", "turn this into a skill",
  "extract a skill from this", "let's make a skill for X", or any mention of creating a reusable Claude
  workflow or skill definition. Always use this skill for skill creation — never just write a SKILL.md
  without going through the loop.
---

# Skill Builder

Collaboratively build a SKILL.md file through a back-and-forth loop with built-in grilling at every
step. Ask, write, probe, confirm — repeat until the skill is airtight. Always end with a dry run
before delivering the final file.

---

## Step 0: How Do We Start?

Always open with:
> "Want to build this skill from scratch, or should I look at our conversation and extract a skill
> from what we've already been doing?"

Then follow the matching path.

---

## Path A: Extract from Conversation

Scan the full conversation history for any repeated workflow, methodology, or pattern the user has
been following. Look for:
- Step-by-step processes that repeated across multiple turns
- Decision points and branching logic
- Quality checks or completion criteria the user kept applying

Draft an initial SKILL.md based on what you find, then say:
> "Here's a skill I pulled from our conversation — [one sentence summary of what it does].
> Does this capture it, or is there something off?"

From here, treat it like Phase 1 of the build loop below — refine section by section.

If nothing clear emerges from the conversation, say:
> "I couldn't find a clear repeatable workflow in our history. Want to build one from scratch instead?"
> Then switch to Path B.

---

## Path B: Build from Scratch

Ask one question at a time to establish the foundation before writing anything:

1. "What should this skill enable Claude to do — describe it in plain language."
2. "When should this skill trigger? What would the user say or do to kick it off?"
3. "Is this a quick checklist-style skill, or a deeper multi-step workflow?"

Once you have answers to all three, write the first draft of the `description` field and `name`,
show it, and enter the build loop.

---

## The Build Loop

After the foundation is set, build the skill section by section:

1. **Write** the next section
2. **Probe** — ask at least one pointed question about what was just written. Always give your recommendation.
3. **Confirm** — get a thumbs up or take feedback
4. **Repeat** until all sections are done

After each confirmed section ask: *"What should we tackle next?"* or suggest the logical next section.

---

## Sections to Build (flexible — adapt to the skill type)

Not every skill needs every section. Use judgment based on complexity.

### 1. Frontmatter — ALWAYS FIRST, ALWAYS GRILLED HARDEST
```
---
name: skill-name
description: >
  [Trigger description here]
---
```
The `description` field is the most critical part of any skill. It is what Claude reads to decide
whether to activate this skill at all. Grill it relentlessly:

- "Is it crystal clear when this should trigger vs. when it shouldn't?"
- "Could this accidentally fire on something unrelated? My recommendation: add 'do NOT trigger when...' to the description."
- "Is it specific enough? Vague descriptions = missed triggers."
- "Does it include concrete trigger phrases the user would actually say?"

Do not move on from the frontmatter until the description is airtight.

### 2. Purpose / What This Skill Does
One clear paragraph. What problem does it solve? Who is it for?

Probe: "Would someone who's never seen this skill understand what it does in 10 seconds?"

### 3. Core Workflow / The Loop
The step-by-step process Claude should follow. This is the heart of the skill.

Rules for writing workflow steps:
- Every step must be actionable — no vague instructions like "handle edge cases"
- Decision points must be explicit — "if X, do Y; if Z, do W"
- No step should require Claude to guess what to do

Probe hard here:
- "Is there any step where Claude would have to guess what you meant?"
- "What happens if the user gives an unexpected answer at step [X]? My recommendation: add a fallback."
- "Is the order logical? Could any steps be combined or split?"

### 4. Trigger Conditions (if complex)
When to activate. When NOT to activate. Be explicit about both.

Probe: "Can you think of a scenario where this skill would fire but shouldn't? Let's add a NOT trigger for that."

### 5. Rules & Constraints
Hard rules Claude must always follow in this skill. Non-negotiables.

Probe: "Is there anything Claude might do that would completely break this workflow? Add it as a hard rule."

### 6. Examples
At least one realistic example showing the skill in action — trigger phrase, what Claude does, what the output looks like.

Probe: "Is this example actually representative of how you'd use this in real life, or is it too simple/too perfect?"

### 7. Edge Cases
What should Claude do when things go sideways — ambiguous input, missing info, unexpected responses.

Probe: "What's the most likely way a user would use this wrong? How should the skill handle that?"

---

## The Dry Run (Always Before Finalizing)

Once all sections are confirmed, always run a dry run before delivering the file:

> "Let's do a quick dry run to make sure this skill actually works. I'm going to pretend to be a user
> triggering this skill cold — no context — and we'll see if it fires correctly and behaves the way
> you'd expect."

Simulate a realistic trigger:
- Use an actual trigger phrase from the description
- Walk through the first 2-3 steps of the workflow as if executing it live
- Call out anything that felt unclear, missing, or broken

Then ask:
> "Did that feel right? Anything that should have happened differently?"

If issues surface, go back into the loop and fix them. Run the dry run again if major changes were made.

Only move to finishing once the dry run passes cleanly.

---

## Finishing

When the dry run passes and the user is happy:
1. Assemble the complete final SKILL.md
2. Save to `/mnt/user-data/outputs/SKILL.md`
3. Call `present_files`
4. Give a two-line summary: what the skill does, and what phrase triggers it
5. Suggest one follow-up: *"Want to build a related skill next, like [logical next skill]?"*

---

## Hard Rules

- **One question at a time** — never stack questions
- **Always give your recommendation** — don't just ask, say what you'd do
- **Never write the whole skill upfront** — the loop is the point
- **Grill the description hardest** — it is the most critical field, treat it that way
- **Always do the dry run** — no exceptions, even if the skill seems perfect
- **Never move on without confirmation** — show every section and wait
- **Ask don't assume** — unknown details get asked, not invented
- **Be self-contained** — the finished SKILL.md should work without any external files or context