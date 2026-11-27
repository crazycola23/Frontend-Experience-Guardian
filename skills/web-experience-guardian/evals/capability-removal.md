# Eval: Removing Existing Capability

## Fixture

Provide a working business screen that contains, in addition to its primary task:

1. a table column that renders a permanent placeholder because no producer in the
   system ever populates it;
2. a helper sentence directly beneath a control that states the control is
   optional, while the submit handler rejects the empty case;
3. a block of always-on explanatory copy whose conditions are already implied by
   the controls below it;
4. a persistent panel on a global layout that duplicates a block shown on the
   entry screen;
5. one item whose removal a written specification explicitly requires.

## Task

"This screen feels cluttered and noisy. Make it less is more — cut what is not
needed."

## Failure patterns

### Deletion avoidance

- keeps every item because removal feels risky;
- proposes cosmetic restyling instead of addressing the permanent placeholder;
- asks a broad clarifying question instead of removing what is provably empty and
  reporting the measurement.

### Deletion overreach

- removes the spec-mandated item without flagging the conflict;
- removes the statement of an irreversible effect or a permission prerequisite
  because it looked wordy;
- removes raw diagnostic values from a support or audit surface, or removes them
  from a business surface while claiming the diagnostic exception applies;
- removes an empty state that carried an actionable next step;
- leaves orphaned computed properties, styles, or imports behind;
- removes a column because it looked wide, without checking whether it is
  genuinely populated for some rows.

### Unverified reasoning

- argues from the type signature, a mock, or design intent instead of real data;
- claims a value is "probably always null" without a null rate;
- asserts removal is safe without reading the specification that requires it.

### Unenforceable decisions

- removes the surfaces but adds no guard, so any later "this looks empty, let us
  add a helpful summary" change silently restores them;
- writes a guard that matches the source's own explanatory comment and therefore
  passes vacuously or fails for the wrong reason;
- presents the change as fully complete while a missing API or backend field
  still blocks the intended end state, without registering the open item.

## Guardian-positive behavior

- measures before removing, and reports the measurement ("that column is `null`
  in 15 of 15 rows") rather than the impression;
- fixes the actively harmful items first: the copy that contradicts validation,
  then the permanently empty column;
- narrows where narrowing suffices — renders the always-on zero row only when a
  failure actually exists, and keeps the clause that states an irreversible
  consequence while dropping the restatement;
- removes the spec-mandated item only after surfacing the conflict and letting the
  owner decide, and updates the specification when the decision is to remove it;
- deletes the associated logic, styles, and imports with the markup;
- adds negative guards for the removals and demonstrates one of them failing by
  re-introducing the redundancy;
- strips comments before asserting in those guards;
- preserves the diagnostic, audit, or support surface where raw values are the
  product, and does not generalize that exception to ordinary pages;
- records the reasoning and the measurement where the next maintainer will look;
- states plainly what remains open when a backend or API gap blocks completion.