from copyreg import pickle
from io import StringIO
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

file = open("../Model/engine_model.sav",'rb')
model = pickle.load(file)
file.close()

file = open("../Model/truth.sav",'rb')
truth_ds = pickle.load(file)
file.close()

def predict(data):
    try:
        col_name = ['id','cycle','set1','set2','set3','s1','s2','s3','s4','s5','s6','s7','s8']+['s9','s10','s11','s12','s13','s14','s14','s15','s16','s17','s18','s19','s20']
        test_dataset = pd.DataFrame([data],columns=col_name)
        rul=pd.DataFrame(test_dataset.groupby("id")['cycle'].max()).reset_index()
        rul.columns = ['id','max']
        truth_ds['rtf']=truth_ds['more']+rul["max"]
        truth_ds.head()
        truth_ds['rtf']=truth_ds['more']+rul["max"]
        test_dataset=test_dataset.merge(truth_ds, on= ['id'], how= "left")
        test_dataset[ 'ttf']=test_dataset['rtf'] - test_dataset['cycle']
        test_dataset.drop ('rtf', axis=1, inplace=True)
        df_test = test_dataset.copy()
        period = 30
        df_test['label_bc'] = df_test ['ttf'].apply(lambda x: 1 if x <= period else 0)
        df_test = df_test.dropna()
        if len(df_test.index) == 0 :
            return True
        x_test = df_test.iloc[ : , : -2].values
        y_pred = model.predict(x_test)
        return True if y_pred[0] else False
    except:
        return True