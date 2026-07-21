import streamlit as st

from config import PROJECT_NAME, PROJECT_TAGLINE

from components.sidebar import show_sidebar

from services.home_service import get_dashboard_kpis
from services.data_service import load_analytics_dataset

from components.charts import (
    accidents_by_year,
    severity_distribution,
    accidents_by_state,
    accidents_by_weather,
    accidents_by_road_type,
    traffic_density_distribution,
    monthly_trend,
    severity_bar,
)

st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🚗",
    layout="wide"
)

show_sidebar()

st.title("🚗 RoadSafe AI")
st.caption(PROJECT_TAGLINE)

df = load_analytics_dataset()
kpi = get_dashboard_kpis()

st.divider()

# ======================================================
# AI INSIGHTS
# ======================================================

st.subheader("🤖 AI Insights")

col1, col2 = st.columns(2)

with col1:

    st.info(
        f"""
### 📌 Key Insights

• **Highest Risk State:** {df.groupby('state')['risk_score'].mean().idxmax()}

• **Highest Risk City:** {df.groupby('city')['risk_score'].mean().idxmax()}

• **Most Common Weather:** {df['weather'].mode()[0]}

• **Most Common Road Type:** {df['road_type'].mode()[0]}

• **Most Frequent Severity:** {df['accident_severity'].mode()[0]}

• **Average Risk Score:** {df['risk_score'].mean():.2f}

• **Average Casualties:** {df['casualties'].mean():.2f}
"""
    )

with col2:

    st.success("""
### 🚦 Safety Recommendations

• Wear seat belts at all times.

• Follow speed limits, especially in high-risk areas.

• Drive cautiously during adverse weather conditions.

• Avoid distractions while driving.

• Ensure regular vehicle maintenance.

• Follow traffic rules and road signs.

• Avoid driving under the influence of alcohol or drugs.
""")

st.divider()


# ======================================================
# KPI CARDS
# ======================================================

st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚗 Total Accidents",
        f"{kpi['total_accidents']:,}"
    )

with col2:
    st.metric(
        "🤕 Casualties",
        f"{kpi['total_casualties']:,}"
    )

with col3:
    st.metric(
        "🏙 Cities",
        kpi["cities"]
    )

with col4:
    st.metric(
        "🌎 States",
        kpi["states"]
    )

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        "⚠ Average Risk",
        kpi["average_risk"]
    )

with col6:
    st.metric(
        "🌧 Weather",
        kpi["most_common_weather"]
    )

with col7:
    st.metric(
        "🛣 Road Type",
        kpi["most_common_road"]
    )

with col8:
    st.metric(
        "📍 Highest Risk State",
        kpi["highest_risk_state"]
    )

st.divider()

# ======================================================
# OVERVIEW CHARTS
# ======================================================

st.subheader("📈 Accident Overview")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        accidents_by_year(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        severity_distribution(df),
        use_container_width=True
    )

st.divider()

# ======================================================
# ANALYTICS
# ======================================================

st.subheader("📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        accidents_by_state(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        accidents_by_weather(df),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        accidents_by_road_type(df),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        traffic_density_distribution(df),
        use_container_width=True
    )

st.plotly_chart(
    monthly_trend(df),
    use_container_width=True
)

st.plotly_chart(
    severity_bar(df),
    use_container_width=True
)

st.divider()

# ======================================================
# QUICK INSIGHTS
# ======================================================

st.subheader("💡 Quick Insights")

st.info(
    f"""
- Dataset contains **{len(df):,}** accident records.
- **{kpi['highest_risk_state']}** has the highest average risk score.
- Most common weather condition: **{kpi['most_common_weather']}**
- Most common road type: **{kpi['most_common_road']}**
- Dataset covers **{kpi['states']}** states and **{kpi['cities']}** cities.
"""
)

st.divider()

# ======================================================
# RECENT RECORDS
# ======================================================

st.subheader("📝 Recent Accident Records")

st.dataframe(
    df.tail(10),
    use_container_width=True,
    hide_index=True
)
st.divider()

st.warning("""
### 📌 Note

The statistics, visualizations, AI insights, and machine learning predictions
presented in this application are based **only on the road accident records
available in the integrated dataset (2017–2025)**.

The actual number of road accidents occurring in India during this period is
significantly higher than the records included in this dataset. Therefore,
the results should be interpreted as **dataset-based analytical insights**
and not as complete national accident statistics.
""")