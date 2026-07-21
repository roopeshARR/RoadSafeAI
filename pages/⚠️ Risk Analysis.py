import streamlit as st
import plotly.express as px

from config import PROJECT_NAME

from components.sidebar import show_sidebar
from components.filters import show_filters

from services.risk_service import get_risk_dataset

st.set_page_config(
    page_title=f"{PROJECT_NAME} | Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

show_sidebar()

st.title("⚠️ Risk Analysis")

df = get_risk_dataset()

filtered_df = show_filters(df)

# ======================================
# KPI Cards
# ======================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Risk",
        round(filtered_df["risk_score"].mean(), 2)
    )

with col2:
    st.metric(
        "Highest Risk",
        round(filtered_df["risk_score"].max(), 2)
    )

with col3:
    st.metric(
        "Lowest Risk",
        round(filtered_df["risk_score"].min(), 2)
    )

with col4:
    st.metric(
        "Locations",
        len(filtered_df)
    )

st.divider()

# ======================================
# Risk Score Distribution
# ======================================

st.subheader("📈 Risk Score Distribution")

fig = px.histogram(
    filtered_df,
    x="risk_score",
    nbins=25,
    color="accident_severity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Average Risk by State
# ======================================

st.subheader("🗺️ Average Risk by State")

state_risk = (
    filtered_df
    .groupby("state")["risk_score"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig = px.bar(
    state_risk,
    x="state",
    y="risk_score",
    color="risk_score",
    text_auto=".2f"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Top 10 Highest Risk Locations
# ======================================

st.subheader("🚨 Top 10 Highest Risk Locations")

top_risk = (
    filtered_df
    .sort_values("risk_score", ascending=False)
    .head(10)
)

st.dataframe(
    top_risk[
        [
            "city",
            "state",
            "risk_score",
            "accident_severity"
        ]
    ],
    use_container_width=True,
    hide_index=True
)