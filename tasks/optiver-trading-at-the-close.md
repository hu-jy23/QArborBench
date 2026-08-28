# Optiver Trading at the Close

- Cell ID: `optiver-trading-at-the-close`
- Task family: `market_microstructure`
- Benchmark role: `sealed_task_holdout`
- Capability shape: `market_microstructure_regression_with_iterative_interface`
- Metric: `mae` (minimize)
- Primary evidence stage: `sealed_causal_v2`
- v0.1 status: `COMPLETE_CAUSAL_V2_VALID_FLAT_BEST_V1_INVALID_EXCLUDED`
- Preparation repository commit: `6049115c6eb4647822868193c79cd4f5607babdb`
- Frozen time/OOS boundary: date_id 461 through 480

## Accepted primary scores

- native: `5.790414358003`
- flat: `5.699842425752`
- q_arbor: `5.759560855632`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison. A null score remains an explicit typed no-result and is never replaced by another arm's score.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
