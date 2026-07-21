import streamlit as st
import plotly.express as px

from config import PROJECT_NAME
from components.sidebar import show_sidebar
from components.filters import show_filters
from services.map_service import get_map_dataset

st.set_page_config(
    page_title=f"{PROJECT_NAME} | Maps",
    page_icon="🗺️",
    layout="wide"
)

show_sidebar()

st.title("🗺️ Accident Map")

df = get_map_dataset()
filtered_df = show_filters(df)

# ==============================
# KPI Cards
# ==============================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📍 Locations", len(filtered_df))

with col2:
    st.metric("🏙️ Cities", filtered_df["city"].nunique())

with col3:
    st.metric("🗺️ States", filtered_df["state"].nunique())

with col4:
    st.metric(
        "⚠️ Avg Risk Score",
        round(filtered_df["risk_score"].mean(), 2)
    )

st.divider()

# ==============================
# Interactive Map
# ==============================

st.subheader("🌍 Accident Locations")

fig = px.scatter_map(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="accident_severity",
    hover_name="city",
    hover_data={
        "state": True,
        "risk_score": True,
        "latitude": False,
        "longitude": False
    },
    zoom=4,
    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==============================
# Top Cities & States
# ==============================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏙️ Top 10 Cities")

    city_df = (
        filtered_df["city"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city_df.columns = ["City", "Accidents"]

    st.bar_chart(
        city_df.set_index("City")
    )

with col2:

    st.subheader("🗺️ Top 10 States")

    state_df = (
        filtered_df["state"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    state_df.columns = ["State", "Accidents"]

    st.bar_chart(
        state_df.set_index("State")
    )

st.divider()

# ==============================
# Location Data
# ==============================

st.subheader("📋 Accident Locations")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)