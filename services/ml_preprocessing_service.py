"""
=========================================================
RoadSafe AI
ML Preprocessing Service
=========================================================
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


class MLPreprocessor:

    def __init__(self, dataframe):

        self.df = dataframe.copy()

        self.target_encoder = LabelEncoder()

    def remove_duplicates(self):

        self.df.drop_duplicates(inplace=True)

        return self

    def handle_missing_values(self):

        categorical_columns = self.df.select_dtypes(
            include="object"
        ).columns

        for column in categorical_columns:

            self.df[column] = self.df[column].fillna(
                "Unknown"
            )

        return self

    def convert_time(self):

        self.df["Hour"] = pd.to_datetime(
            self.df["Time"],
            format="%H:%M:%S",
            errors="coerce"
        ).dt.hour

        self.df.drop(
            columns=["Time"],
            inplace=True
        )

        return self

    def encode_target(self):

        if self.df["Accident_severity"].dtype == "object":

            self.df["Accident_severity"] = (
                self.target_encoder.fit_transform(
                    self.df["Accident_severity"]
            )
        )

        return self

    def get_dataframe(self):

        return self.df