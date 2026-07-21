"""
=========================================================
RoadSafe AI
Dataset A Analysis (ML Dataset)
=========================================================
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from services.data_service import load_prediction_dataset


def main():

    df = load_prediction_dataset()

    print("=" * 60)
    print("DATASET A INFORMATION")
    print("=" * 60)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nFirst Five Rows")
    print(df.head())

    print("\nTarget Distribution")
    print(df["Accident_severity"].value_counts())


if __name__ == "__main__":
    main()