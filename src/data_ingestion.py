import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.logger import *
import yaml
import os
def params_load(param_path):
    try:
        with open(param_path,'r') as f:
            data=yaml.safe_load(f)
            test_size=data['data_ingestion']['test_size']
            logger.info(f'test_size:{test_size}')
    except Exception as e:
        logger.error(e)

def data_load(file_path):
    try:
        df=pd.read_csv(file_path)
        return df
    except Exception as e:
        logger.error(e)
def main():
    test_size=params_load(os.path.join('params.yaml'))
    df=data_load(os.path.join('gurgaon_properties_cleaned_v2.csv'))
    

    train,test=train_test_split(df,test_size=test_size,random_state=42)
    train.to_csv(os.path.join('data','raw','train.csv'))
    test.to_csv(os.path.join('data','raw','test.csv'))

main()    



