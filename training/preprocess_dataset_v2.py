"""
=========================================================
RoadSafe AI
Dataset Preprocessing (V2)
=========================================================

Loads the combined dataset, cleans missing values,
creates ML-ready features, and splits the dataset.

Author : A. Roopesh Reddy
Version : 2.0
"""

# =========================================================
# Imports
# =========================================================

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTENC
# =========================================================
# Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT /
    "data" /
    "processed" /
    "combined_dataset.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT /
    "data" /
    "processed"
)

# =========================================================
# Load Dataset
# =========================================================

print("=" * 60)
print("Loading Combined Dataset")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

print(f"Dataset Shape : {df.shape}")

# =========================================================
# Remove Missing Target
# =========================================================

# Remove rows without a target label
df = df[df["severity"].notna()]

# Clean severity values
df["severity"] = df["severity"].astype(str).str.strip()

# =========================================================
# Convert Time → Hour
# =========================================================

if "time" in df.columns:

    df["time"] = df["time"].astype(str)

    df["hour"] = (
        pd.to_datetime(
            df["time"],
            format="%H:%M",
            errors="coerce"
        )
        .dt.hour
    )

    df.drop(columns=["time"], inplace=True)

# =========================================================
# Numeric Columns
# =========================================================

numeric_columns = [

    "number_of_vehicles",

    "speed_limit",

    "hour"

]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        df[column] = df[column].fillna(
            df[column].median()
            )

# =========================================================
# Categorical Columns
# =========================================================

categorical_columns = [

    "age_band",

    "vehicle_type",

    "road_type",

    "junction_detail",

    "road_surface",

    "urban_rural",

    "weather",

    "light_condition",

    "day_of_week"

]

for column in categorical_columns:

    if column in df.columns:

        df[column] = (
            df[column]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
        )

# =========================================================
# Remove Duplicate Records
# =========================================================

df.drop_duplicates(inplace=True)

# =========================================================
# Split Features & Target
# =========================================================

X = df.drop(columns=["severity"])

y = df["severity"]

# =========================================================
# Train Test Split
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


# =========================================================
# Save Train Dataset
# =========================================================

train_df = X_train.copy()

train_df["severity"] = y_train.values

train_df.to_csv(

    OUTPUT_DIR / "train.csv",

    index=False

)

# =========================================================
# Save Test Dataset
# =========================================================

test_df = X_test.copy()

test_df["severity"] = y_test.values

test_df.to_csv(

    OUTPUT_DIR / "test.csv",

    index=False

)

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)

print("Preprocessing Completed")

print("=" * 60)

print(f"Training Samples : {len(train_df)}")

print(f"Testing Samples  : {len(test_df)}")

print("\nFiles Saved")

print("✔ train.csv")

print("✔ test.csv")