
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def evaluate_model(df, model):
    print("Evaluating forecasting model...")

    features = ["hour", "day", "month", "day_of_week"]
    target = "Global_active_power"

    X = df[features]
    y = df[target]

    split_index = int(len(df) * 0.8)
    X_test = X.iloc[split_index:]
    y_test = y.iloc[split_index:]

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("\n--- Model Evaluation Results ---")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    output_dir = Path(__file__).resolve().parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(y_test.iloc[:200].to_numpy(), label="Actual")
    plt.plot(predictions[:200], label="Predicted")
    plt.title("Actual vs Predicted Energy Consumption")
    plt.xlabel("Test Sample")
    plt.ylabel("Global Active Power (kW)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "actual_vs_predicted.png", dpi=150)
    plt.close()

    print("Comparison graph saved in outputs/actual_vs_predicted.png")

    return predictions, y_test
