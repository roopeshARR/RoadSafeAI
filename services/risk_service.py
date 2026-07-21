"""
=========================================================
RoadSafe AI
Risk Service
=========================================================
"""

from services.data_service import load_analytics_dataset


def get_risk_dataset():

    df = load_analytics_dataset()

    return df[
        [
            "city",
            "state",
            "risk_score",
            "accident_severity",
            "weather",
            "road_type",
            "casualties",
            "latitude",
            "longitude",
        ]
    ]