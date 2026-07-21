"""
=========================================================
RoadSafe AI
Dataset Builder (V2)
=========================================================

Loads UK and Indian datasets, standardizes columns,
maps categories, merges datasets and creates the final
combined dataset.

Author : A. Roopesh Reddy
Version : 2.0
"""

# =========================================================
# Imports
# =========================================================

from pathlib import Path
import pandas as pd

from feature_mapping import (
    COLUMN_MAPPING,
    WEATHER_MAPPING,
    LIGHT_MAPPING,
    ROAD_SURFACE_MAPPING,
    ROAD_TYPE_MAPPING,
    JUNCTION_MAPPING,
    VEHICLE_MAPPING,
    AREA_MAPPING,
    SEVERITY_MAPPING,
    FINAL_FEATURES
)

# =========================================================
# Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw"
OUTPUT_DATA = PROJECT_ROOT / "data" / "processed"

OUTPUT_DATA.mkdir(exist_ok=True)

# =========================================================
# Load Datasets
# =========================================================

print("Loading datasets...")

india_2017 = pd.read_csv(RAW_DATA / "17-22.csv")
india_2022 = pd.read_csv(RAW_DATA / "22-25.csv")

uk_collision = pd.read_csv(RAW_DATA / "uk_collisions.csv")
uk_vehicle = pd.read_csv(RAW_DATA / "uk_vehicles.csv")

print("Datasets Loaded Successfully")

# =========================================================
# Rename Columns
# =========================================================

def rename_columns(df):
    return df.rename(columns=COLUMN_MAPPING)

india_2017 = rename_columns(india_2017)
india_2022 = rename_columns(india_2022)

uk_collision = rename_columns(uk_collision)
uk_vehicle = rename_columns(uk_vehicle)

# =========================================================
# Merge UK Dataset
# =========================================================

print("Merging UK datasets...")

uk_df = pd.merge(
    uk_collision,
    uk_vehicle,
    on="collision_index",
    how="left"
)

print(f"UK Shape : {uk_df.shape}")

# =========================================================
# Merge Indian Dataset
# =========================================================

print("Merging Indian datasets...")

india_df = pd.concat(
    [india_2017, india_2022],
    ignore_index=True
)

print(f"India Shape : {india_df.shape}")

# =========================================================
# Apply Category Mapping
# =========================================================

def apply_mapping(df):

    if "weather" in df.columns:
        df["weather"] = df["weather"].replace(WEATHER_MAPPING)

    if "light_condition" in df.columns:
        df["light_condition"] = df["light_condition"].replace(LIGHT_MAPPING)

    if "road_surface" in df.columns:
        df["road_surface"] = df["road_surface"].replace(ROAD_SURFACE_MAPPING)

    if "road_type" in df.columns:
        df["road_type"] = df["road_type"].replace(ROAD_TYPE_MAPPING)

    if "junction_detail" in df.columns:
        df["junction_detail"] = df["junction_detail"].replace(JUNCTION_MAPPING)

    if "vehicle_type" in df.columns:
        df["vehicle_type"] = df["vehicle_type"].replace(VEHICLE_MAPPING)

    if "urban_rural" in df.columns:
        df["urban_rural"] = df["urban_rural"].replace(AREA_MAPPING)

    if "severity" in df.columns:

        df["severity"] = (
            df["severity"]
            .astype(str)
            .str.strip()
            .replace(SEVERITY_MAPPING)
    )

    return df

uk_df = apply_mapping(uk_df)
india_df = apply_mapping(india_df)

# =========================================================
# Keep Required Features
# =========================================================

uk_df = uk_df.reindex(columns=FINAL_FEATURES)

india_df = india_df.reindex(columns=FINAL_FEATURES)

# =========================================================
# Combine Datasets
# =========================================================

combined_df = pd.concat(
    [india_df, uk_df],
    ignore_index=True
)

# =========================================================
# Remove Duplicates
# =========================================================

combined_df.drop_duplicates(inplace=True)

# =========================================================
# Save Dataset
# =========================================================

output_file = OUTPUT_DATA / "combined_dataset.csv"

combined_df.to_csv(
    output_file,
    index=False
)

# =========================================================
# Summary
# =========================================================

print("\n========================================")

print("Combined Dataset Created Successfully")

print("========================================")

print(f"Rows    : {len(combined_df)}")
print(f"Columns : {len(combined_df.columns)}")

print(f"\nSaved : {output_file}")