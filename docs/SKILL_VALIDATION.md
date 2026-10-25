# Skill validation — 2026-10-25

Scope: packaging only. No research rounds, private transcripts, unpublished results, paid APIs, or global installation were used. The original public example is unchanged. The prior candidate was a plain directory without .git and matched the fetched public snapshot; it was left unchanged. Work began from public main a3dc5be9c94a95b12e14bc625f8013d2873c0c7a in a fresh checkout.

## Structural and reproducibility checks

- skill-creator `quick_validate.py skills/pioneer`: passed using temporary PyYAML 6.0.3 dependency; no runtime dependency was added to this repository.
- Relative Markdown file links: resolved in the repository and within the standalone skill folder.
- Existing subset-sums example: output equals expected.json; 792 exact positive-rational cases and 3 invalid inputs passed.
- SHA256SUMS: regenerated for all public files except itself and verified.
- `git diff --check`: passed.

## Independent synthetic forward-test

A fresh evaluating agent read SKILL.md and both references and applied them to the following small synthetic inputs. It made no research, network, API, or repository mutations. These were decision exercises, not tests of an implemented scheduler.

| Input | Observed decision |
| --- | --- |
| N=2; A complete, B active; user cancels; cancellation uncertain | Stop dispatch, preserve partial work, report B uncertainty, checkpoint incomplete; no freeze/K; explicit resume and status check required. |
| N=3; C review missing | Keep C pending and declared; no freeze/K; fresh review only within limits. |
| B proposed input includes A output and K synthesis | Reject input; require isolated clean context; contaminated conversation cannot impersonate B. |
| All outputs present; B reviewer crashes | Record failure; review stays pending; fresh retry within limits or incomplete checkpoint; no freeze/K. |
| No tools, context isolation, files, or sources | In-chat plan and unsaved draft only; no claims of research, review, source access, persistence, or formal checks. |

All five decisions respected the protocol. Evaluator feedback prompted one narrow clarification in runtime.md: preserve and label already-contaminated outputs, halt the affected branch, and require a clean replacement context. This addition was inspected after the independent pass; the independent pass itself preceded this clarification.

## Limits

Behavioral exercises do not prove model compliance, actual isolation, parallel execution, cancellation, or persistence. No live multi-branch research execution or formal verification was performed. The skill contains instructions and a record template, not executable orchestration/helpers. Hashes check byte integrity only. No license was added; distribution does not grant a new reuse license.
