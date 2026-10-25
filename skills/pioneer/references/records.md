# Records and checkpoint template

Copy and adapt this template; retain exact outputs separately. Relative paths below are examples, not a storage implementation.

```yaml
run_id: synthetic-or-user-assigned
question: user-provided definition or question
scope: user-approved scope
state: planned # running, stopped, incomplete, frozen, integrated
budget: user-specified limits
stopping_directions: user-specified directions
branches: [A, B] # configurable N; K is separate
round: 0
common_seed: {path: seed.txt, sha256: recorded-after-saving}
isolation: {mechanism: unavailable, limitations: []}
artifacts: [] # branch, output path/hash, review path/hash, correction links, state
pending: []
failed: []
k_input: null # full frozen manifest only after complete barrier
cancellation: {requested: false, uncertain_active_work: []}
next_permissible_action: await user instruction
```

For each claim keep ID, exact statement, assumptions, author/branch, source provenance (bibliography/URL, location, access date and actually-read portions), proof or counterexample, code/results, review findings, and links to appended corrections. Keep epistemic labels separate: known result, conjecture, proof candidate, AI-reviewed, formally checked. For formal checks record the exact statement, tool/version, command and outcome; formal checking covers only what was encoded. Review verdicts do not replace these labels.

A frozen manifest lists every declared branch output, review, and correction with byte hashes and version identifiers. K receives the full artifacts rather than an unmarked summary. SHA-256 establishes byte integrity only: it does not establish proof correctness, novelty, actual reading, or context isolation. Checkpoint partial work without labeling it frozen. Preserve private originals; any public derivative must disclose editing/omissions and provenance, and requires publication authorization separate from running research.
