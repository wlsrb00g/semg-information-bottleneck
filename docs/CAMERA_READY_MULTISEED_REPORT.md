# Camera-ready multi-seed reviewer analysis

## Scope and inputs

This report aggregates only completed strict 42-subject LOSO artifacts for alpha={1.0, 0.5, 0.0} and seeds={0,1,2,3,4}. No additional training, beta tuning, model change, or new experiment was run by this analysis.

Historical alpha=1.0 (G) and alpha=0.0 (S) endpoints were read from `results/post_submission_controls/MULTISEED_GS_RAW.csv`; alpha=.5 seeds 1–4 were read from their completed XPU fold artifacts. Canonical seed-0 rows were read from `results/camera_ready_alpha_mix/CAMERA_READY_ALPHA_FOLD.csv` rather than substituted from historical rows. Endpoint audit: **PASS_WITH_DISCLOSED_HISTORICAL_BETA_PROVENANCE**. The historical endpoint beta provenance is retained as a limitation: G used an established source-derived beta and S used a seed-0 source-only-calibrated beta fixed for later seeds; no held-out metric selected either beta.

## Five-seed condition means (mean ± sample SD, ddof=1)

| alpha | Mean KL | Gesture Macro-F1 | Gesture Accuracy | Subject AUC |
| --- | --- | --- | --- | --- |
| 1.00 | 6.5930 ± 0.1232 | 0.6666 ± 0.0020 | 0.7939 ± 0.0023 | 0.6798 ± 0.0107 |
| 0.50 | 6.7524 ± 0.1480 | 0.5673 ± 0.0098 | 0.7764 ± 0.0065 | 0.8209 ± 0.0217 |
| 0.00 | 6.6150 ± 0.1046 | 0.1011 ± 0.0018 | 0.6124 ± 0.0007 | 0.7556 ± 0.0078 |

## Seed-wise ordering and contrasts

Gesture ordering `F1(1.0) > F1(.5) > F1(0.0)` held in **5/5** seeds.

| contrast | mean | sample SD | min | max | positive seeds |
| --- | --- | --- | --- | --- | --- |
| Delta_1_05 | 0.0993 | 0.0100 | 0.0898 | 0.1129 | 5/5 |
| Delta_05_0 | 0.4662 | 0.0095 | 0.4514 | 0.4765 | 5/5 |
| Delta_1_0 | 0.5654 | 0.0035 | 0.5622 | 0.5711 | 5/5 |

## Rate robustness

All seed×alpha conditions were checked using their achieved held-out fold-average Mean KL against target 6.7. **15/15** conditions are within 5%. The per-condition values and mismatches are recorded in `CAMERA_READY_MULTISEED_SEED_SUMMARY.csv`.

## Automatic decision

**MULTISEED_STRONG**

Predeclared aggregation rule: STRONG requires 5/5 ordered seeds, 15/15 rate-comparable conditions, positive main adjacent contrasts in 5/5 seeds, and mean adjacent F1 contrast larger than its sample SD. MIXED requires at least 3/5 ordered seeds and at least 12/15 rate-comparable conditions. Otherwise the decision is FAIL. This is seed-level inference; the 210 folds are not treated as independent replicate seeds.

## Limitations

The repeated unit is random seed (n=5), while LOSO folds are used only to form each seed-level condition mean. Results describe accessible task/subject metrics under the fixed protocol and do not directly measure mutual information, prove disentanglement, establish causality, or quantify exact information allocation.
