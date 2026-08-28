# MITSUI Commodity Prediction

- Cell ID: `mitsui-commodity-prediction`
- Task family: `ranking`
- Benchmark role: `development_benchmark`
- Capability shape: `multi_target_quant_ranking`
- Metric: `rank_correlation_sharpe` (maximize)
- Primary evidence stage: `data_oos`
- v0.1 status: `COMPLETE_FLAT_BEST`
- Preparation repository commit: `d61a1285cd3b48bba6902a7a84cb977e7aca01c0`
- Frozen time/OOS boundary: final 45 labelled dates

## Accepted primary scores

- native: `-0.004011802664`
- flat: `0.339090144813`
- q_arbor: `0.023397789702`

Scores are meaningful only within this task, metric, stage and frozen role-model-policy comparison. A null score remains an explicit no-result. Deferred cells receive no score.

## Reproduction boundary

This repository distributes the task contract and accepted aggregate result. It does not redistribute task data, hidden labels, protected evaluator/selector source, candidate worktrees or internal run traces. Reproduction requires obtaining the original data under its source license and independently implementing or receiving an authorized evaluator.
