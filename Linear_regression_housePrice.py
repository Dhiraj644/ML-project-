import streamlit as st
import pickle
import pandas as pd

# Page Config (Best practice to put this right at the top)
st.set_page_config(
    page_title="California House Price Predictor",
    layout="centered"
)

# Load Model with caching to optimize performance
@st.cache_resource
def load_model():
    with open("Linear_regression_california.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Title & Subheaders
st.title("🏠 California House Price Predictor")
st.subheader("Developed by Dhiraj Ekal")
st.write("Enter property details to predict the house value.")

# Sidebar Information
st.sidebar.header("📋 Feature Description")
st.sidebar.write("""
**Median Income** → Average income of households in the area.

**House Age** → Age of houses in the area (years).

**Area Population** → Total population in the area.

**Average Occupancy** → Average number of people living in a house.

**Average Bedrooms** → Average number of bedrooms per house.

**Property Latitude** → Geographical latitude of the property location.
""")

# Input Fields
median_income = st.number_input(
    "💰 Median Income",
    min_value=0.0,
    value=5.0,
    step=0.1
)

house_age = st.number_input(
    "⏳ House Age (Years)",
    min_value=0.0,
    value=20.0,
    step=1.0
)

area_population = st.number_input(
    "👥 Area Population",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

average_occupancy = st.number_input(
    "👨‍👩‍👧‍👦 Average Occupancy",
    min_value=0.0,
    value=3.0,
    step=0.1
)

average_bedrooms = st.number_input(
    "🛏️ Average Bedrooms",
    min_value=0.0,
    value=1.0,
    step=0.1
)

property_latitude = st.number_input(
    "📍 Property Latitude",
    value=34.0,
    step=0.01
)

# Prediction Logic
if st.button("Predict House Value", type="primary"):

    input_data = pd.DataFrame(
        [[
            median_income,
            house_age,
            area_population,
            average_occupancy,
            average_bedrooms,
            property_latitude
        ]],
        columns=[
            "MedInc",
            "HouseAge",
            "Population",
            "AveOccup",
            "AveRooms",
            "Latitude"
        ]
    )

    # Generate prediction from model
    prediction = model.predict(input_data)
    
    # Scale prediction (assuming model output is in $100k blocks)
    house_price = prediction[0] * 100000

    # Display the result formatted nicely as currency
    st.success(f"### 🎉 Predicted House Value: ${house_price:,.2f}")

    st.info(
        "The predicted value is based on the trained California Housing Linear Regression model."
    )
