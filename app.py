
import streamlit as st
import pandas as pd
from pathlib import Path
import joblib

# Configure dashboard
st.set_page_config(
    page_title="AI Energy Forecasting",
    page_icon="⚡",
    layout="wide"
)

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "energy_model.pkl"
DATA_PATH = (
    PROJECT_DIR / "data" / "household_power_consumption.txt"
)

# Dashboard heading
st.title("⚡ AI Energy Consumption Forecasting System")
st.markdown(
    "### Smart electricity forecasting using Machine Learning"
)

st.write(
    "Analyze historical household electricity consumption "
    "and generate preliminary energy estimates."
)

st.divider()

# Check trained model
if not MODEL_PATH.exists():
    st.error("Trained model not found. Please run python main.py first.")
    st.stop()

# Load model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Forecast section
st.header("🔮 Predict Energy Consumption")

col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input("Choose a date")

with col2:
    selected_hour = st.slider(
        "Choose an hour",
        min_value=0,
        max_value=23,
        value=10
    )

if st.button("⚡ Forecast Energy"):
    date = pd.Timestamp(selected_date)

    input_data = pd.DataFrame([{
        "hour": selected_hour,
        "day": date.day,
        "month": date.month,
        "day_of_week": date.dayofweek
    }])

    prediction = float(model.predict(input_data)[0])

    st.subheader("Forecast Result")
    st.metric(
        label="Predicted Global Active Power",
        value=f"{prediction:.3f} kW"
    )

    if prediction >= 2:
        st.warning("Higher estimated power consumption.")
    else:
        st.info("Lower estimated power consumption.")

    st.caption(
        "This is a preliminary model estimate, not a guaranteed "
        "future electricity reading."
    )

st.divider()

# Historical consumption section
st.header("📊 Historical Electricity Consumption")

@st.cache_data
def load_data():
    df = pd.read_csv(
        DATA_PATH,
        sep=";",
        na_values=["?"],
        low_memory=False
    )

    df["Global_active_power"] = pd.to_numeric(
        df["Global_active_power"],
        errors="coerce"
    )

    return df.dropna(subset=["Global_active_power"])

if DATA_PATH.exists():
    with st.spinner("Loading electricity dataset..."):
        energy_df = load_data()

    st.metric(
        "Valid Historical Records",
        f"{len(energy_df):,}"
    )

    st.subheader("Electricity Consumption Trend")
    st.line_chart(
        energy_df["Global_active_power"].iloc[:500]
    )

    st.caption("Displaying the first 500 valid readings.")

else:
    st.warning("Dataset not found. Check your data folder.")

st.divider()

# Footer
st.markdown(
    "**AI Energy Forecasting System** | "
    "Python • Pandas • Scikit-learn • Streamlit"
)
