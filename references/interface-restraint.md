# Interface Restraint

Use this reference when a page feels busy, demo-like, over-explained, over-carded, or artificially scrollable.

## Core test

For every visible element ask:

> What unique user job does this perform?

Useful jobs include understanding state, making a decision, completing a task, preventing an error, recovering from a problem, or communicating necessary business information.

If removing an element leaves the workflow equally understandable, removal is usually preferable.

## Content gate

Reject visible content whose primary purpose is to explain the implementation rather than help the user.

Do not expose normal users to:

- debug state;
- internal enum/token/component names;
- framework or API implementation details;
- temporary migration or fallback labels;
- test controls;
- AI reasoning or implementation commentary.

Do not invent production data to avoid an empty state.

## Avoid AI-demo bloat

Common symptoms:

- welcome hero on an operational screen;
- several KPI cards with no decision value;
- decorative gradients and icons with no functional role;
- Card inside Card inside Card;
- title + section title + card title repeating the same concept;
- explanatory paragraphs compensating for unclear interaction;
- status badges on information that is already obvious;
- many identical primary-looking buttons.

Prefer fixing hierarchy, grouping, naming, spacing, or workflow first.

## Surface budget

Cards, panels, borders, badges, dividers, icons, shadows, buttons, and colored surfaces all consume attention.

Before adding a surface, ask whether whitespace, typography, alignment, grid, or a divider would communicate the relationship more clearly with less visual noise.

Cards should represent meaningful grouping or interaction surfaces, not become the default wrapper for every section.

## Operational space

SaaS/admin/workspace screens are not marketing landing pages. Avoid pushing the primary task below the fold with oversized headings, decorative hero regions, huge gaps, repeated descriptions, or oversized cards.

Use available horizontal space intentionally on desktop while preserving readable line lengths and clear grouping.

## Scroll review

Treat new independent scroll regions as architecture decisions.

Before `overflow-y: auto`, `max-height`, or fixed heights:

1. remove unnecessary fixed geometry;
2. let natural layout grow;
3. reduce redundant chrome;
4. improve grouping;
5. allow controls to wrap;
6. use horizontal space better;
7. prefer page scrolling if the region does not need independent navigation.

Legitimate bounded scrolling includes virtualized data, editors, logs, chats, large dropdowns/command menus, or independent workspaces.

Do not remove useful readability merely to fit everything in one viewport.

## Dashboard restraint

For each metric or chart ask:

- What decision does it support?
- What action follows?
- Does the user need it here?

A dashboard should support `Understand → Decide → Act`, not maximize chart count.

## Copy restraint

Prefer short task-oriented labels. Avoid generic AI-generated marketing copy such as “Welcome to your powerful dashboard” unless onboarding or promotion is truly part of the product.

If instructions are long, inspect whether the interface itself can become more self-explanatory.
