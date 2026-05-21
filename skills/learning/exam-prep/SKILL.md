---
name: exam-prep
description: 'Build targeted exam preparation from lecture notes, previous exams, or course materials. Generates multi-problem practice sets with timing, confidence tracking, and subject-specific exam strategies. Use when studying for midterms, finals, standardized tests, or comprehensive exams.'
argument-hint: 'Share exam topics, lecture notes, or past exam papers'
---

# Exam Prep Skill

Build a structured, effective exam preparation plan with timed practice problems and confidence tracking.

## What This Skill Produces

1. **Exam Format Overview** — What to expect (question types, time limit, grading, passing score)
2. **Topic Breakdown** — All topics likely to appear with estimated coverage percentage
3. **Timed Practice Problem Set** — 4–6 representative problems covering the full range of difficulty
4. **Worked Solutions with Timing** — Each problem solved with annotations showing a reasonable time budget
5. **Confidence Tracker** — Track your mastery across topics as you practice
6. **Exam-Day Strategies** — Time management, prioritization, and subject-specific tips

## When to Use This Skill

Trigger this skill when you need to:
- **Prepare for a midterm, final, or cumulative exam**
- **Study for standardized tests** (SAT, GRE, LSAT, AP exams, etc.)
- **Practice for a technical interview** or coding assessment
- **Build a study plan** from existing lecture notes or past exams
- **Assess weak areas** and focus revision on low-confidence topics

Share any combination of:
- **Exam syllabus** or list of topics covered
- **Lecture notes or slides** from the course
- **Previous exam papers** or sample questions
- **Textbook chapters** or practice problem sets
- **General topic** ("I need to study for a calculus exam")

---

## Workflow

### Step 1 — Identify the Exam

Ask yourself (or clarify with the user):
- **Exam name/course** — What are you studying for?
- **Format** — Multiple choice? Free response? Mixed? Time-limited?
- **Scope** — Full course or specific units? How many chapters/topics?
- **Difficulty level** — Is this introductory, intermediate, or advanced?

If the user doesn't specify, ask one clarifying question:
> "What course or exam are you preparing for, and do you know the format (multiple choice, short answer, essay, etc.)?"

---

### Step 2 — Build the Topic Breakdown

Extract all topics/chapters/units that could appear on the exam. For each topic, estimate:
- **Likelihood** — How heavily tested (high/medium/low)
- **Your confidence** — How well you understand it (1-5 scale, initially)
- **Estimated weight** — Percentage of exam that covers this topic

**Format:**
```
## 📋 Exam Topics & Coverage

| Topic | Confidence | Weight | Priority |
|-------|-----------|--------|----------|
| [Topic 1] | 🟡 3/5 | 25% | High |
| [Topic 2] | 🟢 4/5 | 15% | Medium |
| [Topic 3] | 🔴 2/5 | 30% | High |
```

Use this to identify weak areas early and allocate study time accordingly.

---

### Step 3 — Create Timed Practice Problems

Design **4–6 representative problems** that span the difficulty and topic range of the actual exam.

For each problem:
- **State the topic** clearly
- **Show the problem statement** exactly as it might appear
- **Indicate time budget** (e.g., "Budget: 5 minutes for this MCQ block")
- **Difficulty flag** (Easy / Medium / Hard)
- **Multiple-choice options** (if applicable) or blank space for written answers

**Format:**
```
## 🎯 Timed Practice Set

### Problem 1 — [Topic] [Easy]
**Time Budget:** 3 minutes

[Problem statement]

A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

---

### Problem 2 — [Topic] [Medium]
**Time Budget:** 8 minutes

[Problem statement with any diagrams or context]

Answer: _____________________

---
```

---

### Step 4 — Worked Solutions with Timing

After the problem set, provide **complete solutions** for each problem.

For each solution:
- **Show the full working/reasoning** step-by-step
- **Annotate timing** ("At 2 minutes, you should have identified that...", "By 4 minutes, you should be at this step")
- **Highlight the key insight** that solves the problem
- **Flag common mistakes** people make on this problem type
- **Note alternative approaches** if multiple valid methods exist

**Format:**
```
## ✅ Worked Solutions

### Solution 1 — [Topic]

**Expected timing:** 3 minutes

**Step 1:** [Identify what the problem is asking]
*(1 minute mark: You should recognize this is a [problem type])*

**Step 2:** [Work through the method]
*(2 minute mark: By now, you should have [intermediate result])*

**Step 3:** [Arrive at the answer]

**Answer:** [Final answer with justification]

**Key insight:** Why this approach works — the core concept
**Common mistake:** What trips people up here
**Faster method:** If applicable, show a shortcut
```

---

### Step 5 — Build the Confidence Tracker

Create a simple self-assessment tool the user can fill in as they practice.

**Format:**
```
## 📊 Confidence Tracker

After completing the practice set, rate yourself on each topic:

| Topic | Before | After | Notes |
|-------|--------|-------|-------|
| [Topic 1] | 2/5 | __/5 | |
| [Topic 2] | 4/5 | __/5 | |
| [Topic 3] | 2/5 | __/5 | |

**Goal:** Get all topics to 4/5 or higher before exam day.
**Next steps:** Topics still below 3/5 need targeted review.
```

---

### Step 6 — Exam-Day Strategies

Provide **subject-specific, exam-format-specific tips** for performing well on test day.

**For all exams:**
- Read all instructions carefully before starting
- Scan the entire exam first to allocate time strategically
- Answer easy problems first to build confidence
- Flag hard problems and return to them if time permits
- Review answers if time allows

**By subject:**

**Math/Physics/Engineering:**
- Show units/labels throughout
- Double-check arithmetic in the final step
- If stuck, try working backwards from the answer choices
- For word problems, define variables clearly at the start

**Computer Science/Programming:**
- Write pseudocode first, then code (if it's coding)
- Test with simple inputs before complex ones
- For algorithm questions, state time/space complexity explicitly
- Practice on actual exam format (online? paper? IDE?)

**History/Social Sciences/Humanities:**
- Structure essay answers: intro → body points → conclusion
- Use specific examples (not vague generalizations)
- Define key terms in the first mention
- If unsure about a date/name, skip specific claims and focus on concepts

**Chemistry/Biology:**
- Draw mechanisms or structures (even if rough) to organize thinking
- Label all parts of diagrams clearly
- For calculations, show the formula first, then plug in numbers
- State assumptions (pressure, temperature, etc.)

**Languages/Standardized Tests:**
- For reading comprehension, answer questions without rereading if possible
- For grammar, read the sentence aloud mentally to catch errors
- For listening/speaking, don't panic on missed words — keep going
- For timed sections, skip and return rather than get stuck

**Format:**
```
## 🎯 Exam-Day Strategies

### Time Management
- [Specific time budget per section]
- [Which types of questions to do first]

### Priority Strategy
- Easy problems first → builds confidence and locks in points
- Medium difficulty problems second → maximize score
- Hard problems last → only if time permits

### Subject-Specific Tips
- [Tip 1 specific to this subject]
- [Tip 2 specific to this exam format]
- [Common pitfall and how to avoid it]

### Stress Management
- If you get stuck, move on and return later
- Breathe between sections if allowed
- Remember: partial credit counts on [exam type]
```

---

## Output Format Summary

Present the exam prep package in this order:

1. `## 📋 Exam Topics & Coverage` (Topic breakdown with confidence ratings)
2. `## 🎯 Timed Practice Set` (4–6 representative problems with time budgets)
3. `## ✅ Worked Solutions` (Full solutions with timing annotations and strategies)
4. `## 📊 Confidence Tracker` (Self-assessment table)
5. `## 🎯 Exam-Day Strategies` (Subject-specific tips and time management)

---

## Subject-Specific Emphasis

**Math/Physics/Engineering:**
- Include multiple problem types (computation, proof, application)
- Show common algebraic/trigonometric errors
- Practice problems with realistic numbers (not just simple integers)

**Computer Science:**
- Include algorithm complexity analysis for each problem
- Mix conceptual and coding problems
- Show pseudocode and actual code solutions
- Include edge cases and off-by-one errors

**Languages:**
- Include all four skills if applicable (reading, writing, speaking, listening)
- For reading, explain why wrong answers are wrong
- For grammar, explain the rule being tested

**History/Humanities:**
- Include essay prompt + source analysis + short answer mix
- Provide thesis statement templates for essays
- Show how to structure comparative/thematic answers

**Standardized Tests:**
- Mimic the actual test format (timing, question order, scoring)
- Include explanations for every wrong answer, not just right ones
- Note patterns in question types and traps

---

## Quality Standards

✓ **Topic breakdown must be comprehensive** — covers every likely exam question  
✓ **Practice problems are representative** — range from easy to hard, cover all topics  
✓ **Timing annotations are realistic** — budgets match actual exam pace  
✓ **Solutions show the reasoning** — not just answers, but the thought process  
✓ **Confidence tracker is actionable** — identifies weak areas needing review  
✓ **Strategies are subject-specific** — not generic test-taking tips  
✓ **Problems build in difficulty** — start easy, progress to harder types  
