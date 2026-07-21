"""
=========================================================
RoadSafe AI
Prediction Service
=========================================================
"""

from pathlib import Path
import json
import joblib
import pandas as pd


# =========================================================
# Model Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODELS_DIR = PROJECT_ROOT / "models"

MODEL_PATH = MODELS_DIR / "severity_model.pkl"
PREPROCESSOR_PATH = MODELS_DIR / "feature_preprocessor.pkl"
ENCODER_PATH = MODELS_DIR / "target_encoder.pkl"
FEATURE_INFO_PATH = MODELS_DIR / "feature_info.json"


# =========================================================
# Severity Predictor
# =========================================================

class SeverityPredictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.preprocessor = joblib.load(PREPROCESSOR_PATH)

        self.encoder = joblib.load(ENCODER_PATH)

        with open(FEATURE_INFO_PATH, "r", encoding="utf-8") as file:

            self.feature_info = json.load(file)

    # =====================================================
    # Feature Information
    # =====================================================

    def get_input_columns(self):

        return self.feature_info["input_columns"]

    def get_categorical_columns(self):

        return self.feature_info["categorical_columns"]

    def get_numeric_columns(self):

        return self.feature_info["numeric_columns"]

    def get_category_values(self, column):

        return self.feature_info["categorical_values"][column]

    # =====================================================
    # Prediction
    # =====================================================

    def predict(self, user_input):

        df = pd.DataFrame([user_input])

        # Ensure column order matches training
        df = df[self.get_input_columns()]

        encoded = self.preprocessor.transform(df)

        prediction = self.model.predict(encoded)[0]

        probabilities = self.model.predict_proba(encoded)[0]

        confidence = float(probabilities.max()) * 100

        label = self.encoder.inverse_transform([prediction])[0]

        probability_table = {
        class_name: round(float(probabilities[index]) * 100, 2)
        for index, class_name in enumerate(self.encoder.classes_)
}

        return {

            "prediction": label,

            "confidence": round(confidence, 2),

            "probabilities": probability_table

        }