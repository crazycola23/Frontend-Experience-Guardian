# Changelog

All notable changes to Frontend Experience Guardian are documented here.

## 0.5.1 — 2026-11-10

### Added

- Added **Viewport-filling pagination defaults & total-count clarity** and **Quiet per-row action restraint** to `SKILL.md` (Rule 6) and `references/product-ux.md`:
  - Avoid tiny default page sizes (`5` or `8` rows/page) on primary operational tables that leave half the viewport blank and mislead users into thinking the partial page is the entire dataset. Default to a viewport-filling page size (`20` rows/page for single-line atomic rows) paired with an explicit `共 N 条 · 第 a–b 条` readout and a `10 / 20 / 50` page-size selector.
  - Keep repeated per-row action buttons borderless at rest (revealing their border/surface on row `:hover` or `:focus-visible`) so 20-row tables do not stack dozens of heavy button boxes down the right edge.

## 0.5.0 — 2026-11-10

### Added

- Added **Compensatory structural & surface hierarchy (Preventing flat white-on-white pages)** to `SKILL.md` (Rule 3) and `references/interface-restraint.md`:
  - Enforce a three-layer surface luminance hierarchy (`Recessed Workspace Canvas #F2F5F7 → Elevated Primary Surface #FFFFFF → Tinted Sticky Header / Filter Control Band #EDF2F4`) so color restraint ("Normal is Silent") never collapses into a flat, undifferentiated white-on-white sheet ("视觉层级缺失").
  - Enforce a three-tier typographic & structural content hierarchy: Tier 1 Focal Anchor (top actionable KPI summary strip & bold entity names), Tier 2 Structural Taxonomy (neutral structural chips `.struct-tag` for key classification dimensions while keeping chromatic pills strictly for anomalies), and Tier 3 Recessed Metadata (muted tabular numerals for IDs, codes, and timestamps).
- Added **Closed-loop navigation & eliminating page islands** to `SKILL.md` (Rule 6) and `references/product-ux.md`:
  - Maintain a live location breadcrumb trail and navigation history stack in the application shell.
  - Require interactive dashboard drill-downs to display a removable **Drill-Down Context Banner** (`当前正查看由「...」穿透筛选的记录 · [← 返回原视图] [查看全部]`) in the target list view.
  - Require detail views to provide an **origin-aware Back button** (dynamically restoring the actual caller — Dashboard, Audit Log, or related entity detail — rather than a hardcoded list path), **bidirectional cross-entity jump links/chips**, and **in-detail `Prev / Next` (`上一份 / 下一份`) sequential stepping**.

## 0.4.0 — 2026-11-09

### Added

- Added **Color semantics & "Normal is Silent"** guardrails to `SKILL.md` (Rule 3) and `references/interface-restraint.md`:
  - Decouple traffic-light status semantic colors (green/amber/red) from categorical chart/series palettes, and require distinct muted multi-hue palettes for multi-category charts (>3 series) rather than indistinguishable single-hue opacity steps.
  - Default to "normal is silent": compliant, valid, or passing items remain visually neutral rather than flooding operational screens with green badges and green progress bars.
  - Keep progress bars single-duty (numeric ratio only) and delegate pass/fail or risk status to an independent badge or icon.
  - Enforce a visual weight hierarchy (`Critical Alert > Warning > Core Metric > Categorical Chart`) with unified warning hues and non-color accessibility cues (`×`, `!`).
- Added **Card & border restraint** to `SKILL.md` and `references/interface-restraint.md`: prohibit thick colored left borders (`border-left: 3px/4px solid`) on rounded cards and list items that create curved corner artifacts.
- Added **Single-line atomic table columns & strict alignment discipline** to `SKILL.md` (Rule 6) and `references/product-ux.md`:
  - Prefer single-line atomic columns (`one attribute per column, single-line alignment`) over stacking a primary value and a muted subtitle (`cell-primary` + `cell-sub`) inside table cells.
  - Prohibit applying `display: flex` directly to `<th>` or `<td>` elements so native `display: table-cell` and `vertical-align: middle` invariants are preserved.
  - Align mixed-unit metric lists and columns along a straight vertical axis with explicit headers, and prevent 1–2 character orphan wraps (`white-space: nowrap`).
- Added **Table column stability across pagination & filtering** and **Non-fullscreen window shell contraction** to `references/layout-stability.md`:
  - Lock data table column geometry with `table-layout: fixed; width: 100%;` and explicit `<colgroup>` definitions so variable inline badges or action buttons never cause horizontal column jitter across pages or filter states.
  - Enforce `minmax(0, 1fr)` on CSS Grid app shells and `min-width: 0; min-height: 0` across workspace containers so non-fullscreen windows never clip the rightmost action column or bottom-right pagination bar.

### Changed

- Expanded Rule 5 (`MUST justify every independent scroll region & unify sticky boundaries`) and `references/interface-restraint.md` with an explicit application-wide scroll contract: fixed context headers/toolbars outside the scroll container, consistent `position: sticky; top: 0` criteria for full-width primary data tables, and zero nested vertical scrollbars.

## 0.3.0 — 2026-10-02

### Added

- Added `references/less-is-more.md`: the decision procedure for removing capability that already ships. Covers proving emptiness against real data rather than type signatures, surfacing specification conflicts instead of quietly deleting or quietly complying, preferring narrowing (render only the non-empty case, keep the irreversible-consequence clause, drop the restatement) over wholesale deletion, removing orphaned logic with the markup, and adding negative guards that are verified by re-introducing the redundancy.
- Added `evals/capability-removal.md` to test both failure directions: deletion avoidance (keeping provably empty surfaces) and deletion overreach (removing spec-mandated copy, irreversible-effect warnings, diagnostic surfaces, or actionable empty states).

### Changed

- Extended Rule 3 with a "Removal is the harder half" subsection. Adding requires justification and so does removing; the section makes the asymmetry explicit and prioritizes actively harmful removals — copy that contradicts validation, raw internal identifiers presented as labels, panels that can only ever render one value — over merely untidy ones.
- Listed the new reference in the Reference Loading index and the repository layout in `README.md`.

## 0.2.1 — 2026-09-01

### Changed

- Strengthened page-header restraint: title-only is now the default, while subtitles, descriptions, eyebrows, and helper copy require explicit user intent or concrete information value.
- Added a removal test and an explicit `when uncertain, omit the subtitle` tie-breaker to reduce generic AI-generated header copy.
- Expanded the interface-restraint reference with clearer valid/invalid subtitle reasons and operational examples.

### Added

- Added `evals/unrequested-page-subtitle.md` to test both redundant subtitle generation and legitimate supporting-copy exceptions.

## 0.2.0 — 2026-08-24

### Changed

- Rebuilt the 35 KB single-file handbook into a compact executable Skill plus on-demand references.
- Added explicit MUST / SHOULD / CONSIDER instruction levels.
- Added the seven-step workflow: Understand → Inspect → Diagnose → Implement → Verify → Regression Check → Finalize.
- Added severity (P0–P3) and confidence (High/Medium/Low) guidance for proactive fixes.
- Promoted the user-facing content gate and scroll-justification rule to core constraints.
- Added verification guidance for console errors, overflow, keyboard/focus, layout shift, reduced motion, zoom, and browser navigation when tooling permits.
- Added mobile platform behavior, internationalization, user preferences, and browser-history guidance.
- Condensed accepted-state / no-negative-echo finalization into one core rule plus a dedicated reference.

### Added

- README with project positioning and usage model.
- MIT License.
- Six focused reference documents.
