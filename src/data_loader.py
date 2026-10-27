
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "household_power_consumption.txt"


def load_data():
    print("Loading electricity consumption dataset...")

    if not DATA_FILE.exists():
        print("Dataset not available. Skipping historical chart.")
        return pd.DataFrame()

    df = pd.read_csv(
        DATA_FILE,
        sep=";",
        na_values=["?"],
        low_memory=False
    )

    df["DateTime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        dayfirst=True,
        errors="coerce"
    )

    df.drop(columns=["Date", "Time"], inplace=True)

    df["Global_active_power"] = pd.to_numeric(
        df["Global_active_power"], errors="coerce"
    )

    df.dropna(
        subset=["DateTime", "Global_active_power"],
        inplace=True
    )

    df.sort_values("DateTime", inplace=True)
    df.reset_index(drop=True, inplace=True)

    print(f"Dataset loaded successfully: {len(df)} rows")

    return df


if __name__ == "__main__":
    load_data()
