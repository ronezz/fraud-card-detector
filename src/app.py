from fastapi import FastAPI
from pydantic import create_model
import joblib
import pandas as pd
import numpy as np
import os

# Load Models
model = joblib.load(os.path.abspath("src/model.pkl"))
scaler = joblib.load(os.path.abspath("src/scaler.pkl"))

# Create pydantic model
fields = {f"V{i}": (float, ...) for i in range(1, 29)}
fields["Amount"] = (float, ...)
Transaction = create_model("Transaction", **fields)

app = FastAPI()

@app.post("/predict")
def predict(tx: Transaction): # type: ignore
    # Convert transaction to DataFrame
    tx_dict = tx.dict()
    df = pd.DataFrame([tx_dict])

    # Scale and predict
    df['Amount'] = scaler.transform(df['Amount'].values.reshape(-1, 1))

    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "fraud_prediction": int(prediction),
        "fraud_probability": float(np.round(proba, 4))
    }
