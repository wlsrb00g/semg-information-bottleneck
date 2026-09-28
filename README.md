# sEMG Information Bottleneck

putEMG의 handcrafted sEMG feature를 확률적 bottleneck으로 압축할 때, KL rate와 supervision target이 gesture 성능 및 subject-verification 접근성에 어떤 차이를 만드는지 조사한 연구입니다.

## 문제와 접근

Latent 차원만 줄이는 것과 KL regularization으로 stochastic rate를 제한하는 것은 같지 않습니다. 본 연구는 gesture(G), subject(S), joint(GS) supervision을 비교하고, 같은 정보 예산에 가까운 조건에서 latent로부터 읽을 수 있는 정보를 평가했습니다. 모델은 528-D 입력 → MLP encoder → diagonal Gaussian latent z ~ N(μ, diag(σ²)) → gesture classifier 구조이며, 학습은 cross-entropy와 KL penalty를 결합합니다. 평가 시 posterior mean을 사용한 주요 결과와 별도 sampled-Z 진단은 섞지 않습니다.

```text
528-D sEMG feature → encoder → μ, log σ² → stochastic z → gesture head
                                  └─ KL regularization
```

## 구현 및 재현성 범위

- `src/models/stochastic_bottleneck.py`는 `CommonNoCondition` 모델에서 encoder, reparameterization, KL 계산, classifier를 분리해 정리한 모델 참조 코드입니다. 원본: `Desktop/sEMG/putEMG/scripts/run_putemg_furman_loso_models_v1.py`의 `CommonNoCondition`.
- 기존 주요 프로토콜은 42-subject strict LOSO, 528-D fixed feature cache, fold별 train-only StandardScaler, 15 epochs, batch 512, Adam 1e-3, posterior-mean 평가입니다. 데이터·캐시·학습 runner 전체는 포함하지 않아 이 저장소만으로 실험을 재현할 수 없습니다.
- **학습/실험 실행 명령은 제공하지 않습니다.** 원자료와 고정 cache가 포함되어 있지 않으며, 의도적으로 실행하지 않았습니다.

## 확인된 결과 (서로 다른 분석 버전)

- Locked seed-0 3-condition 결과(alpha=1/.5/0; G/GS/S)에서 achieved Mean KL은 6.689/6.840/6.725, Gesture Macro-F1은 .665/.575/.103, Subject AUC는 .682/.853/.747이었습니다. 보고서에 따르면 rate mismatch는 각각 0.16%, 2.09%, 0.37%입니다. 조건 및 paired-fold 통계는 [`docs/CAMERA_READY_FINAL_DECISION.md`](docs/CAMERA_READY_FINAL_DECISION.md)에 있습니다.
- 위 seed-0 집계는 G endpoint(XPU)와 alpha=.5(XPU)는 구분해 기록하지만 S endpoint는 과거 CPU 결과 재사용입니다. 이 backend 차이를 README의 결과 해석에도 유지합니다.
- 별도 후속 reviewer 분석의 5-seed 집계에서 Gesture Macro-F1은 G=.6666±.0020, GS(alpha=.5)=.5673±.0098, S=.1011±.0018 (seed 단위 mean±sample SD, n=5)이며, ordering은 5/5 seed에서 유지되었습니다. 해당 집계에는 역사적 endpoint beta provenance가 공개되어 있으므로 seed-0 표와 합치지 않았습니다.
- 528-D 차원 축소 또는 KL을 mutual information의 정확한 측정치로 해석하지 않습니다. Subject AUC는 특정 cross-session verification probe의 접근성 지표일 뿐 subject 정보 제거, disentanglement 또는 인과 메커니즘을 입증하지 않습니다.

## 구조

```text
src/models/      stochastic bottleneck model reference
results/         anonymized aggregate CSVs; no fold-level records
figures/         aggregate plots from distinct, labeled analyses
docs/            result provenance and interpretation limits
```

## 연구 상태와 사용 조건

사용자 제공 최신 상태: KoreaAI 2026 1차 심사 통과. 정식 게재나 발표로 표현하지 않습니다. 심사 증빙은 이 repo에 포함하지 않았습니다. 원본 코드에는 재배포 라이선스가 확인되지 않아 이 선별 저장소에도 라이선스를 부여하지 않았습니다. GitHub 공개 전 코드/그림 및 데이터 유래의 공개 권한을 확인해야 합니다.
