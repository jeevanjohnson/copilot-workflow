---
name: context
description: >
  Create a condensed session summary that captures all essential conversation points so future sessions can pick up seamlessly. Trigger with `/context`. This skill automatically distills the current conversation to its most critical information—goals, decisions, code changes, findings, next steps—then asks if any important details should be added before finalizing the context file. Do NOT trigger for general summarization tasks or one-off conversation reviews; this is specifically for preserving continuity between sessions. Do NOT trigger if the conversation is just starting or is trivial.
---

## Purpose

This skill captures the essential context from your current conversation session and condenses it 
into a focused markdown summary that you can read in future sessions to quickly understand what 
happened and what comes next. Instead of scrolling through full conversation logs, you get a tight 
summary of goals, decisions, code changes, blockers, and next steps — everything your future self 
needs to know to seamlessly continue working without re-reading everything. The summary is saved 
as a markdown file in your current working directory, keeping your context tokens lean while 
preserving continuity between sessions.

## Core Workflow

**Important**: You can trigger `/context` at any point in your session — whether you're just starting, 
mid-task, or wrapping up. The skill will capture the current state of work and conversations at that 
moment. There's no requirement for the session to be "finished" or "polished."

### Step 1: Analyze the Current Conversation
Scan through the entire conversation history from start to finish. Identify and extract:
- **Primary Goal(s)**: What was the user trying to accomplish?
- **Key Decisions Made**: What choices or directions did the user decide on?
- **Code Changes or Outputs**: What files were created, edited, or generated? What was the outcome?
- **Blockers or Issues**: What problems were encountered? How were they resolved?
- **Next Steps**: What work remains? What should happen in the next session?

### Step 2: Condense to Essential Points Only
Create a markdown summary that captures ONLY the must-know information. Omit:
- Long explanations or tangents
- Repeated information
- Implementation details that don't affect continuity
- Back-and-forth clarifications that led to a decision

Keep sentences short and scannable. Use bullet points and headers to organize.

### Step 3: Ask for Missing Context and Confirm
Present the condensed summary to the user and ask:
> "I've condensed the conversation. Is there any important information that should be added to this 
> context file that would help you pick up in the next session?"

Wait for their response. If they provide additions:
1. Integrate the new information into the summary
2. Display the revised summary to the user
3. Ask: "Does this look good now, or any other changes?"
4. Once confirmed, proceed to Step 4 (Save the File)

If they say no additions are needed, proceed directly to Step 4.

### Step 4: Save the File
Save the final markdown file to the current working directory with a timestamped filename in the 
format: `session-context-YYYY-MM-DD-HH-MM-SS.md` (e.g., `session-context-2026-05-20-14-35-22.md`). 
Include a header with the timestamp and a brief session summary.

### Step 5: Confirm Location
Tell the user explicitly where the file was saved:
> "Context saved to `./session-context-2026-05-20-14-35-22.md`"

## Rules & Constraints

1. **Preserve Accuracy — Stick Only to Facts from the Conversation**: Never invent or hallucinate 
   information. This means:
   - Do NOT claim a file was created if it wasn't explicitly mentioned
   - Do NOT infer a decision was made if the user didn't state it
   - Do NOT add details about code changes that didn't occur in the conversation
   - Do NOT fabricate next steps the user didn't explicitly say
   - Extract ONLY what was actually discussed, decided, or done. When in doubt, leave it out.

2. **Condense, Don't Oversimplify**: Remove fluff and repetition, but keep technical details that 
   matter for continuity (file paths, decisions made, specific errors encountered).

3. **Scan the Full Conversation**: Always read through the entire conversation history, not just 
   recent messages. Context from early in the session matters.

4. **Ask Before Saving**: Before saving the final file, ask the user if any important information 
   is missing. Do not assume you've captured everything.

5. **Timestamp Every File**: Always include the current timestamp in the filename. Never overwrite 
   an existing session context file.

6. **Explicit File Path in Output**: After saving, always tell the user exactly where the file was 
   saved. This is non-negotiable.

7. **Markdown Format Only**: The summary must be saved as a `.md` file. Use markdown formatting 
   (headers, bullet points, code blocks) to make it scannable.

## Examples

### Example 1: Building a Skill

**Trigger**: User runs `/context` after spending a session building a new skill

**What Claude does**:
- Scans the full conversation for the workflow loop (ask questions → write → probe → confirm)
- Captures the skill name, trigger phrase, and core sections completed
- Notes any decisions made during the build (e.g., "decided on section order", "changed description wording")
- Identifies what's left to do (dry run, finalizing)

**Output Summary**:
```
# Session Context: 2026-05-20-14-35-22

## Goal
Building a new SKILL.md for session context summarization (triggered by `/context`)

## Completed
- Frontmatter with description finalized
- Purpose section written and confirmed
- Core workflow (5 steps) written and confirmed
- Rules & constraints solidified

## Decisions Made
- Filename format: `session-context-YYYY-MM-DD-HH-MM-SS.md`
- Summary saves to current working directory by default
- Always ask user for missing context before finalizing

## Next Steps
- Write Examples section
- Write Edge Cases section
- Run dry run to validate skill behavior
- Assemble final SKILL.md

## Key Files/References
- Skill definition file location: `/skills/learning/session-context-builder/SKILL.md`
```

### Example 2: Debugging Code

**Trigger**: User runs `/context` after a session troubleshooting a Python import error

**What Claude does**:
- Captures the error message, root cause found, and files modified
- Notes the solution implemented
- Records what didn't work (failed attempts)
- Identifies if the issue is fully resolved or if there are remaining tests to run

**Output Summary**:
```
# Session Context: 2026-05-20-15-22-10

## Goal
Fix circular import error in `src/models.py`

## Problem Found
Circular dependency: `models.py` imports from `services.py`, 
which imports from `models.py`

## Solution Implemented
Refactored `services.py` to import inside function instead of at module level.
Modified: `src/services.py` (line 45-52)

## Testing Status
- Unit tests passed: `tests/test_models.py` ✓
- Integration tests not yet run

## Next Steps
- Run full integration test suite
- Verify no other circular imports exist
- Merge changes to main branch
```

### Example 3: In-Progress Development Work

**Trigger**: User runs `/context` in the middle of implementing a feature (not finished yet)

**What Claude does**:
- Captures the current goal and what's been accomplished so far
- Notes what's *currently being worked on* (the active task)
- Records any blockers or challenges encountered
- Identifies what still needs to be done before the feature is complete

**Output Summary**:
```
# Session Context: 2026-05-20-16-45-30

## Goal
Implement user authentication system with JWT tokens

## Completed
- Database schema for `users` table created
- Hashing function implemented and tested
- Login endpoint scaffolded

## Currently Working On
- Implementing JWT token generation and validation
- Testing token refresh logic
- Stuck on: Token expiration isn't being validated correctly on subsequent requests

## Blocker
JWT validation middleware not catching expired tokens. Need to debug 
why `verifyToken()` is not rejecting tokens past their expiration timestamp.

## Files Modified
- `src/models/User.ts` — added password hashing
- `src/routes/auth.ts` — login endpoint scaffolded
- `src/middleware/auth.ts` — token validation middleware (incomplete)

## Next Steps
- Debug token expiration validation in middleware
- Add unit tests for expired token scenarios
- Implement logout endpoint
- Test full auth flow end-to-end
```

## Edge Cases

### Edge Case 1: Very Short or Trivial Conversation
**Scenario**: User triggers `/context` after only 2-3 brief exchanges with no substantial work done.

**How to Handle**: Still create the summary. Even if there's minimal content, capture what was 
discussed. The summary might just be "Discussed idea for feature X" with next steps being "Need to 
start implementation."

### Edge Case 2: User Provides Conflicting Information
**Scenario**: Earlier in the conversation, user says "we're building X," but later says "actually, 
let's pivot to Y."

**How to Handle**: Capture BOTH the original goal AND the pivot decision. Make it clear what changed 
and why. This preserves the decision-making history.

### Edge Case 3: Technical Details Are Incomplete or Unclear
**Scenario**: User mentions modifying a file but doesn't specify the exact file path or line numbers.

**How to Handle**: Capture what WAS stated clearly. Use quotes from the conversation if needed 
(e.g., "User mentioned 'updating the auth middleware' but exact file path not specified"). Don't 
hallucinate the details.

### Edge Case 4: User Asks to Exclude Certain Information
**Scenario**: During the "ask for missing context" step, user says "Don't include X in the summary, 
it's sensitive" or "That's not important."

**How to Handle**: Respect the request immediately. Remove or omit that information from the final 
summary. This is about *their* continuity, so *their* call on what matters.

### Edge Case 5: Very Long Conversation with Many Tangents
**Scenario**: 50+ message conversation with multiple topics, dead ends, and rabbit holes.

**How to Handle**: Ruthlessly condense. Focus on: (1) What was actually completed? (2) What decisions 
were made? (3) What are the next steps? Omit the exploratory tangents that didn't lead anywhere.

### Edge Case 6: Conversation Includes File Content or Code Blocks
**Scenario**: User pasted large code snippets, error logs, or multi-page documentation.

**How to Handle**: Don't copy the entire blocks into the summary. Instead, summarize them 
(e.g., "Fixed circular import in models.py by refactoring service imports") or reference the lines 
(e.g., "Modified auth.ts lines 45-52 to add token validation").

### Edge Case 7: User Wants to Skip the "Ask for Missing Context" Step
**Scenario**: User triggers `/context` and adds a note like "Just save it, don't ask" or 
"Skip asking for additions."

**How to Handle**: Respect the request. Condense the conversation, then go straight to Step 4 (Save the File). 
Skip Step 3 (Ask for Missing Context) entirely. The user knows what they want — trust them.
