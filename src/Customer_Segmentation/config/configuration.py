from Customer_Segmentation.constants import *
from Customer_Segmentation.entity.config_entity import (DataIngestionConfig,DataValidationConfig,
                                                        DataTransfomrationConfig,ModelTrainingConfig,
                                                        ModelEvaluationConfig)
from Customer_Segmentation.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            scheme_filepath=SCHEMA_FILE_PATH
    ):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(scheme_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            file_key=config.file_key,
            download_path=config.download_path
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            target_file=config.target_file,
            result_path=config.result_path,
            all_schema=schema
        )
        return data_validation_config
    def get_data_transfomration_config(self)->DataTransfomrationConfig:
        config=self.config.data_transformation
        params=self.params.PCA
        create_directories([config.root_dir])
        data_transformation_config=DataTransfomrationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            n_components=params.n_components,
            random_state=params.random_state
        )
        return data_transformation_config
        
    def get_model_training_config(self)->ModelTrainingConfig:
        config=self.config.model_training
        params=self.params.KMeans
        create_directories([config.root_dir])
        model_training_config=ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            model_name=config.model_name,
            n_clusters=params.n_clusters,
            random_state=params.random_state,
            max_iter=params.max_iter,
            tol=params.tol
        )
        return model_training_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config=self.config.model_evaluation
        create_directories([config.root_dir])
        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name
        )   
        return model_evaluation_config 
    
