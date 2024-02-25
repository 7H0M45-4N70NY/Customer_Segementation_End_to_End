import os
import sys
import pandas as pd
import numpy as np
from Customer_Segmentation.exception.exception import customexception
from Customer_Segmentation.utils.common import save_bin
from Customer_Segmentation.logger import logging
from Customer_Segmentation.entity.config_entity import ModelTrainingConfig
from sklearn.cluster import KMeans

class ModelTraining:
    def __init__(self,config=ModelTrainingConfig):
        self.config=config
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        logging.info("Successfully read the data")
        model=KMeans(n_clusters=self.config.n_clusters,random_state=self.config.random_state,
                     max_iter=self.config.max_iter,tol=self.config.tol,init='k-means++',n_init=1)
        logging.info("Model setup")
        model.fit(train_data)
        logging.info("Finished model training")
        save_bin(model,os.path.join(self.config.root_dir,self.config.model_name))
        logging.info("Model saved to training artificats")
        print("I love you")

