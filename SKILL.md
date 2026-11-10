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

### 3. MUST apply the user-facing content gate & visual restraint

Every visible element and every chromatic highlight must earn its place.

Before adding text, heading, description, badge, banner, tooltip, card, metric, chart, section, helper copy, placeholder, or status color, ask whether the user needs it to:

- understand current state;
- make a decision;
- complete a task;
- avoid a mistake;
- recover from a problem.

If not, omit it.

Never dump agent reasoning, debug data, developer notes, component/token names, raw API details, backend enums, migration notes, temporary labels, TODOs, or implementation commentary into normal product UI.

Do not invent production users, metrics, transactions, charts, or records merely to make a page look complete. Demo fixtures belong only in clearly non-production demo, test, storybook, or design-system contexts.

Prefer fixing the interface over explaining the interface.

#### Page-header default

**Default to title-only page headers.** A page title should normally stand on its own.

Do not add a subtitle, description, eyebrow, helper sentence, or explanatory copy beneath or around a page title unless the user explicitly requested it or the text communicates a concrete information need that is not already visible elsewhere.

Valid reasons include a non-obvious constraint, prerequisite, scope distinction, consequence, warning, eligibility condition, meaningful current state, or guidance required to understand an unfamiliar or ambiguous workflow.

Do not add supporting copy merely to make a header feel complete, create hierarchy, fill empty space, sound polished, paraphrase the title, or describe controls/content already visible on the page. Solve hierarchy with typography, spacing, alignment, grouping, and control placement before adding words.

Use the removal test: if deleting the supporting text does not materially change what the user understands, decides, or does next, omit it.

**When uncertain, omit the subtitle.** Supporting copy is exceptional, not a standard page-header ingredient.

Apply the same restraint to section headings, card descriptions, dialog subtitles, drawer descriptions, and helper text.

#### Color semantics, "Normal is Silent" & compensatory visual hierarchy

- **Decouple status colors from categorical colors:** Keep status semantic colors (pass/warn/fail: green/amber/red) strictly separate from categorical chart/series palettes. Do not reuse traffic-light status colors in category breakdown bars or legends, and ensure multi-category charts (>3 series) use distinct muted multi-hue steps rather than indistinguishable single-hue opacity fades.
- **Default to "normal is silent":** Compliant, valid, normal, or passing states should remain visually quiet (neutral text or plain subtle pills). Reserve chromatic badges and fills for warnings, exceptions, and actionable items so alerts stand out immediately.
- **Compensate color restraint with 3-layer surface & 3-tier typographic hierarchy:** Never let color subtraction flatten a page into uniform white-on-white blocks with identical font weights. Establish clear figure-ground contrast (`Recessed Workspace Canvas` → `Elevated Pure-White Card/Table Surface` → `Tinted Sticky Header / Filter Control Band`) and a 3-tier content hierarchy (`Tier 1 Focal Anchor: KPI hero numbers & bold entity names` → `Tier 2 Structural Taxonomy: neutral structural chips for roles/categories + chromatic badges strictly for anomalies` → `Tier 3 Recessed Metadata: smaller muted tabular numerals for IDs/codes/dates`).
- **Single-duty progress bars:** Progress bars should express numeric proportion only (using a single calm neutral/brand fill). Delegate pass/fail or risk status to an independent label or icon rather than overloading the bar with both proportion and status color.
- **Visual weight hierarchy & non-color redundancy:** Maintain a strict visual weight order (`Critical Alert > Warning > Core Metric > Categorical Chart`), unify warning hues/saturation across the app, and pair status colors with symbols or text (`×`, `!`) so color is never the sole indicator.
- **Reject decorative thick side-borders on cards:** Avoid `border-left: 3px/4px solid ...` accent strips on rounded cards or list items, which create awkward curved corner artifacts. Use a clean `1px` full border and an internal badge or status dot instead.

Read `references/interface-restraint.md` for UI bloat, excess cards/copy, color semantics, surface hierarchy, dashboards, or scroll questions.

#### Removal is the harder half

Adding requires justification. Removing something that already ships does too — it is a product decision, not a styling one, and "it looks cluttered" is never a sufficient argument.

Before removing a capability:

- prove it is empty in real data (null rate, single-value constants, duplicate sources), not in the type signature;
- check whether a specification, acceptance criterion, or compliance rule mandates it — if so, surface the conflict and let the owner decide rather than deleting quietly or silently complying;
- prefer narrowing to removing: render only the non-empty case, keep the one new clause of a warning, drop only the restatement;
- remove the orphaned logic, styles, and imports with the markup;
- add a negative guard that fails if the surface returns, and verify it by re-introducing the redundancy.

Removing something creates no failing test, so nothing prevents a later well-intentioned change from restoring it. Record the reason where the next maintainer will look, and record the measurement the decision rested on.

Some redundancy is load-bearing: mandated copy, the only statement of a consequence or irreversible effect, and dedicated diagnostic or audit surfaces are legitimate exceptions. Do not extend that exception to ordinary business pages.

Prioritize removals that are actively harmful over removals that are merely untidy: copy that contradicts validation, raw internal identifiers shown as labels, and panels that can only ever render one value.

Read `references/less-is-more.md` for the full removal decision procedure.

### 4. MUST preserve interface geometry across state changes

Loading, routing, resizing, sidebar changes, theme changes, and data refreshes should not rebuild the application unnecessarily.

Loading is the final interface before its data has arrived. Keep stable geometry where practical: page identity, toolbar, grids, cards, tables, charts, and action areas.

Distinguish initial loading from refreshing. Once real data is visible, prefer preserving it during refresh instead of returning the entire page to skeletons.

Do not hide layout instability with fade, scale, slide, or delayed reveal.

Read `references/layout-stability.md` for loading, routing, sidebar, theme, pagination column locks, non-fullscreen window contraction, animation, or CLS work.

### 5. MUST justify every independent scroll region & unify sticky boundaries

A scrollbar is not automatically wrong, but every newly introduced independent scroll region is a design-review trigger, and scroll behavior must be predictable across all pages in the same application.

Before adding fixed height, max-height, `overflow-y: auto`, or nested scrolling, ask whether natural page growth, better composition, reduced redundant chrome, wrapping, or more effective use of width removes the need.

Prefer:

1. a unified scroll contract across the app (either natural page scrolling or a single explicit `Fixed Context Header + Single Scrollable Body + Fixed Pagination Footer` per workspace view);
2. keeping navigation rails, page title/actions, filter toolbars, detail breadcrumbs, and pagination bars fixed outside the scroll container so context is never lost while scrolling long lists;
3. applying sticky table headers (`position: sticky; top: 0`) consistently to full-width primary data tables that scroll vertically, while omitting them on short embedded summary tables;
4. zero nested vertical scrollbars (`overflow-y: auto` inside `overflow-y: auto` is prohibited unless structurally unavoidable).

Do not force everything into one viewport by shrinking text, touch targets, or useful spacing. Avoid artificial scrolling, not all scrolling.

### 6. SHOULD optimize real task cost, closed-loop navigation, table scannability & alignment discipline

Identify primary tasks and prioritize improvements by:

`Frequency × Friction × User Impact`

Evaluate total interaction cost: clicks, page transitions, waiting, repeated input/search, context reconstruction, decision complexity, and error risk.

Make primary actions discoverable. Preserve search/filter/sort/pagination/selection/scroll context where reasonable. Keep equivalent actions predictable across similar pages.

For multi-view navigation and entity relationships (**No Page Islands / Closed-Loop Navigation**):

- **Persistent location breadcrumb & history stack:** Maintain a live navigation history stack and render an interactive breadcrumb trail (`Scope / Module / Current Entity or Filter`) in the shell topbar/header so users never lose spatial context.
- **Interactive dashboard drill-down with origin context banner:** Overview KPI cards, category bars, and compliance rows should drill down into target lists with filters pre-applied, and the target list must render a removable **Drill-Down Context Banner** (`当前由「...」穿透筛选 · [← 返回概览] [查看全部]`).
- **Origin-aware back navigation:** Never hardcode generic `返回列表` on detail pages when entered from an overview alert, audit log, global search, or a related entity. Dynamically display and restore the actual caller (`← 返回概览工作台`, `← 返回调阅登记簿`, `← 返回关联实体档案`).
- **Bidirectional cross-entity linking & sequential stepping:** Render foreign-key domain references (e.g., `Doctor ⇄ Patient`, `Staff ⇄ Assigned Clients`, `Log ⇄ Target Archive`) as interactive jump chips rather than dead plain text, and provide `上一份 / 下一份` (`Prev / Next` with `k / N` position indicator) in detail headers so users can review adjacent records without pogo-sticking (`列表 ↔ 详情`).

For data tables and metric lists:

- **Prefer single-line atomic columns over stacked cell subtitles:** Do not stack a primary value and a muted secondary subtitle (`cell-primary` + `cell-sub`) inside every table column. Split distinct attributes into dedicated single-line columns (`one attribute per column, single-line alignment`) so rows scan cleanly along a horizontal line.
- **Never apply `display: flex` directly to `<th>` or `<td>`:** Keep `<th>` and `<td>` as native `display: table-cell` elements with `vertical-align: middle` and `white-space: nowrap`; wrap inline badges or buttons in an inner `<div>` or `<span>` when flex alignment is needed.
- **Align mixed-unit columns along a straight vertical axis:** When rows mix different units or prefixes (`100%`, `38.4 岁`, `24/24 人`, `要求 100%`), right-aligning the combined string creates a ragged vertical edge. Left-align on fixed grid tracks with an explicit header row, or separate the number and unit columns.
- **Prevent 1–2 character orphan wraps:** Use `white-space: nowrap` on labels, badges, dates, IDs, and compact table cells so short text never wraps into awkward two-line fragments.

Read `references/product-ux.md` for tables, forms, search/filter, closed-loop navigation, dashboards, quick actions, and workflow redesign.

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
- no unintended page-level or table-level horizontal overflow;
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

- default to title-only page headers; treat supporting copy as an exception that requires concrete information value;
- prefer fewer purposeful surfaces over card-on-card composition, while maintaining clear figure-ground contrast between the workspace canvas (`--canvas`) and elevated cards/tables (`--surface`);
- avoid thick colored left borders (`border-left: 3px/4px solid`) on rounded cards;
- keep normal/compliant states visually quiet ("normal is silent") and reserve chromatic highlights for warnings and anomalies;
- compensate color restraint with 3-tier typographic & structural hierarchy (hero KPI numbers, bold entity anchors, neutral structural category chips, recessed tabular metadata);
- separate status semantic colors from categorical chart palettes, and give multi-category charts distinct muted hues;
- keep progress bars single-duty (numeric ratio only) and put status in an independent badge or icon;
- close every navigation loop: maintain topbar location breadcrumbs, show drill-down origin banners on filtered lists, make detail back buttons origin-aware, link related entities bidirectionally, and provide `Prev / Next` record stepping in detail views;
- prefer single-line atomic table columns (`one attribute per column`) over two-line stacked primary + subtitle cells;
- never set `display: flex` directly on `<th>` or `<td>`;
- lock data table column geometry with `table-layout: fixed` and `<colgroup>` so pagination and filtering never cause horizontal column jitter;
- use `minmax(0, 1fr)` and `min-width: 0; min-height: 0` on CSS Grid app shells so non-fullscreen windows never clip bottom-right controls;
- avoid decorative copy in operational interfaces;
- avoid many equally prominent actions;
- use whitespace, typography, grid, and dividers before another panel;
- avoid `transition-all` when it unintentionally animates layout geometry;
- avoid arbitrary fixed heights;
- prevent page-level and unintended table-level horizontal scrolling;
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

### Content, Visual Hierarchy & Restraint
- No unnecessary agent-generated UI copy.
- No debug/developer/internal information in normal product UI.
- No invented production data.
- No redundant explanation that clearer layout could replace.
- Page headers remain title-only unless supporting copy passes the concrete-information and removal tests.
- No page or section subtitle that merely restates a clear title or obvious surrounding context.
- Normal/passing states are not over-colored; status colors and categorical chart colors do not collide.
- Color subtraction is compensated by clear surface elevation (`Canvas → Card/Table → Header/Control Well`) and 3-tier typographic weight hierarchy (never a flat white-on-white sheet).
- No thick colored left-border accent strips on rounded cards.

### Layout, Alignment & Scroll
- Alignment, spacing, content width, and page padding are intentional.
- Mixed-unit metric lists and table columns align on clean vertical axes without ragged edges or 1–2 character orphan wraps.
- Data tables use single-line atomic columns (`table-layout: fixed` + `<colgroup>`) without stacked primary+subtitle clutter, `display: flex` directly on `<td>`/`<th>`, or cross-page column jitter.
- Non-fullscreen windows contract cleanly (`minmax(0, 1fr)`) without clipping rightmost action columns or bottom-right pagination controls.
- No unexplained page-level or table-level horizontal overflow.
- Scroll container boundaries and sticky table headers follow one consistent rule across the app with zero nested vertical scrollbars.
- No arbitrary fixed-height workaround when natural layout is better.

### Stability
- Relevant loading/refreshing/navigation/resize/sidebar/theme transitions are stable.
- Media reserves geometry where necessary.
- No animation masks structural instability.

### Readability & Accessibility
- Text remains readable in affected themes/states.
- Status indicators include non-color cues (text/symbols) alongside color.
- Focus is visible.
- Keyboard/touch operation remains practical.
- No essential interaction exists only on hover.

### UX & Navigation Closed-Loop
- Primary action is discoverable.
- High-frequency work is not needlessly indirect.
- No isolated "page islands": breadcrumb location context is visible, dashboard drill-downs show an origin context banner with one-click return, detail back buttons restore the actual caller, related domain entities link bidirectionally, and detail views support sequential `Prev / Next` stepping.
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

- `references/interface-restraint.md` — UI bloat, copy, cards, color semantics, compensatory surface/typographic hierarchy, borders, scroll architecture, dashboards.
- `references/less-is-more.md` — deciding to remove existing capability: proving emptiness, spec conflicts, narrowing before deleting, negative guards.
- `references/layout-stability.md` — loading, refreshing, CLS, routing, sidebar, theme geometry, pagination column lock, non-fullscreen grid contraction, animation.
- `references/product-ux.md` — workflows, closed-loop navigation, anti-page-island patterns, single-line atomic tables, column alignment, forms, search/filter, task efficiency.
- `references/responsive-platform.md` — responsive layout, mobile reality, viewport/browser behavior, restoration.
- `references/accessibility-i18n.md` — keyboard, focus, contrast, zoom, preferences, localization, RTL.
- `references/finalization.md` — accepted-state delivery, naming, comments, commits, PRs, handoffs.

## Success Standard

A new user should understand where they are, what the page does, and what action matters without documentation.

An experienced user should experience less unnecessary clicking, navigation, repeated input, waiting, and context reconstruction.

The product should feel like one coherent mature application — not a collection of independently generated AI demos.
