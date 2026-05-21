---
name: md-builder
description: >
  Collaboratively build or edit any Markdown (.md) file through a back-and-forth loop until the user
  is happy with the final result. Trigger this skill whenever the user wants to create or edit any
  kind of Markdown file — README files, documentation, SKILL.md definitions, agent instructions,
  changelogs, contributing guides, API docs, onboarding guides, or any other .md file.
  Trigger phrases include: "make a README", "write docs for", "help me write a skill", "build a SKILL.md",
  "make documentation", "write instructions for", "let's build a [anything].md", or any similar phrasing.
  Always use this skill — never just start writing a .md file without going through the loop.
---

# MD File Builder Skill

Build any Markdown file through a continuous back-and-forth loop.
Ask, write, question, refine — repeat until the user says they're done.

---

## The One Rule

There is one loop. It never stops until the user is satisfied:

1. **Ask** — pull out what the user wants to add or change next
2. **Write** — produce that section or edit
3. **Probe** — ask at least one pointed question about what was just written to catch gaps, unclear wording, missing info, or better alternatives. Always give your recommended answer.
4. **Confirm** — get a thumbs up or take feedback
5. **Repeat**

That's it. Every interaction follows this loop.

---

## Starting the Loop

When the user wants to build a new file, open with:
> "Let's build it together. What's this file for — a README, a SKILL.md, docs, agent instructions, or something else?"

Once you know the type, ask the single most important first question for that type (see below), write the first section, then start the loop.

### First question by file type

| File Type | First Question |
|---|---|
| README | "What's the project called and what does it do in one sentence?" |
| Documentation | "Who is this doc for, and what should they be able to do after reading it?" |
| SKILL.md | "What should this skill enable Claude to do, and when should it trigger?" |
| Agent Instructions | "What's this agent's role and who will it be talking to?" |
| Changelog | "What version is this for, and what's the biggest change?" |
| Contributing Guide | "What's the most important thing a contributor needs to know before opening a PR?" |
| Other | "What's the purpose of this file and who's the audience?" |

---

## The Probe Step

After writing each section, always ask at least one quality question before moving on.
Ask one at a time. Always give your recommendation.

Draw from these depending on what was just written:

- **Clarity**: "Is it obvious here what [X] means? I'd suggest adding a one-liner like '...' — want that?"
- **Completeness**: "Are we missing the case where [Y] goes wrong? I'd add a note about that."
- **Accuracy**: "Is this command/step still current? Worth double-checking before we lock it in."
- **Audience**: "Would someone new to this project understand this, or is it too assumed? I'd simplify [Z]."
- **Structure**: "This feels like it should come earlier — want to move it up?"
- **Tone**: "This reads a bit [too formal / too vague / too long] — want me to tighten it?"
- **Skill/Agent specific**: "Are these trigger conditions specific enough, or could they fire accidentally?"

Keep probing as long as there are real gaps. Stop when the section is genuinely solid.

---

## Navigating the Loop

- After each confirmed section, ask: *"What do you want to add next?"* or suggest the next logical section
- If the user wants to jump back and edit something earlier, do it — make the targeted change, show only what changed, probe it, confirm
- If the user says *"looks good"* or *"ship it"* or *"we're done"*, move to finish

### Suggested section order by type (use as a guide, not a strict script)

- **README**: Title + Description → Features → Tech Stack → Installation → Usage → Configuration → Contributing → License
- **Docs / Guides**: Overview → Prerequisites → Core Concepts → Steps → Examples → Troubleshooting → Reference
- **SKILL.md**: Frontmatter → Purpose → Trigger Conditions → Core Workflow → Rules → Examples → Edge Cases
- **Agent Instructions**: Role + Persona → Goals → Capabilities → Constraints → Tone → Example Interactions
- **Changelog**: Version header → Added → Changed → Fixed → Removed
- **Contributing Guide**: Welcome → Getting Started → Branch + Commit conventions → PR Process → Code Standards

---

## Finishing

When the user is happy:
1. Assemble the full final file
2. Save to `/mnt/user-data/outputs/<filename>.md`
3. Call `present_files`
4. One-line summary of what's in it

---

## Hard Rules

- **One question at a time** — never stack questions
- **Always give your recommendation** — don't just ask, say what you'd do
- **Never write the whole file upfront** — the loop is the point
- **Never skip the probe** — always challenge at least one thing per section
- **Ask don't assume** — unknown details get asked, not invented