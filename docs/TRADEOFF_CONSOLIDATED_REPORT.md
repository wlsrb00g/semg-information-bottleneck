# Tradeoff Consolidated Report

## Scope

This figure set reuses the frozen Furman-style LDA gesture benchmark and the existing beta-KL bottleneck sweep. No neural model training, beta tuning, feature engineering, split change, or new stochastic evaluation was performed.

## LDA audit

- Cohort: 42-subject integrity-verified cohort, 252 recordings.
- Features: 528-D FURMAN_22 handcrafted cache.
- Split: strict 42-fold LOSO; 41 source subjects train each fold and the held-out subject is evaluation-only.
- Gesture baseline: Accuracy=0.779056; Macro-F1=0.581785.
- LDA representation for subject verification: train-fold StandardScaler -> train-fold `LinearDiscriminantAnalysis(solver="svd")` -> `LDA.transform(X)`.
- Observed LDA.transform dimension: 7D.
- LDA Subject AUC: 0.845198 (mean of bidirectional same-gesture cross-session verification AUC over 42 folds).

## Subject verification protocol

The existing `run_putemg_implicit_subject_domain_quick_diag.py` protocol was reused. For every subject x session x gesture, deterministic balanced prototypes are formed from equally sized session samples. Same-gesture cosine distances are evaluated in both Exp1-to-Exp2 and Exp2-to-Exp1 directions. The diagonal same-subject pairs are positives; all off-diagonal subject pairs are negatives; ROC-AUC is computed from negative cosine distances and the two directions are averaged. No held-out subject samples enter scaler/LDA fitting, and no probe hyperparameter or threshold tuning is performed.

The stochastic primary comparison uses the existing posterior-mean `subject_auc` in `results/kl_beta_cpu6/kl_beta_summary.csv`, whose source code calls the same diagnostic. The separate sampled-Z artifact is retained as a provenance/sensitivity artifact; it is not substituted into the primary figure.

Sampled-Z mean Subject AUC by beta (secondary artifact): 0: 0.812166, 0.001: 0.761629, 0.003: 0.747721, 0.01: 0.679384, 0.03: 0.623708, 0.1: 0.559858. Its draw-level SD is retained in `tradeoff_data.csv` and is not mixed into the posterior-mean primary curve.

## Beta sweep data

| beta_KL | Mean KL | Gesture Macro-F1 | Subject AUC |
|---:|---:|---:|---:|
| 0 | 127.957803 | 0.667608 | 0.900954 |
| 0.001 | 19.101680 | 0.665250 | 0.860067 |
| 0.003 | 11.761917 | 0.666465 | 0.848330 |
| 0.01 | 6.689059 | 0.662585 | 0.791586 |
| 0.03 | 4.139675 | 0.665241 | 0.741361 |
| 0.1 | 2.500598 | 0.656924 | 0.683633 |

No 5-seed summary was found for this exact six-point beta sweep; values are the existing seed-0 CPU6 sweep aggregation over the fixed 42 LOSO folds. LDA subject-wise fold SD and stochastic sweep variability are not displayed as interchangeable error bars.

## Interpretation

The primary figure shows the empirical tradeoff trajectory in a common gesture Macro-F1 versus subject-verification-AUC coordinate system, with LDA as a fixed baseline operating point. Subject AUC near 0.5 is only a low-accessibility reference in this verification task; it is not proof of information removal or complete identity independence. The plot does not establish causality, disentanglement, exact mutual information, or a universal real-sEMG law.

## Figures

- `figure_1_f1_vs_subject_auc.png/.pdf/.svg`
- `figure_2_kl_vs_f1.png`
- `figure_3_kl_vs_subject_auc.png`

## Source files

- `furman_loso_benchmark_v1/furman_lda_folds.csv`
- `results/lda_macro_f1_audit/lda_loso_fold_metrics.csv`
- `scripts/run_putemg_furman_loso_models_v1.py`
- `scripts/run_putemg_kl_beta_cpu6.py`
- `scripts/run_putemg_implicit_subject_domain_quick_diag.py`
- `results/kl_beta_cpu6/kl_beta_summary.csv`
- `results/kl_sweep_sampled_z_auc_xpu5/KL_SWEEP_SAMPLED_Z_AUC_SUMMARY.csv`
