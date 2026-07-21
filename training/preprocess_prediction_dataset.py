"""
=========================================================
RoadSafe AI
Prediction Dataset Preprocessing
=========================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import pandas as pd

from config import (
    DATASET_PREDICTION,
    CLEAN_PREDICTION
)


def main():

    print("=" * 60)
    print("Prediction Dataset Preprocessing")
    print("=" * 60)

    # -----------------------------------------------------
    # Load Dataset
    # -----------------------------------------------------

    print("\nLoading Dataset...")

    df = pd.read_csv(DATASET_PREDICTION)

    print(f"Original Shape : {df.shape}")

    # -----------------------------------------------------
    # Remove Duplicate Records
    # -----------------------------------------------------

    duplicates = df.duplicated().sum()

    print(f"Duplicate Rows : {duplicates}")

    df.drop_duplicates(inplace=True)

    # -----------------------------------------------------
    # Handle Missing Values
    # -----------------------------------------------------

    print("Handling Missing Values...")

    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:

        df[column] = df[column].fillna("Unknown")

    # -----------------------------------------------------
    # Convert Time → Hour
    # -----------------------------------------------------

    print("Converting Time Column...")

    df["Hour"] = pd.to_datetime(
        df["Time"],
        format="%H:%M:%S",
        errors="coerce"
    ).dt.hour

    df.drop(columns=["Time"], inplace=True)

    # -----------------------------------------------------
    # Remove Unrealistic Features
    # -----------------------------------------------------

    print("Removing Post-Accident Features...")

    columns_to_remove = [

        "Casualty_class",
        "Sex_of_casualty",
        "Age_band_of_casualty",
        "Casualty_severity",
        "Work_of_casuality",
        "Fitness_of_casuality",
        "Number_of_casualties"

    ]

    df.drop(
        columns=columns_to_remove,
        inplace=True
    )

    # -----------------------------------------------------
    # Save Dataset
    # -----------------------------------------------------

    CLEAN_PREDICTION.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        CLEAN_PREDICTION,
        index=False
    )

    print(f"\nProcessed Shape : {df.shape}")

    print(f"Saved To : {CLEAN_PREDICTION}")

    print("\nPrediction Dataset Preprocessed Successfully!")


if __name__ == "__main__":

    main()