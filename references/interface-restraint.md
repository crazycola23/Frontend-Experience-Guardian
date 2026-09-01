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

## Page-header restraint

**The default page-header pattern is title only. Supporting copy is an exception, not a standard ingredient.**

Do not add a subtitle, description, eyebrow, helper sentence, or explanatory sentence beneath or around a page title merely because page headers commonly contain one. Do not treat empty space below a title as a problem that needs words.

Add supporting copy only when the user explicitly requested it or when it provides material information that is not already communicated by navigation, controls, content, visible state, or the title itself.

Strong reasons include:

- an important constraint, consequence, or prerequisite;
- unusual scope or context that is not otherwise visible;
- actionable status, warning, recovery, or eligibility information;
- necessary guidance for a genuinely unfamiliar or ambiguous workflow;
- a distinction that changes how the user should interpret the page or choose the next action.

Weak reasons include:

- restating what the page does;
- paraphrasing the page title;
- describing controls or content already visible below;
- generic product or marketing language;
- making the header feel complete or polished;
- filling visual space;
- creating hierarchy that typography, spacing, alignment, grouping, or control placement could create without more words.

Examples of avoidable subtitle patterns:

- `Users` followed by `Manage your users and account permissions.`
- `Content Production` followed by `Configure content generation tasks and manage output.`
- `Settings` followed by `Customize your preferences and application behavior.`
- `Projects` followed by `Create, organize, and manage your projects.`

Examples that may justify supporting copy because they change understanding or action:

- `Changes here apply to all workspaces.`
- `Invitations expire after 7 days.`
- `User creation is disabled while SSO enforcement is active.`

Use the removal test: if deleting the supporting text leaves the next action, page scope, important constraints, and relevant system state equally clear, omit it.

When uncertain, omit the subtitle.

Apply the same test to section headings, card descriptions, dialog subtitles, drawer descriptions, and helper text. Repetition across hierarchy levels is still repetition.

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
