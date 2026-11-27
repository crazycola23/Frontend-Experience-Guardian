# Eval: Unnecessary Scroll

## Fixture

A dashboard layout uses:

```css
.workspace { height: calc(100vh - 64px); overflow-y: auto; }
.panel { max-height: 520px; overflow-y: auto; }
.table-wrap { max-height: 360px; overflow: auto; }
```

The content would comfortably fit through natural page layout at common desktop sizes.

## Task

“Make this dashboard layout more comfortable and responsive.”

## Failure patterns

- preserves all nested scrolling because it technically works;
- hides scrollbars visually without changing architecture;
- compresses typography/spacing just to fit one viewport;
- creates new fixed heights on mobile.

## Guardian-positive behavior

- treats each independent scroll region as a design decision;
- removes artificial height constraints when not needed;
- prefers natural page scrolling;
- retains local horizontal scrolling only for intrinsically wide table content;
- verifies mobile and desktop behavior.
