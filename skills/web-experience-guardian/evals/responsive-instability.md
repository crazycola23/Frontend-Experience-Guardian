# Eval: Responsive Instability

## Fixture

A Vue page uses Tailwind `md:` at 768px, a composable with `isMobile = width < 800`, a ResizeObserver that updates card columns, and `transition-all` on sidebar/main containers.

## Task

“Fix the layout shaking when the browser is resized.”

## Failure patterns

- adds debounce without diagnosing the feedback loop;
- keeps competing breakpoint thresholds;
- animates width/margin while resizing;
- keys components by viewport mode and remounts them.

## Guardian-positive behavior

- identifies conflicting responsive sources;
- moves ordinary layout behavior to coherent CSS rules;
- removes or narrows unnecessary reactive geometry logic;
- targets transitions instead of `transition-all`;
- verifies just below/at/above important breakpoints.
