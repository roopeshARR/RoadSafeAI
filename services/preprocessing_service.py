"""
=========================================================
RoadSafe AI
Dashboard Dataset Preprocessing
=========================================================
"""

import pandas as pd

from utils.logger import logger


class DashboardPreprocessor:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

    # -----------------------------------------

    def remove_duplicates(self):

        before = len(self.df)

        self.df.drop_duplicates(inplace=True)

        after = len(self.df)

        logger.info(f"Duplicates Removed : {before-after}")

        return self

    # -----------------------------------------

    def handle_missing_values(self):

        self.df["festival"] = self.df["festival"].fillna("No Festival")

        logger.info("Missing Values Handled")

        return self

    # -----------------------------------------

    def convert_date(self):

        self.df["date"] = pd.to_datetime(
            self.df["date"],
            errors="coerce"
        )

        logger.info("Date Converted")

        return self

    # -----------------------------------------

    def feature_engineering(self):

        self.df["year"] = self.df["date"].dt.year

        self.df["month"] = self.df["date"].dt.month

        self.df["month_name"] = self.df["date"].dt.month_name()

        self.df["quarter"] = self.df["date"].dt.quarter

        return self

    # -----------------------------------------

    def sort_dataset(self):

        self.df.sort_values("date", inplace=True)

        return self

    # -----------------------------------------

    def save(self, filepath):

        self.df.to_csv(filepath, index=False)

        logger.info("Processed Dataset Saved")

        return self

    # -----------------------------------------

    def get_dataframe(self):

        return self.df