# Accessibility, Preferences, and Internationalization

Use this reference when forms, typography, motion, localization, mobile interaction, or accessibility are material to the task.

## Keyboard and focus

Core workflows should remain usable without a pointer where the product type reasonably requires keyboard access.

Keep focus visible. Do not remove outlines without an accessible focus-visible replacement.

When dialogs, drawers, menus, and route changes occur, verify focus moves and returns sensibly.

## Semantics and labels

Prefer native semantic controls where possible. Inputs need understandable labels. Icon-only controls need accessible names. Status should not rely on color alone.

Essential actions must not be available only on hover.

## Contrast and readability

Use WCAG-informed targets. Common targets are 4.5:1 for normal text and 3:1 for large text, while respecting the applicable standard and component context.

Frequently missed states:

- muted/helper text;
- placeholders;
- disabled states;
- table metadata;
- inactive navigation;
- badges;
- tooltip content;
- chart labels;
- dark themes.

Minimal styling must not become unreadable styling.

## User preferences

When relevant, respect:

- `prefers-reduced-motion`;
- system font scaling;
- browser zoom;
- high-contrast/forced-colors behavior when supported by the product;
- light/dark/system preferences.

Motion should not be necessary to understand state.

For substantial UI changes, 200% browser zoom is a useful practical check when tooling permits.

## Touch

Keep important touch targets reasonably sized and separated. Do not assume hover exists on touch devices.

## Internationalization

Do not design only for the current English/Chinese string length.

Expect text expansion. Avoid fixed widths that only fit one locale. Use flexible wrapping/truncation intentionally and ensure truncation does not hide essential meaning.

When the product supports localization, respect locale-aware date, number, percentage, and currency formatting.

If RTL support is in scope, avoid physical left/right assumptions where logical properties or direction-aware layout should be used.

Test mixed content and longer labels in high-risk areas such as buttons, tabs, navigation, tables, dialogs, and form labels.
