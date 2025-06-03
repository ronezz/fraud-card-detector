# Fraud Card Detection API

**Fraud Card Detection** is a machine learning API that predicts whether a credit card transaction is fraudulent based on a set of input features.

This project showcases the use of core DevOps tools like Docker, Terraform, and AWS EC2 to automate the deployment of a fraud detection API, with a user-friendly HTML interface served via NGINX.

---

## 🛠 Technologies Used

- **Python 3.12 + FastAPI**
- **Scikit-learn + Joblib**
- **HTML + JavaScript (Bootstrap)**
- **Docker**
- **Terraform**
- **AWS EC2**
- **NGINX**
- **Git**

---

##  Project Structure

```
fraud-card-detector/
├── src/
│   └── app.py                # FastAPI backend API
├── fraud-ui/
│   └── index.html            # HTML + JS frontend
├── model.pkl                 # Trained ML model
├── Dockerfile                # Docker configuration
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   └── init.sh
└── README.md
```

---

##  Docker

### Build the image

```bash
docker build -t fraud-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 --name fraud_backend fraud-api
```

> The backend will be available at `http://localhost:8000/predict`

---

##  Frontend (local)

You can serve the HTML file using Python:

```bash
cd fraud-ui
python3 -m http.server 8080
```

Then visit: `http://localhost:8080/index.html`

> The frontend sends JSON input to the backend and displays the prediction.

---

## ☁️ Deploy to AWS EC2 with Terraform

### Prerequisites

- AWS account
- AWS CLI configured (`aws configure`)
- SSH key (`ssh-keygen -t rsa -f ~/.ssh/fraud-key`)

### Steps

1. Go to the `terraform/` folder
2. Replace the public key path in `main.tf`:

```hcl
public_key = file("~/.ssh/fraud-key.pub")
```

3. Launch the infrastructure:

```bash
terraform init
terraform apply
```

4. Once deployed, visit:

```
http://<PUBLIC_IP>/
```

> You will see the HTML UI. Transactions are sent to the backend through NGINX reverse proxy.

---

## 📤 Endpoint

### `POST /predict`

Send a JSON like this:

```json
{
  "V1": -1.3598071336738,
  "V2": -0.0727811733098497,
  "V3": 2.53634673796914,
  "V4": 1.37815522427443,
  "V5": -0.338320769942518,
  ...
  "V28": 0.021572,
  "Amount": 149.62
}
```

### Response:

```json
{
  "prediction": 0
}
```

Where:
- `0` means **not fraudulent**
- `1` means **fraud detected**
