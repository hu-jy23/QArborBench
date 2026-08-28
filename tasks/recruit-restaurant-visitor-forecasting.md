# Recruit Restaurant Visitor Forecasting

- Cell ID: `recruit-restaurant-visitor-forecasting`
- Task family: `demand_forecasting`
- Benchmark role: `public_validation`
- Capability shape: `relational_demand_forecasting`
- Metric: `rmsle` (minimize)
- Primary evidence stage: `public_validation`
- v0.1 status: `COMPLETE_FLAT_BEST_Q_SLIGHTLY_BEATS_NATIVE`
- Preparation repository commit: `6a2c011d174fe8d5c802a82f600c9b3eeef85040`
- Frozen time/OOS boundary: 2017-03-26 through 2017-04-22

## Accepted primary scores

- native: `0.541021166797`
- flat: `0.524996786919`
- q_arbor: `0.540233041806`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison. A null score remains an explicit typed no-result and is never replaced by another arm's score.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
