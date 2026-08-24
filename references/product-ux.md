# Product UX and Task Efficiency

Use this reference for workflows, navigation, tables, forms, settings, search/filter, dashboards, quick actions, and learning-cost reduction.

## Start with the task

Identify primary, secondary, advanced, dangerous, high-frequency, and high-friction tasks.

Prioritize by:

`Frequency × Friction × User Impact`

Optimize total interaction cost, not raw click count. Count navigation, waiting, repeated input, repeated search, context rebuilding, decision complexity, and error risk.

## Action hierarchy

Classify actions as Primary, Secondary, Utility, Rare, or Dangerous.

Avoid many equally prominent actions. Put equivalent actions in predictable locations across similar pages to build muscle memory.

Dangerous actions should be protected but should not dominate normal work.

## Preserve context

When users move List → Detail → Back or open/close quick editors, preserve search, filters, sort, pagination, selection, scroll position, and view mode when practical.

Browser back/forward should behave sensibly rather than resetting the work context unnecessarily.

## Search and filters

Users should understand what is being searched, which filters are active, why results look the way they do, and how to reset the state.

Keep important active filters visible rather than hiding all state inside a closed filter panel.

## Tables and lists

Inspect column priority, width, density, row actions, bulk actions, sort, filters, search, pagination, selection, and responsive overflow.

Avoid a row containing many equally prominent buttons. Usually expose one or two frequent actions and place lower-frequency actions in More.

If users repeatedly enter a detail page only to inspect status, copy a value, toggle one field, or read brief metadata, consider Quick View, Sheet, Popover, Inline Edit, or Row Action.

## Interaction-container defaults

- Popover: lightweight choice or supporting information.
- Dropdown: action menu.
- Dialog: short focused task or high-value confirmation.
- Sheet/Drawer: contextual quick view or medium-complexity work.
- Full page: deep workflow, long form, complex information.

These are defaults, not universal laws.

## Forms

Order fields by user thinking rather than database schema. Group Basic Information, Business Configuration, Advanced Settings, or equivalent domain sections when helpful.

Use sensible defaults, reduce unnecessary required fields, validate inline, preserve user input after recoverable failures, and avoid asking for information the system already knows.

Recognition is generally better than recall: searchable selection is preferable to memorizing IDs or internal codes.

## Progressive disclosure

Keep common operations visible. Put advanced/rare controls behind secondary UI. The goal is simple for beginners and efficient for experienced users.

Do not use tooltips as the only way to understand core actions.

## Feedback and recovery

A user action should acknowledge input promptly. Use button loading, disabled state, inline status, optimistic state, toast, or progress as appropriate.

Editing screens should make unchanged/unsaved/saving/saved/failed understandable.

Errors should say what happened, why when known, and what the user can do next.

Low-risk reversible actions may benefit from Undo rather than repeated confirmation. High-risk irreversible actions still need explicit safeguards.

## Navigation

Organize around user mental models and actual workflows, not internal code/database organization when those differ.

Use global navigation for major product areas and local tabs/sub-navigation for the current area. Avoid excessive menu depth.

## Dashboard

Metrics and charts should support decisions. Do not add analytics because “dashboards have charts.” Ask what action follows from each piece of information.
