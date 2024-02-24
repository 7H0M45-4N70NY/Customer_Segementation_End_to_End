import os
from pathlib import Path
from Customer_Segmentation.logger import logging
from Customer_Segmentation.entity.config_entity import DataValidationConfig
import pandas as pd
import sys
from Customer_Segmentation.exception.exception import customexception

class DataValidation:
    def __init__(self,config=DataValidationConfig):
        self.config=config
    def get_data_validation(self):
        logging.info("Data Validation started")
        try:
            validation_status=None
            train=pd.read_csv(self.config.target_file)
            all_schema=self.config.all_schema
            for i,j in all_schema.items():
                if i in train.columns and train[i].dtype==j:
                    validation_status=True
                    with open(self.config.result_path,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=False
                    with open(self.config.file_path,'w') as f:
                        f.write(f" Vlaidtaion status : {validation_status}")
            return validation_status
        except Exception as e:
            raise customexception(e,sys)
               