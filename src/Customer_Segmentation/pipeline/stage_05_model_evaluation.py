from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.components.model_evaluation import ModelEvaluation
from Customer_Segmentation.logger import logging as  logger
from Customer_Segmentation.exception.exception import customexception
import sys

STAGE_NAME = "Model Evlaution stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer_config = ModelEvaluation(config=model_trainer_config)
        model_trainer_config.initiate_model_evaluation()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise customexception(e,sys)