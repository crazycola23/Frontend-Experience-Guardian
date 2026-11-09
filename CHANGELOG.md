# Changelog

All notable changes to Frontend Experience Guardian are documented here.

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
- Five benchmark-style eval scenarios.

## 0.1.0 — 2026-08-24

- Initial single-file Frontend Experience Guardian Skill.
