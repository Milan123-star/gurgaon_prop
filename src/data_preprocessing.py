import pandas as pd
import numpy as np
from src.logger import *
import os
from sklearn.preprocessing import OrdinalEncoder
train=pd.read_csv(os.path.join('data','raw','train.csv'))
test=pd.read_csv(os.path.join('data','raw','test.csv'))

columns=['property_type','sector','balcony','agePossession','luxury_category','floor_category']
oe=OrdinalEncoder()

train[columns]=oe.fit_transform(train[columns])
test[columns]=oe.fit_transform(test[columns])

train.to_csv(os.path.join('data','raw','processed','train_processed.csv'),index=False)
test.to_csv(os.path.join('data','raw','processed','test_processed.csv'),index=False)



