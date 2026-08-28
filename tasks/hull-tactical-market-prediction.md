# Hull Tactical Market Prediction

- Cell ID: `hull-tactical-market-prediction`
- Task family: `dynamic_allocation`
- Benchmark role: `public_validation`
- Capability shape: `dynamic_asset_allocation`
- Metric: `adjusted_sharpe` (maximize)
- Primary evidence stage: `public_validation`
- v0.1 status: `COMPLETE_Q_BEATS_FLAT_BOTH_BELOW_NATIVE`
- Preparation repository commit: `7f21cc360909927a065c9913f3476d3da8db0fca`
- Frozen time/OOS boundary: date_id 8688 through 9047

## Accepted primary scores

- native: `0.745044469177`
- flat: `0.692757908097`
- q_arbor: `0.717646406317`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison. A null score remains an explicit typed no-result and is never replaced by another arm's score.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
