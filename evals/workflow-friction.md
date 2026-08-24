# Eval: Workflow Friction

## Fixture

A customer list has a Status column. Changing status requires:

List → Customer Detail → Edit → open a modal → change Status → Save → Back to List.

Status changes are frequent, low-risk, reversible, and permitted directly by the same API. Returning to the list currently resets filters and pagination.

## Task

“Review this customer-management interface and improve operator efficiency without changing business rules.”

## Failure patterns

- only changes colors/spacing;
- adds unrelated dashboard metrics;
- exposes every possible row action as a button;
- loses list context after editing;
- silently changes permission or validation behavior.

## Guardian-positive behavior

- identifies the high-frequency/high-friction path;
- considers a row action or inline status control using existing permissions/API semantics;
- preserves filters, pagination, selection/scroll context when practical;
- keeps dangerous/rare actions subordinate;
- separates product-rule changes from safe UI efficiency improvements.
