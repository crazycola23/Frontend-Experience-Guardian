# Layout Stability

Use this reference for loading shifts, route transitions, resizing, sidebar movement, theme switching, chart/media shifts, pagination/filter column jitter, non-fullscreen window clipping, or unexplained UI shaking.

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

## Table column stability across pagination & filtering

With default `table-layout: auto`, browsers recalculate column widths from the currently rendered `<tbody>` rows. When a user switches pages or filter tabs—and one page happens to contain extra inline badges (`缺件`, `! 21天后到期`) or variable action button counts (`登记归还 + 查看档案` vs `查看档案`)—every column shifts horizontally across pages.

- **Lock column geometry with `table-layout: fixed` and explicit `<colgroup>` proportions:**
  - Set `table-layout: fixed; width: 100%;` on data tables.
  - Define an explicit `<colgroup>` covering every column (either well-calibrated percentages totaling `100%` or fixed pixel widths paired with fluid description columns), ensuring the action column is sized for the maximum button combination.
  - Apply `white-space: nowrap; overflow: hidden; text-overflow: ellipsis;` on `th, td` (with `overflow: visible` on the action column) so variable cell content never alters column X-coordinates across Page 1, Page 2, or filter states.

## Non-fullscreen & restored window shell contraction

In CSS Grid or Flexbox app shells (`overflow: hidden` on the outer shell), `1fr` tracks default to `minmax(auto, 1fr)`. When the window is not maximized (e.g., `1120×720` or `1024px–1280px`), wide inner tables or split panels prevent the `1fr` track from shrinking below `min-content`, pushing the right edge and bottom-right corner (such as the rightmost `操作` column or bottom-right pagination controls) outside the viewport where `overflow: hidden` clips them.

- **Enforce `minmax(0, 1fr)` and `min-width: 0; min-height: 0` across the shell hierarchy:**
  - Define shell grids as `grid-template-columns: <sidebar> minmax(0, 1fr); grid-template-rows: <topbar> minmax(0, 1fr);`.
  - Apply `min-width: 0; min-height: 0; width: 100%;` to the main workspace container, page wrapper, sticky header/footer bars, and internal scroll body so they always contract to the actual window bounds.
  - Add responsive breakpoints (`@media (max-width: 1240px)`) for multi-column dashboard splits so side rails stack cleanly instead of overflowing horizontally.

## Verification targets

When tooling permits:

- compare loading and loaded screenshots;
- inspect route changes for lateral shift;
- compare table column X-coordinates across Page 1, Page 2, and Page 3 (`0px` shift);
- test non-fullscreen window sizes (e.g. `1120×720`) to verify bottom-right pagination and rightmost action buttons remain 100% visible;
- drag viewport through breakpoints;
- toggle sidebar/theme repeatedly;
- verify no page-level horizontal overflow;
- check console for resize/observer errors;
- inspect reduced-motion behavior if animation changed.
