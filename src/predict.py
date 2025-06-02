import joblib
import pandas as pd

def load_model(path='model.pkl'):
    
    return joblib.load(path)

def load_scaler(path='scaler.pkl'):
    
    return joblib.load(path)

def preprocess_transaction(transaction_df, scaler):
    transaction_df['Amount'] = scaler.transform(transaction_df['Amount'].values.reshape(-1, 1))
    return transaction_df

def predict_transaction(model, transaction_df):

    return model.predict(transaction_df), model.predict_proba(transaction_df)
