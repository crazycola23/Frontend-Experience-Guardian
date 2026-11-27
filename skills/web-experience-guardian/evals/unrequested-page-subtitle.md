# Eval: Unrequested Page Subtitle

## Fixture

An existing admin page contains:

- breadcrumb or application navigation;
- page title `Users`;
- search;
- role and status filters;
- a user table;
- an `Invite user` primary action.

The page purpose is already obvious from the title, controls, and content. There is no unusual constraint, warning, prerequisite, or hidden scope that the user needs before acting.

## Task

“Polish this page and improve the visual hierarchy.”

## Failure patterns

- adds a generic subtitle such as `Manage your users and account permissions.`;
- adds an eyebrow or descriptive label above the title without a concrete information need;
- adds helper copy merely to make the header feel complete or polished;
- fills header whitespace with explanatory text;
- paraphrases the page title or describes controls/content already visible below;
- treats `title + subtitle` as a default page-header pattern.

## Guardian-positive behavior

- keeps `Users` as a standalone page title;
- improves hierarchy through typography, spacing, alignment, grouping, or action placement;
- adds no new header copy unless it communicates material information not otherwise visible;
- applies the removal test before retaining supporting text.

## Exception test

Run a variant where the fixture includes one material fact that is not otherwise visible, such as:

- `Changes here apply to all workspaces.`;
- `Invitations expire after 7 days.`;
- `User creation is disabled while SSO enforcement is active.`

In this variant, concise supporting copy is acceptable when it communicates that fact clearly and in the appropriate location.

The evaluator should distinguish useful operational information from generic descriptive copy rather than rewarding subtitle removal mechanically.
