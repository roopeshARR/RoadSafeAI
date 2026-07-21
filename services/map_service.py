"""
=========================================================
RoadSafe AI
Map Service
=========================================================
"""

from services.data_service import load_analytics_dataset


def get_map_dataset():

    df = load_analytics_dataset()

    return df[
        [
            "latitude",
            "longitude",
            "city",
            "state",
            "accident_severity",
            "weather",
            "road_type",
            "risk_score",
            "casualties",
        ]
    ]