# Finalization: Deliver the Accepted State

This reference adapts a no-negative-echo principle for frontend engineering: rejected session-only alternatives are control information, not the final product identity.

## Build final surfaces from the result

After revisions, derive final names, comments, documentation, commit messages, PR titles/descriptions, and handoff text from:

- the accepted implementation;
- the actual final diff;
- verified final behavior.

Do not rewrite rejected wording token-by-token. Regenerate high-salience surfaces from the final state.

## Avoid rejected-history residue

Do not leave task-owned names such as:

- NewSidebar / OldSidebar;
- SidebarV2;
- BetterDashboard / FinalDashboard;
- FixedTheme;
- NoScrollLayout;
- ImprovedTable.

Prefer current-purpose names such as Sidebar, Dashboard, PageContainer, DataTable, SettingsLayout, or ThemeSwitcher.

Do not preserve abandoned approaches through comments like “old implementation”, “user did not like this”, “removed scroll version”, or “temporary new design”. Comments should explain current invariants, constraints, compatibility requirements, or non-obvious behavior.

## Cleanup

Inspect task-owned changes for:

- unused CSS/classes/components;
- commented-out alternatives;
- debug output;
- temporary feature flags;
- duplicate tokens;
- abandoned variants;
- temporary labels;
- experimental files;
- fake production data added during implementation.

Do not delete unrelated user changes or required tests, diagnostics, snapshots, API names, migration facts, or audit history.

## Commit and PR language

Prefer positive current-state language:

- `fix(ui): stabilize responsive workspace layout`
- `refactor(ui): unify theme-aware surfaces`
- `feat(ui): streamline record actions`

Avoid session-history framing such as “remove ugly layout”, “fix rejected version”, “try sidebar again”, or “replace bad attempt” unless the historical change is materially required to understand a real baseline transition.

PR summaries should explain:

- what now works;
- what became easier or more stable;
- relevant architecture changes;
- what was actually verified.

## Preserve necessary history

Do not hide facts required for safety, security, compatibility, migration, audit, testing, API contracts, or a user-requested comparison.

Final-state orientation is not permission to falsify history.

## Final read-back

After tools or external systems create user-facing delivery surfaces, read back the actual result when possible and re-check names, comments, commit/PR text, and handoff for stale rejected framing.
