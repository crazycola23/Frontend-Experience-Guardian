---
name: frontend-experience-guardian
description: >
  Product-quality guardrail for AI coding agents working on real frontend applications.
  Use when creating, modifying, reviewing, debugging, or refactoring user-facing UI.
  Protect business behavior while improving interface restraint, layout stability,
  responsiveness, readability, accessibility, learnability, task efficiency, and
  final delivery quality. Prevent AI-demo bloat, unnecessary scrolling, unstable
  geometry, theme leakage, and rejected implementation residue.
---

# Frontend Experience Guardian

## Mission

Treat every frontend task as both an engineering task and a product-design task.

A user-facing implementation is not finished merely because it compiles, renders, or satisfies the literal request. It is finished when the affected experience is also stable, readable, understandable, efficient, predictable, responsive, accessible, and consistent with the product.

Continuously ask:

> Is anything here harder, noisier, less stable, more confusing, or more cumbersome than necessary?

## Priority

Resolve concerns in this order:

1. Functional correctness
2. Layout stability
3. Readability
4. Task clarity
5. Operational efficiency
6. Interaction predictability
7. Cross-page consistency
8. Responsive quality
9. Accessibility
10. Visual polish

Stable before animated. Clear before clever. Efficient before decorative. Consistent before novel.

## Rule Levels

- **MUST** — hard constraint. Do not violate without an explicit higher-priority requirement.
- **SHOULD** — default. Override only for a concrete product or technical reason.
- **CONSIDER** — optional technique. Use only when it lowers total interaction cost or improves clarity without unnecessary complexity.

## Ten Core Rules

### 1. MUST inspect the real interface when tooling permits

For substantial UI work, inspect the rendered result rather than reasoning from source alone. If browser, preview, screenshot, visual test, or runtime tooling is available, use it before making strong claims about visual quality.

Rendered behavior is the final authority.

### 2. MUST protect real product behavior

Do not silently change API behavior, permissions, authentication, billing, validation semantics, business rules, security behavior, destructive-operation semantics, or data meaning while performing UI work.

If a UX improvement requires a product decision, separate the recommendation from the safe UI implementation unless the user explicitly authorized the behavior change.

### 3. MUST apply the user-facing content gate

Every visible element must earn its place.

Before adding text, heading, description, badge, banner, tooltip, card, metric, chart, section, helper copy, placeholder, or status, ask whether the user needs it to:

- understand current state;
- make a decision;
- complete a task;
- avoid a mistake;
- recover from a problem.

If not, omit it.

Never dump agent reasoning, debug data, developer notes, component/token names, raw API details, backend enums, migration notes, temporary labels, TODOs, or implementation commentary into normal product UI.

Do not invent production users, metrics, transactions, charts, or records merely to make a page look complete. Demo fixtures belong only in clearly non-production demo, test, storybook, or design-system contexts.

Prefer fixing the interface over explaining the interface.

Read `references/interface-restraint.md` for UI bloat, excess cards/copy, dashboards, hierarchy, or scroll questions.

### 4. MUST preserve interface geometry across state changes

Loading, routing, resizing, sidebar changes, theme changes, and data refreshes should not rebuild the application unnecessarily.

Loading is the final interface before its data has arrived. Keep stable geometry where practical: page identity, toolbar, grids, cards, tables, charts, and action areas.

Distinguish initial loading from refreshing. Once real data is visible, prefer preserving it during refresh instead of returning the entire page to skeletons.

Do not hide layout instability with fade, scale, slide, or delayed reveal.

Read `references/layout-stability.md` for loading, routing, sidebar, theme, animation, or CLS work.

### 5. MUST justify every independent scroll region

A scrollbar is not automatically wrong, but every newly introduced independent scroll region is a design-review trigger.

Before adding fixed height, max-height, `overflow-y: auto`, or nested scrolling, ask whether natural page growth, better composition, reduced redundant chrome, wrapping, or more effective use of width removes the need.

Prefer:

1. natural document/page scrolling;
2. one intentional regional scroll area;
3. nested scrolling only when structurally necessary.

Do not force everything into one viewport by shrinking text, touch targets, or useful spacing. Avoid artificial scrolling, not all scrolling.

### 6. SHOULD optimize real task cost, not screenshot aesthetics

Identify primary tasks and prioritize improvements by:

`Frequency × Friction × User Impact`

Evaluate total interaction cost: clicks, page transitions, waiting, repeated input/search, context reconstruction, decision complexity, and error risk.

Make primary actions discoverable. Preserve search/filter/sort/pagination/selection/scroll context where reasonable. Keep equivalent actions predictable across similar pages.

Read `references/product-ux.md` for tables, forms, search/filter, navigation, dashboards, quick actions, and workflow redesign.

### 7. SHOULD fix systems before symptoms

When a defect repeats, inspect shared infrastructure first: design tokens, global CSS, app shell, page containers, shared components, toolbars/tables/forms, loading/empty/error patterns, and responsive rules.

Prefer one correct shared fix over many page-specific overrides.

Do not over-abstract. Different workflows may need different compositions. Abstract genuinely repeated patterns only.

### 8. SHOULD design responsiveness as reflow, not rerender

Prefer CSS Grid, Flexbox, media queries, container queries, `minmax()`, `clamp()`, `auto-fit`, and `auto-fill` for ordinary responsive layout.

Treat `window.innerWidth`, resize listeners, `ResizeObserver`, manual `isMobile`, and reactive column calculations as audit targets when CSS could handle presentation more stably.

Avoid competing breakpoint systems and resize feedback loops. Mobile is not compressed desktop.

Read `references/responsive-platform.md` for responsive, mobile, viewport, browser-history, focus, or restoration work.

### 9. MUST preserve accessibility and readability

Do not create accessibility regressions during visual cleanup.

Preserve visible keyboard focus, semantic controls, usable labels, reasonable touch targets, keyboard operation, readable contrast, and alternatives to essential hover-only behavior.

Treat muted, placeholder, disabled, table-secondary, sidebar-inactive, badge, tooltip, and chart-label contrast as common failure points.

When relevant, account for zoom, font scaling, reduced motion, high-contrast behavior, text expansion, localization, and RTL.

Read `references/accessibility-i18n.md` when typography, motion, localization, forms, mobile interaction, or accessibility are material.

### 10. MUST deliver only the verified accepted state

Experiments are allowed, but rejected proposals and abandoned approaches are control information, not the product's identity.

Generate final UI copy, names, filenames, comments, documentation, commit messages, PR text, and handoff from the verified accepted result.

Do not leave task-owned residue such as `NewSidebar`, `FinalDashboard`, commented-out alternatives, debug code, experimental styles, temporary labels, or explanations of options that no longer matter.

Preserve real history when required for safety, accuracy, compatibility, migration, audit, testing, API contracts, or requested comparison.

Read `references/finalization.md` before commit/PR/handoff work after multiple revisions or rejected alternatives.

## Working Procedure

Follow this sequence for substantial frontend work.

### 1. Understand

Identify the user's real task, existing design system/shared patterns, business constraints, technical constraints, and whether the problem is local or systemic.

Do not start by blindly editing CSS.

### 2. Inspect

Inspect the affected page plus relevant shared layout/components. When runnable tooling exists, inspect the actual interface before editing.

Check related theme, loading, responsive, overflow, navigation, and interaction states.

### 3. Diagnose

Classify findings as Functional, Stability, Readability, UX friction, Consistency, Responsive, Accessibility, or Visual polish.

Assign internal:

- **Severity:** P0 / P1 / P2 / P3
- **Confidence:** High / Medium / Low

Policy:

- High-confidence + high-impact + low-risk: fix directly when within scope.
- Medium-confidence: prefer conservative changes or clearly scoped recommendations.
- Low-confidence product-structure guesses: do not redesign silently.

### 4. Implement

Fix root causes. Prefer shared/system changes when defects repeat.

Do not expand UI work into unrelated features, new analytics/settings/onboarding, or invented user-facing information.

When the project is Vue, audit relevant `v-if` layout replacement, presentation-driven `:key` remounts, Teleport/theme inheritance, geometry watchers, reactive resize logic, duplicate responsive/theme state, scoped-style token overrides, and router-layout remounting. These are audit targets, not blanket prohibitions.

### 5. Verify

Inspect the changed result with available tooling.

Use the smallest relevant state matrix, for example desktop + mobile, loading + loaded, empty + error, light + dark, or sidebar expanded + collapsed.

Do not claim a state was verified if it was not actually observed or tested.

### 6. Regression Check

Check that shared changes did not break neighboring screens or behavior.

When tooling permits, verify:

- no unexpected console errors;
- no unintended page-level horizontal overflow;
- keyboard path remains usable;
- focus remains visible;
- loading → loaded does not materially jump;
- reduced-motion preference is respected when motion is involved;
- 200% zoom remains operable for relevant workflows;
- browser Back/Forward and focus/scroll restoration remain sensible when navigation changed.

Use existing project tooling first. Do not install large dependencies solely for this checklist unless requested or clearly warranted.

### 7. Finalize

Remove task-owned debug residue and abandoned experiments. Re-read final user-facing surfaces. Derive comments, commit, PR, and handoff language from final verified behavior.

## Default Heuristics

These are SHOULD defaults, not universal laws:

- prefer fewer purposeful surfaces over card-on-card composition;
- avoid decorative copy in operational interfaces;
- avoid many equally prominent actions;
- use whitespace, typography, grid, and dividers before another panel;
- avoid `transition-all` when it unintentionally animates layout geometry;
- avoid arbitrary fixed heights;
- prevent page-level horizontal scrolling;
- keep theme changes focused on appearance rather than geometry;
- prefer semantic design tokens over hard-coded UI-theme colors;
- prefer recognition over recall;
- progressively disclose advanced/rare controls;
- organize forms by user thinking rather than database schema;
- make errors actionable and preserve recoverable user work.

Optional techniques such as Quick View, Inline Edit, Bulk Actions, Undo, Auto Save, Command Palette, Sticky Actions, Container Queries, Virtualization, Optimistic Updates, and keyboard accelerators are CONSIDER items only. Use them when they reduce total interaction cost without increasing confusion, risk, or scope.

## Completion Gate

Before finishing substantial frontend work, check the affected surface.

### Function
- Intended task still works.
- Business rules and data semantics are preserved.

### Content
- No unnecessary agent-generated UI copy.
- No debug/developer/internal information in normal product UI.
- No invented production data.
- No redundant explanation that clearer layout could replace.

### Layout & Scroll
- Alignment, spacing, content width, and page padding are intentional.
- No unexplained page-level horizontal overflow.
- Every new independent scroll region has a concrete reason.
- No arbitrary fixed-height workaround when natural layout is better.

### Stability
- Relevant loading/refreshing/navigation/resize/sidebar/theme transitions are stable.
- Media reserves geometry where necessary.
- No animation masks structural instability.

### Readability & Accessibility
- Text remains readable in affected themes/states.
- Focus is visible.
- Keyboard/touch operation remains practical.
- No essential interaction exists only on hover.

### UX
- Primary action is discoverable.
- High-frequency work is not needlessly indirect.
- User context is preserved where practical.
- Feedback and recovery are understandable.

### Responsive
- Affected desktop/mobile compositions are usable.
- Breakpoint transitions do not visibly oscillate or shake.

### Finalization
- Task-owned dead experiments are removed.
- Names/comments describe current purpose and invariants.
- Delivery language is derived from final verified behavior.

If a high-impact check fails, the task is not finished.

## Reference Loading

Load only the relevant reference; do not read all references for every task.

- `references/interface-restraint.md` — UI bloat, copy, cards, scroll, hierarchy, dashboards.
- `references/layout-stability.md` — loading, refreshing, CLS, routing, sidebar, theme geometry, animation.
- `references/product-ux.md` — workflows, tables, forms, search/filter, navigation, task efficiency.
- `references/responsive-platform.md` — responsive layout, mobile reality, viewport/browser behavior, restoration.
- `references/accessibility-i18n.md` — keyboard, focus, contrast, zoom, preferences, localization, RTL.
- `references/finalization.md` — accepted-state delivery, naming, comments, commits, PRs, handoffs.

## Success Standard

A new user should understand where they are, what the page does, and what action matters without documentation.

An experienced user should experience less unnecessary clicking, navigation, repeated input, waiting, and context reconstruction.

The product should feel like one coherent mature application — not a collection of independently generated AI demos.
