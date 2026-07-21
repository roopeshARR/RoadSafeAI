"""
=========================================================
RoadSafe AI
Model Training Pipeline
=========================================================

Author : A. Roopesh Reddy
Version : 2.0
"""

from pathlib import Path
import sys
import json
import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# =========================================================
# Project Imports
# =========================================================

from services.data_service import load_prediction_dataset
from services.ml_preprocessing_service import MLPreprocessor

# =========================================================
# Machine Learning
# =========================================================

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from imblearn.over_sampling import SMOTE

# =========================================================
# Model Definitions
# =========================================================

MODELS = {

    "Decision Tree": DecisionTreeClassifier(

        max_depth=10,

        random_state=42

    ),

    "Random Forest": RandomForestClassifier(

        n_estimators=300,

        random_state=42,

        n_jobs=-1

    ),

    "Gradient Boosting": GradientBoostingClassifier(

        random_state=42

    )

}

# =========================================================
# Helper Function
# =========================================================

def print_metrics(model_name,
                  y_test,
                  predictions):

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    balanced = balanced_accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    print("\n" + "=" * 70)

    print(model_name)

    print("=" * 70)

    print(f"Accuracy            : {accuracy:.4f}")

    print(f"Balanced Accuracy   : {balanced:.4f}")

    print(f"Weighted Precision  : {precision:.4f}")

    print(f"Weighted Recall     : {recall:.4f}")

    print(f"Weighted F1 Score   : {f1:.4f}")

    print("\nClassification Report\n")

    print(

        classification_report(

            y_test,

            predictions,

            zero_division=0

        )

    )

    print("Confusion Matrix\n")

    print(

        confusion_matrix(

            y_test,

            predictions

        )

    )

    return {

        "accuracy": accuracy,

        "balanced_accuracy": balanced,

        "precision": precision,

        "recall": recall,

        "f1": f1

    }
# =========================================================
# Main Function
# =========================================================

def main():

    print("=" * 70)
    print("RoadSafe AI - Model Training")
    print("=" * 70)

    # =====================================================
    # Load Dataset
    # =====================================================

    print("\nLoading Prediction Dataset...")

    df = load_prediction_dataset()

    print(f"Dataset Shape : {df.shape}")

    # =====================================================
    # ML Preprocessing
    # =====================================================

    print("\nApplying ML Preprocessing...")

    # Dataset is already preprocessed.
# Only encode the target labels.

    preprocessor_obj = MLPreprocessor(df)

    preprocessor_obj.encode_target()

    df = preprocessor_obj.get_dataframe()

    print(f"Processed Shape : {df.shape}")

    # =====================================================
    # Features & Target
    # =====================================================

    X = df.drop(columns=["Accident_severity"])

    y = df["Accident_severity"]

    categorical_columns = X.select_dtypes(
        include="object"
    ).columns

    numeric_columns = X.select_dtypes(
        exclude="object"
    ).columns

    # =====================================================
    # Train Test Split
    # =====================================================

    print("\nSplitting Dataset...")

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.20,

        random_state=42,

        stratify=y

    )

    print(f"Training Samples : {len(X_train)}")

    print(f"Testing Samples  : {len(X_test)}")

    # =====================================================
    # Feature Encoding
    # =====================================================

    print("\nEncoding Features...")

    feature_preprocessor = ColumnTransformer(

        transformers=[

            (

                "categorical",

                OneHotEncoder(

                    handle_unknown="ignore"

                ),

                categorical_columns

            ),

            (

                "numeric",

                "passthrough",

                numeric_columns

            )

        ]

    )

    X_train_encoded = feature_preprocessor.fit_transform(

        X_train

    )

    X_test_encoded = feature_preprocessor.transform(

        X_test

    )

    print("Encoding Complete")

    # =====================================================
    # Apply SMOTE
    # =====================================================

    print("\nApplying SMOTE...")

    smote = SMOTE(

        random_state=42

    )

    X_train_balanced, y_train_balanced = smote.fit_resample(

        X_train_encoded,

        y_train

    )

    print(f"Original Training Shape : {X_train_encoded.shape}")

    print(f"Balanced Training Shape : {X_train_balanced.shape}")

    # =====================================================
    # Train Models
    # =====================================================

    results = {}

    best_model = None

    best_model_name = ""

    best_metrics = None

    best_score = 0

    print("\nStarting Model Training...\n")

    for model_name, model in MODELS.items():

        print("\n" + "-" * 70)

        print(f"Training : {model_name}")

        print("-" * 70)

        model.fit(

            X_train_balanced,

            y_train_balanced

        )

        predictions = model.predict(

            X_test_encoded

        )

        metrics = print_metrics(

            model_name,

            y_test,

            predictions

        )

        results[model_name] = metrics

        if metrics["f1"] > best_score:

            best_score = metrics["f1"]

            best_model = model

            best_model_name = model_name

            best_metrics = metrics

    # =====================================================
    # Save Best Model
    # =====================================================

    print("\n" + "=" * 70)
    print("Saving Best Model")
    print("=" * 70)

    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(exist_ok=True)

    # Save trained model
    joblib.dump(
        best_model,
        models_dir / "severity_model.pkl"
    )

    # Save feature preprocessor (OneHotEncoder + ColumnTransformer)
    joblib.dump(
        feature_preprocessor,
        models_dir / "feature_preprocessor.pkl"
    )

    # Save target encoder
    joblib.dump(
        preprocessor_obj.target_encoder,
        models_dir / "target_encoder.pkl"
    )

    # Save metrics
    metrics = {
    "best_model": best_model_name,
    "results": results
}

# =====================================================
# Save Feature Information
# =====================================================

    feature_info = {

    "input_columns": X.columns.tolist(),

    "categorical_columns": categorical_columns.tolist(),

    "numeric_columns": numeric_columns.tolist(),

    "categorical_values": {}

}

    for column in categorical_columns:

        feature_info["categorical_values"][column] = sorted(

        df[column]
        .dropna()
        .astype(str)
        .unique()
        .tolist()

    )

    with open(
    models_dir / "feature_info.json",
    "w",
    encoding="utf-8"
    ) as file:

        json.dump(
        feature_info,
        file,
        indent=4
    )

    with open(
    models_dir / "model_metrics.json",
    "w",
    encoding="utf-8"
    ) as file:

        json.dump(
        metrics,
        file,
        indent=4
    )

    # =====================================================
    # Training Summary
    # =====================================================

    print("\n")
    print("=" * 70)
    print("RoadSafe AI Model Training Summary")
    print("=" * 70)

    for model_name, values in results.items():

        print(f"\n{model_name}")

        print(
            f"Balanced Accuracy : "
            f"{values['balanced_accuracy']:.4f}"
        )

        print(
            f"Weighted F1 Score : "
            f"{values['f1']:.4f}"
        )

    print("\n" + "-" * 70)

    print(f"Best Model : {best_model_name}")

    print(
        f"Balanced Accuracy : "
        f"{best_metrics['balanced_accuracy']:.4f}"
    )

    print(
        f"Weighted F1 Score : "
        f"{best_metrics['f1']:.4f}"
    )

    print("\nSaved Files")

    print(f"✔ severity_model.pkl")
    print(f"✔ feature_preprocessor.pkl")
    print(f"✔ target_encoder.pkl")
    print(f"✔ feature_info.json")
    print(f"✔ model_metrics.json")

    print("\nTraining Completed Successfully!")

# =========================================================
# Entry Point
# =========================================================

if __name__ == "__main__":

    main()