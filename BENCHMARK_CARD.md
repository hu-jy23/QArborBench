# QArborBench Benchmark Card

## Identity

- Name: **QArborBench**
- Long name: **A Protocolized Multi-Task Benchmark for Quantitative Research Harnesses**
- Release: `v0.1`
- Registry size: 12 task contracts
- Executed coverage: 9 task cells
- Deferred coverage: 3 task cells
- Comparison arms: Native, Flat Agent, Q-Arbor

## Intended use

QArborBench evaluates how an autonomous research harness organizes, executes and preserves iterative quantitative experimentation under frozen task interfaces, budgets and evidence-stage rules. It is designed for harness comparison, evidence admissibility and recovery analysis. It is not a universal trading leaderboard, profitability test or pure base-model benchmark.

## Benchmark unit

One `cell` is a versioned bundle of:

- task and candidate contract;
- data and split identities;
- task-local metric and direction;
- adapter, runner and evaluator identities;
- development and held-out stage policy;
- query, dispatch, token and wall-time ceilings;
- result, provenance and terminal receipts.

## Task-family coverage

| Family | Registered cells | v0.1 status |
|---|---|---|
| Cross-sectional and multi-target ranking | MITSUI, JPX | 2 executed |
| Dynamic asset allocation | Hull | 1 executed |
| Market-microstructure prediction | Optiver | 1 executed |
| Tabular and relational demand forecasting | Bike, Recruit, Walmart | 3 executed |
| Hierarchical, panel and multi-series forecasting | M5, Web Traffic, Rossmann, Store Sales, Favorita | 2 executed, 3 deferred |

## Evidence regimes

| Regime | Purpose | Feedback rule |
|---|---|---|
| Development | bounded candidate search | reusable task-local feedback |
| Data-OOS | time-tail test of a frozen development candidate | one query per frozen candidate; no reselection |
| Public validation | one-time external check after candidate freeze | score cannot update candidate or core |
| Sealed task holdout | task-level holdout under frozen protocol | evaluator result unavailable during development |

## v0.1 execution portfolio

| Cell | Family | Primary evidence | Status |
|---|---|---|---|
| Bike | tabular demand forecasting | data-OOS | executed |
| MITSUI | multi-target ranking | data-OOS | executed |
| M5 | hierarchical forecasting | development; OOS resource-blocked | partial explicit no-result for Q-Arbor |
| Hull | dynamic allocation | public validation | executed |
| JPX | cross-sectional ranking | public validation causal-v2 | executed after leakage reconciliation |
| Recruit | relational demand forecasting | public validation | executed |
| Walmart | weighted panel forecasting | public validation | executed |
| Optiver | market microstructure | sealed causal-v2 | executed after leakage reconciliation |
| Web Traffic | large-scale multi-series forecasting | sealed | executed |
| Rossmann | panel forecasting | none | deferred due to scope/time |
| Store Sales | multi-series forecasting | none | deferred due to scope/time |
| Favorita | large sparse forecasting | none | deferred due to scope/time |

## Frozen primary summary

- Flat vs Native: 7 wins, 2 losses, 0 no-results.
- Q-Arbor vs Native: 6 wins, 2 losses, 1 no-result.
- Q-Arbor vs Flat: 4 wins, 4 losses, 1 no-result.
- Public-validation Q-Arbor vs Flat: 3 wins in 4 cells.
- Q-Arbor three-way winners: Bike data-OOS and Walmart public validation.
- Historical invalid variants: JPX Flat v1 and Optiver v1; both excluded from primary results.

## Integrity policy

- Invalid scores stay addressable but never enter the primary table.
- Missing scores remain no-results; no baseline value is relabeled as an agent score.
- Deferred tasks remain visible with zero formal score.
- Raw metrics from different tasks are never averaged.
- Every accepted result binds candidate, code, task, data, split, evaluator and environment identities.
- Development feedback cannot select a candidate after validation/data-OOS/sealed access.

## Known limitations

- One formal run per primary arm; no variance, confidence interval or statistical-stability estimate.
- Flat and Q-Arbor Coordinator use Sol/high; Q-Arbor Executors use Luna/high.
- The comparison therefore evaluates a frozen role-model-policy harness.
- Three registered cells were not executed in v0.1.
- Exact per-arm provider token usage and billing receipts are unavailable.
- Reproduction of formal scores requires task data and protected evaluator components.

## Safe headline

> QArborBench-v0.1 shows that Q-Arbor remains competitive across heterogeneous quantitative tasks while providing persistent research state, capability-gated evaluation, explicit no-results and auditable evidence reconciliation.
