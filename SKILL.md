---
name: frontend-experience-guardian
description: >
  Proactive frontend product-design and UX quality guardian for user-facing
  interfaces. Use when creating, modifying, reviewing, debugging, or
  refactoring frontend pages and shared UI. Detect and correct unnecessary
  scrolling, layout instability, weak hierarchy, poor readability, theme
  leakage, responsive friction, inefficient workflows, excessive UI content,
  inconsistent interaction patterns, and residual experimental design decisions.
  Optimize for stability, clarity, efficiency, learnability, consistency,
  responsiveness, accessibility, and restrained visual quality while preserving
  business behavior.
---

# Frontend Experience Guardian

## Mission

Treat every user-facing frontend task as both an engineering task and a product-design task.

A frontend implementation is not complete merely because:

- it compiles;
- it renders;
- the API works;
- the requested button exists;
- the screenshot looks attractive.

It is complete only when the interface is also:

- stable;
- readable;
- understandable;
- efficient;
- predictable;
- responsive;
- consistent;
- accessible;
- restrained;
- easy to learn.

Develop sensitivity to problems users often feel before they can clearly describe them.

Continuously ask:

> Does anything here feel harder, noisier, less stable, more confusing, or more cumbersome than necessary?

## 1. Priority Order

Resolve concerns in this order:

1. Functional correctness
2. Layout stability
3. Readability
4. Task clarity
5. Operational efficiency
6. Interaction predictability
7. Cross-page consistency
8. Responsive quality
9. Accessibility
10. Visual polish

Use these principles:

> Stable before animated.  
> Clear before clever.  
> Efficient before decorative.  
> Consistent before novel.  
> Beautiful after usable.

Never trade stability or usability for a prettier screenshot.

## 2. Inspect the Rendered Product, Not Only the Code

When a runnable preview, browser, screenshot environment, or visual inspection mechanism is available, inspect the actual rendered interface.

Do not make strong visual-quality claims from source code alone when the rendered result can be inspected.

For substantial interface work, examine representative states and viewport sizes.

At minimum consider:

- Desktop
- Tablet
- Mobile

and important state transitions such as:

- Loading → Loaded
- Loaded → Refreshing
- Loaded → Empty
- Error → Retry
- Route A → Route B
- Light → Dark
- Theme A → Theme B
- Expanded Sidebar → Collapsed Sidebar

A technically reasonable CSS rule may still produce a poor real interface.

Rendered behavior is the final authority.

## 3. Proactive UI Sensitivity

Do not wait for the user to identify every defect.

When touching a page, actively inspect the relevant interface for:

- awkward spacing;
- wasted space;
- overcrowding;
- unnecessary scrolling;
- nested scrolling;
- horizontal overflow;
- weak hierarchy;
- poor contrast;
- misalignment;
- inconsistent page padding;
- inconsistent content width;
- unstable loading states;
- route-change jumping;
- resize shaking;
- breakpoint instability;
- sidebar-induced movement;
- duplicate information;
- too many cards;
- too many borders;
- too many badges;
- too many equally prominent buttons;
- unclear labels;
- hidden important actions;
- unnecessary navigation;
- excessive confirmations;
- context loss;
- theme leakage;
- legacy hard-coded styles;
- unnecessary animation;
- unnecessary UI copy;
- debug information exposed to users.

High-confidence, low-risk interface defects inside the task's affected surface may be corrected proactively.

Do not expand the task into unrelated product redesign.

## 4. User-Facing Content Gate

This is a hard rule.

Do not place content into the user interface merely because there is available space or because additional explanation makes the implementation appear more complete.

Before adding any visible text, heading, description, helper copy, badge, banner, alert, tooltip, status, card, metric, section, technical value, example, placeholder, or instruction, ask:

### A. Is it needed?

Does the user need this information to:

- understand the current state;
- make a decision;
- complete a task;
- avoid a mistake;
- recover from a problem?

If not, omit it.

### B. Is it user-facing domain information?

Prefer:

- business terminology;
- user-understandable states;
- actual data;
- task-oriented labels.

Avoid exposing implementation terminology.

### C. Is it already communicated elsewhere?

Do not repeat the same idea through Page Title + Section Title + Card Title + Description + Banner unless each layer adds distinct meaning.

### D. Could layout solve the problem instead?

If explanatory text is only necessary because the interface is confusing, first improve:

- hierarchy;
- grouping;
- labeling;
- placement;
- spacing;
- interaction design.

Do not compensate for poor design by writing paragraphs of instructions.

### E. Does it increase cognitive load?

Every additional visible element consumes attention.

If removing it leaves the workflow equally understandable, remove it.

## 5. Never Dump Agent/Internal Information Into the UI

Do not expose agent-working information to end users.

Unless explicitly part of the product requirement, never add visible UI containing:

- debug information;
- implementation notes;
- developer explanations;
- internal reasoning;
- temporary states;
- AI commentary;
- migration notes;
- TODOs;
- test labels;
- component names;
- CSS token names;
- backend enum names;
- database identifiers;
- raw API values;
- technical stack information;
- internal timestamps;
- temporary version markers;
- experimental flags.

Examples of inappropriate user-facing additions:

- Debug Mode
- Current Component: UserTable
- Theme Token: --primary
- Loaded from API v2
- Temporary implementation
- New layout
- Fixed version
- Fallback state
- Vue watcher active

Such information belongs in developer tooling, logs, tests, documentation, or code where appropriate — not normal product UI.

## 6. Do Not Invent Product Copy Unnecessarily

Do not generate marketing-style or explanatory copy merely to fill space.

Avoid unsolicited text such as:

- Welcome to your powerful new dashboard
- Everything you need, all in one place
- Here's what you can do
- Manage your workflow effortlessly

unless the product actually requires onboarding or promotional messaging.

Operational interfaces should prioritize useful information over decorative copy.

## 7. No Fake Production Data

Do not introduce invented users, metrics, transactions, statuses, customer names, charts, or operational records into production-facing UI unless:

- the task explicitly requests mock/demo data;
- the environment is clearly a demo/storybook/design-system environment;
- fixtures are required for tests.

Do not make an empty production interface appear complete by fabricating business data.

Use appropriate Empty States instead.

## 8. UI Surface Budget

Treat every new visible surface as having a cost.

Before creating another Card, Panel, Banner, Badge, Divider, Toolbar, Section, Popover, Tooltip, Button, or Icon, ask:

> What unique job does this element perform?

If the answer is merely "looks nicer", "fills space", or "separates things that are already clear", do not add it.

The interface should contain the minimum structure necessary for clarity and efficient operation.

Not the minimum amount of design. The minimum necessary design structure.

## 9. Inspect the Whole Composition

Evaluate pages as complete compositions.

Use this mental model:

Application
├── Global Navigation
├── Header
└── Main
    ├── Page Identity
    ├── Primary Action
    ├── Local Navigation
    ├── Toolbar
    ├── Primary Content
    ├── Secondary Content
    └── Feedback

Ask:

- What is the first visual focal point?
- Should it be?
- Can the user immediately tell where they are?
- Can they tell what the page is for?
- Can they identify the primary action?
- Is the most important information available early?
- Are related elements grouped?
- Are unrelated things competing visually?
- Is operational content pushed downward by decoration?

Do not optimize components in isolation while damaging the page-level hierarchy.

## 10. Scrollbars Trigger Design Review

Every newly introduced internal scrollbar is a design-review trigger.

A scrollbar is not automatically wrong. But it must have a reason.

Default preference:

> If the content can reasonably be displayed naturally, display it naturally.

Before introducing `overflow-y: auto`, `overflow: scroll`, `max-height`, or fixed heights, ask:

- Can the container grow?
- Can an unnecessary fixed height be removed?
- Can padding be reduced without harming readability?
- Can the layout use width more effectively?
- Can controls wrap?
- Can information be regrouped?
- Can the page naturally scroll instead?
- Does this region genuinely require independent navigation?

If there is no meaningful reason for independent scrolling, do not create it.

## 11. Preferred Scroll Hierarchy

Prefer:

1. Natural document/page scrolling
2. One intentional regional scrolling area
3. Nested scrolling only when structurally necessary

Treat this as suspicious:

Page Scroll
└── Panel Scroll
    └── Table Scroll
        └── Inner List Scroll

Nested scrolling increases:

- trackpad friction;
- mouse-wheel ambiguity;
- touch friction;
- focus-navigation complexity;
- layout complexity;
- learning cost.

## 12. Legitimate Independent Scroll Regions

Independent scrolling can be appropriate for:

- large data grids;
- virtualized lists;
- chat histories;
- log viewers;
- terminals;
- code editors;
- long command palettes;
- bounded quick-view panels;
- large dropdown menus;
- timeline workspaces.

Even then verify:

- the region truly needs bounded independent navigation;
- users can tell what scrolls;
- nested scroll levels are minimized;
- resizing does not trap or hide important actions.

## 13. Do Not Force Everything Into One Screen

Avoiding unnecessary scrollbars does not mean forcing everything above the fold.

Never solve scrolling by:

- shrinking fonts;
- reducing touch targets;
- removing useful information;
- compressing every gap;
- making dense unreadable forms;
- forcing the entire application into `100vh`.

The goal is:

> Avoid artificial scrolling while using available space intelligently.

Not:

> Eliminate all scrolling.

## 14. Avoid Arbitrary Fixed Heights

Treat fixed `height`, `max-height`, and `overflow-y: auto` as suspicious when applied without clear interaction reasons, especially for:

- Cards;
- Settings sections;
- Forms;
- Tables;
- Dashboards;
- Dialogs;
- Drawers;
- Sheets;
- Side panels.

Natural content height is usually preferable.

## 15. Prevent Page-Level Horizontal Scrolling

The application page itself should rarely scroll horizontally.

Audit:

- Main;
- Cards;
- Tables;
- Charts;
- Tabs;
- Toolbars;
- Breadcrumbs;
- Long strings;
- Code;
- Forms.

Use appropriate techniques such as:

- `min-width: 0`;
- `max-width: 100%`;
- `flex-wrap`;
- `overflow-wrap`;
- `break-words`;
- responsive grids.

For intrinsically wide data such as large tables, use local horizontal scrolling.

Do not make the whole application wider than the viewport.

## 16. Stable App Shell

Prefer a persistent structure:

App
├── Sidebar
├── Header
└── Main
    └── Router Content

Page changes should normally replace only router content.

Avoid rebuilding Sidebar, Header, Global background, or Main container during normal navigation.

Navigation should feel like:

> same product → different workspace

not:

> old product disappears → blank state → new product appears

## 17. Loading Is Not Another Page

Use this principle:

> Loading is the final interface before its data has arrived.

Keep stable:

- Page Header;
- Toolbar;
- Grid;
- Card geometry;
- Table container;
- Chart container;
- Pagination area.

Skeletons should occupy approximately the final geometry.

Avoid tiny spinner → large interface appears.

## 18. Initial Loading and Refreshing Are Different

Initial load may use Skeletons.

When existing content is refreshing, keep the current content visible whenever safe and appropriate.

Prefer:

Current content + subtle refreshing state → Updated content

over:

Current content → Entire page disappears → Skeleton → Updated content

Preserve context.

## 19. Empty, Error, and Retry States Are Part of the Layout

Audit transitions:

- Loading → Loaded
- Loading → Empty
- Loading → Error
- Loaded → Refreshing
- Error → Retry

Empty or Error states should not make the application unexpectedly collapse.

They should be intentionally composed and tell users what they can do next when applicable.

## 20. Avoid Layout Remounts

Audit presentation-driven keys and structural conditions such as:

- `:key="loading"`
- `:key="theme"`
- `:key="isMobile"`
- `:key="width"`
- `:key="mode"`

Do not remount large component trees merely because presentation state changed.

Prefer updating content inside stable component geometry.

## 21. Responsive Layout Should Reflow, Not Shake

Test representative widths such as:

- 320
- 375
- 430
- 768
- 1024
- 1280
- 1440
- 1920

and breakpoint boundaries such as:

- 767 / 768 / 769
- 1023 / 1024 / 1025
- 1279 / 1280 / 1281

The interface should naturally reflow.

It should not:

- oscillate;
- flicker;
- remount;
- shift sideways;
- replay animations;
- continually recalculate width;
- bounce between desktop and mobile states.

## 22. Prefer CSS-Driven Responsiveness

For ordinary layout behavior prefer:

- CSS Grid;
- Flexbox;
- Media Queries;
- Container Queries;
- `minmax()`;
- `clamp()`;
- `auto-fit`;
- `auto-fill`.

Treat as audit targets:

- `window.innerWidth`;
- resize event listeners;
- `ResizeObserver`;
- `useWindowSize`;
- manual `isMobile`;
- manual column calculations.

If CSS can solve it cleanly, avoid reactive JavaScript layout state.

## 23. Avoid Conflicting Breakpoint Systems

Do not let Tailwind breakpoints, custom CSS breakpoints, JavaScript breakpoints, and container-query breakpoints disagree.

Example problem:

- CSS mobile < 768
- JS mobile < 800

This creates unstable intermediate states.

Use one coherent responsive strategy.

## 24. Detect Resize Feedback Loops

Investigate:

ResizeObserver → state update → element resize → ResizeObserver → state update

Do not reach for debounce as the first fix.

Correct the feedback loop first.

## 25. Stabilize Browser Scrollbar Geometry

Different route heights should not make the entire application move horizontally.

When appropriate evaluate:

```css
html {
  scrollbar-gutter: stable;
}
```

Treat unexplained route-to-route horizontal movement as a defect.

## 26. Avoid `transition-all`

Audit:

- `transition-all`;
- `transition: all`.

particularly around layout components.

Do not unintentionally animate:

- width;
- height;
- padding;
- margin;
- grid geometry;
- top;
- left.

Prefer transitions targeted to:

- background-color;
- color;
- border-color;
- box-shadow;
- opacity.

Use transforms deliberately.

## 27. Motion Cannot Hide Structural Problems

Do not fix layout instability with:

- fade;
- scale;
- slide;
- translate;
- delayed reveal.

First make the interface structurally stable.

Then use subtle motion only when it communicates state or improves comprehension.

## 28. Reserve Media Geometry

For avatars, logos, images, charts, thumbnails, covers, and media, reserve expected space through:

- width;
- height;
- aspect-ratio;
- stable containers.

Assets should not arrive and push the page around.

## 29. Theme Controls Appearance, Not Geometry

Themes may change:

- background;
- surface;
- foreground;
- primary;
- secondary;
- accent;
- border color;
- focus color;
- semantic status colors;
- chart palette;
- shadow tone.

Themes should not normally change:

- width;
- height;
- padding;
- margin;
- gap;
- grid;
- font size;
- line height;
- sidebar width;
- header height;
- border width;
- layout.

Theme switching should not produce Layout Shift.

## 30. Semantic Design Tokens

Prefer semantic tokens:

- background / foreground;
- card / card-foreground;
- popover / popover-foreground;
- primary / primary-foreground;
- secondary / secondary-foreground;
- muted / muted-foreground;
- accent / accent-foreground;
- border / input / ring;
- success / warning / info / destructive;
- chart-1 through chart-5.

Business components should not need theme-specific conditional logic.

## 31. Theme Leakage Audit

Search for possible UI-theme leakage:

- `bg-white`;
- `text-white`;
- `text-black`;
- gray/zinc/slate/neutral utility colors;
- hex colors;
- `rgb(...)` / `rgba(...)` / `hsl(...)`;
- inline color styles;
- `!important`;
- manual dark overrides;
- legacy scoped styles.

Classify before changing:

- UI theme color;
- legitimate business / brand / semantic color.

Do not mechanically replace real business colors.

## 32. Readability Is a Hard Requirement

Do not accept weak text contrast because it looks subtle.

Use WCAG-informed targets approximately:

- Normal text >= 4.5:1
- Large text >= 3:1

Pay special attention to:

- muted text;
- placeholder;
- disabled text;
- metadata;
- table secondary text;
- sidebar inactive items;
- badges;
- tabs;
- tooltips;
- chart labels;
- helper text;
- footnotes;
- empty states.

Minimalism must not reduce legibility.

## 33. Typography Is Information Architecture

Maintain predictable semantic levels such as:

- Page Title;
- Section Title;
- Card Title;
- Body;
- Secondary;
- Muted;
- Caption;
- Label;
- Helper;
- Disabled.

Avoid arbitrary typography differences between pages.

Typography should help users understand structure before reading everything.

## 34. Identify User Tasks Before Optimizing UI

Understand:

- Primary Tasks;
- Secondary Tasks;
- Advanced Tasks;
- Dangerous Tasks;
- High-frequency Tasks;
- High-friction Tasks.

Prioritize using:

> Frequency × Friction × User Impact

Do not spend disproportionate effort polishing rare screens while daily workflows remain cumbersome.

## 35. Action Hierarchy

Classify actions:

- Primary;
- Secondary;
- Utility;
- Rare;
- Dangerous.

Do not make many actions equally visually prominent.

Equivalent actions should appear in predictable places across similar pages.

Predictability builds muscle memory.

## 36. Optimize Total Interaction Cost

Do not optimize only raw click count.

Consider:

- clicks;
- navigation;
- waiting;
- repeated input;
- repeated search;
- context reconstruction;
- decision complexity;
- error risk.

For frequent, simple, safe, reversible operations consider:

- inline action;
- quick action;
- row action;
- quick view;
- popover;
- sheet;
- keyboard accelerator;
- bulk action.

Do not expose excessive controls simply to save one click.

## 37. Preserve Working Context

Where practical, preserve:

- search;
- filters;
- sorting;
- pagination;
- selection;
- scroll position;
- view mode.

when moving List → Detail → Back or List → Quick Edit → Close.

Do not make users reconstruct their previous working state.

## 38. Search and Filter UX

Users should quickly understand:

- what is being searched;
- which filters are active;
- why the current result set looks this way;
- how to reset it.

Keep applied filters visible when helpful.

Do not hide important active state inside a closed filter panel.

## 39. Table Efficiency

For data-heavy interfaces inspect:

- column priority;
- column width;
- density;
- row actions;
- bulk actions;
- sorting;
- filters;
- search;
- pagination;
- selected state;
- responsive behavior.

Avoid filling every row with many buttons.

Prefer 1–2 high-frequency actions + More menu for secondary operations.

## 40. Do Not Force Tiny Actions Through Full Detail Pages

If users repeatedly enter Detail pages merely to:

- check status;
- copy a value;
- toggle a setting;
- change one small field;
- inspect short metadata;

consider Quick View, Sheet, Inline Edit, Popover, or Row Action.

Use full pages for genuinely deep tasks.

## 41. Use Interaction Containers Intentionally

Default guidance:

- Popover → lightweight choice or information
- Dropdown → action menu
- Dialog → short focused task or confirmation
- Sheet / Drawer → contextual quick view or medium-complexity task
- Full Page → deep task, long form, complex information

Do not put every workflow in a modal.

## 42. Form Design

Order fields by user thinking, not database structure.

Use logical sections where helpful:

- Basic Information;
- Business Configuration;
- Advanced Settings.

Prefer:

- fewer required fields;
- sensible defaults;
- inline validation;
- preserved input after failure;
- clear optional/required status.

Do not make users repeatedly provide information the system already knows.

## 43. Recognition Over Recall

Avoid requiring users to remember:

- IDs;
- codes;
- technical names;
- previous-screen values;
- hidden states.

when the interface can offer:

- search;
- selection;
- labels;
- recent items;
- preview;
- context.

Recognition reduces learning cost.

## 44. Progressive Disclosure

Keep common functionality visible.

Move rare or advanced complexity behind secondary UI.

Target:

> Simple for beginners, efficient for experienced users.

Do not remove advanced capability. Reveal it when needed.

## 45. Navigation Should Match User Mental Models

Audit:

- Sidebar grouping;
- menu order;
- menu depth;
- module naming;
- active state;
- local tabs;
- settings structure.

Organize according to real workflows rather than implementation architecture whenever possible.

High-frequency destinations should be easier to reach.

## 46. Global and Local Navigation Have Different Jobs

Use global navigation for major product areas.

Use Tabs, Sub-navigation, or Section navigation for the current area.

Do not overload the Sidebar with every destination.

## 47. Dashboards Should Enable Decisions

Do not add charts or KPI cards simply because dashboards commonly contain them.

For each important metric ask:

- What decision does this support?
- What action follows?

Prefer:

> Understand → Decide → Act

over decorative analytics.

## 48. Avoid Excessive Cardization

Do not automatically wrap every section in a Card.

Use Whitespace, Typography, Grid, Sections, and Dividers when sufficient.

Cards should represent real grouping or interaction surfaces.

Avoid Card inside Card inside Card without strong reason.

## 49. Reduce Visual Noise

Audit the amount of:

- Borders;
- Shadows;
- Badges;
- Buttons;
- Icons;
- Separators;
- Surface colors;
- Decorations.

The product should feel restrained but clear.

Not empty. Not noisy.

## 50. Operational Interfaces Should Use Space Efficiently

Do not blindly apply marketing-page spacing to operational software.

Avoid pushing useful content downward through:

- oversized titles;
- decorative hero areas;
- huge vertical gaps;
- repeated descriptions;
- oversized cards.

Desktop SaaS interfaces should use available horizontal space intelligently.

## 51. Mobile Is Not Compressed Desktop

At narrow widths reconsider composition.

Appropriate transformations may include:

- Sidebar → Drawer;
- Toolbar → wrapped/grouped controls;
- Filters → Sheet;
- Wide Table → local horizontal scroll;
- Cards → fewer columns;
- Tabs → horizontal tab rail;
- Actions → larger touch targets.

Do not simply shrink desktop UI.

## 52. Immediate Interaction Feedback

User actions must visibly acknowledge input.

Use appropriate:

- button loading;
- disabled state;
- inline status;
- optimistic update;
- toast;
- progress.

Avoid silent waiting that encourages duplicate clicks.

## 53. Save State Should Be Understandable

Editing interfaces should communicate:

- unchanged;
- unsaved;
- saving;
- saved;
- failed.

For simple low-risk preferences, consider immediate saving.

Do not force unnecessary Save workflows.

## 54. Prevent Errors Where Possible

Prefer:

- good defaults;
- disabled impossible choices;
- clear constraints;
- inline validation;
- specific warnings;
- reversible actions.

For low-risk reversible actions consider Action → Undo instead of repetitive confirmation dialogs.

High-risk destructive actions still require appropriate safeguards.

## 55. Actionable Error Messages

Errors should communicate:

- what happened;
- why, when known;
- what the user can do next.

Avoid generic messages when specific recovery guidance exists.

## 56. Empty States Teach Next Steps

Do not stop at "No data".

When applicable explain:

- what belongs here;
- why it is empty;
- what the user can do next.

Useful Empty States reduce onboarding cost.

## 57. Accessibility Is Product Quality

Audit:

- keyboard navigation;
- focus-visible;
- semantic controls;
- form labels;
- touch target size;
- contrast;
- disabled states;
- hover-only interactions;
- screen-reader meaning.

Core functionality must not depend entirely on hover.

Do not remove focus indicators for visual cleanliness.

## 58. Consistency Reduces Learning Cost

Similar operations should use similar:

- wording;
- placement;
- icons;
- components;
- behavior;
- feedback.

Especially:

- Create;
- Edit;
- Save;
- Cancel;
- Delete;
- Search;
- Filter;
- Sort;
- More.

Do not reinvent familiar patterns on every page.

## 59. Design-System Showcase

When appropriate, maintain a development-only Design System / UI QA page using real shared components.

It may cover:

- Design Tokens;
- Typography;
- Buttons;
- Cards;
- Forms;
- Tables;
- Badges;
- Alerts;
- Tabs;
- Dialogs;
- Dropdowns;
- Popovers;
- Tooltips;
- Sheets;
- Sidebar;
- Empty;
- Loading;
- Error;
- Charts.

And interaction patterns:

- Page Header;
- Toolbar;
- Filters;
- Search;
- Quick View;
- Table Actions;
- Bulk Actions;
- Form Actions;
- Delete Flow;
- Loading Flow.

Do not create fake production components solely for the showcase.

## 60. Review Every Relevant State

Inspect important components in:

- Default;
- Hover;
- Focus;
- Active;
- Selected;
- Disabled;
- Loading;
- Empty;
- Error;
- Refreshing.

Many defects exist outside the Default state.

## 61. Vue-Specific Guardrails

When the detected project is Vue, inspect:

- `v-if` replacing large layouts;
- `:key` causing unnecessary remount;
- Teleport and theme inheritance;
- reactive resize logic;
- watchers controlling geometry;
- duplicate responsive state;
- duplicate theme state;
- scoped styles overriding design tokens;
- route-component remount behavior.

Prefer stable component trees and CSS-driven layout when possible.

## 62. Fix Systems Before Symptoms

When the same defect appears repeatedly, first inspect shared infrastructure:

- Design Tokens;
- Global CSS;
- App Shell;
- Page Container;
- Shared Components;
- Shared Toolbar;
- Shared Table Shell;
- Shared Form Layout;
- Shared Loading Pattern;
- Shared Empty/Error State.

Fixing the system is preferable to dozens of page-specific overrides.

## 63. Do Not Over-Abstract

Consistency does not require every page to have the same composition.

Only abstract patterns that are genuinely repeated.

Shared components should support appropriate slots, variants, sizes, and responsive behavior.

The goal is one product design system, not one layout used everywhere.

## 64. Scope Discipline

Do not introduce unrelated product features while improving UI.

Do not invent:

- new analytics;
- new settings;
- new dashboards;
- new filters;
- new product workflows;
- new onboarding flows;
- new user-facing data.

unless justified by the requested task.

A UI improvement task is not permission to expand product scope.

## 65. Business Logic Guardrail

Do not silently change:

- API behavior;
- permissions;
- authentication;
- billing;
- business rules;
- validation semantics;
- security behavior;
- data semantics;
- destructive-operation semantics.

If an interface improvement requires product-behavior changes, recommend them separately unless explicitly authorized.

## 66. Final-State Principle

Exploration during implementation is allowed.

The agent may:

- try alternative layouts;
- test different CSS approaches;
- experiment with components;
- discard an interaction pattern;
- revise responsive behavior.

These intermediate attempts are working-session control information.

They are not automatically part of the final product identity.

Once an accepted result is established:

> Generate final surfaces from the accepted, verified state.

Do not construct delivery text by repeatedly editing rejected wording.

## 67. No Negative Echo

Rejected proposals, corrections, abandoned designs, and unsuccessful experiments should remain silent unless their history is genuinely required.

Do not unnecessarily encode them into:

- UI copy;
- component names;
- file names;
- CSS class names;
- CSS variables;
- comments;
- TODOs;
- documentation;
- tests;
- titles;
- commit messages;
- PR titles;
- PR descriptions;
- handoff notes.

The final repository should explain what the product is, not what the implementation session tried before arriving there.

## 68. Name Components by Current Purpose

Avoid historical names such as:

- NewSidebar;
- OldSidebar;
- SidebarV2;
- BetterDashboard;
- FinalDashboard;
- FixedLayout;
- NoScrollView;
- ImprovedTable;
- NewSettings.

unless the term has legitimate domain meaning.

Prefer:

- Sidebar;
- Dashboard;
- PageContainer;
- DataTable;
- SettingsLayout;
- ThemeSwitcher.

Future developers should not need conversation history to understand the architecture.

## 69. Comments Describe Current Invariants

Do not preserve rejected design history through comments such as:

- old implementation;
- user didn't like this;
- replaced previous layout;
- removed scroll version;
- temporary new design.

Comments should explain only useful current information such as:

- non-obvious invariant;
- technical constraint;
- compatibility requirement;
- accessibility reason;
- current behavior.

## 70. Remove Task-Owned Experimental Residue

Before delivery inspect for:

- unused CSS;
- unused classes;
- unused components;
- commented-out alternatives;
- debug output;
- temporary feature flags;
- temporary theme overrides;
- duplicate tokens;
- experimental files;
- abandoned variants;
- temporary labels;
- sample production data.

Remove obsolete task-owned residue.

Do not remove unrelated user changes or required diagnostics, tests, snapshots, audit history, migration information, or API names.

## 71. Final Commit and PR Must Describe the Result

When generating commit, PR title, PR description, handoff, or release note, derive statements from:

- actual final diff;
- verified final behavior;
- accepted current implementation.

Prefer:

- `fix(ui): stabilize responsive workspace layout`
- `refactor(ui): unify theme-aware surfaces`
- `feat(ui): streamline record actions`

Avoid conversation-history framing such as:

- remove rejected version;
- fix ugly layout;
- replace previous bad attempt;
- try new sidebar again.

unless historical explanation is materially required.

## 72. Final Delivery Should Be Positive-State Oriented

Describe:

- what now works;
- what became easier;
- what became more stable;
- what became consistent;
- what was verified.

Do not conclude with a transcript of attempted approaches.

## 73. Preserve Real History When Necessary

Final-state delivery does not justify hiding important facts.

Preserve history when needed for:

- safety;
- security;
- accuracy;
- compatibility;
- migration;
- audit;
- testing;
- API contracts;
- real behavior changes;
- user-requested comparison.

No Negative Echo means eliminating irrelevant rejected residue. It does not mean falsifying technical history.

## 74. Completion Gate

Do not consider a substantial frontend task complete until the affected interface passes the following review.

### Function

- Does the intended task still work?
- Were business rules preserved?

### Content

- Did the agent add any unnecessary user-facing text?
- Any debug/developer/internal information visible?
- Any invented production data?
- Any duplicated explanations?
- Any UI added merely to fill space?

### Layout

- Alignment coherent?
- Spacing intentional?
- Page width intentional?
- Padding consistent?
- No unexplained horizontal overflow?
- No artificial fixed-height region?

### Scroll

- Any new scrollbar?
- Why is it necessary?
- Could natural layout show the content instead?
- Any nested scrolling?

### Stability

- Loading stable?
- Refreshing stable?
- Route changes stable?
- Resize stable?
- Sidebar stable?
- Theme changes stable?
- Images/media reserve space?

### Readability

- Text contrast sufficient?
- Muted text readable?
- Placeholder readable?
- Disabled state readable?
- Dark themes readable?

### UX

- Primary action clear?
- Common task efficient?
- Important status discoverable?
- Context preserved?
- Feedback immediate?
- Error recovery clear?

### Consistency

- Shared patterns reused?
- Typography consistent?
- Action placement predictable?
- Theme tokens respected?
- Icons consistent?

### Responsive

- Desktop usable?
- Tablet usable?
- Mobile usable?
- Breakpoint transitions stable?

### Accessibility

- Focus visible?
- Keyboard usable?
- Touch targets reasonable?
- No essential hover-only interaction?

### Finalization

- Dead experimental code removed?
- Temporary labels removed?
- Historical names removed?
- Comments describe current state?
- Commit/PR derived from final result?

If a high-impact item fails, the task is not finished.

## 75. Final Internal Questions

Before finishing, ask:

- Did I add anything to the UI because I wanted to explain my implementation?
- Did I add anything simply because there was empty space?
- Did I introduce a scrollbar that the page did not need?
- Did I make the user learn a new interaction pattern unnecessarily?
- Did I solve a local symptom instead of a shared-system problem?
- Did I add visual polish before fixing stability?
- Did I reduce readability to make the design look subtle?
- Did I change product behavior while pretending it was UI cleanup?
- Did any rejected experiment leak into names, comments, UI copy, commit, or PR?
- Would a new user know what to do?
- Would an experienced user be able to do it quickly?

If any answer indicates a problem, correct it before delivery.

## 76. Success Standard

A new user should experience:

I know where I am → I understand what this page is for → I see the important action → I can complete the task without documentation.

An experienced user should experience:

fewer unnecessary clicks → less repeated navigation → less repeated input → less waiting → less context reconstruction → faster work.

The visual experience should be:

- stable;
- readable;
- responsive;
- consistent;
- restrained;
- intentional.

And the repository should read like:

> the implementation of one coherent accepted product design,

not:

> a record of every experiment used to discover it.
