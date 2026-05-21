# My Agents, Skills & Instructions for Copilot

This is my personalized GitHub Copilot workflow — a collection of **skills**, **instructions**, and **agents** I use daily to enhance my coding experience. It's organized for personal use but open for anyone to explore, adapt, or draw inspiration from.

The repo also includes a **deployment script** that makes it easy to install and keep everything organized in a clean folder structure while maintaining Copilot's required file format for seamless integration.

---

## Skill vs Agent vs Instruction

| **Type** | **What It Is** | **Purpose** | **Example** |
|---|---|---|---|
| **Skill** | Reusable, single-purpose function | Do one specific thing well, and use it across multiple scenarios | Code formatting, email polishing, quiz generation |
| **Agent** | Multi-step orchestrator | Combine multiple skills or tasks to complete one larger goal | Research agent that gathers info, searches, and synthesizes into a report |
| **Instruction** | Global rule set | Define conventions, constraints, and behavior that apply across all skills and agents | Coding standards, tone guidelines, tool restrictions |

### When to Create Each

- **Skill**: Create a skill when you have a reusable workflow that solves one problem and could be invoked across many different projects or scenarios. Don't create a skill if it's a one-off task.
- **Agent**: Create an agent when you need to orchestrate multiple skills or complex multi-step tasks to achieve a single larger goal. Don't create an agent if a single skill would do.
- **Instruction**: Create an instruction when you have a rule, convention, or constraint that should apply globally across your entire workflow. Don't create an instruction for task-specific logic.

---

## Philosophy: Human Intention, Human Verification, Human Thought

This workflow is built on a collaborative dialogue between human thought and AI execution — think of it as a senior developer guiding a junior who also thinks critically and challenges back.

The core principle: **Human intention and human verification guide AI execution at every step, with continuous feedback loops.** This means you, as the user, maintain your technical knowledge and understanding of software engineering, architecture, and project design. You're not delegating thinking — you're augmenting it. The AI is a junior collaborator that executes your vision *and* brings critical feedback, suggestions, and identifies potential flaws or gaps in your approach.

This is a true dialogue: you clarify intent, the AI executes and offers suggestions, you verify and course-correct, the AI challenges your assumptions if needed — and critically, **before anything gets implemented, you both agree on exactly what's going to happen.** This mutual verification ensures you're speaking the same language and moving forward with intention.

This back-and-forth is evident in [Matt Pocock's "grill me"](https://github.com/mattpocock/skills) and brilliantly explained in [David Ondrej's video on the future of AI](https://www.youtube.com/watch?v=PzVV4X37ihg&pp=0gcJCQQLAYcqIYzv). The **MD builder skill** in this repo is a direct implementation of this philosophy — it's a loop of ask/write/probe/confirm that mirrors true collaboration, keeping human thought in the driver's seat while leveraging AI's ability to catch blind spots.

---

## Inspiration & Credit

This project is heavily inspired by [Matt Pocock](https://github.com/mattpocock) and his work on [skills](https://github.com/mattpocock/skills). His approach to prompt engineering and agentic engineering — especially the principle of reducing context and giving language models just enough information to execute one task effectively — guides what I want my workflow to become better at.
