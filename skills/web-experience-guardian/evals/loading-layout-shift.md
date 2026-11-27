# Eval: Loading Layout Shift

## Fixture

A data page implements:

```vue
<Spinner v-if="loading" />
<DashboardContent v-else :data="data" />
```

`DashboardContent` contains a page header, four KPI cards, a 320px chart, and a table. Refreshing existing data sets `loading = true` again.

## Task

“Fix the page transition so loading feels smoother.”

## Failure patterns

- adds fade/scale animation but keeps the geometry jump;
- replaces spinner with an unrelated skeleton layout;
- returns to full skeleton on every refresh;
- remounts content through `:key="loading"`.

## Guardian-positive behavior

- keeps stable page/content geometry;
- matches skeleton structure to loaded layout;
- separates initial loading from refreshing;
- preserves existing content during refresh when safe;
- uses motion only after structural stability is achieved.
