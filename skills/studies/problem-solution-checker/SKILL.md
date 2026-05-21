---
name: problem-solution-checker
description: 'Validate and provide detailed feedback on any problem solution or assignment work. Identifies conceptual gaps, marks errors with explanations, highlights what was done well, and recommends targeted review. Use when checking homework, classwork, practice problems, or any academic assignment.'
argument-hint: 'Share the problem, your attempt/solution, and the correct answer if you have it'
---

# Problem Solution Checker Skill

Get detailed, constructive feedback on your problem work to identify gaps and improve.

## What This Skill Produces

1. **Correctness Assessment** — Is the answer right? Which parts were correct/incorrect?
2. **Conceptual Gap Analysis** — What concept(s) did you miss or misunderstand?
3. **Detailed Error Breakdown** — Where exactly did things go wrong, and why
4. **What You Did Well** — Specific strengths to build on
5. **Targeted Review** — Exactly which topics you need to study based on the errors
6. **Attempt-Specific Guidance** — Not just "this is wrong," but "here's what you were trying and where it derailed"

## When to Use This Skill

Trigger this skill when you:
- **Just finished a problem** and want to verify your work
- **Got a problem wrong** and want to understand why
- **Want detailed feedback** beyond a grade or mark
- **Have a partially correct answer** and want to know what's salvageable
- **Need to understand a mistake** before resubmitting or revising
- **Want to know if your approach is on the right track** before going further

Share:
- **The original problem** (exact wording)
- **Your attempt/solution** (show your work, all steps, reasoning)
- **The correct answer** (if you know it, or what was marked as correct)
- **What you're uncertain about** (if applicable)

---

## Workflow

### Step 1 — Receive and Parse the Submission

Gather what the student did:
- The **problem statement** (complete and exact)
- The **student's full attempt** (including all work shown, not just the final answer)
- The **known correct answer** (or mark/grade received)
- Any **additional context** (course level, topic being studied, what was confusing)

If any critical piece is missing, ask briefly:
> "Can you also share your attempt/work for this problem so I can see where things went off track?"

---

### Step 2 — Check Correctness

Verify the student's answer:
- **Is the final answer correct?** (Yes/No/Partially)
- **Are the intermediate steps correct?** (Mark which ones are right/wrong)
- **Is the method/approach valid?** (Even if the answer is wrong, is the strategy sound?)

Be specific: don't just say "wrong," mark exactly which step(s) failed.

---

### Step 3 — Identify Conceptual Gaps

Diagnose *why* each error occurred:

- **Conceptual misunderstanding** — Student has the right idea but misapplied a concept
- **Procedural error** — Student knows the concept but made an arithmetic/calculation mistake
- **Missed condition** — Student didn't notice a constraint or special case in the problem
- **Wrong method** — Student used a valid technique but the wrong one for this problem
- **Careless mistake** — Correct understanding but a slip (dropped a negative sign, wrong unit, etc.)

This distinction matters: conceptual gaps require learning; careless mistakes just need proofreading.

---

### Step 4 — Detailed Error Breakdown

For **each incorrect step or mistake**:

1. **What they did:** Quote or describe their work
2. **What was supposed to happen:** Correct step with explanation
3. **Why it went wrong:** The root cause (concept, procedure, misread)
4. **How to spot this mistake next time:** What to watch for

**Format:**
```
## ❌ Error 1: [Topic/Concept]

**What you did:**
[Student's incorrect work]

**What should happen:**
[Correct step and result]

**Why it went wrong:**
[The root cause — conceptual / procedural / misread / careless]

**How to avoid this:**
[Specific check or verification step]
```

Repeat for each error.

---

### Step 5 — Acknowledge What Was Done Well

Explicitly highlight strengths:

- **Correct intermediate steps:** "Your calculation in step 2 was spot-on"
- **Valid approach:** "You chose the right method, just applied it to the wrong part"
- **Clear work:** "Your explanation was easy to follow"
- **Good catch:** "You correctly identified the special case here"

This builds confidence and shows the student what to keep doing.

**Format:**
```
## ✅ What You Did Well

- [Specific strength 1 with example]
- [Specific strength 2 with example]
- [Specific strength 3 with example]
```

---

### Step 6 — Targeted Review Recommendations

Based on the errors identified, recommend exactly what to review:

- **If conceptual:** "You need to review [concept] — specifically [sub-topic]"
- **If procedural:** "Practice more [procedure type] problems to build fluency"
- **If careless:** "Before submitting, use [verification check] to catch these"

Include resources: practice problems from the textbook, Khan Academy, course notes, etc.

**Format:**
```
## 📚 Targeted Review

Based on the errors above, focus on:

1. **[Topic] — Conceptual review**
   - Problem type that went wrong: [Type]
   - Why it matters: [Connection to bigger picture]
   - Review resource: [Textbook chapter / Khan Academy / lecture notes / etc.]
   - Practice: Try [similar problem type] until you get 3 in a row correct

2. **[Topic 2] — Procedural practice**
   - Specific skill: [The procedure]
   - Practice problem set: [Where to find more like this]

3. **[Generic habit] — For next time**
   - Verification step: [What to check before submitting]
```

### Step 7 — Offer Video Learning Paths (Optional)

For **conceptual gaps only** (not procedural or careless mistakes), proactively offer curated video learning:

**If gaps are primarily conceptual:**
> "Would you like me to research curated YouTube video sequences for [identified concepts]? I can find beginner-friendly tutorials and progressively deeper resources to help you fully understand these topics before attempting similar problems again."

**Only if the user explicitly says yes**, delegate to `LRS-youtube-research` skill with:
- The specific concepts identified as gaps (e.g., "chain rule in calculus", "photosynthesis mechanisms")
- The problem type that exposed the gap (so videos are problem-solving focused)
- Request: "Create a beginner-to-advanced video sequence for this topic, ending with worked examples similar to [problem type]"

**Do NOT offer videos for:**
- Purely procedural errors (practice is more useful than watching)
- Careless/arithmetic mistakes (verification steps are better)
- When the student is short on time before a deadline (videos take longer than targeted review)

**This creates a natural workflow:**
1. Student solves problem
2. You identify gaps with problem-solution-checker
3. If conceptual: offer videos via youtube-research
4. Student watches videos and revisits the problem
5. Loop back to problem-solution-checker if needed

---

### Step 8 — Revision Guidance (Optional)

If the student wants to resubmit or redo the problem:

1. **Start fresh or patch?** — Is the conceptual understanding there (just fix steps) or rethink from scratch?
2. **Step-by-step guide:** If they want help revising, outline the correct approach without spoiling it
3. **Self-check:** Give them a checklist to verify their new attempt before resubmitting

---

## Output Format Summary

Present feedback in this order:

1. `## 📊 Correctness Assessment` (Overall: right/wrong/partial, and marking of each step)
2. `## ❌ Error Breakdown` (Each mistake with root cause and how to avoid it)
3. `## ✅ What You Did Well` (Specific strengths and correct work)
4. `## 📚 Targeted Review` (Exactly what concepts/procedures to study, with resources)
5. `## 🎬 Video Learning Paths (Optional)` (Only if conceptual gaps exist; ask if user wants curated videos)
6. `## 🔧 Revision Guidance` (Optional: how to redo it if they want)

---

## Subject-Specific Feedback Styles

**Math / Physics / Engineering:**
- Mark arithmetic errors separately from conceptual errors
- Show the correct step immediately after the error (not at the end)
- Use "Did you mean...?" when the approach is sound but slightly off-target
- Check units and significant figures explicitly

**Computer Science / Programming:**
- Show the bug in context (quote the line of code)
- Explain what the code *does* vs. what was *intended*
- For logic errors, trace through execution with sample inputs
- Highlight edge cases or boundary conditions missed
- Praise good naming, comments, structure when present

**Chemistry / Biology:**
- Be very precise with terminology (don't accept approximate language)
- For reactions/mechanisms, check each step of the process
- Draw or describe structures if relevant to the error
- Link procedural errors back to the underlying chemistry/biology

**History / Social Sciences / Humanities:**
- For essays, check: thesis clarity, evidence quality, logical flow, relevance
- For source analysis, verify: accurate interpretation, context awareness, bias recognition
- For debate-style questions, note: argument strength, counterargument awareness, evidence support
- Praise: clear writing, specific examples, nuanced thinking

**Languages:**
- For translation, check: accuracy, idiom, tone
- For grammar, cite the specific rule violated
- For essays, check: coherence, vocabulary precision, structure
- For listening/reading comprehension, explain why wrong answers are incorrect

---

## Video Learning Integration

When conceptual gaps are identified, offer to delegate to `LRS-youtube-research` skill for curated video learning paths.

**Example offer:**
```
## 🎬 Video Learning Paths (Optional)

Your gaps are primarily conceptual (chain rule, implicit differentiation, related rates). These topics are best understood through visual explanation and worked examples.

**Would you like me to research curated YouTube videos for:**
- Chain rule in calculus (with visual derivatives explained)
- Implicit differentiation (step-by-step technique)
- Related rates problems (worked examples similar to the one you attempted)

I'll find beginner-friendly tutorials, visual explanations, and worked examples that match your problem type. Just say yes, and I'll create ordered video sequences.
```

**When user says yes**: Delegate to LRS-youtube-research with the specific concepts and problem type, requesting problem-solving focused video paths.

---

## Tone Guidelines

- **Be encouraging** — Highlight what was done well first
- **Be specific** — Not "you made a mistake," but "in step 3, you distributed incorrectly because..."
- **Be constructive** — Offer the path forward ("here's what to study next")
- **Match the level** — Adjust language complexity to the student's apparent level
- **Avoid shame** — Mistakes are learning moments, not failures

---

## Quality Standards

✓ **Every error gets a root cause** — not just "wrong," but *why* it's wrong  
✓ **Positives are specific** — praise concrete work, not vague encouragement  
✓ **Review recommendations are actionable** — point to exact topics and resources  
✓ **Feedback matches the problem type** — subject-specific language and emphasis  
✓ **Student's reasoning is acknowledged** — even if wrong, show what they were trying  
✓ **Next steps are clear** — what to study, what to practice, what to verify before resubmitting  
✓ **Video learning paths offered for conceptual gaps** — user must explicitly request videos  
✓ **Clear distinction** — videos for conceptual gaps, practice for procedural, verification for careless mistakes
