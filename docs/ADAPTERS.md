# Adapter contract

A QArborBench cell is a versioned task contract, not a task-name branch in a harness core. An adapter contribution must provide:

- a stable `cell_id`, task family and benchmark role;
- candidate syntax and the only permitted edit surface;
- task-local data and split identities;
- metric identity, direction and numerical validity rules;
- adapter and runner identities with required outputs;
- an open namespaced stage policy;
- query, dispatch, token and wall-time ceilings;
- result and provenance fields sufficient to bind code, candidate, data, evaluator and environment;
- an explicit policy for failure, no-result, invalidation and deferred evaluation.

Task-specific dependencies, platform APIs and evaluator logic stay within the cell implementation. The public benchmark registry may expose hashes and task cards while withholding protected evaluator source and licensed data.

New tasks should add a task card and registry entry without changing Q-Arbor core semantics. A task used to tune a core version must be labelled development for that core version and cannot later be called task-unseen.
