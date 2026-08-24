# Layout Stability

Use this reference for loading shifts, route transitions, resizing, sidebar movement, theme switching, chart/media shifts, or unexplained UI shaking.

## Preserve geometry

The application shell should remain stable where the architecture permits:

`App → Sidebar / Header / Main → Router Content`

Normal route changes should not rebuild global shell geometry without reason.

## Loading

Loading is the final interface before data arrives.

Prefer stable page identity, toolbars, card grids, table containers, chart areas, and action regions. Skeletons should approximate final geometry rather than replace a large page with a tiny spinner.

Distinguish:

- **Initial loading:** skeletons may be appropriate.
- **Refreshing:** preserve existing content when safe; show a subtle refresh state while new data arrives.

Also inspect Loading → Empty, Loading → Error, Error → Retry, and Loaded → Refreshing.

## Avoid presentation-driven remounts

Audit keys and conditions such as `key=loading`, `key=theme`, `key=isMobile`, or route keys that recreate large trees unnecessarily.

Update content inside stable component trees when possible.

## Scrollbar geometry

Different page heights can shift the whole viewport when the browser scrollbar appears/disappears. When appropriate consider `scrollbar-gutter: stable` or an equivalent project-compatible strategy.

## Layout transitions

Audit `transition-all` and `transition: all`. Width, height, margin, padding, top, left, and grid geometry should not animate accidentally.

Use targeted transitions for color, background, border, shadow, opacity, or deliberate transforms.

Motion must not hide structural instability.

## Sidebar

Use one coherent sizing model for expanded/collapsed states. Avoid independent simultaneous calculations across sidebar width, main margin, main width, padding, and transforms unless the architecture requires them.

## Theme geometry

Theme changes should normally change color/surface/ring/shadow/chart/status appearance, not width, height, spacing, font metrics, border width, sidebar width, or layout.

## Media and charts

Reserve expected geometry with width/height/aspect-ratio/stable containers. Images and charts should not arrive and push surrounding content around.

## Responsive stability

Resize should reflow, not oscillate. Investigate competing CSS/JS breakpoints and ResizeObserver feedback loops before adding debounce.

## Verification targets

When tooling permits:

- compare loading and loaded screenshots;
- inspect route changes for lateral shift;
- drag viewport through breakpoints;
- toggle sidebar/theme repeatedly;
- verify no page-level horizontal overflow;
- check console for resize/observer errors;
- inspect reduced-motion behavior if animation changed.
