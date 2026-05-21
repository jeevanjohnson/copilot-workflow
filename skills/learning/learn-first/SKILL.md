---
name: learn-first
description: 'Use this skill whenever the user describes a project idea and wants to know what they should learn or understand before starting to build it. Triggers on: "what do I need to know to build X", "I want to make X but don''t know where to start", "what concepts should I learn before building X", "break down what I need to understand for X", "I have this project idea". Always apply proactively when someone describes a project goal and seeks prerequisite knowledge—don''t answer from general knowledge alone, follow the full structured workflow.'
argument-hint: 'Describe your project idea'
---

# Learn-First Skill

**Purpose**: Help users figure out **what they need to learn before starting a project** by producing a comprehensive, structured learning roadmap with prioritized concepts, learning resources, and curated video paths for each major topic.

## Core Goal

Given a project idea, produce a **complete prerequisite knowledge map** that:
- Identifies all the concepts, tools, and domains involved
- Explains each in plain language and *why* it matters for this specific project
- Prioritizes them with clear learning order (must-know first vs. nice-to-knows)
- Recommends concrete learning resources and video tutorials for each concept
- Builds a logical learning sequence you can follow step-by-step
- Distinguishes foundational knowledge from domain-specific expertise

## Workflow

### Step 1: Clarify the Project (if needed)

If the project description is vague, ask **ONE clarifying question** to understand:
- What platform/language/environment they're targeting (if relevant)
- What their current skill level is (beginner, some coding experience, etc.)
- Approximate scope/complexity level
- Timeline expectations (learning before building)

Don't over-ask. If you have enough to work with, proceed directly to Step 2.

### Step 2: Decompose the Project

Mentally break the project down into its core components. Think about:
- What does this thing actually *do* at a technical level?
- What systems interact? (data, UI, algorithms, APIs, storage, etc.)
- What's custom-built vs. what's off-the-shelf?
- What domain knowledge is needed (math, domain-specific formats, subject matter expertise, etc.)?
- What are the hardest/most critical parts to learn first?

### Step 3: Map Prerequisites by Category

Group prerequisites into **themed clusters** relevant to the project. Common clusters include (pick what's relevant, don't force all of them):

- **Core language / platform** — what language, runtime, or environment they'll work in
- **Domain concepts** — subject matter knowledge (e.g., audio theory for music apps, game file formats for modding tools)
- **Algorithms / math** — any math, logic, or algorithmic thinking required
- **Libraries / frameworks** — key tools they'll lean on and what each one does
- **Data & I/O** — how data is stored, read, formatted, and transformed
- **AI / ML** (if applicable) — models, training, inference, datasets
- **Infrastructure** — APIs, deployment, databases, services
- **Dev fundamentals** — version control, debugging, structuring a codebase
- **Testing & quality** — unit testing, integration testing, performance profiling
- **Design patterns** — architectural choices and best practices for this domain

### Step 4: For Each Concept, Build a Complete Entry

Each entry should include:

1. **Concept name** (clear, searchable)
2. **What it is** — plain-language, 1-2 sentences
3. **Why you need it for this project** — specific to their idea, not generic
4. **Priority** — 🔴 Must Know First / 🟡 Learn When You Get There / 🟢 Nice to Know
5. **Learning time estimate** — rough hours needed (1-2 hours, 5-10 hours, etc.)
6. **Concrete starting resources** — specific tutorials, courses, or video topics (not just generic search terms)
7. **Key skills to practice** — what you should actually *do* to learn this concept

### Step 5: Suggest a Logical Learning Order

Build a **recommended learning sequence** — a numbered path from "start here" to "now you're ready to build." Keep it to 5–10 steps max. This should form a dependency graph where prerequisites are learned before dependent concepts.

Show the path visually if helpful (e.g., "Learn X → Then Y → Then Z, alongside A and B in parallel").

### Step 6: Optional — Offer Curated Video Learning Paths

For the top 3–5 most critical concepts, offer to provide a **curated video learning path**. 

Ask: **"Would you like me to research YouTube videos and create ordered learning paths for [List the 3-5 core concepts]? I'll find beginner-friendly tutorials and progressively deeper resources so you can learn by watching."**

Only if the user explicitly says yes, delegate to `LRS-youtube-research` skill for each major concept, requesting:
- A structured video sequence (foundations → core concepts → worked examples)
- Mix of beginner and intermediate resources
- Diverse formats: short explainers, longer tutorials, visual demonstrations

## Output Format

Use this structure in your response:

```
## 🗺️ What You Need to Learn: [Project Name]

### [Category Name]

**[Concept Name]** — 🔴 / 🟡 / 🟢
What it is: ...
Why you need it: ...
Learning time: ...
Where to start: ...
Practice by: ...

[repeat for each concept in category]

---

### [Next Category]
...

---

## 📚 Recommended Learning Order

**Phase 1: Foundations (you can start immediately)**
1. [Concept A] — learn in X hours via [Resource]
2. [Concept B] — learn in X hours via [Resource]
...

**Phase 2: Core Skills (after Phase 1)**
N. ...

**Phase 3: Advanced Topics (optional, learn as you build)**
...

---

## 🎬 Video Learning Paths

For your top priorities, I can research curated YouTube video sequences. Would you like ordered video learning paths for:
- [Core Concept 1]
- [Core Concept 2]
- [Core Concept 3]

Just say yes, and I'll find beginner-friendly tutorials and progressively deeper resources for each.

---

## 💡 Key Insights & Warnings

[Optional: any important caveat, hard parts, common beginner mistakes, or encouragement about learning this domain]
```

### Key elements of strong output:

**Concept Entries:**
```
**[Concept Name]** — 🔴 / 🟡 / 🟢
What it is: [1-2 sentence plain-language definition]
Why you need it: [Specific to this project — how it connects to the final goal]
Learning time: [3-5 hours / 2-3 days / 1-2 weeks]
Where to start: [Specific resource: "Khan Academy course: Python Functions" NOT just "search for functions"]
Practice by: [Concrete action: "Build a function library", "Write 5 small functions", "Refactor existing code"]
```

**Resource specificity:**
- ✅ "Khan Academy's Python course, Videos 1-5 (Functions section)"
- ✅ "Codecademy's JavaScript tutorial, Module 3"
- ✅ "MDN Web Docs: Async/Await (https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)"
- ❌ "Google 'Python functions tutorial'"
- ❌ "Some online course about X"

## Tone & Style Guidelines

- **Plain language first.** Assume the user is smart but not yet familiar with the jargon. Define specialized terms when first mentioned.
- **Be specific and actionable.** Generic advice like "learn Python" is not helpful. "Learn how to read and write files in Python (file I/O) via Khan Academy's Python course, Module 5" is better.
- **Be honest about complexity and time.** If something is hard (e.g., training a custom ML model), say so. Suggest simpler alternatives when they exist ("You don't need to train a model yourself; try a pre-trained model first to understand the concept").
- **Connect each concept to the project.** Every line should answer "Why do I need this for my specific project?" not generic information.
- **Don't overwhelm.** If a project is huge, focus on the most critical prerequisites (Phase 1) and mention that there's more to discover as you build.
- **Encourage strategic thinking.** The user is trying to be smart about their learning path — validate this and reinforce that this approach will save them time and frustration.
- **Suggest practical learning methods.** Don't just name concepts — recommend HOW to learn them: "Build X to practice Y" or "Complete this tutorial and then try building Z."
- **Estimate time honestly.** Help users allocate learning time realistically. Phase 1 might be 20-40 hours; Phase 2 another 30 hours. Let them know what they're committing to.

## When to Use This Skill

✅ **Use when**:
- User describes a project idea and explicitly asks what to learn first or where to start
- User says "I don't know where to start" for a project idea
- User wants a prerequisite knowledge map before diving into building
- User is planning a learning journey for a specific goal
- User mentions having a project idea and is uncertain about scope/requirements
- A project requires learning in an unfamiliar domain

❌ **Don't use when**:
- User is asking for general programming knowledge (e.g., "how do I learn Python in general?") — use `LRS-study-guide` or `LRS-youtube-research` instead
- User is debugging or fixing existing code
- User is asking for implementation help on an active project
- User has already started building and is now asking how-to questions
- User asks "should I learn X or Y" as a general career question without a specific project context

## Quality Standards

✓ **Every concept must have a clear "why"** — Connect to the project goal, not abstract learning  
✓ **Resources must be specific** — Not "search for X" but "Khan Academy's Y course, Module Z"  
✓ **Learning time estimates must be realistic** — Include time for tutorials AND practice  
✓ **Organize into digestible phases** — Phase 1 (must-know first), Phase 2 (core), Phase 3 (optional)  
✓ **Offer video learning paths proactively** — Ask if they want curated YouTube sequences for top concepts  
✓ **Include practice recommendations** — Tell them what to *build* or *do* to solidify each concept  
✓ **Be honest about prerequisites** — If they need to learn something foundational first (e.g., algebra for ML), mention it  
✓ **Acknowledge the difficulty curve** — Warn about genuinely hard topics and suggest ways to tackle them  
✓ **Don't orphan users mid-learning** — Suggest when to take breaks, start building, and iterate

## Example Walkthrough

**Project idea**: "I want to build an OSU beatmap AI generator"

**Decomposition**: This involves audio processing, domain-specific file formats, ML/AI concepts, data pipelines, and Python tooling.

**Categories**:
- OSU Domain Knowledge
- Audio Processing Fundamentals
- AI/ML Fundamentals
- Data Pipeline & Training
- Core Language & Tools
- Dev Fundamentals

**Learning Order**:
1. OSU beatmap format basics (what you're generating) — 2-3 hours via official wiki + YouTube tutorials
2. Audio file reading and BPM analysis (input understanding) — 3-4 hours via librosa documentation and tutorials
3. ML concepts: what generative models are (high-level framing) — 4-5 hours via 3Blue1Brown videos
4. Python file I/O and libraries (implementation basics) — 5-8 hours via Codecademy or freeCodeCamp
5. Audio processing with librosa (domain tool) — 4-6 hours of hands-on tutorial + practice projects
6. Sequence modeling concepts (ML specifics for time-series) — 8-10 hours via deeplearning.ai course
7. Datasets and training pipelines (data engineering) — 6-8 hours via Hugging Face tutorials
8. Ready to start building!

**Video paths offered**: "Would you like me to find curated YouTube videos for Audio Processing, Deep Learning Fundamentals, and Sequence Modeling? I'll create ordered learning sequences so you can learn by watching."
