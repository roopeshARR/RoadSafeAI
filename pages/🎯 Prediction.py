"""
=========================================================
RoadSafe AI
AI Accident Severity Prediction
=========================================================
Author : Avuthu Roopesh Reddy
"""

# ==========================================================
# IMPORTS
# ==========================================================

import json
from pathlib import Path

import streamlit as st

from services.prediction_service import SeverityPredictor


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Severity Prediction",
    page_icon="🚦",
    layout="wide"
)


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_predictor():
    return SeverityPredictor()


predictor = load_predictor()
feature_info = predictor.feature_info


# ==========================================================
# LOAD MODEL METRICS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

METRICS_PATH = PROJECT_ROOT / "models" / "model_metrics.json"

try:

    with open(METRICS_PATH, "r", encoding="utf-8") as file:

        model_metrics = json.load(file)

except:

    model_metrics = None


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def clean_label(text):

    return (
        str(text)
        .replace("_", " ")
        .replace("  ", " ")
        .strip()
    )


def create_dropdown(label, column_name):

    values = feature_info["categorical_values"][column_name]

    options = {
        clean_label(value): value
        for value in values
    }

    selected = st.selectbox(
        label,
        list(options.keys())
    )

    return options[selected]


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🚦 AI Accident Severity Prediction")

st.write(
    """
Estimate the expected severity of a road accident using a
machine learning model trained on historical accident records.
"""
)

st.divider()


# ==========================================================
# USER INPUT
# ==========================================================

user_input = {}
# ==========================================================
# PREDICTION FORM
# ==========================================================

with st.form("prediction_form"):

    # ======================================================
    # DRIVER INFORMATION
    # ======================================================

    st.subheader("👤 Driver Information")

    col1, col2 = st.columns(2)

    with col1:

        user_input["Day_of_week"] = create_dropdown(
            "Day of Week",
            "Day_of_week"
        )

        user_input["Age_band_of_driver"] = create_dropdown(
            "Driver Age",
            "Age_band_of_driver"
        )

        user_input["Sex_of_driver"] = create_dropdown(
            "Driver Gender",
            "Sex_of_driver"
        )

        user_input["Educational_level"] = create_dropdown(
            "Educational Level",
            "Educational_level"
        )

        user_input["Driving_experience"] = create_dropdown(
            "Driving Experience",
            "Driving_experience"
        )

    with col2:

        user_input["Vehicle_driver_relation"] = create_dropdown(
            "Driver Relation",
            "Vehicle_driver_relation"
        )

        user_input["Owner_of_vehicle"] = create_dropdown(
            "Vehicle Owner",
            "Owner_of_vehicle"
        )

        user_input["Service_year_of_vehicle"] = create_dropdown(
            "Vehicle Service Year",
            "Service_year_of_vehicle"
        )

        user_input["Defect_of_vehicle"] = create_dropdown(
            "Vehicle Defect",
            "Defect_of_vehicle"
        )

    st.divider()

    # ======================================================
    # VEHICLE INFORMATION
    # ======================================================

    st.subheader("🚗 Vehicle Information")

    col1, col2 = st.columns(2)

    with col1:

        user_input["Type_of_vehicle"] = create_dropdown(
            "Vehicle Type",
            "Type_of_vehicle"
        )

        user_input["Vehicle_movement"] = create_dropdown(
            "Vehicle Movement",
            "Vehicle_movement"
        )

    with col2:

        user_input["Number_of_vehicles_involved"] = st.number_input(
            "Number of Vehicles Involved",
            min_value=1,
            max_value=20,
            value=2,
            step=1
        )

    st.divider()

    # ======================================================
    # ROAD INFORMATION
    # ======================================================

    st.subheader("🛣 Road Information")

    col1, col2 = st.columns(2)

    with col1:

        user_input["Area_accident_occured"] = create_dropdown(
            "Accident Area",
            "Area_accident_occured"
        )

        user_input["Lanes_or_Medians"] = create_dropdown(
            "Road Lanes / Median",
            "Lanes_or_Medians"
        )

        user_input["Road_allignment"] = create_dropdown(
            "Road Alignment",
            "Road_allignment"
        )

        user_input["Types_of_Junction"] = create_dropdown(
            "Type of Junction",
            "Types_of_Junction"
        )

    with col2:

        user_input["Road_surface_type"] = create_dropdown(
            "Road Surface Type",
            "Road_surface_type"
        )

        user_input["Road_surface_conditions"] = create_dropdown(
            "Road Surface Condition",
            "Road_surface_conditions"
        )

        user_input["Light_conditions"] = create_dropdown(
            "Light Condition",
            "Light_conditions"
        )

        user_input["Weather_conditions"] = create_dropdown(
            "Weather Condition",
            "Weather_conditions"
        )

    st.divider()

    # ======================================================
    # ACCIDENT INFORMATION
    # ======================================================

    st.subheader("⚠ Accident Information")

    col1, col2 = st.columns(2)

    with col1:

        user_input["Type_of_collision"] = create_dropdown(
            "Type of Collision",
            "Type_of_collision"
        )

        user_input["Pedestrian_movement"] = create_dropdown(
            "Pedestrian Movement",
            "Pedestrian_movement"
        )

    with col2:

        user_input["Cause_of_accident"] = create_dropdown(
            "Cause of Accident",
            "Cause_of_accident"
        )

        user_input["Hour"] = st.slider(
            "Hour of Accident",
            min_value=0,
            max_value=23,
            value=12
        )

    st.divider()

    # ======================================================
    # SUBMIT BUTTON
    # ======================================================

    predict_button = st.form_submit_button(
        "🚦 Predict Accident Severity",
        use_container_width=True,
        type="primary"
    )
# ==========================================================
# PREDICTION
# ==========================================================

if predict_button:

    with st.spinner("Analyzing accident conditions..."):

        result = predictor.predict(user_input)

    prediction = result["prediction"]
    confidence = result["confidence"]
    probabilities = result["probabilities"]

    st.divider()

    # ======================================================
    # PREDICTION RESULT
    # ======================================================

    st.subheader("📊 Prediction Result")

    if prediction == "Fatal injury":

        st.error(f"""
### 🔴 Fatal Injury

**Confidence : {confidence:.2f}%**
""")

    elif prediction == "Serious Injury":

        st.warning(f"""
### 🟠 Serious Injury

**Confidence : {confidence:.2f}%**
""")

    else:

        st.success(f"""
### 🟢 Slight Injury

**Confidence : {confidence:.2f}%**
""")

    # ======================================================
    # PROBABILITY SUMMARY
    # ======================================================

    st.subheader("📋 Probability Summary")

    probability_data = []

    for label, value in sorted(
        probabilities.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        probability_data.append({

            "Severity": label,

            "Probability (%)": round(value, 2)

        })

    st.dataframe(
        probability_data,
        use_container_width=True,
        hide_index=True
    )
# ==========================================================
# AI INTERPRETATION
# ==========================================================

    st.subheader("🤖 AI Interpretation")

    if prediction == "Fatal injury":

      st.error("""
**High Risk Scenario**

The accident conditions indicate a high probability of a fatal outcome.

**Recommended Actions**
- Reduce vehicle speed
- Follow traffic regulations
- Avoid risky overtaking
- Ensure immediate emergency response
""")

    elif prediction == "Serious Injury":

      st.warning("""
**Moderate to High Risk Scenario**

The accident is likely to result in serious injuries.

**Recommended Actions**
- Drive cautiously
- Maintain safe distance
- Reduce speed in adverse conditions
- Improve driver awareness
""")

    else:

         st.success("""
**Lower Risk Scenario**

The predicted severity is slight injury, but accidents can still cause
injuries and property damage.

**Recommended Actions**
- Follow traffic rules
- Wear seat belts
- Stay alert while driving
- Maintain safe vehicle distance
""")

st.divider()


# ==========================================================
# SAFETY REMINDER
# ==========================================================

st.subheader("🚦 Road Safety Tips")

col1, col2 = st.columns(2)

with col1:

    st.info("""
✔ Wear Seat Belt

✔ Follow Speed Limits

✔ Avoid Mobile Phone Usage

✔ Obey Traffic Signals
""")

with col2:

    st.info("""
✔ Maintain Safe Distance

✔ Do Not Drink and Drive

✔ Drive Carefully in Bad Weather

✔ Keep Vehicle Well Maintained
""")