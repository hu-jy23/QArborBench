# Evidence policy

## Accepted primary evidence

- Development cells use data-OOS when an authorized frozen-candidate result exists.
- Public-validation cells use one-time post-freeze results.
- Sealed cells use valid results produced after the core and protocol were frozen.
- M5 uses development evidence because its data-OOS evaluation produced no arm score.

## Invalid and missing evidence

- JPX Flat v1 and Optiver v1 were invalidated for temporal leakage and excluded from primary comparisons.
- Corrected causal-v2 evidence is primary for JPX Flat and all Optiver arms.
- A missing score remains a no-result; no Native or Flat score is substituted for Q-Arbor.
- Resource and budget failures remain visible typed outcomes.

## Aggregation

Raw metrics from different tasks are never averaged. Aggregate records count only within-task directional wins, losses and no-results. Percentage summaries near a zero reference, such as MITSUI, are fragile; raw scores remain primary.

## Statistical boundary

Each primary arm has one formal run. QArborBench-v0.1 does not estimate run-to-run variance, confidence intervals, statistical significance, false-discovery rates or transaction-cost robustness.
