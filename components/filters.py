"""
=========================================================
RoadSafe AI
Global Filters
=========================================================
"""

import streamlit as st


def show_filters(
    df,
    state=True,
    city=True,
    weather=True,
    road=True,
    severity=True
):
    """
    Display sidebar filters and return the filtered dataframe.
    """

    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filters")

    # ---------- State ----------
    states = ["All"] + sorted(df["state"].unique().tolist())

    selected_state = st.sidebar.selectbox(
        "State",
        states
    )

    # ---------- City ----------
    if selected_state == "All":
        cities = sorted(df["city"].unique().tolist())
    else:
        cities = sorted(
            df[df["state"] == selected_state]["city"].unique().tolist()
        )

    cities = ["All"] + cities

    selected_city = st.sidebar.selectbox(
        "City",
        cities
    )

    # ---------- Weather ----------
    weather = ["All"] + sorted(df["weather"].unique().tolist())

    selected_weather = st.sidebar.selectbox(
        "Weather",
        weather
    )

    # ---------- Road Type ----------
    road_types = ["All"] + sorted(df["road_type"].unique().tolist())

    selected_road = st.sidebar.selectbox(
        "Road Type",
        road_types
    )

    # ---------- Severity ----------
    severity = ["All"] + sorted(df["accident_severity"].unique().tolist())

    selected_severity = st.sidebar.selectbox(
        "Severity",
        severity
    )

    # ---------- Apply Filters ----------

    filtered_df = df.copy()

    if selected_state != "All":
        filtered_df = filtered_df[
            filtered_df["state"] == selected_state
        ]

    if selected_city != "All":
        filtered_df = filtered_df[
            filtered_df["city"] == selected_city
        ]

    if selected_weather != "All":
        filtered_df = filtered_df[
            filtered_df["weather"] == selected_weather
        ]

    if selected_road != "All":
        filtered_df = filtered_df[
            filtered_df["road_type"] == selected_road
        ]

    if selected_severity != "All":
        filtered_df = filtered_df[
            filtered_df["accident_severity"] == selected_severity
        ]

    return filtered_df