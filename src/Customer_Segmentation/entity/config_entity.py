from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    file_key : str
    download_path : Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    target_file: Path
    result_path: Path
    all_schema: dict