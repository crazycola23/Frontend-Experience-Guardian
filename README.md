# Frontend Experience Guardian

A product-quality guardrail for AI coding agents working on real frontend applications.

Most frontend prompts teach agents how to make a page look modern. Frontend Experience Guardian focuses on a different failure mode: an agent can keep implementing features successfully while gradually turning a real product into an unstable, over-explained, over-carded, demo-like interface.

This Skill adds a product-quality review layer around frontend implementation.

## What it protects

- interface restraint — visible elements must earn their place;
- layout stability — loading, routing, resizing, sidebar and theme changes should preserve geometry;
- scrolling quality — every independent scroll region requires a reason;
- task efficiency — optimize real workflow cost, not screenshot aesthetics;
- responsive behavior — reflow naturally instead of bouncing through JS-driven layout states;
- readability and accessibility — protect focus, contrast, semantics, zoom and user preferences;
- product consistency — fix shared systems before accumulating local patches;
- finalization quality — ship the accepted result, not the history of rejected experiments.

## The ten core rules

1. Inspect the real interface when tooling permits.
2. Protect real product behavior.
3. Every visible element must earn its place.
4. Preserve interface geometry across state changes.
5. Every independent scrollbar needs justification.
6. Optimize real user task cost.
7. Fix systems before symptoms.
8. Design responsive behavior as reflow, not rerender.
9. Preserve accessibility and readability.
10. Deliver only the verified accepted state.

## Instruction architecture

The Skill intentionally distinguishes:

- **MUST** — hard constraints;
- **SHOULD** — defaults that can be overridden for a concrete product/technical reason;
- **CONSIDER** — optional techniques such as Quick View, Inline Edit, Undo, Auto Save, Command Palette, virtualization, and optimistic updates.

This prevents useful heuristics from being mistaken for universal laws.

## Agent workflow

For substantial frontend changes the Skill uses:

`Understand → Inspect → Diagnose → Implement → Verify → Regression Check → Finalize`

It also classifies findings by severity (P0–P3) and confidence (High/Medium/Low), reducing the risk that a design guardian becomes an agent that redesigns unrelated product areas without enough evidence.

## Repository structure

```text
SKILL.md
references/
  interface-restraint.md
  layout-stability.md
  product-ux.md
  responsive-platform.md
  accessibility-i18n.md
  finalization.md
evals/
  README.md
  ai-demo-bloat.md
  unnecessary-scroll.md
  loading-layout-shift.md
  responsive-instability.md
  workflow-friction.md
CHANGELOG.md
LICENSE
```

There is still only **one Skill**. Files under `references/` are detailed knowledge loaded only when relevant.

## Using it

Use `SKILL.md` as the primary agent instruction according to the Skill/custom-instruction mechanism supported by your coding environment. Keep the repository structure intact so the agent can load referenced files when the task calls for them.

The Skill is framework-agnostic, with a small set of Vue-specific audit targets because common Vue patterns (`v-if`, presentation-driven `:key`, Teleport, watchers, responsive reactive state) can create geometry and theme issues. The principles apply equally to React, Svelte, Solid, server-rendered applications, and other web UI stacks.

## What it is not

It is not:

- a component library;
- a CSS framework;
- a visual theme;
- an instruction to remove all scrolling;
- an instruction to minimize every interface;
- permission to rewrite product business rules.

Its purpose is to stop product-quality regressions during AI-assisted frontend development.

## Evaluation

`evals/` contains benchmark-style scenarios intended to compare an agent with and without the Skill. The benchmark focuses on common agent regressions rather than subjective visual taste.

Suggested evaluation dimensions:

- business correctness;
- unnecessary visible surfaces/copy;
- scroll architecture;
- layout stability;
- responsive behavior;
- task efficiency;
- accessibility regressions;
- scope discipline;
- finalization residue.

## License

MIT. See `LICENSE`.
