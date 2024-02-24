from Customer_Segmentation.constants import *
from Customer_Segmentation.entity.config_entity import (DataIngestionConfig,DataValidationConfig)
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

if __name__=="__main__":
    obj=ConfigurationManager()
    print(obj.schema)
