"""
=========================================================
RoadSafe AI
Preprocess Dataset B (Dashboard Dataset)
=========================================================
"""

from pathlib import Path
import sys

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from services.data_service import load_analytics_dataset
from services.preprocessing_service import DashboardPreprocessor
from config import CLEAN_ANALYTICS


def main():

    print("=" * 60)
    print("RoadSafe AI - Dataset B Preprocessing")
    print("=" * 60)

    # Load Dataset
    df = load_analytics_dataset()

    print(f"\nOriginal Shape : {df.shape}")

    processor = DashboardPreprocessor(df)

    clean_df = (
        processor
        .remove_duplicates()
        .handle_missing_values()
        .convert_date()
        .feature_engineering()
        .sort_dataset()
        .save(CLEAN_ANALYTICS)
        .get_dataframe()
    )

    print(f"Processed Shape : {clean_df.shape}")

    print("\nProcessed Dataset Saved Successfully")

    print(CLEAN_ANALYTICS)


if __name__ == "__main__":
    main()