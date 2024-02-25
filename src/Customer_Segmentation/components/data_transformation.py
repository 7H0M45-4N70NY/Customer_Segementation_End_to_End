import os
import sys
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from Customer_Segmentation.utils.common import save_bin
from Customer_Segmentation.logger import logging
from Customer_Segmentation.entity.config_entity import DataTransfomrationConfig
from Customer_Segmentation.exception.exception import customexception


class DataTansformation:
    def __init__(self,config=DataTransfomrationConfig):
        self.config=config
    def run_transformation(self):
        try:
            logging.info('Data Transformation initiated')
            logging.info('Pipeline Initiated')
            column_transformer=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="median")),
                    ('scaler',StandardScaler()),
                    ('pca',PCA(n_components=self.config.n_components,random_state=self.config.random_state))
                    ])
            logging.info('Pipeline created')
            return column_transformer
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
    def initialize_Data_transfomration(self):
        try:
            X=pd.read_csv(self.config.data_path)
            X=X.drop("ID",axis=1)
            logging.info("Successfully read files")
            preprocessing_obj=self.run_transformation()
            final_data=pd.DataFrame(preprocessing_obj.fit_transform(X))
            final_data.to_csv(os.path.join(self.config.root_dir,"final_data.csv"),index=False)
            logging.info("Transformed data has beem stored to trnasformation artifacts")
            save_bin(preprocessing_obj,os.path.join(self.config.root_dir,"preprocessor.joblib"))
            logging.info("trained Preprocesser saved to transformation artifacts")
            logging.info(final_data.shape)
            logging.info("Finished  transformation componenets activities")
            print("ok")
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)






            
                

