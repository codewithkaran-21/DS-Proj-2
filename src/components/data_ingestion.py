import os , sys 
import pandas as pd 
import numpy as np 
from src.logger import logging
from src.exception import CustomeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifact/data_ingestion","train_csv")
    test_data_path = os.path.join("artifact/data_ingestion","test_csv")
    raw_data_path = os.path.join("artifacts/data_ingestion", "raw.csv")