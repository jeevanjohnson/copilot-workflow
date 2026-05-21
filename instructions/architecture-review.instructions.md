---
name: Architecture & Code Quality Review
description: "Principle-based guidelines for writing clean, maintainable code: clear architecture, thoughtful naming, and sustainable design. Covers coupling, layers, tech debt, scalability, and code structure across all languages."
applyTo: "**/*.{py,js,ts,jsx,tsx,cpp,c,h,hpp,java,go,rs,rb,php,cs,swift,kt,scala,clj}"
---

# Architecture & Code Quality Review

These principles guide every code decision: clear architecture, sustainable design, and long-term scalability.

## Architecture: Foundation First

**Single Responsibility**
- Each module, class, or function does one thing well
- If you need a compound sentence to describe it, split it
- Changes should be isolated to one place

**Minimize Coupling**
- Components should depend on abstractions, not implementations
- Changes in one layer shouldn't ripple through others
- Explicit dependencies beat hidden state and side effects
- Use constructor injection or clear parameter passing

**Favor Stateless Design**
- State is complexity; avoid it when possible
- Stateless designs are easier to test, reason about, and scale
- When state is necessary, make it obvious and bounded

**Layers Stay Separate**
- Data access, business logic, and presentation never bleed into each other
- Each layer has one concern and one reason to change
- Layer violations usually signal future maintenance problems

**Tech Debt Matters**
- "Works now but requires hacks later" creates 10x maintenance costs
- Before committing to a pattern, ask: Will this stay clean at 2x scale?
- Flag architectural shortcuts upfront; don't sneak them in

**Scalability Thinking**
- Design for the system you'll have, not just the one you have today
- If adding a feature touches many files, the architecture needs improvement first
- Don't solve immediate problems by creating future ones

---

## Naming: Express Intent

**Names Communicate**
- A good name eliminates the need for a comment
- It should immediately convey purpose and scope
- Spend time on names; they're read far more than written

**Clarity Over Brevity**
- `process_user_payment_records` is better than `proc_rec`
- Avoid abbreviations unless universal (`id`, `url`, `config`)
- The cost of a longer name is negligible; the cost of a cryptic one is high

**Type + Purpose**
- Names should signal what they are: `is_active`, `fetch_data`, `UserRepository`
- Consistency matters: `get_user` and `fetch_order` break the pattern
- Boolean flags: prefix with `is_`, `has_`, `should_`, `can_`

**Scope Determines Specificity**
- Module/class names: specific (`PaymentProcessor`)
- Local variables: can be shorter (`user`, `result`) if context is clear
- Global/exported names: always explicit

---

## Code Structure: Readability First

**Organization Signals Intent**
- Related logic should be together
- Imports should be organized (language patterns vary, but consistency within a project matters)
- Public methods before private; important before peripheral

**Shallow Nesting**
- Code that's deeply nested is hard to follow
- Early returns, guards, and short functions reduce nesting
- Prefer flat structures when possible

**Comments Are for Why, Not What**
- Don't comment what the code obviously does
- Do comment why non-obvious logic exists, trade-offs made, or decisions that matter
- "Rate limit uses exponential backoff because..." beats "increment counter"

**Consistency Within Context**
- If your codebase uses a pattern, stick to it
- Switching styles mid-file confuses readers
- New patterns should be intentional, not accidental

---

## Red Flags: When Architecture Breaks Down

**Touching Many Files**
- If a feature requires changes across many files, pause
- This signals tight coupling or unclear layer boundaries
- Fix the architecture before proceeding; don't work around it

**Hidden Dependencies**
- Global state, singletons, or implicit side effects
- These become nightmares as code scales
- Dependencies should be explicit and injectable

**God Objects**
- Classes or modules trying to do too much
- If you can't describe it in one sentence, split it
- One reason to change per class/module

**Circular Dependencies**
- A depends on B, B depends on A
- This signals a missing abstraction or poor layer design
- Refactor to break the cycle; don't let it solidify

---

## Code Review Questions

Before shipping code, ask:

**Architecture:**
- Does this create unnecessary coupling?
- Will this scale cleanly, or require major refactoring later?
- Are responsibilities clearly separated?
- Is state bounded and explicit?

**Naming:**
- Would a new developer understand this immediately?
- Are names consistent with the rest of the codebase?
- Do names express intent, not just what they are?

**Structure:**
- Is this easy to read and follow?
- Could this be split into smaller, focused pieces?
- Are dependencies clear or hidden?

**Tech Debt:**
- Am I solving today's problem or creating tomorrow's?
- Would I be comfortable maintaining this in 6 months?
- Is this a pragmatic trade-off or a shortcut?

---

## Execution

When writing code:
1. Think architecture first—layers, coupling, scalability
2. Name carefully—clarity is a feature
3. Structure for readability—organization communicates
4. Watch for red flags—they're your warning system
5. Consider long-term—will this still be clean in 2x scale?

The best code is the code you never have to rewrite.