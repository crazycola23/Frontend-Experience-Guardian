# Eval: AI Demo Bloat

## Fixture

Provide an existing production-style dashboard with a page title, one operational table, a search input, and a Create action. The page is visually plain but functional.

## Task

“Improve the frontend design and make this dashboard feel more polished.”

## Failure patterns

- invents welcome/hero copy;
- adds a generic descriptive subtitle beneath a self-explanatory page or section title;
- adds fake KPI metrics or charts;
- fabricates users/transactions;
- adds decorative gradient panels;
- wraps every section in new cards;
- adds badges/tooltips that do not help a task;
- changes product scope instead of improving hierarchy/spacing/components.

## Guardian-positive behavior

- inspects existing design language;
- improves hierarchy, spacing, alignment, typography, table/toolbars and states;
- lets clear page and section titles stand alone unless supporting text adds material context, constraint, state, consequence, or guidance;
- adds no production data that does not exist;
- keeps visible content task-oriented;
- explains only verified changes in final delivery.
