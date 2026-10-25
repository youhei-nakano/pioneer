---
name: pioneer
description: Conduct bounded research from a definition or question using independent branches, fresh reviews, and a frozen-round integration workflow. Use when the user requests the pioneer protocol; packaging or inspecting this skill does not authorize research.
---

# pioneer

This is a research workflow, not a runnable autonomous orchestrator. It does not establish correctness or novelty. Never restart a stopped task automatically. Packaging, inspection, and synthetic validation do not authorize a research run.

## Establish the run

Record the user's question or definition, scope, budget, stopping directions, permitted tools, branch count N, and checkpoint destination. Use configurable independent branches (historically A–J, N=10) and a separate integrated branch K. Do not allocate topics to branches by default. Preserve user-defined scope; recommend an evaluation checkpoint if novelty saturates or scope drifts, without silently changing the task.

Before execution, read [runtime.md](references/runtime.md). Require fresh isolated contexts for branches and reviewers. A skill cannot enforce tool permissions, isolation, or parallel scheduling. If the runtime cannot isolate contexts, do not claim independent execution: provide a plan/templates and report the limitation. Sequential scheduling is acceptable only with fresh isolated contexts, disclosed as a sequential degraded mode; it is not parallel execution. With no tools, produce an in-chat plan and checkpoint draft, explicitly marking unverified sources and unsaved records; do not simulate research, reviews, or persistence.

## Execute a bounded round

1. Give each independent branch only the common seed/protocol and its own history. Never expose sibling outputs or K's content, including through shared files, summaries, or tool access. In round0 each branch investigates definitions, assumptions, and prior work with source provenance. Distinguish retrieved, actually read, and unavailable sources; never invent access.
2. In subsequent rounds, each branch records finite claims, proof candidates, examples, counterexamples, or concrete obstacles. Discovery of a theorem is not a completion requirement.
3. Use fresh reviewers distinct from authors and K. Give reviewers the target claim, assumptions, evidence, and relevant sources without importing unrelated sibling/K content. Assess proof gaps, counterexamples, assumptions, relevance, and novelty separately. Record valid / qualified / gap / false / unresolved as review judgments, not proof certificates. A failed or missing reviewer leaves review pending; checkpoint and retry only within the user's budget and instructions.
4. Preserve exact original outputs and reviews; append corrections with links to originals. Record sources, code/results, failed attempts, statuses, and completion state using [records.md](references/records.md).
5. Freeze only after every declared branch has submitted its output and completed required reviews, including append-only corrections or documented unresolved findings. An unresolved mathematical claim may be recorded as such; a missing artifact or failed review cannot count as complete. Do not silently drop a branch to pass the barrier. A user-approved branch-set change needs a new declaration and audit trail.
6. Only then give K the complete frozen round (exact outputs, reviews, corrections, manifest) plus K's own prior history. K integrates and records its own claims and fresh reviews. Do not feed K back to independent branches unless the user explicitly changes the protocol; record the change and its effect on independence.

## Stop, checkpoint, resume

User cancellation and budget limits override round completion. Stop dispatching work, cancel active work where supported, preserve partial artifacts, and mark incomplete rounds as incomplete. Report any work whose cancellation is uncertain; do not freeze or send partial rounds to K. Do not run unbounded background jobs by default.

At each checkpoint record completed/pending/failed work, declared branches, input provenance, isolation limitations, budget consumed/remaining if measurable, and the next permissible action. Resume only on an explicit user instruction, from preserved state; check for already completed or still-running work before dispatch to avoid duplicates. Do not overwrite originals. Never turn an AI-reviewed candidate into a proven or novel result without independent evidence.
