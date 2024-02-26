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


@dataclass(frozen=True)  
class DataTransfomrationConfig:
    root_dir: Path
    data_path: Path
    n_components: float
    random_state: int

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    model_name: str
    n_clusters: int
    random_state:42
    max_iter:1000
    tol:float

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    
