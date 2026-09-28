# 공개 저장소 선별 감사 — putEMG

- 원본: `Desktop/sEMG/putEMG` (대용량 데이터/캐시/다수 실험 변형 포함).
- 선별: `CommonNoCondition`의 모델 구조 참조 코드, 최종 3조건 및 별도 5-seed 요약 CSV, 집계 figure 3개.
- 버전 구분: `camera_ready_alpha_mix`의 locked seed-0 결과와 `camera_ready_multiseed` reviewer 분석은 별도 표기. 후자는 과거 endpoint beta provenance를 명시하며 seed-0 결과를 대체하지 않음.
- 제외: 모든 raw dataset, 528-D feature cache, subject/fold row CSV, checkpoints, logs, run state, 환경/개인 경로 포함 runner, 실패/중간 실험, 원고 초안 및 심사자료.
- 코드 기여자: 파일 내용은 구현 구조의 증거이지 작성자 신원의 증명은 아님. 이 repo는 원본 Git history를 복사하지 않음.
- 검증: 선택한 숫자는 원본 aggregate/report를 기준으로 README에 버전별 요약. 실험 미실행. 라이선스/재배포 권한과 심사 증빙은 별도 확인 필요.
