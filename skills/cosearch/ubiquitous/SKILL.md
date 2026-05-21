---
name: ubiquitous
description: >
  Establish and maintain ubiquitous language through structured, multi-turn 
  dialogue. Trigger with `/ubiquitous [what you want to implement or build]` 
  (e.g., `/ubiquitous I want to add authentication`, `/ubiquitous building a 
  scoring system`). Before any coding or design, this skill surfaces and aligns 
  on domain concepts, vocabulary, constraints, and hidden assumptions around 
  that feature or system. Output is formatted as clean, organized Markdown 
  (single or multiple files) in the `.cosearch/` folder, creating a knowledge 
  base that prevents hallucinations and ensures Claude and user share identical 
  mental models. Works for new projects and existing systems alike. DO NOT 
  trigger for debugging, quick answers, or implementation queries — only for 
  foundational knowledge building and feature specification through dialogue.
---

## Purpose

This skill orchestrates a deep, multi-turn dialogue that builds a shared mental 
model between you and Claude around a specific feature, system, or project. Before 
any implementation, pseudocode, or brainstorming, this skill asks the hard 
questions — What does this term actually mean to you? What are the edge cases? 
What constraints matter? What assumptions are we both making? — and documents 
the answers in a structured knowledge base (`.cosearch/`).

The result: Claude stops hallucinating about your project's intent, vocabulary, 
and constraints. You and Claude are reading from the same sheet. That knowledge 
base then feeds into pseudocode design, coding, and all downstream work, ensuring 
consistency and preventing costly misalignments.

Who it's for: Anyone building software who wants to move fast *and* stay aligned 
with Claude on what they're actually building.

---

## The Dialogue Loop

When triggered with `/ubiquitous [what you want to build]`, follow this workflow:

### Step 1: Intake & Scope
- Parse what the user wants to implement/build
- Clarify the boundary: Is this a new feature, a redesign, a new system, or an 
  enhancement to existing code?
- Confirm: "So we're establishing shared understanding around [X]. Let's make sure 
  we're on the same page before we design or code."

### Step 2: Core Questions & Grill (Multi-Turn Dialogue)
Ask these in sequence, one at a time. Wait for real answers. If answers are vague, 
force concrete examples:

- **Ubiquitous Language:** "When you say [key term], what exactly do you mean? Walk me 
  through a concrete example."
- **User/Actor Flows:** "Who uses this? What's the happy path? What are the edge 
  cases?"
- **Constraints & Rules:** "What are the hard constraints? What *can't* happen?"
- **Integration:** "How does this fit into your existing system? What else does it 
  touch?"
- **Success Criteria (Measurable):** "How do you know this is done and correct? What are the specific metrics or outcomes?"

For each answer: "Is that [restate] correct? Anything I'm missing?"

If you sense there are important questions left unasked, ask them explicitly. If 
a question feels important but the user wants to defer it, ask: "Should we nail 
this now, or can we circle back to it later?" Only defer if they explicitly say 
so — document the deferral in the `.cosearch/` file.

If you disagree with an answer or something feels off, ask clarifying questions 
until you both align. Disagreement = opportunity to drill deeper, not skip over.

### Step 3: Extract & Document
From the dialogue, build:
- **Ubiquitous Language (Glossary):** Key domain terms with definitions, examples, and constraints
- **Mental Model:** A narrative or structured breakdown of what this thing is, 
  who uses it, main flows, and what matters most
- **Success Criteria (from dialogue):** Hard success criteria from the conversation
- **Assumptions:** Explicitly state what you're assuming about their domain, 
  constraints, and success criteria

Then ask: "Did I capture your mental model correctly? Where am I off?"

### Step 4: Success Criteria Validation Checkpoint
Before alignment check, confirm that success criteria are concrete and testable:
- "How do we know this is done? What does success look like?"
- Push for measurable outcomes, not vague language
- If answers are fuzzy ("it should be fast"), drill for specifics ("what's the latency target? 100ms? 1s?")
- Document these as hard success criteria that pseudocode and code will validate against

### Step 5: Alignment Check
Ask directly: "On a scale of 1-10, how aligned are we now on what this thing 
actually is and how it should work?"

If below 9/10, identify the gap and loop back to Step 2 to re-grill that specific 
area. Keep drilling until you both reach 9/10 or higher. Once aligned at 9+, 
move to Step 6.

### Step 6: Save to `.cosearch/`
Format as clean Markdown and save to `.cosearch/` with naming pattern: **`.cosearch/ubiquitous_[feature-name].md`** containing:
- **Ubiquitous Language (Glossary)** — all key domain terms with definitions and constraints
- **Mental Model** — narrative + structured breakdown
- **Constraints & Rules** — hard constraints that cannot be violated
- **Success Criteria** — measurable, testable outcomes
- **Architecture Notes** — how it fits into the broader system, integration points
- **Deferred Items** — if any, with explicit user agreement and reason

**Critical:** File naming must follow `ubiquitous_[feature-name].md` so downstream skills (pseudocode, code) can locate it.

Summarize: "Here's our shared understanding, saved to `.cosearch/ubiquitous_[feature-name].md`. From here:
- **Next step:** Trigger `/pseudocode` and attach this file to develop implementation logic.
- **Or:** Use `/handoff` to hand off to another skill or agent.
- **Or:** Branch into architecture brainstorming or implementation — all grounded in this knowledge base.

No hallucinations, no assumptions. We're reading from the same page."

---

## Rules & Constraints

- **One question at a time:** Never stack multiple questions. Wait for a real 
  answer before moving to the next.
- **No guessing:** If the user's answer is vague or unclear, ask for a concrete 
  example. Do not infer or assume.
- **Restate before moving on:** After each answer, restate what they said back to 
  them to confirm you heard it right.
- **Disagreement is a feature, not a bug:** If you sense misalignment (their 
  answer contradicts earlier statements, or something doesn't add up), call it 
  out immediately and drill deeper.
- **Establish fundamentals before architecture:** Ubiquitous language, flows, 
  constraints, and success criteria come first (Steps 1-3). Architecture discussion 
  is valid in Step 3/4 once fundamentals are solid, but don't let it overshadow 
  core understanding. If the user is unclear on a fundamental, circle back before 
  diving into how to structure it. Architecture Notes are part of final output but 
  should never override domain clarity.
- **9/10 is the minimum:** Don't save until alignment is 9+. Not 8. Not 7.5. 
  Close enough is not good enough.
- **The `.cosearch/ubiquitous_[feature].md` file is the source of truth:** Every term, constraint, and 
  flow you document must be directly traceable to what the user said. No 
  interpolation, no "reasonable assumptions." File naming must match this pattern so downstream skills can locate it.

---

## Example: Implementing a Real-Time Notification System

**Trigger:**
```
/ubiquitous I want to build a real-time notification system
```

**Step 1: Intake & Scope**

Claude: "So we're establishing shared understanding around a real-time notification 
system. Is this a brand new feature, or replacing something existing? And what do 
you mean by 'real-time' — milliseconds, seconds, just not email?"

You: "It's new. We have a web app and mobile app. By real-time I mean push 
notifications that hit the user's device within a few seconds of an event 
happening."

Claude: "Got it. New feature for web + mobile, push notifications within a few 
seconds. Let's make sure we're aligned before we design or code."

**Step 2: Core Questions & Grill**

Claude: "Let's start with the basics. When you say 'notification,' what do you 
mean? Is it a message? A badge count? A sound? All three?"

You: "A message. We want to send them text notifications to their device."

Claude: "Is that right — just text, no images or actions? And when you say 'push 
notification,' do you mean native OS push (Apple Push Notification Service, 
Firebase Cloud Messaging)?"

You: "Yeah, native push. We're using Firebase."

Claude: "Clear. So you're using Firebase Cloud Messaging to send text notifications. 
What kinds of events trigger a notification? Who sends them?"

You: "Like, when someone follows you, or when you get a comment, or a message. 
Different events. And the system sends them automatically."

Claude: "Is that right — three types of events: follows, comments, messages? And 
'automatically' means the backend detects the event and instantly sends a push?"

You: "Yes, exactly. Instant."

Claude: "Got it. One more thing — if someone gets 100 comments in a row, do they 
get 100 push notifications? Or is there any deduplication or batching?"

You: "No batching. 100 comments = 100 pushes. But we might add batching later."

Claude: "Understood — no batching for now. What if the user is offline? Do we 
queue notifications and send them later?"

You: "Yeah, queue them. Send when they come back online."

Claude: "How long do we keep them in the queue?"

You: "30 days. After that delete them."

Claude: "Got it. And do users see a history of notifications, or just the 
real-time ones?"

You: "They see a history. Like a notification center in the app."

Claude: "Should the notification center show both sent notifications AND queued 
(missed) ones?"

You: "Yes, both."

Claude: "Alright. One more thing — any do-not-disturb rules? Like, no 
notifications between 11pm and 8am? Or notifications during work hours only?"

You: "Not initially. We'll add that later if needed."

Claude: "Got it — deferring DND for now. Should I document that as a known future 
enhancement?"

You: "Yeah, good idea."

**Step 3: Extract & Document**

Claude: "Okay, here's what we've established:

**Glossary:**
- **Notification:** A text message sent to a user's device via Firebase Cloud Messaging
- **Real-time:** Event triggers immediately send a notification (within seconds)
- **Offline Queue:** Notifications held for offline users, sent when they reconnect
- **Notification Center:** In-app history of all notifications (sent and missed)
- **Event Types:** Follows, comments, messages

**Mental Model:**
You want a system that detects three types of events (follows, comments, messages) 
and immediately sends a text push notification to the user's device via Firebase. 
No batching — every event gets a push. If the user is offline, notifications are 
queued and delivered when they reconnect. Queued notifications are retained for 
30 days, then deleted. Users see a notification center that shows both sent and 
missed notifications.

**Constraints:**
- Native push only (Firebase Cloud Messaging)
- Three event types: follows, comments, messages
- Immediate send (no batching, every event = one push)
- 30-day queue retention
- Offline queue required
- Notification center shows sent + missed notifications

**Deferred for Later:**
- Do-not-disturb scheduling (11pm-8am, or work hours)
- Batching logic (if needed)

**Success Criteria:**
- Events trigger push notifications within seconds
- Offline users receive queued notifications when online
- Notification center displays all sent and queued notifications
- Notifications older than 30 days are deleted
- System works on web and mobile apps

Does that capture your mental model correctly?"

You: "Yeah, that's exactly it."

**Step 4: Alignment Check**

Claude: "On a scale of 1-10, how aligned are we now on what this notification 
system actually is and how it should work?"

You: "9.5. Perfect."

Claude: "Excellent. We're locked in at 9.5."

**Step 5: Save to `.cosearch/`**

Claude saves to `.cosearch/notifications.md` with the full glossary, mental model, 
constraints, deferred items, and success criteria.

Claude: "Here's our shared understanding. From here, you can branch into pseudocode 
design, brainstorming architecture, or jump straight to implementation — all 
grounded in this knowledge base. No hallucinations, no assumptions. We're reading 
from the same page."
**Next Step:** To develop the implementation logic, trigger `/pseudocode` and attach this `.cosearch/` file as context. The pseudocode skill will use your glossary, constraints, and success criteria to validate the logic.
---

## Edge Cases & How to Handle Them

**1. User gives vague answers**
- Example: "I dunno, auth is just important to me."
- How to handle: Push for concrete examples. "Walk me through a specific 
  scenario where auth matters. What would go wrong if we got it wrong?"
- Don't move on until you have specifics.

**2. User contradicts themselves**
- Example: "We don't need rate limiting... wait, actually we probably do."
- How to handle: Call it out immediately. "I noticed you said [X] but now you're 
  saying [Y]. Which is it? Or are both true in different contexts?" Drill until 
  you understand the actual requirement.

**3. User says they don't know**
- Example: "I'm not sure how often users will retry. Maybe a lot?"
- How to handle: Offer educated guesses to anchor the conversation. "Do you think 
  it's more like 2-3 retries, or dozens? What's your intuition?" Then lock in 
  their choice.

**4. Scope creep during dialogue**
- Example: User starts with "I want auth" and suddenly they're talking about 
  payment integration.
- How to handle: Acknowledge it and scope it out. "Payment is important, but 
  let's nail auth first, then we can establish ubiquitous language around 
  payments. Sound good?"

**5. User gets impatient**
- Example: "Can we just start coding? I have a sense of what I need."
- How to handle: Remind them directly. "I get the urge to move fast, but 
  skipping this step is how hallucinations creep in. We need this clarity to get 
  the best results — and it saves massive rework later. Can we push to 9/10 
  alignment before we code?" Don't compromise on this.

**6. Technical vs. domain confusion**
- Example: User says "We need caching" but doesn't understand that auth tokens 
  are a form of caching strategy.
- How to handle: Ask domain questions, not tech questions. "What problem are you 
  trying to solve with caching? Why do you need it?" Then map it back to domain 
  terms (auth, performance, cost, etc.).

**7. Missing critical context**
- Example: You're establishing auth, but don't know if it's single-tenant or 
  multi-tenant, or if there's existing user data to migrate.
- How to handle: Stop and ask. "This feels incomplete — I need to understand 
  [X] before we move forward." Don't proceed with a partial document. Drill until 
  you have the full picture or explicitly scope out the unknowns with the user's 
  agreement.
