# JPX Tokyo Stock Exchange Prediction

- Cell ID: `jpx-tokyo-stock-exchange-prediction`
- Task family: `ranking`
- Benchmark role: `public_validation`
- Capability shape: `cross_sectional_equity_ranking`
- Metric: `spread_sharpe` (maximize)
- Original task source: [JPX Tokyo Stock Exchange Prediction](https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction)
- Primary evidence stage: `public_validation_causal_v2_flat`
- v0.1 status: `COMPLETE_CAUSAL_RECONCILED_Q_BEATS_FLAT_BOTH_BELOW_NATIVE`
- Preparation repository commit: `1e3aa7e300e8b8182211e87ebc121db3a321a596`
- Frozen time/OOS boundary: final 60 trading days

## Accepted primary scores

- native: `0.267662407403`
- flat: `0.224665972247`
- q_arbor: `0.243708844901`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
