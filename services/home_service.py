"""
=========================================================
RoadSafe AI
Home Dashboard Service
=========================================================
"""

from services.data_service import load_analytics_dataset


def get_dashboard_kpis():

    df = load_analytics_dataset()

    kpis = {

        "total_accidents": len(df),

        "total_casualties": int(df["casualties"].sum()),

        "states": df["state"].nunique(),

        "cities": df["city"].nunique(),

        "average_risk": round(df["risk_score"].mean() * 100, 2),

        "highest_risk_state": (
            df.groupby("state")["risk_score"]
            .mean()
            .idxmax()
        ),

        "most_common_weather": (
            df["weather"]
            .mode()[0]
        ),

        "most_common_road": (
            df["road_type"]
            .mode()[0]
        )
    }

    return kpis