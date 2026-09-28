# Final camera-ready decision

## Final scientific protocol

The final includable result is the locked seed-0, strict 42-subject LOSO three-point experiment: d=8, 528-D fixed cache, train-fold-only scaling, 15 epochs, batch 512, Adam lr=1e-3, posterior-mean evaluation, and source-training-KL-only beta selection. Alpha=1 and alpha=0 are audited reused endpoints; alpha=.5 is the completed MUST1 condition.

## Confirmed three-point result

| alpha | beta | MeanKL | Gesture_Acc | Gesture_F1 | Subject_AUC | KL_mismatch_percent |
| --- | --- | --- | --- | --- | --- | --- |
| 1.000000 | 0.010000 | 6.689059 | 0.795301 | 0.665353 | 0.682346 | 0.163293 |
| 0.500000 | 0.083300 | 6.840091 | 0.782297 | 0.574958 | 0.853078 | 2.090914 |
| 0.000000 | 0.120000 | 6.724625 | 0.612420 | 0.103120 | 0.746806 | 0.367531 |

The achieved rate mismatch is within 5% for every condition. Gesture Macro-F1 is ordered `alpha=1 > .5 > 0`.

## Paired Gesture-F1 evidence

| contrast | mean | ci95_low | ci95_high | positive_count | negative_count | tie_count |
| --- | --- | --- | --- | --- | --- | --- |
| 1_minus_0.5 | 0.090395 | 0.072274 | 0.108053 | 39.000000 | 3.000000 | 0.000000 |
| 0.5_minus_0 | 0.471838 | 0.433002 | 0.509879 | 42.000000 | 0.000000 | 0.000000 |
| 1_minus_0 | 0.562233 | 0.522468 | 0.601020 | 42.000000 | 0.000000 | 0.000000 |

## PLUS B status

**ABORTED_WITH_REASON.** Alpha=.75 source-only calibration encountered a reproducible float32 `exp(logvar)` overflow at beta=.07, held-out subject 20. The failure fold had finite raw/scaled inputs, but logvar reached 90.836319 and `exp(logvar)` overflowed. A float64 mathematical-implementation candidate was tested on two independent normal folds before recovery. It did not meet the pre-specified equivalence thresholds (KL <=0.5% relative; Accuracy/F1 <=0.01; Subject AUC <=0.02; final loss <=0.01), so it was not used. No protocol-changing repair, third raw retry, alpha=.75 Full42, or alpha=.25 run was performed.

## Final decision

**Use the three-point result as the camera-ready evidence (`STRONG_INCLUDE`). Do not include a five-point trajectory or any PLUS B result.** The valid three-point conclusion remains intact because PLUS B was an optional strong-gate extension and no invalid artifact was incorporated.

## Strongest limitation

The evidence is seed=0 only, and the reused S endpoint has CPU provenance. The result demonstrates an ordered task-performance trajectory at comparable achieved KL rates in this fixed protocol; it does not establish an exact semantic-information ratio, mutual information, disentanglement, subject-information removal, a causal mechanism, or a continuous law.

## What enters / does not enter camera-ready

Include: three-condition aggregate table, paired Gesture-F1 contrasts with 5,000 subject-cluster bootstrap CIs, rate-matching table, and the bounded interpretation above.

Do not include: alpha=.75/.25 five-point claims, float64 recovery results, the non-finite diagnostic as main scientific evidence, multi-seed conclusions, or any causal/disentanglement claim.
