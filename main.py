from src.Customer_Segmentation.logger import logging
from src.Customer_Segmentation.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.Customer_Segmentation.exception.exception import customexception
import sys

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)