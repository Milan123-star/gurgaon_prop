import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
import os
import pickle

X_train=pd.read_csv(os.path.join('data','raw','processed','train_processed.csv')).drop(columns='price')
y_train=pd.read_csv(os.path.join('data','raw','processed','train_processed.csv'))[['price']]
X_test=pd.read_csv(os.path.join('data','raw','processed','test_processed.csv')).drop(columns='price')
y_test=pd.read_csv(os.path.join('data','raw','processed','test_processed.csv'))[['price']]

rf=RandomForestRegressor()
rf.fit(X_train,y_train)
y_pred=rf.predict(X_test)
print(r2_score(y_pred,y_test))

model_path = os.path.join('data','raw','model','model.pkl')


with open(model_path, 'wb') as f:
    pickle.dump(rf, f)

