---
name: pseudocode
description: >
  Iteratively develop pseudocode through a grilling loop. Trigger with `/pseudocode` 
  followed by attached context (problem description, requirements, code snippets, etc.). 
  Claude asks clarifying questions and challenges assumptions back-and-forth until the 
  pseudocode is solid and unambiguous. Once approved, saves the final pseudocode to a 
  markdown file in the `.cosearch/` folder for future reference and handoff to other skills.
  DO NOT trigger for general code questions, debugging existing code, or explaining 
  existing pseudocode — this is specifically for *building* new pseudocode collaboratively.
---

## Purpose

This skill enables you to collaboratively build pseudocode while establishing a shared language 
with Claude. Rather than writing pseudocode in isolation, you iterate back-and-forth to stress-test 
logic, identify gaps, and refine the algorithm until it's solid and unambiguous. The final pseudocode 
becomes part of `.cosearch/` — your project's central knowledge base. This directory isn't just 
storage; it's the single source of truth for ubiquitous language, domain concepts, design decisions, 
and context that you and Claude reference throughout the project. By building this knowledge base 
together, you ensure shared understanding, faster handoffs to other agents for actual implementation, 
and a consistent vocabulary that keeps the entire project aligned. Each pseudocode document becomes 
a reference point for future work, reducing miscommunication and rework.

---

## Core Workflow

### Phase 1: Parse & Clarify
1. **Check for ubiquitous context first:** If the user is coming from `/ubiquitous`, they should attach the `.cosearch/ubiquitous_[feature].md` file. Extract and reference it:
   - Use the ubiquitous language (glossary) to ensure terminology alignment
   - Note the constraints and success criteria
   - Ask about deferred items: "I see ubiquitous deferred [X]. Should we scope the pseudocode around that?"
   - If ubiquitous file is missing, ask: "I don't see `.cosearch/ubiquitous_[feature].md`. Do you have it, or should we create it via `/ubiquitous` first?"
2. Read the attached context (problem description, requirements, code, constraints, etc.)
3. Identify what's clear and what's ambiguous
4. Ask **one clarifying question at a time** to nail down:
   - The primary goal / what problem this pseudocode solves
   - Key inputs and expected outputs
   - Logic-specific edge cases (domain edge cases were covered in ubiquitous)
   - Any dependencies or assumptions
5. **Do not move to Phase 2 until you have a solid understanding** — if answers are vague, grill deeper
6. **Confirm Phase 1**: Once clarification is complete, summarize what you understand and ask "Should we move to drafting the pseudocode?"

### Phase 2: Draft & Challenge
1. **Acknowledge architecture constraints:** If ubiquitous defined architecture decisions (e.g., "event-driven via Firebase"), state them upfront: "I'm designing this pseudocode within these architecture constraints from ubiquitous: [list]. All domain terms and success criteria come from `.cosearch/ubiquitous_[feature].md`."
2. Write a first draft of the pseudocode based on your understanding
3. Show it to the user
4. Ask **at least one pointed question** about what you just wrote. Challenge assumptions:
   - "Is this order of operations correct, or should X come before Y?"
   - "What happens if [edge case]? Should the pseudocode handle it?"
   - "Is there a simpler way to express this logic?"
5. Wait for feedback
6. **Confirm Phase 2**: Once user approves the draft, ask "Ready to refine, or should we rethink anything?"

### Phase 3: Refine Loop
1. User provides feedback (revisions, clarifications, new questions)
2. Update the pseudocode
3. Show the updated version
4. **Validate against success criteria:** If ubiquitous defined success criteria, ask: "Does this pseudocode satisfy all the success criteria from ubiquitous? [list them]" If not, identify the gap and refine.
5. Ask a new probing question about the changes
6. Repeat until user confirms "This is solid" or "Ready to save"
7. **Confirm Phase 3**: Ask "Are we happy with this pseudocode, or should we iterate more?"

### Phase 4: Save & Handoff Ready
1. Once user confirms the pseudocode is solid, assemble the final version
2. Save to `.cosearch/pseudocode_[feature-name].md` with:
   - Problem statement (from context)
   - Reference to ubiquitous source (e.g., "Based on `.cosearch/ubiquitous_[feature].md`")
   - Final pseudocode
   - Key assumptions/decisions made
   - Architecture notes (if divergent from ubiquitous)
3. Confirm save: "Saved to `.cosearch/pseudocode_[feature-name].md`"

**Next Steps:**
- **To implement:** Trigger `/code [feature-name]` to generate the actual code using this pseudocode as the blueprint
- **Or:** Use `/handoff` to hand off to another skill or agent
- **Note:** The code skill will load both `.cosearch/ubiquitous_[feature].md` and `.cosearch/pseudocode_[feature-name].md` to ensure full spec adherence

---

## Rules & Constraints

1. **One question at a time** — Never stack multiple questions. Ask, wait for answer, then ask next.

2. **Always give your recommendation** — Don't just probe; tell the user what you'd do or change.

3. **Ask, don't assume** — Unknown details get asked about, never invented or assumed.
4. **Use ubiquitous language consistently** — Every term in pseudocode must come from the ubiquitous glossary. No synonyms, no shortcuts.
4. **Grill on logic and edge cases** — Every phase should include at least one challenge:
   - Is the order correct?
   - What about [edge case]?
   - Is there a simpler way?
   - Does this handle [constraint from ubiquitous]?

5. **Stay in scope** — Only build pseudocode. Don't write actual code, explain existing code, 
   or debug implementations.

6. **Explicit phases** — Always confirm before moving between phases. Never skip.

7. **Save with context** — When saving to `.cosearch/pseudocode_[feature].md`, always include the problem statement, 
   reference to ubiquitous source, and key assumptions alongside the pseudocode. Don't save bare pseudocode.

8. **File naming matters** — Use `.cosearch/pseudocode_[feature-name].md` so the code skill can find it.

9. **Offer next step** — After saving, always mention `/code [feature-name]` for implementation.

---

## Examples

### Example 1: User Authentication Flow

**Trigger:**
```
/pseudocode
Context: I need to build a user login flow. Requirements: validate email, check password against bcrypt hash, 
handle failed attempts (max 5), lock account for 15 min after 5 failed attempts, return JWT token on success.
```

**Phase 1 (Clarify):**
Claude asks: "When the account is locked, should the user be notified via email, or just get an error message?"
User: "Email notification."
Claude: "Got it. And if a user tries to login while locked, do they still get an email? Or only when they hit the 5th failure?"
User: "Only when locked — once is enough."
Claude: "Clear. Ready to draft?"

**Phase 2 (Draft):**
Claude writes pseudocode and asks: "Should we validate the email format before even checking it exists in the database? It's more efficient upfront."

**Phase 3 (Refine):**
User: "Yes, validate format first."
Claude updates pseudocode, then asks: "Should we log the failed attempt *before* or *after* checking the lock status?"
User: "Before, so we have a full audit trail."
Claude updates and confirms.

**Phase 4 (Save):**
Claude saves to `.cosearch/pseudocode_user_auth.md` with problem statement, final pseudocode, and assumptions.
Offers: "Want to handoff this to another skill via `/handoff`?"

---

### Example 2: Search Algorithm with Mid-Stream Pivot

**Trigger:**
```
/pseudocode
Context: I need pseudocode for a search algorithm that finds users by name. It should return results sorted by relevance.
```

**Phase 1 (Clarify):**
Claude: "What defines 'relevance' — exact matches first, then partial matches? Or something else?"
User: "Exact matches, then partial, then fuzzy matches."
Claude: "Got it. Should the search be case-insensitive?"
User: "Yes."
Claude: "And should we limit results to, say, top 10, or return everything?"
User: "Top 10 is fine."
Claude: "Ready to draft?"

**Phase 2 (Draft):**
Claude writes pseudocode with three-tier matching logic. Asks: "Should we build the relevance score as we go, or rank after collecting all matches?"

User realizes mid-answer: "Actually, wait — we're getting thousands of results. Building relevance score as we go might be slower. How about we just return exact matches first, up to 10, then partial if we don't have 10 yet?"

**Phase 3 (Refine — Pivot):**
Claude: "Ah, so early-exit once we hit 10 results?"
User: "Yeah, exactly."
Claude updates pseudocode completely — removes ranking logic, adds early-exit. Then asks: "If we early-exit on exact matches, should we even bother with fuzzy matching, or just stop at partial?"
User: "Stop at partial. Fuzzy is overkill."
Claude updates again, confirms the revised approach.

**Phase 4 (Save):**
Claude saves to `.cosearch/pseudocode_user_search.md` with the pivot noted in assumptions:
"Initial design used three-tier ranking. Revised to early-exit on result count (top 10) for performance — scope reduced to exact + partial match only."

---

## Edge Cases

1. **Vague or incomplete context**
   - If the user's initial context is too vague (e.g., "I need an algorithm"), ask clarifying questions 
     in Phase 1 until you understand the actual problem.
   - Do not proceed to Phase 2 (drafting) with fuzzy requirements.

2. **User changes mind mid-stream**
   - Accept the pivot, acknowledge it, update pseudocode, and ask a new probing question.
   - This is normal and expected — the grilling process surfaces better ideas.
   - Note the pivot in final assumptions when saving.

3. **User is satisfied faster than expected**
   - If user says "that's perfect" early, confirm Phase 2 or Phase 3 and move to save.
   - Don't force iteration if the pseudocode is genuinely solid.

4. **User asks for actual code**
   - Politely redirect: "This skill builds pseudocode, not actual code. Once we have solid pseudocode, 
     you can implement it directly or handoff to another skill."
   - Stay in scope.

5. **User challenges your probe**
   - If user says "that's not a real concern," accept it and move on.
   - You're grilling to find flaws, not to be right. If the user is confident, respect that.

6. **Pseudocode becomes complex mid-way**
   - If you realize the logic needs diagrams or flowcharts to clarify, mention it: 
     "This is getting complex. Should we break it into smaller components?"
   - Stay focused on pseudocode, but surface complexity issues.

7. **User wants to save but isn't ready**
   - If pseudocode still has gaps or ambiguities, gently push back: 
     "I noticed we skipped the error handling case. Should we refine that before saving?"
   - Better to catch it now than save half-baked pseudocode.

8. **File already exists in `.cosearch/`**
   - Always check if a file with that name exists. If it does, ask: 
     "This file already exists in `.cosearch/`. Should we create a new version with a 
     different name (e.g., `pseudocode_user_search_v2.md`), or would you rather replace the content?"
   - Never silently overwrite — the `.cosearch/` directory is your project's knowledge base.
