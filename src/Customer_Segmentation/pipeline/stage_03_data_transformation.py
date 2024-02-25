from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.components.data_transformation import DataTansformation
from Customer_Segmentation.logger import logging
import sys
from Customer_Segmentation.exception.exception import customexception
from pathlib import Path



STAGE_NAME = "Data Tranformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/result.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status == "True":
                config=ConfigurationManager()
                data_vaidation_config=config.get_data_transfomration_config()
                data_vaidation=DataTansformation(config=data_vaidation_config)
                data_vaidation.initialize_Data_transfomration()
            else:
                raise Exception("You data schema is not valid")
        except Exception as e:
            print(customexception(e,sys))

if __name__=="__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
        