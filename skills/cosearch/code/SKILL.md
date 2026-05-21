---
name: code
description: >
  Implement end-to-end code from ubiquitous + pseudocode context. Trigger with 
  `/code [scope]` (e.g., `/code user authentication`, `/code notification system`) 
  after ubiquitous and pseudocode have been established in `.cosearch/`. Claude creates 
  file structure, implements each file, and validates all code against ubiquitous 
  language and pseudocode constraints. Output: fully functional, tested code with 
  comments linking back to pseudocode logic. DO NOT trigger for debugging existing 
  code, explaining code, or refactoring — only for new implementation from scratch 
  based on ubiquitous + pseudocode spec.
---

## Purpose

This skill transforms pseudocode and domain language into production-ready code. After ubiquitous and pseudocode establish *what* to build and *how* to build it, this skill takes over to build it *actually*. Claude creates the full file structure, implements each file with code that traces back to pseudocode logic, validates every line against ubiquitous constraints, and delivers tested, documented code ready for integration. This is the final step in the ubiquitous → pseudocode → code workflow — no hallucinations, no scope creep, no gaps between specification and implementation.

---

## Core Workflow

### Phase 1: Load Context
1. User triggers `/code [feature-name]`
2. Load context files using exact naming patterns:
   - **Ubiquitous:** `.cosearch/ubiquitous_[feature-name].md` (contains glossary, constraints, success criteria, architecture notes)
   - **Pseudocode:** `.cosearch/pseudocode_[feature-name].md` (contains logic, edge cases, assumptions)
3. If either file is missing, ask: "I don't see `.cosearch/ubiquitous_[feature-name].md` or `.cosearch/pseudocode_[feature-name].md`. Should we create them first via `/ubiquitous` and `/pseudocode`, or do you have them stored differently?"
4. If user provides files or confirms they exist, extract and parse:
   - **Ubiquitous Language (Glossary):** Key terms, definitions, constraints, success criteria
   - **Context:** Project setup, tech stack, database, dependencies, existing architecture
   - **Pseudocode:** Logic, edge cases, assumptions, architecture notes
5. Summarize back: "I've loaded `.cosearch/ubiquitous_[feature-name].md` and `.cosearch/pseudocode_[feature-name].md`. Ready to implement [feature-name]. Any deferred items or late additions I should know about?"

### Phase 2: Architecture & File Structure
1. Review ubiquitous for project context:
   - If ubiquitous mentions "new project" → Design fresh file structure based on pseudocode logic
   - If ubiquitous mentions existing codebase/architecture → Use that as baseline
   - If ubiquitous mentions tech stack/database/dependencies → Account for those in file design
2. Propose file structure (either fresh or integrated with existing):
   - List each file, its purpose, and what pseudocode logic it implements
3. Ask: "Does this structure work for you, or should I adjust anything?"
4. Get confirmation before proceeding

### Phase 3: Implement File by File
1. For each file:
   - Write the code using exact terminology from ubiquitous glossary (no synonyms)
   - Add inline comments explaining logic in domain terms (not meta-references to pseudocode)
   - Keep code self-explanatory using ubiquitous terminology
2. After each file, ask: "Does this match the pseudocode logic and ubiquitous constraints? Any changes?"
3. Repeat until all files are written and confirmed

### Phase 4: Validation Pass
1. Read through all files together
2. Check each one against:
   - **Ubiquitous constraints:** Are all hard rules enforced?
   - **Pseudocode logic:** Does the code trace back to pseudocode steps?
   - **Terminology:** Are all glossary terms (from ubiquitous language) used consistently?
   - **Success criteria:** Will this satisfy all criteria from ubiquitous?
   - **Deferred items:** Are deferred items properly handled (skipped, noted, or implemented)?
3. **If issues found:**
   - Ask user: "Should I fix the code, or update the spec?"
   - Fix the code AND update both `.cosearch/ubiquitous_[feature].md` and `.cosearch/pseudocode_[feature].md` to match
   - Re-validate after changes
4. Ask: "All constraints satisfied, terminology consistent, deferred items handled. Ready to proceed to testing?"

### Phase 5: Testing & Documentation
1. Write unit tests or integration tests (based on pseudocode edge cases)
2. Add a README or module docstring that traces the feature back to ubiquitous/pseudocode
3. Run through success criteria one final time
4. Ask: "Ready to deliver?"

---

## Trigger Conditions

### ACTIVATE When:
- User triggers `/code [scope]` after ubiquitous and pseudocode are established in `.cosearch/`
- User wants to implement a new feature/system based on a spec (ubiquitous + pseudocode)
- Works for both new projects and new features being added to existing codebases
- User is ready for end-to-end implementation

### DO NOT ACTIVATE When:
- User is debugging existing code (use debugging skill instead)
- User is refactoring or optimizing existing code without a new spec
- User asks for a code snippet or example without a full spec
- User hasn't completed ubiquitous (`.cosearch/ubiquitous_[feature].md`) and pseudocode (`.cosearch/pseudocode_[feature].md`) first (ask them to complete those first)
- User asks to "explain this code" or "understand how X works"

---

## Rules & Constraints

1. **Never skip ubiquitous + pseudocode context** — If `.cosearch/ubiquitous_[feature].md` or `.cosearch/pseudocode_[feature].md` is missing, stop and help the user create it via `/ubiquitous` or `/pseudocode`. No implementation without a spec.

2. **Use ubiquitous terminology consistently** — Every variable name, function name, and domain concept must use exact terms from the ubiquitous language (glossary). No synonyms or shortcuts. If ubiquitous says "user authentication flow," not "login process."

3. **Every implementation traces back to pseudocode** — Add inline comments that explain code logic in domain terms. If you implement something that isn't in the pseudocode, ask first: "The pseudocode doesn't mention [X]. Should I add it, or skip it?"

4. **Validate against constraints before delivery** — Before finalizing, verify:
   - All ubiquitous constraints are enforced (e.g., "max 5 login attempts")
   - All pseudocode logic is implemented
   - All success criteria are met
   - Deferred items are explicitly handled (skipped, noted, or implemented)
   - If any are missing, flag them and ask before moving on

5. **If errors are found, update both code and spec** — If the skill discovers gaps between code and pseudocode/ubiquitous, fix the code AND update both `.cosearch/ubiquitous_[feature].md` and `.cosearch/pseudocode_[feature].md` to match. This keeps the spec and implementation in sync.

6. **Test or validate each file** — Write tests for logic-heavy files (validators, handlers, business logic). At minimum, verify syntax and imports are correct.

7. **One question at a time** — Ask for confirmation after each file. Don't batch files together.

8. **Never assume** — If ubiquitous or pseudocode is ambiguous, ask the user for clarification before implementing.

---

## Examples

### Example: Real-Time Notification System

**Setup:**
- User has already run `/ubiquitous real-time notification system` → saved to `.cosearch/notifications.md`
- User has run `/pseudocode` → saved to `.cosearch/pseudocode_notifications.md`
- Ubiquitous defines: event types (follows, comments, messages), Firebase Cloud Messaging, offline queue (30 days), no batching, project context (new backend, Node.js + Express, Firebase admin SDK)

**Trigger:**
```
/code real-time notification system
```

**Phase 1 — Load Context:**
Claude loads `.cosearch/notifications.md` and `.cosearch/pseudocode_notifications.md`, extracts:
- Glossary: notification, event types, offline queue, real-time, etc.
- Project context: New Node.js + Express backend, Firebase integration
- Constraints: 30-day retention, Firebase only, no batching
- Success criteria: Events trigger pushes within seconds, offline queue works, notification center displays history

Claude summarizes: "I've loaded your ubiquitous language and pseudocode. New Node.js backend with Firebase. Three event types (follows, comments, messages), offline queue with 30-day retention, no batching. Ready to implement?"

**Phase 2 — Architecture & File Structure:**
Claude auto-detects "new Node.js project" from ubiquitous and proposes:
- `models/notification.js` — Notification data structure
- `services/firebaseService.js` — Firebase integration
- `handlers/eventHandler.js` — Detects events and triggers notifications
- `utils/queueManager.js` — Offline queue logic
- `tests/notification.test.js` — Integration tests

Claude asks: "Does this structure fit your plan, or should I adjust?"

**Phase 3 — Implement File by File:**
Claude writes `models/notification.js`:
```javascript
class Notification {
  /**
   * Text message sent to user device via Firebase Cloud Messaging.
   */
  constructor(eventType, recipientId, payload) {
    this.eventType = eventType;  // "follow", "comment", or "message"
    this.recipientId = recipientId;
    this.payload = payload;
    this.createdAt = new Date();
  }
}
```

Notice: No references to pseudocode. Domain terms are self-explanatory.

Claude asks: "Does this match the pseudocode? Ready for the next file?"

*[Repeat for each file...]*

**Phase 4 — Validation Pass:**
Claude verifies:
- ✅ All constraints enforced (30-day retention in `queueManager.js`, no batching logic)
- ✅ Pseudocode logic traced (event detection → Firebase send → queue if offline)
- ✅ Terminology consistent (always "notification," "eventType," "offline queue")
- ✅ Success criteria met (real-time delivery, offline handling, notification history)

If Claude finds a gap (e.g., "The code doesn't validate event types, but ubiquitous lists three valid types"), Claude asks: "Should I add validation for event types in the event handler?"

User confirms. Claude updates code AND `.cosearch/pseudocode_notifications.md` to note the validation step.

**Phase 5 — Testing & Documentation:**
Claude writes tests for edge cases from pseudocode (offline user, 30-day retention expiry) and adds README linking back to ubiquitous/pseudocode.

Delivers: "Ready to integrate."

---

## Edge Cases

### 1. Ubiquitous/Pseudocode are incomplete or contradictory
- **What happens:** User provides ubiquitous but pseudocode is still vague, or they contradict each other
- **How to handle:** Stop and ask user: "I found a gap: [ubiquitous says X, but pseudocode suggests Y]. Should we clarify this in the spec files first, or proceed with your best judgment?"
- **Don't implement with ambiguity** — go back to the source files

### 2. Code implementation reveals a spec gap
- **What happens:** During implementation, you realize the pseudocode doesn't cover an edge case
- **How to handle:** Ask: "The pseudocode doesn't mention [X edge case]. Should I handle it, skip it, or should we update the pseudocode first?"
- **Update both files** if proceeding

### 3. User changes mind mid-implementation
- **What happens:** User asks to pivot halfway through (e.g., "actually, let's use a different architecture")
- **How to handle:** Pause implementation, ask: "Should we update the pseudocode/ubiquitous to reflect this change first, then continue? Or revert what we've done?"
- **Respect the spec** — don't implement outside the boundary

### 4. Code doesn't pass validation against constraints
- **What happens:** During Phase 4, you find the code violates a ubiquitous constraint
- **How to handle:** Flag it explicitly: "This code violates [constraint]. Should I fix it, or should we loosen the constraint?"
- **Always ask before overriding a constraint**

### 5. Existing codebase conventions conflict with pseudocode
- **What happens:** Project uses a pattern that the pseudocode doesn't call for
- **How to handle:** Ask: "Your existing code uses [pattern], but pseudocode suggests [different approach]. Which should we follow?"
- **Prefer consistency with existing codebase**, but confirm with user

### 6. User provides ubiquitous but no pseudocode
- **What happens:** User triggers `/code` with `.cosearch/ubiquitous_[feature].md` but `.cosearch/pseudocode_[feature].md` is missing
- **How to handle:** Ask: "I have ubiquitous but no pseudocode. Want me to help generate pseudocode via `/pseudocode` first, or do you want to skip that step?"
- **Recommend not skipping** — pseudocode is critical for tracing logic back to spec

### 7. User is impatient and wants to skip the spec
- **What happens:** User says "Can we just start coding?" without completing ubiquitous or pseudocode
- **How to handle:** Remind them directly: "Skipping the spec is how hallucinations creep in. Without ubiquitous language and pseudocode, I can't validate that the code matches your intent — and you'll end up reworking it later. Let's nail the spec first. Can we run `/ubiquitous` and `/pseudocode`?"
- **Don't budge on this** — the spec is non-negotiable

### 8. Ambiguous terminology or unclear requirements
- **What happens:** Ubiquitous or pseudocode uses vague language
- **How to handle:** Always ask for clarification: "When you say [term], do you mean [specific definition A] or [specific definition B]? Walk me through an example."
- **Never assume** — ask until it's clear
