import os
from pathlib import Path
from Customer_Segmentation.logger import logging
from Customer_Segmentation.entity.config_entity import DataIngestionConfig
from Customer_Segmentation.utils.common import get_size
import pandas as pd 
import sys
from Customer_Segmentation.exception.exception import customexception

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, EndpointConnectionError

from dotenv import load_dotenv
load_dotenv()

access_key=os.getenv("YOUR_ACCESS_KEY")
secret_key=os.getenv("YOUR_SECRET_KEY")


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            self.download_from_s3()
            logging.info("File downloaded from S3 successfully")
            #logging.info("Creating Ingestion file")
            #os.makedirs(os.path.dirname(os.path.join(self.config.download_path)),exist_ok=True)
            #self.download_from_s3('my-ml-projects', self.config.file_key, self.config.download_path)
            data=pd.read_csv(self.config.download_path)
            logging.info("Reading File")
            data.to_csv(self.config.download_path,index=False)
        except Exception as e:
            logging.info("Data Ingestion failed")
            raise customexception(e,sys)
        
    def download_from_s3(self):
        # Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with your AWS credentials
        aws_access_key_id = access_key
        aws_secret_access_key = secret_key
        
        # Create an S3 client
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        try:
            # Download the file from S3
            s3.download_file('my-ml-projects', self.config.file_key, self.config.download_path)
            logging.info(f"File downloaded successfully to {self.config.download_path}")
        except NoCredentialsError:
            print("AWS credentials not available or incorrect.")
        except PartialCredentialsError:
            print("Partial AWS credentials provided.")
        except EndpointConnectionError:
            print("Could not connect to the S3 endpoint. Check the AWS region.")
        except Exception as e:
            print(f"Error downloading file: {e}")