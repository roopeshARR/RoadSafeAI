import streamlit as st

from config import PROJECT_NAME, PROJECT_TAGLINE
from components.sidebar import show_sidebar

st.set_page_config(
    page_title=f"{PROJECT_NAME} | About",
    page_icon="ℹ️",
    layout="wide"
)

show_sidebar()

st.title("ℹ️ About RoadSafe AI")

st.caption(PROJECT_TAGLINE)

st.divider()

st.subheader("📌 Project Overview")

st.write("""
**RoadSafe AI** is a data-driven road accident analysis and severity prediction
platform developed to analyze accident trends and identify high-risk conditions.

The application helps users visualize accident data, explore accident patterns,
identify risk factors, predict accident severity using machine learning, and
generate meaningful insights through interactive dashboards.
""")

st.divider()

st.subheader("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- 📊 Interactive Dashboard
- 🗺️ Accident Location Mapping
- ⚠️ Risk Analysis
- 🎯 Accident Severity Prediction
""")

with col2:
    st.markdown("""
- 🤖 AI-Based Insights
- 📈 Interactive Charts
- 🔍 Data Filtering
- 📍 Geographic Visualization
""")

st.divider()

st.subheader("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
**Frontend**
- Streamlit
- Plotly
""")

with col2:
    st.markdown("""
**Backend**
- Python
- Pandas
- NumPy
""")

with col3:
    st.markdown("""
**Machine Learning**
- Scikit-learn
- Joblib
""")

st.divider()

st.subheader("📂 Dataset")

st.write("""
This project uses a cleaned and integrated **Indian Road Accident Dataset**
covering the years **2017–2025**.

The dataset includes:

- Date and Time
- Year and Month
- State and City
- Weather Conditions
- Road Type
- Traffic Density
- Casualties
- Risk Score
- Accident Severity
- Geographic Coordinates (Latitude & Longitude)

Multiple yearly datasets were combined, cleaned, and preprocessed to build
a single dataset for analysis and machine learning.
""")

st.markdown("""
**Dataset Sources**

- Road Accident Dataset (2022–2025)
  https://www.kaggle.com/datasets/sehaj1104/indian-road-accident-dataset-20222025?utm_source=chatgpt.com

- Road Accident Dataset (2017–2022)
  https://www.kaggle.com/datasets/s3programmer/road-accident-severity-in-india?utm_source=chatgpt.com


""")

st.divider()

st.subheader("👨‍💻 Developer")

st.markdown("""
**Avuthu Roopesh Reddy**

B.Tech – Electronics & Communication Engineering

Anurag University

**Project Title**

RoadSafe AI – AI-Powered Road Accident Analysis & Severity Prediction Platform
            

https://www.linkedin.com/in/avuthu-roopesh-reddy-09938b315/
            

https://github.com/roopeshARR
""")



st.divider()

st.subheader("🎯 Project Objective")

st.info("""
To analyze road accident data from **2017–2025** using data analytics and
machine learning to identify accident patterns, visualize risk factors,
predict accident severity, and support better road safety awareness and
decision-making.
""")