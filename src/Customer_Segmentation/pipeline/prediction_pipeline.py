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
        self.preprocessor=joblib.load("artifacts\data_transformation\preprocessor.joblib")
    def predict(self,data):
        try:
            mapping = {
            'Settlement size': {'Small': 0, 'Medium': 1, 'Large': 2},
            'Occupation': {'Skilled': 0, "Manager":1,'Business': 2},
            'Education': {'12th': 0, 'Bachelors': 1, 'Masters': 2, 'Phd': 3},
            'Marital status': {'Single': 0, 'Married': 1},
            'Sex': {'Female': 0, 'Male': 1}
            }
        # Map user input to numerical values using np.where
            for feature, value_mapping in mapping.items():
                data[feature] = data[feature].apply(lambda x: value_mapping.get(x, x))
            order=['Sex', 'Marital status', 'Age', 'Education', 
                   'Income','Occupation', 'Settlement size']
            transformed_data=self.preprocessor.transform(data[order])
            prediction=self.model.predict(transformed_data)
            return prediction
        except Exception as e:
            raise customexception(e,sys)
    def predict_bulk(self,data):
        try:
            order=['Sex', 'Marital status', 'Age', 'Education', 
                   'Income','Occupation', 'Settlement size']
            transformed_data=self.preprocessor.transform(data[order])
            prediction=self.model.predict(transformed_data)
            return prediction
        except Exception as e:
            raise customexception(e,sys)
class CustomData:
    def __init__(self,Age:int,Income:int,marital_status:str,Education:str,Occupation:str,Settlement:str,Sex:str):
        self.Age=Age
        self.Income=Income
        self.marital_status=marital_status
        self.Education=Education
        self.Occupation=Occupation
        self.Settlement=Settlement
        self.Sex=Sex
    def get_as_df(self):
        try:
            custom_data_dict={
                "Age":[self.Age],
                "Income":[self.Income],
                "Marital status":[self.marital_status],
                "Education":[self.Education],
                "Occupation":[self.Occupation],
                "Settlement size":[self.Settlement],
                "Sex":[self.Sex]
            }
            df=pd.DataFrame(custom_data_dict)
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customexception(e,sys)   
        





