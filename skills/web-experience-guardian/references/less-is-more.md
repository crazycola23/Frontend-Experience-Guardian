# Less Is More: Deleting Capability

This reference is for the harder half of restraint. `interface-restraint.md` covers
surfaces a user can see — titles, subtitles, cards, scroll regions. This one covers
the case where the restraint requires **removing capability that already works**.

Removing something that ships is not a cosmetic decision. It is a product decision.
Treat it accordingly, and never let "it looks cluttered" be the whole argument.

## The asymmetry that matters

Every agent is fluent at adding and hesitant at deleting. That asymmetry produces
two recurring failures:

1. **Deletion avoidance** — redundant UI survives because nobody is willing to own
   the removal.
2. **Deletion overreach** — a capability is removed because it looked noisy, without
   checking whether it carries information or satisfies a rule.

Both are failures. The remedy is not conservatism; it is a better decision procedure.

## Establish that it is actually empty

Before removing anything, prove it carries no information in real data.

A surface that looks redundant in the source may be the only place a real value
appears. Conversely, a surface that looks informative may be permanently blank.

Check the actual production data, not the type signature, not the mock, and not
the design intent:

- If a field is nullable and no producer ever sets it, the UI will show a
  permanent placeholder. Verify the null rate, not the possibility of a value.
- If two panels render the same value from the same source, one of them is
  redundant regardless of how it is styled.
- If a value is constant by construction (a single branch, a fixed enum with one
  member), it is decoration, not information.

Report the measurement, not the impression. "Three columns were removed; column X
was `null` in 15 of 15 rows" is a decision. "That column looked redundant" is not.

## Check for a specification mandate

Specifications, acceptance criteria, compliance requirements, and design-system
contracts can require a surface to exist. This is not the same as it being useful.

When you find one, do **not** quietly delete it and do **not** silently comply.
Surface the conflict and let the owner decide:

> This block is required by `SPEC-123`, but it is constant across every page and
> duplicates the sidebar. Keep it as specified, or remove it and update the spec?

If removal is chosen, update the specification in the same change. A code-only
deletion against a written requirement is drift, and the next agent will restore
the block because the spec still demands it.

## Prefer narrowing over removing

Before deleting a capability, check whether a smaller change already removes the
cost:

- **Hide only the empty case.** Render the surface only when it has content. A row
  that lists "0 failures · 0 cancelled · 0 not collected" in healthy data can become
  a row that appears only when a failure exists.
- **Collapse the always-true sentence.** A note whose condition is already implied
  by the control can go, while its one genuinely new clause stays.
- **Keep the consequence, drop the restatement.** A warning block may legitimately
  warn about an irreversible effect while redundantly restating who may act.
  Split it rather than deleting the whole block.
- **Change the default, keep the capability.** A feature can remain reachable
  behind progressive disclosure instead of occupying permanent surface area.

This ordering matters: narrow, then measure, then delete only if narrowing is
insufficient. Wholesale removal of something that could have been scoped is a
larger change than the problem requires.

## Deleting behavior, not just markup

Removing a visible element can orphan the logic behind it. Before committing:

- remove now-unused computed properties, helpers, styles, and imports;
- keep a reverse guard if the removal is a decision worth preserving.

Dead code left behind is residue. Rule 10 of the parent skill covers this, and a
half-deleted feature is worse than either extreme.

## Make the removal enforceable

Deleting something creates no failing test. Nothing about the remaining suite
regresses, so nothing prevents a later "this looks empty, let's add a helpful
summary back" change from undoing the decision.

Add a negative guard that fails when the removed surface returns:

- assert the removed selector or literal is absent from the source;
- assert the paired spec requirement is still absent;
- assert a deliberate replacement is still present, so the guard cannot be
  satisfied by deleting the file.

Verify the guard by re-introducing the redundancy and confirming it turns red. A
guard that has never failed is not known to work.

Strip comments before asserting. A guard that reads its own source will match the
"previously removed" note it is documenting and pass vacuously — or worse, fail
for the wrong reason and train people to ignore it.

## Distinguish misleading from merely redundant

Some removals are not tidiness. Prioritize them, because they actively harm users:

- **Copy that contradicts behavior.** A field labeled "optional" that the submit
  handler rejects when empty. The user follows the instruction and is blocked.
- **Internal identifiers in the product surface.** Raw primary keys, storage keys,
  enum codes, and upstream service names presented as if they were user-facing
  labels.
- **Permanently uninformative panels.** A status region that can only ever render
  one value, or a column that is blank for every row in the database.
- **Content duplicated within one viewport.** The same fact stated at three levels
  of hierarchy, or the same panel rendered twice side by side.

These outrank aesthetic cleanup regardless of how small they are.

## Know when not to delete

Some redundancy is load-bearing. Leave it alone and say why:

- a specification, acceptance criterion, or compliance rule requires it;
- it is the only place a consequence, irreversible effect, permission prerequisite,
  or recovery step is stated;
- it exists on a dedicated diagnostic, audit, or support surface where raw values
  are the product;
- it provides an empty state with an actionable next step;
- removing it would leave the user unable to complete, verify, or recover.

Diagnostic surfaces are a legitimate exception to the general rule against
exposing internal state. A support or audit view whose purpose is to show raw
values is doing its job. Do not extend that exception to ordinary business pages
merely because a viewer happens to be an administrator.

## Recording the decision

When a removal is a judgment call rather than an obvious defect, record it where
the next maintainer will look:

- note the reason in the specification or decision log, not only in code comments;
- when a specification requirement changes, change it in the same change;
- when the removal was based on a measurement, record the measurement so the
  decision can be revisited if the data changes;
- register an open item when a missing backend or API field blocked a complete fix,
  rather than presenting a partial fix as finished.

A removal without a recorded reason will be undone by someone who cannot see why
it was made. That is not disrespect for the decision; it is the correct response
to an unexplained one.