from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.components.data_validation import DataValidation
from Customer_Segmentation.logger import logging
import sys
from Customer_Segmentation.exception.exception import customexception


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_vaidation_config=config.get_data_validation_config()
        data_vaidation=DataValidation(config=data_vaidation_config)
        data_vaidation.get_data_validation()

if __name__=="__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
        
