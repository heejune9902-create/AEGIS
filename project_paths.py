"""프로젝트 공통 경로 설정."""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_ROOT = Path(os.environ.get("AEGIS_DATA_ROOT", PROJECT_ROOT / "data")).expanduser().resolve()
RAW_DIR = DATA_ROOT / "raw"
PROCESSED_DIR = DATA_ROOT / "processed"
OUTPUT_DIR = Path(os.environ.get("AEGIS_OUTPUT_ROOT", PROJECT_ROOT / "outputs")).expanduser().resolve()

PATIENT_MAPPING_PATH = PROCESSED_DIR / "AEGIS-PT" / "pt_noise_date_time.csv"

def deidentified_path(source_path):
    """원본 테이블의 하위 폴더를 유지해 처리본 경로를 만든다."""
    relative = Path(source_path).resolve().relative_to(DATA_ROOT)
    parts = list(relative.parts)
    for index, part in enumerate(parts[:-1]):
        if part in {"raw", "raw2"}:
            parts[index] = "de"
            break
    else:
        raise ValueError(f"원본 폴더 하위 파일이 아닙니다: {source_path}")
    target = PROCESSED_DIR.joinpath(*parts)
    return str(target.with_name(target.stem + "_de2.csv"))
