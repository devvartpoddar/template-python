# Gotchas

Institutional memory. When a quirk bites once, it gets written down here so it never has to bite twice, and no session has to re-discover it from scratch. Format: symptom → cause → rule.

Add to this file in the same PR where you hit the thing — see the PR template's "Gotchas discovered" section.

---

**Symptom:** `pg_query` returns "workflow did not return a response."
**Cause:** The query matched zero rows. This is not a broken tool or a connection problem.
**Rule:** Use `COUNT(*)` to check whether rows exist before treating an empty result as an error.

---

**Symptom:** Todoist's `/tasks/completed/by_completion_date` silently excludes recurring task completions.
**Cause:** That endpoint doesn't cover recurring tasks the way its name implies.
**Rule:** Use the activity log endpoint instead whenever recurring tasks are in scope.

---

**Symptom:** A process backgrounded with `nohup`, `&`, or disown-and-abandon keeps running unsupervised, or silently dies, outside the agent's control.
**Cause:** None of those actually detach the process from the agent's process group — they just stop you watching it.
**Rule:** `nohup` / `&` / disown-and-abandon are banned in agent preambles. Use `setsid` with a process-group reap as the actual safety net, not a substitute for one.
