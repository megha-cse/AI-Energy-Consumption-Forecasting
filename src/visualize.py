
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def visualize_energy(df):
    print("Creating electricity consumption graph...")

    # Use a small sample to keep the graph readable
    sample = df.iloc[::60].copy()

    plt.figure(figsize=(12, 5))
    plt.plot(
        sample["DateTime"],
        sample["Global_active_power"],
        linewidth=1
    )

    plt.title("Household Electricity Consumption Over Time")
    plt.xlabel("Date and Time")
    plt.ylabel("Global Active Power (kW)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph_path = OUTPUT_DIR / "energy_consumption.png"
    plt.savefig(graph_path, dpi=150)
    plt.close()

    print(f"Graph saved successfully: {graph_path}")

if __name__ == "__main__":
    from data_loader import load_data
    from preprocessing import preprocess_data

    df = preprocess_data(load_data())
    visualize_energy(df)
