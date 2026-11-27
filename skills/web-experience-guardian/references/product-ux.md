# Product UX and Task Efficiency

Use this reference for workflows, navigation, tables, column alignment, pagination density, forms, settings, search/filter, dashboards, quick actions, and learning-cost reduction.

## Start with the task

Identify primary, secondary, advanced, dangerous, high-frequency, and high-friction tasks.

Prioritize by:

`Frequency × Friction × User Impact`

Optimize total interaction cost, not raw click count. Count navigation, waiting, repeated input, repeated search, context rebuilding, decision complexity, and error risk.

## Action hierarchy

Classify actions as Primary, Secondary, Utility, Rare, or Dangerous.

Avoid many equally prominent actions. Put equivalent actions in predictable locations across similar pages to build muscle memory.

Dangerous actions should be protected but should not dominate normal work.

## Preserve context

When users move List → Detail → Back or open/close quick editors, preserve search, filters, sort, pagination, selection, scroll position, and view mode when practical.

Browser back/forward should behave sensibly rather than resetting the work context unnecessarily.

## Search and filters

Users should understand what is being searched, which filters are active, why results look the way they do, and how to reset the state.

Keep important active filters visible rather than hiding all state inside a closed filter panel.

## Tables, lists & strict alignment discipline

Inspect column priority, width, density, row actions, bulk actions, sort, filters, search, pagination, selection, and responsive overflow.

### 1. Single-line atomic columns (No stacked cell subtitles)

- **Avoid stacking primary + subtitle lines inside table cells:** Putting two lines of text (`cell-primary` on top + muted `cell-sub` underneath) inside multiple columns of a table row creates visual clutter, inflates row height, and breaks horizontal eye scanning.
- **One attribute per column, single-line alignment (`一列一事，单行对齐`):** Split distinct attributes that users actually scan or filter by (e.g., Archive ID, Name, Gender/Age, Role/Category, Specialty/Diagnosis, Certificate/Mode, Duration, Expiry Date, Location) into dedicated atomic columns on a single horizontal line.
- Reserve multi-attribute detail for the detail view, drawer, or quick view rather than cramming secondary subtitles under every cell.

### 2. Native table-cell display invariant

- **Never apply `display: flex` or `display: inline-flex` directly to a `<th>` or `<td>` element.** Overriding `display: table-cell` breaks table column sizing and `vertical-align: middle`, causing text in that cell to jump to the top edge of the row while neighboring cells stay middle-aligned.
- Always keep `<th>` and `<td>` as native `table-cell` elements with `vertical-align: middle` and `white-space: nowrap`. When flex layout is needed for an inline badge or action group, place an inner `<div class="cell-inline">` inside the `<td>`.

### 3. Mixed-unit column alignment & orphan-wrap prevention

- **Avoid ragged right-aligned mixed-unit strings:** When a metric list or table column mixes values with different Chinese/English unit suffixes or prefixes (`100%`, `38.4 岁`, `6 人`, `24/24 人`, `要求 100%`, `不低于 60%`), right-aligning the whole string causes both the numbers and the leading characters to stagger irregularly.
- **Align along a strict vertical axis:** Give structured metric rows an explicit header row (`项目 | 进度 | 当前数值 | 标准 | 状态`) and left-align mixed-unit value/requirement columns on fixed grid tracks (or split the number and unit sub-columns) so every row starts on the exact same vertical line.
- **Eliminate 1–2 character orphan wraps:** Set `white-space: nowrap` on table cells, metric titles, status pills, dates, and archive codes so a label never wraps its last 1–2 characters onto a second line.

### 4. Row actions & visual restraint

- Avoid a row containing many equally prominent buttons or overflowing the table width. Expose one or two high-frequency actions (e.g., `查看`, `打印`) that fit cleanly within the viewport without horizontal clipping, and move low-frequency or destructive actions (`删除`) to the detail view or a secondary menu.
- **Keep per-row secondary action buttons visually quiet at rest:** In dense tables (15–20+ rows), rendering bordered button boxes (`border: 1px solid`) on every row creates a heavy vertical column of button chrome that competes with data and status alerts. Render row action buttons as borderless text/icon buttons at rest (`border-color: transparent; background: transparent; color: var(--muted)`) and reveal their border/surface on row `:hover` or keyboard `:focus-visible`. Note that the action labels and icons remain visible at all times so accessibility and discoverability are never compromised.
- If users repeatedly enter a detail page only to inspect status, copy a value, toggle one field, or read brief metadata, consider Quick View, Sheet, Popover, Inline Edit, or Row Action.

### 5. Viewport-filling pagination defaults & total-count clarity

- **Do not default primary data tables to tiny page sizes (`5` or `8` rows/page):** When a full-screen or desktop table only renders 8 rows and leaves the bottom half of the table viewport empty white space, users frequently misinterpret the partially filled viewport as the entire dataset ("thinking there are only 8 records in total").
- **Default to a viewport-filling page size (`20` rows/page for standard 40–44px single-line rows):** Ensure the default page size fills a standard desktop viewport within the single scroll body while keeping `thead` sticky at the top and the pagination bar pinned at the bottom.
- **Always pair pagination with an explicit total & range readout (`共 N 条 · 第 a–b 条`) and a page-size selector (`10 / 20 / 50 条/页`):** Make total dataset size unmistakable at a glance without repeating the same total count in multiple adjacent headers or toolbars.

## Interaction-container defaults

- Popover: lightweight choice or supporting information.
- Dropdown: action menu.
- Dialog: short focused task or high-value confirmation.
- Sheet/Drawer: contextual quick view or medium-complexity work.
- Full page: deep workflow, long form, complex information.

These are defaults, not universal laws.

## Forms

Order fields by user thinking rather than database schema. Group Basic Information, Business Configuration, Advanced Settings, or equivalent domain sections when helpful.

Use sensible defaults, reduce unnecessary required fields, validate inline, preserve user input after recoverable failures, and avoid asking for information the system already knows.

Recognition is generally better than recall: searchable selection is preferable to memorizing IDs or internal codes.

## Progressive disclosure

Keep common operations visible. Put advanced/rare controls behind secondary UI. The goal is simple for beginners and efficient for experienced users.

Do not use tooltips as the only way to understand core actions.

## Feedback and recovery

A user action should acknowledge input promptly. Use button loading, disabled state, inline status, optimistic state, toast, or progress as appropriate.

Editing screens should make unchanged/unsaved/saving/saved/failed understandable.

Errors should say what happened, why when known, and what the user can do next.

Low-risk reversible actions may benefit from Undo rather than repeated confirmation. High-risk irreversible actions still need explicit safeguards.

## Closed-loop navigation & eliminating page islands

Never build multi-view operational applications as disconnected "page islands" (`页面孤岛`) where jumping from a dashboard, alert, or related entity drops the user into a screen with no memory of how they got there, no way to return to their actual origin, and no way to step through sibling or related records.

1. **Persistent location breadcrumb & navigation history stack:**
   - Maintain an explicit navigation history stack in the application shell when users traverse across views or entities (`Dashboard → Filtered List → Entity A Detail → Related Entity B Detail`).
   - Display a live, clickable breadcrumb trail in the global top bar (`Overview / Module / Current Entity`) alongside a context-aware `← Back` trigger so users always know their exact position and origin.

2. **Interactive dashboard drill-down with origin context banner:**
   - Dashboard KPI cards, compliance indicators, and category distribution rows should act as interactive entry points that drill down into the corresponding list view with filters pre-applied.
   - When a list view is entered via a drill-down, display a prominent, removable **Drill-Down Context Banner** (`概览穿透 · <筛选条件> · N 人 · [← 返回概览工作台] [查看全部记录]`) so the user understands why the list is filtered and can return to the dashboard in one click.

3. **Origin-aware Back button (no hardcoded return paths):**
   - Detail views must not hardcode their back button to "Back to List" when the user actually arrived from a Dashboard alert, an Audit Log entry, or another entity's detail page.
   - Dynamically label and wire the primary return button to restore the exact caller (`← 返回概览工作台`, `← 返回执业医师：王宏博`, `← 返回调阅登记簿`) while preserving the caller's filters and pagination state.

4. **Bidirectional cross-entity linking & in-detail `Prev / Next` stepping:**
   - When entities reference each other (e.g. a Medical Staff archive is assigned to several Disabled Clients, and a Disabled Client record lists their Responsible Doctor, Nurse, and Caregiver), render those references as interactive jump links/chips in both directions rather than dead plain text.
   - Provide `第 k / N 份 · [‹ 上一份] [下一份 ›]` sequential stepping controls directly inside the detail view's sticky header so auditors and operators can inspect consecutive records without repeatedly bouncing back to the list table.

## Dashboard

Metrics and charts should support decisions. Do not add analytics because “dashboards have charts.” Ask what action follows from each piece of information.
