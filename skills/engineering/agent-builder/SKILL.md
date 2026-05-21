---
name: agent-builder
description: >
  Collaboratively build custom Copilot agents from scratch through a structured back-and-forth loop.
  Use this skill whenever you want to create, build, write, or refine a Copilot agent for your
  AI workflow. Triggers when user runs the slash command `/agent-builder`. Outputs a complete,
  deployment-ready agent configuration file. DO NOT trigger on natural language — slash command
  only. DO NOT trigger for general agent advice, debugging existing agents, or architectural
  questions — this is specifically for building new agent files.
---

# Agent Builder

Collaboratively build custom Copilot agents from scratch through a structured back-and-forth loop.
Guides users to define their agent's purpose, workflow, rules, and behavior. The result is a
deployment-ready agent configuration file ready to use immediately.

---

## Purpose

This skill guides you through building a custom Copilot agent from scratch through a structured back-and-forth loop. It takes a specific workflow or task you want to automate—whether that's code generation, multi-step research, testing automation, specialized analysis, or any other domain-specific need—and collaboratively designs an agent to handle it. The result is a deployment-ready agent configuration file that shapes how your Copilot agent behaves when working on that task—defining its scope, workflow, rules, and decision logic. This is for anyone who wants to create specialized agents tailored to their specific AI workflow without building from scratch alone.

---

## Core Workflow

### Phase 1: Foundation Interview

Before writing anything, gather the context for the agent. Ask these questions one at a time:

1. "What workflow or task should this agent handle?"
   (e.g., "Code review automation", "Research synthesis", "Testing framework setup", "Documentation generation")

2. "What problem is this agent solving? Why does it need to exist as a separate agent vs. doing it manually?"
   (e.g., "Saves time on repetitive tasks", "Needs specialized logic", "Requires multi-step orchestration")

3. "What areas or steps does this agent need to cover?"
   (Let them define the scope — e.g., for a code-review agent: style checking, security analysis, performance review, documentation validation)

   If they list more than 5 or seem overwhelmed, help them prioritize: "Which 2-3 of these are most urgent right now? We can always expand later, but let's focus on the core functionality first." Start with their top picks.

Once you have answers, write the first draft of the agent's **frontmatter** (name, description, purpose) and show it.

### Phase 2: Build Loop — Section by Section

Build the agent configuration section by section:

1. **Write** the next section
2. **Probe** — ask at least one pointed quality question. Always give your recommendation.
3. **Confirm** — get thumbs up or take feedback
4. **Repeat** until all sections are done

After each confirmed section, ask: *"What should we tackle next?"* or suggest the logical next section.

### Phase 3: Dry Run

Once all sections are confirmed, simulate a realistic user triggering and using this agent:

**Scenario:** A user invokes the agent via slash command and it executes the first 2-3 steps of its workflow. Walk through this live and call out anything that felt unclear, incomplete, or broken.

Ask: "Did that feel right? Anything that should have happened differently?"

Fix any issues and re-run if needed.

### Phase 4: Finalize & Deliver

When the dry run passes and the user is happy:
1. Assemble the complete final agent configuration file
2. Deliver it ready to deploy
3. Give a one-line summary of what the agent does

---

## Trigger Conditions

### Execution Model
This skill is slash-command only. It does NOT trigger on natural language. Users must explicitly invoke it via `/agent-builder` or equivalent command to activate.

### WHEN to activate this skill:
- User runs the explicit slash command to trigger this skill

### WHEN NOT to activate (do NOT trigger):
- This skill should ONLY run when explicitly commanded via slash — never auto-trigger on natural language
- Do not activate if the user is asking for general agent advice or architecture, even if they mention "building" or "creating"
- Do not activate if the user is trying to debug or fix an existing agent (that's a different operation)
- Do not activate if the user is asking Claude to behave as an agent or take on a specific role in the current chat (they want different behavior now, not a reusable agent file)
- Do not activate if the user is asking for help choosing which tool or capability to use

---

## Rules & Constraints

### Hard Rules
- **One question at a time** — never stack questions in the foundation interview
- **Always give your recommendation** — don't just ask, say what you'd do
- **Never write the whole agent upfront** — build section by section through the loop
- **Grill the frontmatter hardest** — name and description are the foundation; make sure they're crystal clear before moving on
- **Always do the dry run** — no exceptions, even if the agent seems perfect
- **Never move on without confirmation** — show every section and wait for feedback before proceeding
- **Ask, don't assume** — unknown details get asked, not invented
- **Be deployment-ready** — the final agent configuration should be complete and usable immediately, no follow-up work needed
- **Slash command only** — this skill activates only when explicitly invoked; never auto-trigger on natural language
- **Help users get unstuck immediately** — if a user is overwhelmed, indecisive, or stuck during the build, diagnose the problem and help them move forward right then. Don't defer. Options: simplify the agent scope, provide concrete examples, suggest a minimal version to start, or narrow the workflow focus. Get them unstuck in the current session.

---

## Examples

### Example 1: Building a Code Review Agent

**Trigger:** User runs `/agent-builder`

**Foundation Interview:**

Claude: "What workflow or task should this agent handle?"
User: "Automated code review for pull requests"

Claude: "What problem is this agent solving?"
User: "Developers waste time on manual code reviews. We need consistent, fast feedback on style, security, and performance."

Claude: "What areas does this agent need to cover?"
User: "Style violations, security issues, performance problems, and documentation gaps"

**Build Loop Sample:**

Claude writes and shows the **frontmatter**:
```
---
name: code-review-agent
description: >
  Automated Copilot agent that reviews code for style, security, performance, and documentation.
  Triggers on user demand via slash command. Analyzes pull requests and returns structured feedback.
---
```

Claude probes: "Does this capture the right scope? Should we mention what it does NOT do — like refactoring code or rewriting logic?"
User: "Good catch. It should only report issues, not fix them."

Claude refines, confirms, moves to next section.

[Loop repeats for each section: Workflow Steps → Rules & Constraints → Edge Cases → Checklist]

**Dry Run:**

Claude simulates a user triggering the agent:
- User: "Review this PR for code style and security"
- Agent: Walks through the workflow, pulls code, analyzes it, returns structured feedback
- Claude calls out: "Should the agent ask for context first, or just dive in?"

User approves or gives feedback. Claude adjusts if needed.

**Final Output:**

Complete agent configuration file ready to deploy.

---

## Edge Cases

### Edge Case 1: User is vague about what the agent should do
**Problem:** User says "I want an agent for my workflow" but doesn't explain what the workflow is or what problem it solves.

**Solution:** Don't proceed. Ask clarifying questions: "What specific task or workflow should this agent handle? What problem are you trying to solve?" Get specific before moving forward.

### Edge Case 2: User picks too many areas for the agent to cover
**Problem:** User lists 8+ responsibilities, wants everything in one agent.

**Solution:** Help prioritize. Say: "That's a lot of ground to cover. Which 2-3 are the most urgent? Let's nail those first, then we can expand." Start with core functionality, not everything at once.

### Edge Case 3: User wants to modify an existing agent instead
**Problem:** User says "I have an existing agent — can we update it?"

**Solution:** This skill is for building new agents from scratch, not editing existing ones. Clarify: "This skill builds new agents. If you want to refine an existing one, that's a different process. Want to keep building this new one, or switch gears?" Stay in scope.

### Edge Case 4: User gets stuck or overwhelmed during the build loop
**Problem:** User can't decide on the agent's behavior, doesn't know how to describe a workflow step, or wants to abandon the process.

**Solution:** Get them unstuck immediately. Options: (1) Simplify the agent scope, (2) Provide 2-3 concrete examples they can choose from, (3) Suggest a minimal version and promise to expand later, (4) Narrow the focus to one core task. Keep momentum going.

### Edge Case 5: Dry run reveals the agent scope is unclear or incomplete
**Problem:** During the dry run, the agent's responsibilities feel fuzzy, overlapping, or it's not clear what it should do first.

**Solution:** Don't just note it — fix it immediately. Go back into the build loop for that section, clarify the agent's behavior, and re-run the dry run. Keep iterating until it's airtight.

### Edge Case 6: User wants the agent to do something harmful or unsafe
**Problem:** User tries to build an agent for something that violates policies or could cause harm.

**Solution:** Respectfully decline and explain why: "I can't build an agent for that because [reason]. Can we redesign this to accomplish your actual goal safely?" Suggest an alternative approach.

---

## Summary

**What it does:** Collaboratively builds deployment-ready custom Copilot agents from scratch through a structured back-and-forth loop, transforming a workflow idea into a fully configured agent ready to use.

**What triggers it:** The slash command `/agent-builder` — never natural language auto-trigger.
