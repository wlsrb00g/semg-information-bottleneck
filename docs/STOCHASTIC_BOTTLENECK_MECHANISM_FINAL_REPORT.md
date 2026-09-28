# 1. Hypothesis

KL constrains the stochastic information budget; meaningful supervision influences which information remains accessible.

# 2. Existing real-data evidence

The existing dimension/KL sweeps and G/S target swap show target-dependent probe and retrieval behavior. The G/S matched-rate comparison is reused without retraining.

# 3. Experiment A — 3-arm matched-rate result

| Target | beta | Mean_KL | Gesture_F1 | Subject_AUC | relative_KL_mismatch |
| --- | --- | --- | --- | --- | --- |
| G | 0.01 | 6.689059366046905 | 0.665352597999245 | 0.6823461091753775 | 0.0 |
| S | 0.12 | 6.724624577598751 | 0.10311995507552468 | 0.7468060394889664 | 0.005316922695046229 |
| GS | 0.25 | 6.693488178807222 | 0.4892707293050859 | 0.8644018583042973 | 0.0006620979898604247 |

# 4. Experiment B — label-shuffle control

| arm | Mean KL | Gesture F1 | Subject AUC |
| --- | --- | --- | --- |
| G true | 6.689059366046905 | 0.665352597999245 | 0.6823461091753775 |
| G-shuffle | 0.0014389830096054315 | 0.23029633870336225 | 0.8487224157955866 |

# 5. Experiment C — synthetic ground-truth

| arm | gesture_factor_r2 | subject_factor_r2 |
| --- | --- | --- |
| G | 0.7700375914573669 | 0.0009116619825363159 |
| GS | 0.5058806121349335 | 0.37540186047554014 |
| S | 0.0009904682636260986 | 0.4904894232749939 |

# 6. Mechanism verdict

**PARTIAL SUPPORT**

# 7. Exact defensible paper claim

Under a constrained stochastic rate, the information accessible from the latent representation depends strongly on the supervised target, with meaningful supervision preferentially preserving task-relevant structure in these real and synthetic diagnostics.

# 8. Claims that remain unsupported

- mutual information directly measured
- semantic disentanglement proven
- subject identity completely removed
- causal physiological factor identification
- universal mechanism across datasets
