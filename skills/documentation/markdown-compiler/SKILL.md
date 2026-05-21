---
name: markdown-compiler
description: 'Compile raw markdown source files (.raw) into clean, formatted markdown (.md) files. Use when you have rough notes or documentation content that needs tidying up, or when you need to keep source and compiled versions in sync. Trigger on: "compile this raw file", "turn my .raw into markdown", "sync my .raw and .md files", "clean up this raw content".'
argument-hint: 'Share your .raw file path or paste the raw content'
---

# Markdown Compiler Skill

Transform `.raw` source files into clean, readable `.md` files — without killing the author's voice.

- **Input**: `.raw` files (rough notes, outlines, casual writing)
- **Output**: `.md` files (clean, formatted, human-sounding)
- **Sync**: changes to `.raw` flow through to `.md` on request

---

## Core Rules

### 1. Preserve Voice

The author's tone is not a bug. Clean it up, don't replace it.

- Fix spelling, grammar, and clarity
- Remove slang that reads unprofessional in a doc (e.g. "deadass", "lol", "imo")
- Keep the sentence rhythm and casual confidence if that's the source tone
- Don't expand bullet points into paragraphs
- Don't add corporate filler ("This document aims to provide an overview of...")
- Short sentences are fine. Fragments are fine if they're intentional.

**Rule of thumb**: if the source sounds like a person, the output should too — just a tidier one.

---

### 2. Resolve Context Placeholders

Any `[placeholder]` in the `.raw` file is an instruction to resolve from context, not literal text to keep.

**How to handle them:**

| Placeholder | Action |
|---|---|
| `[all available skills]` | Read context, list the actual skills |
| `[current date]` | Insert today's date |
| `[project name]` | Infer from file/folder name, or ask |
| `[anything unresolvable]` | Flag it to the user — never leave raw brackets in the output |

**Never** silently drop or keep a `[placeholder]` in the compiled `.md`. Either it gets filled, or the user gets told:
> ⚠️ Couldn't resolve `[xyz]` — what should go here?

---

### 3. Format, Don't Over-Format

Apply just enough structure to make the doc readable:

- One H1 at the top
- Logical H2/H3 sections if the content warrants it
- Code blocks with language identifiers (` ```bash `, ` ```json `, etc.)
- Inline code for commands, paths, and technical terms
- Bullets stay bullets — don't convert them to prose
- Consistent capitalization in lists

Don't add sections that aren't in the source. Don't pad it out.

---

## Workflow

### Step 1 — Read the source

If given a file path, read it. Assess:
- What type of doc is this? (README, personal notes, guide, etc.)
- What's the tone? (casual, technical, instructional?)
- Are there any `[placeholders]` to resolve?

### Step 2 — Resolve placeholders

Before writing anything, identify all `[placeholders]` and resolve them from context. Flag any you can't resolve.

### Step 3 — Compile

Apply formatting and language cleanup following the core rules above. Keep it tight — don't add fluff.

### Step 4 — Output

Create the `.md` file with the same name in the same directory. Then give a short summary:

```
✅ compiled [filename].raw → [filename].md

changes:
- [brief list of what changed]

placeholders resolved: [list]
placeholders flagged: [list, if any]
```

---

## Sync

When the user asks to sync:

1. Check which file is newer — `.raw` or `.md`
2. If `.raw` is newer → recompile
3. If `.md` is newer → ask: "Your `.md` is ahead of the source — should I merge changes back to `.raw`?"
4. If same → nothing to do

---

## Example

**Source (`workflow.raw`)**:
```
# my production workflow

how i keep my setup consistent accross devices. im on windows rn, might dual boot linux eventually

vsc is my visual studio code settings
copilot is copilot ai — settings, skills, instructions, agents

deadass just copy paste the folders into the right places

for copilot find .copilot and copy the folders in
for vsc open `Open User Settings (JSON)` and paste the json

ALL AVAILABLE SKILLS:
[all available skills]
```

**Compiled (`workflow.md`)**:
```markdown
# Production Workflow

How I keep my setup consistent across devices. Currently on Windows, might dual boot Linux eventually.

## What's Here

- **vsc/** — Visual Studio Code settings
- **copilot/** — Copilot AI settings, skills, instructions, and agents

## How to Use

Copy and paste the folders into the right places — that's it.

- **Copilot**: find `.copilot` and drop the folders in
- **VSC**: open `Open User Settings (JSON)` and paste the JSON

## Available Skills

- markdown-compiler
- docx
- pdf
- [...]
``` 