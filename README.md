# AEGIS

임상 기록에 일관된 가명 처리와 정보 일반화를 적용하고 처리 결과를 점검한다.

## 실행 순서

1. 프로젝트 루트에서 실행한다. 경로는 `project_paths.py`에서 설정하며 `AEGIS_DATA_ROOT`, `AEGIS_OUTPUT_ROOT`로 변경할 수 있다.
2. `notebooks/01_standardize_columns.ipynb`를 실행한다.
3. `notebooks/02_create_patient_mapping.ipynb`와 `03_apply_exclusions.ipynb`를 순서대로 실행한다.
4. `notebooks/04_process_*.ipynb`를 각각 위에서 아래로 한 번씩 실행한다.
5. `notebooks/05_validate_deidentification.ipynb`로 결과를 확인한다.
