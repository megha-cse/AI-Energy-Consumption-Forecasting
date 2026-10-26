from src.visualize import visualize_energy
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.forecast import forecast_energy

def main():
    print("=" * 45)
    print("AI ENERGY CONSUMPTION FORECASTING SYSTEM")
    print("=" * 45)

    df = preprocess_data(load_data())
    visualize_energy(df)
    model = train_model(df)

    evaluate_model(df, model)

    forecast_energy(
        model,
        year=2026,
        month=10,
        day=26,
        hour=10
    )

    print("\nAll steps completed successfully!")

if __name__ == "__main__":
    main()
