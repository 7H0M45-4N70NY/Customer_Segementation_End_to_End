import os
import pandas as pd 
from sklearn.metrics import silhouette_score
from Customer_Segmentation.utils.common import save_json
import numpy as np 
import joblib
from Customer_Segmentation.entity.config_entity import ModelEvaluationConfig,ModelTrainingConfig
import mlflow
import mlflow.sklearn
from Customer_Segmentation.logger import logging
from Customer_Segmentation.exception.exception import customexception
from urllib.parse import urlparse
import sys
from pathlib import Path



class ModelEvaluation:
    def __init__(self,config=ModelEvaluationConfig):
        self.config=config
    def initiate_model_evaluation(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)
        mlflow.set_registry_uri("")   #Dax hub
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
        logging.info("Model has registered")
        preds=model.predict(test_data)
        silhoutte=silhouette_score(test_data,preds)
        save_json(path=Path(self.config.metric_file_name), data={"silhouttes_score":silhoutte}) 
        with mlflow.start_run():
        # Log other model parameters as needed
            mlflow.log_param("n_clusters", model.n_clusters)
            mlflow.log_param("init", model.init)
            # Log other hyperparameters as needed

            mlflow.log_metric("silhouette_score", silhoutte)
            if tracking_url_type_store !="file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
            else :
                mlflow.sklearn.log_model(model,"model")
                



        
    
        