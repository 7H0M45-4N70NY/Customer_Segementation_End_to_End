from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.components.data_ingestion_component import DataIngestion
from Customer_Segmentation.logger import logging
import sys
from Customer_Segmentation.exception.exception import customexception


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()

if __name__=='__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise custom_exception(e,sys)
        