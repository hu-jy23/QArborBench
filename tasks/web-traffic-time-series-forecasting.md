# Web Traffic Time Series Forecasting

- Cell ID: `web-traffic-time-series-forecasting`
- Task family: `scale_panel_forecasting`
- Benchmark role: `sealed_task_holdout`
- Capability shape: `large_scale_multi_series_forecasting`
- Metric: `smape` (minimize)
- Primary evidence stage: `sealed_v1`
- v0.1 status: `COMPLETE_FLAT_BEST`
- Preparation repository commit: `fcfe1d417cb5d0892358515d348754ae6d86f37e`
- Frozen time/OOS boundary: final 60 days of frozen 240-day view

## Accepted primary scores

- native: `41.722702022417`
- flat: `38.965495815907`
- q_arbor: `40.604657780082`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison. A null score remains an explicit typed no-result and is never replaced by another arm's score.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
