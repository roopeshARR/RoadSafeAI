"""
=========================================================
RoadSafe AI
Feature Mapping Configuration (V2)
=========================================================

This file standardizes columns and category values across
all datasets (India + UK).

Author : A. Roopesh Reddy
Version : 2.0
"""

# =========================================================
# COLUMN MAPPING
# =========================================================

COLUMN_MAPPING = {

    # ---------- Target ----------
    "collision_severity": "severity",
    "Accident_severity": "severity",

    # ---------- Date & Time ----------
    "time": "time",
    "Time": "time",

    "day_of_week": "day_of_week",
    "Day_of_Week": "day_of_week",

    # ---------- Vehicle ----------
    "vehicle_type": "vehicle_type",
    "Vehicle_Type": "vehicle_type",

    "number_of_vehicles": "number_of_vehicles",
    "Vehicles_Involved": "number_of_vehicles",

    "age_band_of_driver": "age_band",
    "Age_band_of_driver": "age_band",

    # ---------- Road ----------
    "road_type": "road_type",
    "Road_Type": "road_type",

    "junction_detail": "junction_detail",
    "Junction": "junction_detail",

    "road_surface_conditions": "road_surface",
    "Road_Surface": "road_surface",

    "speed_limit": "speed_limit",

    "urban_or_rural_area": "urban_rural",

    # ---------- Environment ----------
    "weather_conditions": "weather",
    "Weather": "weather",

    "light_conditions": "light_condition",
    "Light": "light_condition",
}

# =========================================================
# WEATHER MAPPING
# =========================================================

WEATHER_MAPPING = {

    "Fine no high winds": "Clear",
    "Fine + high winds": "Clear",
    "Sunny": "Clear",
    "Clear": "Clear",

    "Raining without high winds": "Rain",
    "Raining with high winds": "Rain",
    "Rain": "Rain",
    "Rainy": "Rain",

    "Fog or mist": "Fog",
    "Fog": "Fog",
    "Mist": "Fog",

    "Snowing without high winds": "Snow",
    "Snowing with high winds": "Snow",
    "Snow": "Snow",

    "High winds": "Wind",
    "Windy": "Wind",

    "Unknown": "Other",
    "Other": "Other"
}

# =========================================================
# LIGHT CONDITION MAPPING
# =========================================================

LIGHT_MAPPING = {

    "Daylight": "Day",
    "Day": "Day",

    "Darkness - lights lit": "Night",
    "Darkness - lighting unknown": "Night",
    "Darkness - lights unlit": "Night",
    "Darkness - no lighting": "Night",
    "Night": "Night"
}

# =========================================================
# ROAD SURFACE MAPPING
# =========================================================

ROAD_SURFACE_MAPPING = {

    "Dry": "Dry",

    "Wet or damp": "Wet",
    "Wet": "Wet",

    "Snow": "Snow",

    "Flood over 3cm. deep": "Flooded",
    "Flood": "Flooded",

    "Frost or ice": "Icy",
    "Ice": "Icy",

    "Other": "Other",
    "Unknown": "Other"
}

# =========================================================
# ROAD TYPE MAPPING
# =========================================================

ROAD_TYPE_MAPPING = {

    "Single carriageway": "Single Carriageway",
    "Single Carriageway": "Single Carriageway",

    "Dual carriageway": "Dual Carriageway",
    "Dual Carriageway": "Dual Carriageway",

    "One way street": "One Way",
    "One Way": "One Way",

    "Roundabout": "Roundabout",

    "Slip road": "Slip Road",

    "Motorway": "Motorway",

    "Unknown": "Other",
    "Other": "Other"
}

# =========================================================
# JUNCTION MAPPING
# =========================================================

JUNCTION_MAPPING = {

    "Not at junction or within 20 metres": "No Junction",

    "T or staggered junction": "T Junction",

    "Crossroads": "Crossroads",

    "Roundabout": "Roundabout",

    "Slip road": "Slip Road",

    "Other junction": "Other",

    "Unknown": "Other"
}

# =========================================================
# VEHICLE TYPE MAPPING
# =========================================================

VEHICLE_MAPPING = {

    "Car": "Car",
    "Taxi": "Car",

    "Motorcycle": "Motorcycle",
    "Motorbike": "Motorcycle",
    "Bike": "Motorcycle",
    "Scooter": "Motorcycle",

    "Bus": "Bus",
    "Minibus": "Bus",

    "Goods vehicle": "Truck",
    "Truck": "Truck",
    "Lorry": "Truck",

    "Pedal cycle": "Bicycle",
    "Bicycle": "Bicycle",

    "Auto": "Three Wheeler",
    "Auto Rickshaw": "Three Wheeler",
    "Three Wheeler": "Three Wheeler",

    "Agricultural vehicle": "Agricultural",
    "Tractor": "Agricultural",

    "Other": "Other",
    "Unknown": "Other"
}

# =========================================================
# AREA MAPPING
# =========================================================

AREA_MAPPING = {

    "Urban": "Urban",
    "Rural": "Rural",

    1: "Urban",
    2: "Rural"
}

# =========================================================
# SEVERITY MAPPING
# =========================================================

SEVERITY_MAPPING = {

    # ---------- UK ----------
    "Fatal": "Fatal",
    "Fatal injury": "Fatal",

    "Serious": "Serious",
    "Serious Injury": "Serious",

    "Slight": "Minor",
    "Slight Injury": "Minor",
    "Minor Injury": "Minor",

    # ---------- Numeric (string) ----------
    "1": "Fatal",
    "2": "Serious",
    "3": "Minor",

    # ---------- Numeric (integer) ----------
    1: "Fatal",
    2: "Serious",
    3: "Minor"
}

# =========================================================
# FINAL FEATURES
# =========================================================

FINAL_FEATURES = [

    "age_band",

    "vehicle_type",

    "number_of_vehicles",

    "road_type",

    "junction_detail",

    "road_surface",

    "speed_limit",

    "urban_rural",

    "weather",

    "light_condition",

    "day_of_week",

    "time",

    "severity"
]