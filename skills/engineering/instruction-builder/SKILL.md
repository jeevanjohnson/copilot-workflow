# Instruction Builder

Collaboratively build custom `.instructions.md` files from scratch through a structured back-and-forth
loop. Guides users to define coding standards, preferences, domain knowledge, workflow patterns, and
behavioral guidelines for their specific projects, teams, or domains. The result is a deployment-ready
instruction file ready to use immediately.

---

## Frontmatter

```
---
name: Instruction Builder
description: >
  Collaboratively build custom `.instructions.md` files from scratch through a structured
  back-and-forth loop. Guides users to define coding standards, preferences, domain knowledge,
  and behavioral rules that shape how Claude works on their projects. Triggers when user uses
  the slash command `/instruction-builder`. Outputs a complete, deployment-ready `.instructions.md`
  file. DO NOT trigger for general coding help, debugging, or code reviews — this is specifically
  for building instruction/customization files.
---
```

The `description` field is critical — it determines whether this skill activates at all. This one is
airtight: it's clear what triggers it (slash command only), what it produces (deployment-ready files),
and what it does NOT do (general help, debugging).

---

## Purpose

This skill guides you through building a custom `.instructions.md` file that packages preferences,
domain knowledge, workflow patterns, and behavioral guidelines for your specific projects, domains,
or teams. The result is a deployment-ready instruction file that shapes how Claude behaves when
working in that context — whether it's coding standards (Python, React, Go), writing conventions,
design principles, research methodologies, or any other domain-specific rules and practices. This is
for anyone who wants to codify their context's standards once and reuse them across all future Claude
interactions in that workspace.

---

## Core Workflow

### Phase 1: Foundation Interview

Before writing anything, gather the context for the instruction file. Ask these questions one at a time:

1. "What project, domain, or context are these instructions for?"
   (e.g., "Python backend project", "React frontend team", "Academic writing", "Research methodology")

2. "What problem are you trying to solve with these instructions? What standardization or guidance is missing right now?"
   (e.g., "We need consistent code style", "New team members need onboarding", "We want to enforce architectural patterns")

3. "What areas need to be covered in these instructions?"
   (Let them define what matters for their domain — e.g., for code: style, naming, testing; for writing:
    tone, structure, citations; for research: methodology, validation, documentation)

   If they list more than 5 or are overwhelmed, help them prioritize: "Which 2-3 of these are most
   urgent right now? We can always add more sections later, but let's focus on the core pain points
   first." Start with their top picks and build from there.

Once you have answers, write the first draft of the instruction file's **frontmatter** (target audience +
core philosophy) and show it.

### Phase 2: Build Loop — Section by Section

Build the instruction file section by section:

1. **Write** the next section
2. **Probe** — ask at least one pointed quality question about what was just written. Always give your recommendation.
3. **Confirm** — get thumbs up or take feedback
4. **Repeat** until all sections are done

After each confirmed section, ask: *"What should we tackle next?"* or suggest the logical next section.

### Phase 3: Dry Run

Once all sections are confirmed, simulate a realistic user discovering and using these instructions:

**Scenario 1:** A new team member reads the instructions for the first time and tries to apply them
to a real task (e.g., writing code, making a design decision, or submitting work).

**Scenario 2:** Someone has a specific question covered by the instructions and looks it up to get the
answer quickly.

**Scenario 3:** Someone is reviewing another person's work and uses the instructions as a checklist
to validate against the standards.

Walk through 1-2 of these scenarios live. Call out anything that felt unclear, incomplete, or broken.
Ask: "Did that feel right? Anything that should have happened differently?"

Fix any issues and re-run if needed.

### Phase 4: Finalize & Deliver

When the dry run passes and the user is happy:
1. Assemble the complete final `.instructions.md` file
2. Deliver it ready to deploy
3. Give a one-line summary of what the instructions cover

---

## Trigger Conditions

### Execution Model
This skill is slash-command only. It does NOT trigger on natural language. Users must explicitly
invoke it via `/instruction-builder` or equivalent command to activate.

### WHEN to activate this skill:
- User runs the explicit slash command to trigger this skill

### WHEN NOT to activate (do NOT trigger):
- This skill should ONLY run when explicitly commanded via slash — never auto-trigger on natural language
- Do not activate if the user is asking for general coding help, even if they mention "standards" or "guidelines"
- Do not activate if the user is trying to modify an existing instruction file (that's a different operation)
- Do not activate if the user is asking for architectural advice or design patterns
- Do not activate if user is asking Claude to follow specific instructions in the current chat (they want Claude to behave differently right now, not build a reusable file)

---

## Rules & Constraints

### Hard Rules
- **One question at a time** — never stack questions in the foundation interview
- **Always give your recommendation** — don't just ask, say what you'd do
- **Never write the whole file upfront** — build section by section through the loop
- **Grill the frontmatter hardest** — audience + philosophy is the foundation; make sure it's crystal clear before moving on
- **Always do the dry run** — no exceptions, even if the file seems perfect
- **Never move on without confirmation** — show every section and wait for feedback before proceeding
- **Ask, don't assume** — unknown details get asked, not invented
- **Be deployment-ready** — the final `.instructions.md` should be complete and usable immediately, no follow-up work needed
- **Only works with slash command** — this skill activates only when explicitly invoked; never auto-trigger on natural language
- **Help users get unstuck immediately** — if a user is overwhelmed, indecisive, or stuck during the build, diagnose the problem and help them move forward right then. Don't defer or suggest "we'll do this later". Options: simplify the section, provide concrete examples, suggest a minimal version to start, or narrow the scope. Get them unstuck in the current session.

---

## Examples

### Example 1: Building Instructions for a Python Backend Project

**Trigger:** User runs `/instruction-builder`

**Foundation Interview:**

Claude: "What project, domain, or context are these instructions for?"
User: "Python backend API project using FastAPI"

Claude: "What problem are you trying to solve? What standardization or guidance is missing right now?"
User: "New developers are inconsistent with error handling, logging, and type hints. We want them all aligned."

Claude: "What areas need to be covered in these instructions?"
User: "Coding style, naming conventions, error handling, testing patterns, and logging."

**Build Loop Sample:**

Claude writes and shows the **frontmatter**:
```
---
audience: Python backend developers on the FastAPI team
philosophy: >
  We prioritize consistency, debuggability, and team scalability. Every line of code should
  be readable to someone encountering it for the first time, and every error should be
  traceable and meaningful. Type hints are not optional—they're how we document intent.
---
```

Claude probes: "Does this capture the right audience and philosophy, or should we emphasize something different?"
User: "Looks good, but add something about 'defensive coding' — we want people thinking about edge cases."

Claude refines, confirms, moves to next section.

[Loop repeats for each section: Coding Style → Naming Conventions → Error Handling → Testing Patterns → Logging]

**Dry Run:**

Claude simulates a new developer using the instructions:
- Scenario: Developer writes a new API endpoint and references the instructions for error handling and logging patterns
- Calls out: "The error handling section is clear, but do we need an example of a common mistake to avoid?"

User approves or gives feedback. Claude adjusts if needed.

**Final Output:**

Complete `.instructions.md` file ready to deploy to the repository.

---

## Edge Cases

### Edge Case 1: User is vague about their domain or problem
**Problem:** User says "I want instructions for my project" but doesn't explain what the project is or what's broken.

**Solution:** Don't proceed. Ask clarifying questions: "Tell me more — what does this project do? What domain are we in? What problem are you trying to solve?" Get specific before moving forward.

### Edge Case 2: User picks too many areas to cover
**Problem:** User lists 10+ areas, wants everything covered in one pass.

**Solution:** Help prioritize. Say: "That's a lot. Which 2-3 are causing the most friction right now? Let's nail those first, then we can expand." Start with the core pain points, not everything.

### Edge Case 3: User wants to edit an existing instruction file instead
**Problem:** User says "I have an existing `.instructions.md` — can we update it?"

**Solution:** This skill is for building new instruction files from scratch, not editing existing ones. Clarify: "This skill builds new instruction files. If you want to refine an existing one, that's a different process. Want to keep building this new one, or switch gears?" Stay in scope.

### Edge Case 4: User gets stuck or overwhelmed during the build loop
**Problem:** User can't decide on a section's content, doesn't know how to phrase something, or wants to abandon the process.

**Solution:** Get them unstuck immediately. Options: (1) Simplify the section scope, (2) Provide 2-3 concrete examples they can choose from, (3) Suggest a minimal version and promise to expand later, (4) Narrow the domain focus. Keep momentum going.

### Edge Case 5: Dry run reveals the instructions are incomplete or unclear
**Problem:** During the dry run simulation, something feels broken, unclear, or missing.

**Solution:** Don't just note it — fix it immediately. Go back into the build loop for that section, refine it, and re-run the dry run. Keep iterating until it passes cleanly.

### Edge Case 6: User wants to include sensitive or harmful content in the instructions
**Problem:** User tries to add instructions that violate policies or could cause harm.

**Solution:** Respectfully decline and explain why: "I can't include that in the instructions because [reason]. Can we rephrase this to accomplish your actual goal safely?" Suggest an alternative approach.

---

## Summary

**What it does:** Collaboratively builds deployment-ready custom instruction files that encode standards,
preferences, and domain knowledge for any project or team.

**What triggers it:** The slash command `/instruction-builder` — never natural language auto-trigger.
