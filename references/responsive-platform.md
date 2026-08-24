# Responsive and Platform Behavior

Use this reference for resize issues, breakpoint design, mobile composition, viewport bugs, browser navigation, safe areas, or focus/scroll restoration.

## Reflow before rerender

For ordinary layout prefer CSS Grid, Flexbox, media queries, container queries, `minmax()`, `clamp()`, `auto-fit`, and `auto-fill`.

Audit JavaScript-driven layout state such as `window.innerWidth`, resize listeners, ResizeObserver, `isMobile`, and manual column calculations when CSS could express the same behavior more stably.

Complex editors, canvases, virtualized grids, split panes, and visualization workspaces may legitimately require JavaScript geometry.

## Breakpoint coherence

Avoid different breakpoints in Tailwind, custom CSS, JS state, and container queries unless intentionally coordinated.

Test representative sizes appropriate to the product. A useful generic set is 320, 375, 430, 768, 1024, 1280, 1440, and 1920, plus a pixel on either side of important breakpoints.

Resize should not flicker, remount, replay entrance animation, or oscillate between layouts.

## Mobile reality

Mobile is not compressed desktop.

Account for:

- touch instead of hover;
- adequate touch targets;
- safe-area insets;
- mobile browser chrome;
- dynamic viewport sizing (`dvh`/appropriate fallbacks instead of blindly relying on classic `100vh`);
- on-screen keyboard reducing available space;
- sticky/fixed actions remaining reachable;
- wide tables needing a deliberate mobile strategy;
- filters/toolbars often needing regrouping or a Sheet/Drawer.

Do not trap primary actions behind the mobile keyboard.

## Horizontal overflow

Page-level horizontal scrolling is usually a defect. Audit flex/grid children for `min-width: 0`, long strings, toolbars, charts, tabs, tables, and code.

Intrinsic wide content can own a local horizontal scroll region.

## Browser history and restoration

When navigation or overlays affect URL/history, verify browser Back and Forward produce expected results.

Preserve or intentionally restore scroll/focus state when returning to a list or closing a contextual workflow.

Do not surprise users by resetting search/filter/page state on ordinary navigation unless product semantics require it.

## Autofill and native behavior

Do not break browser password managers, form autofill, copy/paste, text selection, native validation semantics, or normal scrolling merely to create custom visuals.

Prefer progressive enhancement over replacing native behavior without a meaningful UX benefit.
