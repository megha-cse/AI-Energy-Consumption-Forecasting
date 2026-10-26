
import pandas as pd

def preprocess_data(df):
    print("Preprocessing electricity data...")

    df = df.copy()
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    df["hour"] = df["DateTime"].dt.hour
    df["day"] = df["DateTime"].dt.day
    df["month"] = df["DateTime"].dt.month
    df["day_of_week"] = df["DateTime"].dt.dayofweek

    df["Global_active_power"] = pd.to_numeric(
        df["Global_active_power"], errors="coerce"
    )

    df = df.dropna(subset=["Global_active_power"])
    df = df.sort_values("DateTime").reset_index(drop=True)

    print("Preprocessing completed!")
    print("Final dataset shape:", df.shape)
    print(df.head())

    return df
