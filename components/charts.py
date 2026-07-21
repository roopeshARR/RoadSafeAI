"""
=========================================================
RoadSafe AI
Charts
=========================================================
"""

import plotly.express as px


def accidents_by_year(df):

    yearly = (
        df.groupby("year")
        .size()
        .reset_index(name="Accidents")
    )

    fig = px.line(
        yearly,
        x="year",
        y="Accidents",
        markers=True,
        title="Accidents by Year"
    )

    fig.update_layout(height=420)

    return fig


def severity_distribution(df):

    severity = (
        df["accident_severity"]
        .value_counts()
        .reset_index()
    )

    severity.columns = [
        "Severity",
        "Count"
    ]

    fig = px.pie(
        severity,
        names="Severity",
        values="Count",
        hole=0.45,
        title="Severity Distribution"
    )

    fig.update_layout(height=420)

    return fig



def accidents_by_state(df):

    state_df = (
        df.groupby("state")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig = px.bar(
        state_df,
        x="state",
        y="Accidents",
        title="Accidents by State"
    )

    fig.update_layout(height=450)

    return fig


def accidents_by_weather(df):

    weather_df = (
        df.groupby("weather")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig = px.bar(
        weather_df,
        x="weather",
        y="Accidents",
        title="Accidents by Weather"
    )

    fig.update_layout(height=450)

    return fig
def accidents_by_road_type(df):

    road_df = (
        df.groupby("road_type")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig = px.bar(
        road_df,
        x="road_type",
        y="Accidents",
        title="Accidents by Road Type"
    )

    fig.update_layout(height=450)

    return fig

def traffic_density_distribution(df):

    traffic_df = (
        df.groupby("traffic_density")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig = px.bar(
        traffic_df,
        x="traffic_density",
        y="Accidents",
        title="Traffic Density"
    )

    fig.update_layout(height=450)

    return fig
def monthly_trend(df):

    monthly = (
        df.groupby("month_name")
        .size()
        .reset_index(name="Accidents")
    )

    month_order = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]

    monthly["month_name"] = monthly["month_name"].astype("category")
    monthly["month_name"] = monthly["month_name"].cat.set_categories(month_order)

    monthly = monthly.sort_values("month_name")

    fig = px.line(
        monthly,
        x="month_name",
        y="Accidents",
        markers=True,
        title="Monthly Accident Trend"
    )

    fig.update_layout(height=450)

    return fig
def severity_bar(df):

    severity = (
        df.groupby("accident_severity")
        .size()
        .reset_index(name="Accidents")
    )

    fig = px.bar(
        severity,
        x="accident_severity",
        y="Accidents",
        title="Severity Distribution"
    )

    fig.update_layout(height=450)

    return fig