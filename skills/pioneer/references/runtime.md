# Runtime contract

Before a run, identify the mechanism that provides separate branch contexts, fresh reviewer contexts, constrained reads/tool access, cancellation, and durable append-only storage. A shared filesystem is not isolation: restrict access or stage only allowed inputs in each context. Prompt instructions alone do not establish enforcement. Log the actual mechanism and any gaps. Do not use an author context as a fresh reviewer.

Concurrent execution requires an authorized scheduler or agent tools. Sequential degraded execution uses the same declared branches and barrier but schedules each isolated context in turn. A single conversation that has already seen all outputs cannot subsequently impersonate isolated branches or fresh reviewers. If these requirements cannot be met, stop execution at a reviewable plan rather than claiming compliance.

Check available sources and computation tools. Missing network access means sources are unavailable until supplied or retrieved; missing formal tools means no formal-check status. Do not call paid services or obtain credentials without authorization. Set finite run/round limits from the user's budget; checkpoint when a limit prevents completion. No automatic scheduling or restart is implied by installing this skill.

If leakage has already occurred, record the affected inputs/context and independence failure, preserve outputs as contaminated, and halt the affected branch. Use a clean replacement context with only permitted inputs before claiming compliance; retain the incident and supersession links rather than erasing it.
