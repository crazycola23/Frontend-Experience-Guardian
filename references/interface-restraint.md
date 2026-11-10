# Interface Restraint

Use this reference when a page feels busy, demo-like, over-explained, over-carded, over-colored, or artificially scrollable.

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
- rounded cards with thick colored left borders (`border-left: 3px/4px solid`);
- title + section title + card title repeating the same concept;
- explanatory paragraphs compensating for unclear interaction;
- green "Normal / Compliant / Active" badges and green progress bars on every passing item;
- status badges on information that is already obvious;
- many identical primary-looking buttons.

Prefer fixing hierarchy, grouping, naming, spacing, or workflow first.

## Surface & border restraint

Cards, panels, borders, badges, dividers, icons, shadows, buttons, and colored surfaces all consume attention.

Before adding a surface, ask whether whitespace, typography, alignment, grid, or a divider would communicate the relationship more clearly with less visual noise.

Cards should represent meaningful grouping or interaction surfaces, not become the default wrapper for every section.

**Avoid thick colored side-borders on rounded cards:** Applying `border-left: 3px solid` or `4px solid` to a container with `border-radius` creates crescent-shaped corner artifacts and visual clutter when stacked in a list. Use a uniform `1px solid` border on the card and express severity or category inside the card via a compact status pill, icon, or dot.

## Color semantics & "Normal is Silent"

Color in operational interfaces must have stable meaning and clear visual priority:

1. **Separate status semantic colors from categorical chart colors:**
   - **Status colors** (green / amber / red) communicate compliance, risk, or urgency.
   - **Categorical colors** distinguish categories in distribution bars, legends, or breakdowns.
   - Do not reuse traffic-light status colors inside categorical charts, or the eye will confuse category membership with pass/fail status.
   - When a categorical chart has 4–8 categories, do not rely on a single hue with stepped opacity (which makes adjacent categories hard to tell apart). Use a muted multi-hue palette (e.g., slate teal, indigo blue, plum violet, cyan, warm ochre, neutral slate, magenta) that remains distinct while staying lower in saturation than alert badges.

2. **Practice "Normal is Silent" (正常静默):**
   - When 80%+ of items are compliant, valid, or normal, attaching green badges and green progress bars to every passing row floods the screen with chromatic noise and weakens real warnings.
   - Keep normal/compliant items visually neutral (plain text or a quiet neutral pill). Reserve chromatic highlights exclusively for warnings, expirations, missing requirements, and errors.

3. **Keep progress bars single-duty:**
   - Do not make a progress bar simultaneously carry numeric ratio AND pass/fail color semantics.
   - Use a consistent, calm fill color for the progress bar to represent proportion (`0–100%`), and use an independent status pill or icon beside it when pass/fail or risk state needs to be called out.

4. **Unify warning tones and establish visual weight hierarchy:**
   - Maintain a strict visual weight hierarchy: **Critical Alert > General Warning > Core Metric > Categorical Chart**.
   - Keep general warnings (expiring soon, pending attachment, under review) on one consistent amber/ochre hue and saturation family across the entire product rather than mixing random yellows and oranges.
   - Pair status colors with non-color cues (`×` for critical/error, `!` for warning, explicit text labels) to support accessibility and rapid scanning.

## Compensatory structural & surface hierarchy (Preventing flat white-on-white pages)

When you strip away decorative colors and practice "Normal is Silent", **you MUST compensate with structural surface depth and typographic contrast**. Otherwise, the page collapses into a flat, monotonous sheet of identical text where the eye has no natural entry point or scanning rhythm ("视觉层级缺失").

1. **Three-layer surface luminance hierarchy (`Canvas → Elevated Surface → Tinted Header/Control Band`):**
   - **Layer 0 — Recessed Workspace Canvas** (e.g. `#F2F5F7` or `#F4F6F8`): Use a cool-neutral recessed background for the scrolling workspace canvas so primary content blocks do not float in undifferentiated white space.
   - **Layer 1 — Elevated Primary Surface** (`#FFFFFF` with `1px solid` border and subtle ambient shadow `0 1px 3px rgba(15, 23, 42, 0.04)`): Use pure white for primary operational tables, KPI summary strips, and inspection cards so they lift clearly off the canvas.
   - **Layer 2 — Tinted Header / Control Band** (e.g. `#EDF2F4` or `#F8FAFB` with stronger bottom border): Use a distinct tinted band for sticky table headers (`<thead>`), filter toolbars, and card section headers so data boundaries are unmistakable at a glance.

2. **Three-tier typographic & structural content hierarchy:**
   - **Tier 1 — Focal Anchor (视觉锚点):**
     - On dashboards/overviews: provide a compact top summary strip (e.g. 4 actionable KPI cards with `24px–28px` bold tabular numerals and interactive drill-down affordance) that anchors the eye immediately before detailed lists.
     - In tables and rosters: render the primary entity identifier (e.g. Person Name, Subject Title) in `13.5px–14px` bold (`font-weight: 600–700`) high-contrast ink (`#142029`).
   - **Tier 2 — Structural Taxonomy (结构化分类胶囊):**
     - Even when status is normal ("Normal is Silent"), key categorical dimensions (Role, Disability Level, Service Mode, Department) should not all be bare uniform text. Wrap primary classification attributes in quiet, neutral structural chips (`.struct-tag`: `#F1F5F8` background, `#D5E0E6` border, `#2C424E` text) while keeping chromatic pills strictly for anomalies and warnings.
   - **Tier 3 — Recessed Metadata (退后辅助元数据):**
     - Render archive codes, serial numbers, timestamps, and unit suffixes in smaller (`12px`), muted (`#6E808C`) monospace/tabular type (`font-variant-numeric: tabular-nums`) so they never compete with Tier 1 names or Tier 2 classifications.

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

## Scroll architecture & sticky boundary standard

Treat scroll containers and sticky boundaries as an application-wide contract rather than ad-hoc per-component choices:

1. **Unified scroll container expectation:**
   - Do not mix whole-page scrolling on some workspace views with arbitrary inner-container scrolling on others.
   - In an application shell with a fixed sidebar and top bar, each workspace view should follow a consistent two-zone structure: a fixed context top bar (`flex-shrink: 0`) and a single vertically scrollable body (`flex: 1; min-height: 0; overflow-y: auto; overflow-x: hidden`).
2. **Fixed context boundary retention:**
   - Global navigation, page title/actions, filter toolbars, active filter tags, and detail-view back/action headers must stay pinned outside the scroll container so users never lose context while scrolling long records.
3. **Clear sticky table header criteria:**
   - Apply `position: sticky; top: 0; z-index: 10` to the `<thead>` of full-width primary roster/log tables that live directly inside the main scroll body.
   - Do not add sticky headers or independent `max-height` scroll wrappers to short embedded sub-tables inside cards or detail sheets.
4. **Zero nested vertical scrollbars:**
   - Never nest a scrollable panel or table inside another vertical scroll container. Let cards and sub-tables inside a scrollable workspace body expand naturally to their content height.

## Dashboard restraint

For each metric or chart ask:

- What decision does it support?
- What action follows?
- Does the user need it here?

A dashboard should support `Understand → Decide → Act`, not maximize chart count.

## Copy restraint

Prefer short task-oriented labels. Avoid generic AI-generated marketing copy such as “Welcome to your powerful dashboard” unless onboarding or promotion is truly part of the product.

If instructions are long, inspect whether the interface itself can become more self-explanatory.
