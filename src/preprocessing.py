import pandas as pd 
from sklearn.preprocessing import StandardScaler
import joblib
import os

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    x = df.drop(['Class', 'Time'], axis=1)
    y = df['Class']
    
    scaler = StandardScaler()
    x['Amount'] = scaler.fit_transform(x['Amount'].values.reshape(-1,1))
    
    return x, y, scaler
    
def save_scaler(scaler, path='scaler.pkl'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(scaler, path)
    
