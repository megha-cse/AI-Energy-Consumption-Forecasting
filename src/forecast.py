
from datetime import datetime
import pandas as pd

def forecast_energy(model, year, month, day, hour):
    date = datetime(year, month, day, hour)

    data = pd.DataFrame([{
        "hour": date.hour,
        "day": date.day,
        "month": date.month,
        "day_of_week": date.weekday()
    }])

    prediction = model.predict(data)[0]

    print("\n--- Energy Consumption Forecast ---")
    print("Date and time:", date.strftime("%Y-%m-%d %H:%M"))
    print(f"Predicted global active power: {prediction:.3f} kW")

    return prediction
