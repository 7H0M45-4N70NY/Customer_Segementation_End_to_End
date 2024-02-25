from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.components.model_training import ModelTraining
from Customer_Segmentation.logger import logging as logger 
import sys
from Customer_Segmentation.exception.exception import customexception

STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer_config = ModelTraining(config=model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise customexception(e,sys)