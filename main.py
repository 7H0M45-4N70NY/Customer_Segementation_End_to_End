from src.Customer_Segmentation.logger import logging
from src.Customer_Segmentation.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.Customer_Segmentation.pipeline.stage_02_data_validation import DataValidationTrainingPipeline 
from src.Customer_Segmentation.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Customer_Segmentation.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline
from src.Customer_Segmentation.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from src.Customer_Segmentation.exception.exception import customexception
import sys

"""STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
"""
"""STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)

STAGE_NAME = "Data Transformation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)


STAGE_NAME = "Model Trianing stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelTrainerTrainingPipeline()
   model_training.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
"""
STAGE_NAME= "Model Evaluation Stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelEvaluationTrainingPipeline()
   model_training.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)