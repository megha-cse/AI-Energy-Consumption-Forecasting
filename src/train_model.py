
import pandas as pd
import joblib
from pathlib import Path
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

def train_model(df):
    print("Training energy forecasting model...")

    features = ["hour", "day", "month", "day_of_week"]
    target = "Global_active_power"

    X = df[features]
    y = df[target]

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", MLPRegressor(
    hidden_layer_sizes=(32,),
    max_iter=50,
    early_stopping=True,
    random_state=42
))
    ])

    model.fit(X, y)

    model_path = MODEL_DIR / "energy_model.pkl"
    joblib.dump(model, model_path)

    print("Model training completed!")
    print(f"Model saved at: {model_path}")

    return model

if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import preprocess_data

    df = preprocess_data(load_data())
    train_model(df)
