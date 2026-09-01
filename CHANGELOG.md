# Changelog

All notable changes to Frontend Experience Guardian are documented here.

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
