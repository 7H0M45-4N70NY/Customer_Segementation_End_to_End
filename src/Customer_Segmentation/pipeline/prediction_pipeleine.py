import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from Customer_Segmentation.components.data_transformation import DataTansformation
from Customer_Segmentation.config.configuration import ConfigurationManager
from Customer_Segmentation.logger import logging
from Customer_Segmentation.exception.exception import customexception
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load("artifacts/model_training/model.joblib")
    def predict(self,data):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transfomration_config()
            preprocessor=DataTansformation(config=data_transformation_config)
            transformed_data=preprocessor.run_transformation(data)
            prediction=self.model.predict(transformed_data)
            return prediction
        except Exception as e:
            raise customexception(e,sys)
class CustomData:
    def __init__(self,
                 
    )


