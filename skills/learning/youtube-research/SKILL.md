---
name: youtube-research
description: >
  Use this skill whenever a user wants to learn about a topic through YouTube videos,
  wants video recommendations for a subject, or asks "what should I watch to understand X",
  "find me YouTube videos about X", "best videos to learn X", "help me learn X through videos",
  or any variation of wanting curated video content to deeply understand a topic.
  Also trigger when a user says "research X for me" and would benefit from video learning,
  or when they ask to "fully understand" a topic and video content would help.
  This skill performs structured research on the topic first, then finds and ranks the best
  YouTube videos that together give the user a complete, layered understanding from beginner
  to advanced. Additionally, it generates a comprehensive lecture-style markdown document
  that teaches the topic using the videos as reference material.
---

# YouTube Research Skill

Helps users deeply understand any topic by researching it, finding the best videos
to watch via Invidious — curated, ordered, and explained so they know exactly why to watch each one.
Additionally, generates a comprehensive lecture-style markdown document that teaches the topic
using the videos as reference material — perfect for learning at your own pace.

**For the agent:** This skill delegates research to the **Explore** subagent, uses `fetch_webpage` to search Invidious
and verify videos, and applies quality curation to build a learning path from beginner to advanced.
It then synthesizes the topic into a structured markdown document with lecture-style content.

---

## Workflow

### Step 1 — Understand the context and topic scope

**Determine the context first:**
- Are you being called from **LRS-study-guide with a specific problem?** If yes, activate **Problem-Solving Mode** (see Step 6B below)
- Or is this a general topic research request? Continue with standard research mode.

**For topic scope:**
- Is this a broad domain (e.g. "machine learning") or a specific question (e.g. "how does backpropagation work")?
- What level of depth is implied? Adjust the search strategy accordingly.
- Break broad topics into logical sub-themes (foundations, mechanisms, applications, debates, etc.)

### Step 2 — Research the topic first

Build a real understanding of the topic before hunting for videos using `runSubagent` with the **Explore** agent. This is what separates a curated list from a random one.

**How to research:**
- Delegate to Explore agent with queries like: "Research [topic]: what are the core concepts, key subtopics, common misconceptions, and recent developments?"
- Ask about foundational knowledge vs. advanced nuances
- Gather context on expert perspectives and best practices in the field

Do **2–4 research queries** on the topic itself before searching YouTube.

### Step 3 — Find the best YouTube videos

Search videos via **Invidious** (privacy-focused YouTube frontend) using `fetch_webpage`:

**Search Invidious directly for:**
- `https://inv.nadeko.net/search?q=[topic]+explained`
- `https://inv.nadeko.net/search?q=[topic]+tutorial`
- `https://inv.nadeko.net/search?q=[topic]+deep+dive`
- `https://inv.nadeko.net/search?q=[educator+name]` (for known experts)
- `https://inv.nadeko.net/search?q=[topic]+lecture`

**Example searches:**
- `https://inv.nadeko.net/search?q=big+O+notation`
- `https://inv.nadeko.net/search?q=Master+Theorem+algorithm`
- `https://inv.nadeko.net/search?q=algorithm+complexity+analysis`

**For each promising video, fetch its Invidious page** using `fetch_webpage` on the Invidious URL (format: `https://inv.nadeko.net/watch?v=[VIDEO_ID]`) to verify:
- Actual title, channel name, view count, and description
- Upload date and relevance to learning goals
- No login walls or accessibility issues (Invidious is login-free)

### Step 4 — Curate and rank

Select **6–10 videos** that together form a complete learning path. Apply these criteria:

**Quality signals:**
- High view count relative to upload date
- Reputable channel or recognized expert
- Description matches the actual depth needed
- Covers something unique the other videos don't

**Diversity requirements — your list MUST include:**
- At least 1 beginner/overview video
- At least 1 deep-dive or technical video  
- At least 1 visual/animated explainer if available
- At least 1 longer lecture or comprehensive walkthrough
- Mix of formats: short explainers, long lectures, interviews, demos

**Exclude:**
- Clickbait titles with no substance
- Outdated content on fast-moving topics (flag if unavoidable)
- Redundant videos covering the same ground

### Step 5 — Generate a comprehensive lecture markdown

After identifying the best videos, synthesize the topic into a detailed markdown document structured like lecture slides. This document should:

**Structure:**
- **Title & Introduction** — Overview of the topic and what will be covered
- **Table of Contents** — Clear navigation
- **Core Sections** — Organized by logical progression (foundations → intermediate → advanced)
- **Key Concepts** — Defined terms and foundational ideas
- **Examples & Diagrams** — Use ASCII art, tables, or descriptions of visual concepts
- **Common Misconceptions** — Address frequent confusions
- **Practical Applications** — Real-world uses and implementation guidance
- **Further Learning** — Links to the curated videos, additional resources

**Writing approach:**
- Write as if teaching the topic, with narrative flow
- Use the video titles, descriptions, and topics as reference points for content organization
- Create a self-contained document that teaches the subject (don't just link to videos)
- Include specific concepts that appear in multiple videos as emphasis on importance
- Structure with headers, bullet points, and clear sections for readability
- Aim for 3,000–5,000 words of substantive content

**Example structure:**
```markdown
# [Topic]: A Comprehensive Guide

## Introduction
[Brief overview of what the topic is and why it matters]

## Table of Contents
1. [Foundations](#foundations)
2. [Core Concepts](#concepts)
...

## Foundations
### What is [Topic]?
[Definition and context]

### Historical Context
[Where it came from]

## Core Concepts
### Concept 1: [Name]
[Detailed explanation with examples]

...

## Advanced Topics
[Deeper dives for those wanting mastery]

## Common Misconceptions
- **Misconception:** ...
  **Reality:** ...

## Practical Applications
[How to use this knowledge]

## Further Learning
[Video links, books, papers]
```

### Step 6 — Present the results

Present videos in **two distinct learning paths**:

#### Path 1: Deep Dive (Comprehensive Understanding)

Order videos chronologically by progression from foundational to advanced concepts. Group into phases:

**Format for each video:**
```
## [Phase Name] (e.g., Foundations, Core Concepts, Advanced Mastery)

### [N]. [Video Title]
**Channel:** [Channel Name]  
**Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]  
**Length:** [duration if known]  
**Why watch this:** [2–3 sentences explaining what this covers, why it's good, and what the viewer will get from it]  
**Best for:** [Beginner / Intermediate / Advanced]
```

**After the list, include:**
- A narrative explaining the progression and **why this order builds understanding**
- A "If you only watch one" recommendation with a sentence explaining why
- Any key concepts to look up alongside the videos (books, papers, docs)
- A link to the **generated lecture markdown** for self-contained learning

#### Path 2: Quick Review (Fast Grasp)

Create a shorter subset (3–4 essential videos) that captures the core concepts in minimal time:

**Format:**
```
## Quick Review Path (~[total duration])

Watch these videos in order for a rapid but solid understanding of the topic:

### [N]. [Video Title]
**Channel:** [Channel Name]  
**Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]  
**Length:** [duration if known]  
**Why this:** [1–2 sentences on why this is essential and what's the minimum you need to know]
```

**Guidance:**
- Focus on overview + 1–2 deep dives on critical concepts
- Skip tutorials or niche applications for this path
- Should take 30–90 minutes total depending on topic complexity
- Useful for time-constrained learners or quick refreshers

#### Presentation Structure

Present both paths clearly with:
1. **Deep Dive Path** — Full progression with all 6–10 videos
2. **Quick Review Path** — Streamlined 3–4 video option
3. A note on when to use each ("Use Deep Dive if you want mastery; use Quick Review if time is limited")

**Output both:**
1. The curated video list with both paths
2. A complete markdown document on the topic (generated as a separate artifact or file)

---

### Step 6B — Problem-Solving Mode (When Called from Study Guide with a Specific Problem)

**When you receive a problem context from LRS-study-guide**, restructure the output explicitly as:

**"Watch these videos in this order to solve this problem:"**

**Format:**

```
## 🎬 Video Learning Path to Solve This Problem

### Watch These Videos In Order:

**Video 1: [Prerequisite Concept]**
- **Title:** [Exact video title]
- **Channel:** [Channel name]
- **Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]
- **Length:** [duration]
- **Why:** This teaches [concept needed for Step 1 of the solution]
- **Key takeaway:** [What you'll understand after watching]

→ **After Video 1, you'll understand:** [concept summary]

---

**Video 2: [Core Technique from Solution Step 2]**
- **Title:** [Exact video title]
- **Channel:** [Channel name]
- **Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]
- **Length:** [duration]
- **Why:** This teaches the [specific technique/method] needed to [solve Step 2 of the problem]
- **Key takeaway:** [What you'll be able to do after watching]

→ **After Video 2, you can:** [skill gained]

---

**Video 3: [Next Solution Step]**
- **Title:** [Exact video title]
- **Channel:** [Channel name]
- **Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]
- **Length:** [duration]
- **Why:** This covers [method/concept] which is [how it's used in Step 3]
- **Key takeaway:** [Actionable understanding]

→ **After Video 3, you can:** [skill or understanding]

---

**Video 4: [Worked Example Problem]**
- **Title:** [Exact video title]
- **Channel:** [Channel name]
- **Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]
- **Length:** [duration]
- **Why:** Watch someone solve a problem **like the one you're trying to solve** using the techniques from Videos 1–3
- **Key takeaway:** See the full strategy in action

→ **After Video 4:** You've seen the complete workflow

---

**Video 5 (Optional): [Similar Problem Type or Advanced Application]**
- **Title:** [Exact video title]
- **Channel:** [Channel name]
- **Link:** [https://inv.nadeko.net/watch?v=VIDEO_ID]
- **Length:** [duration]
- **Why:** Extends to [related problem type or concept], so you can solve similar problems and variations
- **Key takeaway:** Apply the technique to [broader context]

---

## Now You Can Solve It

**After watching Videos 1–4 in order, you have:**
- ✅ Understood [Prerequisite 1]
- ✅ Mastered [Technique from Solution Step 2]
- ✅ Learned [Technique from Step 3]
- ✅ Seen the full problem-solving workflow in action

**You're ready to solve:**
- ✅ The original problem
- ✅ Similar problems of this type
- ✅ Related problems using the same techniques (as shown in Video 5)
```

**Key differences from standard mode:**
1. **Explicit mapping** — Each video is tied to a specific step in the problem solution
2. **Progressive enablement** — Each video unlocks a new capability ("After Video X, you can...")
3. **Problem-focused framing** — "To solve THIS problem, watch X, then Y, then Z"
4. **Worked example emphasis** — Always include a real problem solved using these exact techniques
5. **Recap** — End with a summary showing the viewer is now ready to solve the problem and variations

---

## Tool Usage & Limitations

**Available tools:**
- `runSubagent` with **Explore** agent for topic research and background knowledge
- `fetch_webpage` to search Invidious and verify video URLs/metadata
- Direct knowledge to propose well-known educators and channels

**Search method:**
- Use `fetch_webpage` with Invidious search URLs: `https://inv.nadeko.net/search?q=[QUERY]`
- Invidious provides YouTube content without login walls
- Parse search results to extract video URLs in format: `https://inv.nadeko.net/watch?v=[ID]`
- Fetch individual video pages to confirm titles, descriptions, view counts, and dates

**Advantages:**
- No authentication required
- Privacy-focused (no tracking)
- Full access to YouTube video metadata
- Can search by topic, educator name, or video type
- Works reliably via `fetch_webpage`

---

## Quality Standards

- Never fabricate video URLs. Use only URLs you've verified with `fetch_webpage` from Invidious search results
- **Always use Invidious links (https://inv.nadeko.net/watch?v=...) as the default** — validate URL accessibility by fetching the Invidious page before including it
- **YouTube direct links only if:** They are verified as valid/clickable through Invidious verification AND you explicitly confirm the URL exists and is accessible
- Verify video metadata: title, channel, view count, upload date before recommending via Invidious page inspection
- If a video requires YouTube Premium or has accessibility issues on Invidious, note it and use Invidious link only
- Prefer timeless content over trending content unless the topic is current events
- For technical topics, value high view counts and reputable channels (Abdul Bari, MIT OpenCourseWare, NeetCode, etc.)
- When uncertain about a video, say so rather than guessing about its content
- **Never present a video link without first checking it exists:** Use `fetch_webpage` on the inv.nadeko.net URL to confirm accessibility
- **Invidious advantage:** All searches and verification happen without login, making this completely accessible and privacy-respecting

---

## Example Trigger Phrases

- "What videos should I watch to understand quantum computing?"
- "Find me the best videos to learn Rust programming"
- "I want to deeply understand the French Revolution — what should I watch?"
- "Research blockchain for me and find the best educational videos"
- "Help me learn about stoic philosophy through video"
- "Curate the best videos for studying algorithm complexity"
