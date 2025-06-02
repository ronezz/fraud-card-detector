import requests


# Building Example transaction request

url = "http://127.0.0.1:8000/predict"


sample_transaction = {
    "V1": -1.3598,
    "V2": -0.0727,
    "V3": 2.5363,
    "V4": 1.3781,
    "V5": -0.3383,
    "V6": 0.4623,
    "V7": 0.2395,
    "V8": 0.0986,
    "V9": 0.3637,
    "V10": 0.0907,
    "V11": -0.5515,
    "V12": -0.6178,
    "V13": -0.9913,
    "V14": -0.3111,
    "V15": 1.4681,
    "V16": -0.4704,
    "V17": 0.2079,
    "V18": 0.0257,
    "V19": 0.4039,
    "V20": 0.2514,
    "V21": -0.0183,
    "V22": 0.2778,
    "V23": -0.1104,
    "V24": 0.0669,
    "V25": 0.1285,
    "V26": -0.1891,
    "V27": 0.1335,
    "V28": -0.0210,
    "Amount": 149.62
}


response = requests.post(url, json=sample_transaction)

# Show Response
if response.status_code == 200:
    data = response.json()
    print("Fraud Prediction:")
    print("Fraud:", bool(data['fraud_prediction']))
    print("Prob:", data['fraud_probability'])
else:
    print("Error:", response.status_code)
    print(response.text)
