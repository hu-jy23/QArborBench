# QArborBench

QArborBench is a protocolized multi-task benchmark for comparing quantitative research harnesses. It standardizes task contracts, comparison arms, budgets, evaluation stages, result identity and evidence admissibility while keeping task semantics outside the harness core.

We propose QArborBench as a harness and evidence-governance benchmark. It does not claim complete coverage of quantitative finance or newly invented underlying datasets.

## v0.1 at a glance

- 12 registered, replaceable task contracts.
- 9 executed cells and 3 explicitly deferred cells.
- 5 representative task families.
- 4 evidence regimes.
- Native baseline, Flat Agent and Q-Arbor comparison arms.
- Frozen task-local metrics; heterogeneous raw metrics are never averaged.

## Coverage map

| Task family | Development | Data-OOS | Public validation | Sealed holdout |
|---|---|---|---|---|
| Ranking | — | MITSUI | JPX | — |
| Dynamic allocation | — | — | Hull | — |
| Market microstructure | — | — | — | Optiver |
| Demand forecasting | — | Bike | Recruit, Walmart | — |
| Scale/panel forecasting | M5 (Q no-result) | — | — | Web Traffic |

Registered extension pool: Rossmann, Store Sales and Favorita; all were deferred in v0.1 due to scope/time and remain eligible for later execution.

## Agent Harness × Task

Arrows indicate metric direction. Results are accepted primary evidence after invalidation and causal-boundary reconciliation.

| Task / evidence | Metric | Native | Flat Agent | Q-Arbor | Outcome |
|---|---|---:|---:|---:|---|
| Bike / data-OOS | RMSLE ↓ | 0.32202345 | 0.31798259 | **0.31222229** | Q best |
| MITSUI / data-OOS | Rank-corr. Sharpe ↑ | -0.00401180 | **0.33909014** | 0.02339779 | Flat best |
| M5 / development | WRMSSE ↓ | 0.80740016 | **0.63424971** | N/A | Q no-result before dispatch |
| Hull / public validation | Adjusted Sharpe ↑ | **0.74504447** | 0.69275791 | 0.71764641 | Native best; Q > Flat |
| JPX / public validation causal-v2 | Spread Sharpe ↑ | **0.26766241** | 0.22466597 | 0.24370884 | Native best; Q > Flat |
| Recruit / public validation | RMSLE ↓ | 0.54102117 | **0.52499679** | 0.54023304 | Flat best |
| Walmart / public validation | WMAE ↓ | 1659.06914 | 1412.26849 | **1389.20251** | Q best |
| Optiver / sealed causal-v2 | MAE ↓ | 5.79041436 | **5.69984243** | 5.75956086 | Flat best; v1 excluded |
| Web Traffic / sealed | SMAPE ↓ | 41.72270202 | **38.96549582** | 40.60465778 | Flat best |
| Rossmann / deferred | RMSPE ↓ | N/A | N/A | N/A | Deferred |
| Store Sales / deferred | RMSLE ↓ | N/A | N/A | N/A | Deferred |
| Favorita / deferred | NWRMSLE ↓ | N/A | N/A | N/A | Deferred |

Primary directional summary:

- Flat Agent vs Native: 7 wins, 2 losses, 0 no-results.
- Q-Arbor vs Native: 6 wins, 2 losses, 1 no-result.
- Q-Arbor vs Flat Agent: 4 wins, 4 losses, 1 no-result.
- Public validation, Q-Arbor vs Flat Agent: 3 wins in 4 cells.

## Repository map

- [`benchmark/registry.json`](benchmark/registry.json): sanitized 12-cell registry and frozen source identities.
- [`protocol/protocol.json`](protocol/protocol.json): comparison, budget, stage and admissibility rules.
- [`schemas/task-contract.schema.json`](schemas/task-contract.schema.json): public adapter contract schema.
- [`results/summary.json`](results/summary.json): machine-readable accepted results.
- [`tasks/`](tasks/): one public card per registered cell.
- [`docs/ADAPTERS.md`](docs/ADAPTERS.md): contribution and integration rules.
- [`docs/EVIDENCE_POLICY.md`](docs/EVIDENCE_POLICY.md): no-result, leakage, deferred and held-out evidence rules.

## Use with Q-Arbor

QArborBench tasks are replaceable experiment adapters. [Q-Arbor](https://github.com/hu-jy23/Q-Arbor) consumes task-local adapter, runner, stage-policy, result-envelope and provenance identities through its open control surface. Competition and platform names never enter the shared core semantics.

## Reproduction boundary

This repository publishes benchmark specifications, public task cards and accepted aggregate evidence. It does not redistribute raw or derived row-level data, hidden labels, unopened time tails, protected evaluator/selector implementations, credentials, internal Agent sessions, attempts, ledgers or smoke outputs.

Each primary arm has one formal run. Results do not establish statistical score stability, universal superiority, trading profitability or exact provider cost.

## License

Benchmark code and documentation are licensed under Apache-2.0. Underlying datasets remain governed by their original licenses and platform terms.
