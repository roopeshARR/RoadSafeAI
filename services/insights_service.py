"""
=========================================================
RoadSafe AI
Insights Service
=========================================================
"""

from services.data_service import load_analytics_dataset


def get_insights_dataset():

    df = load_analytics_dataset()

    return df[
        [
            "city",
            "state",
            "weather",
            "road_type",
            "accident_severity",
            "risk_score",
            "casualties",
        ]
    ]