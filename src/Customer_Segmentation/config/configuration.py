from Customer_Segmentation.constants import *
from Customer_Segmentation.entity.config_entity import (DataIngestionConfig)
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