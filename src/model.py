# src/model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import joblib
import os

def train_model(X_train, y_train):
    """Entrena un modelo RandomForest con balanceo de clases."""
    model = RandomForestClassifier(
        n_estimators=100,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evalúa el modelo y muestra métricas relevantes."""
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, y_pred))
    print("AUC:", roc_auc_score(y_test, y_proba))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def save_model(model, path='model.pkl'):
    """Guarda el modelo entrenado en disco."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
