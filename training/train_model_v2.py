"""
=========================================================
RoadSafe AI
Model Training Pipeline (V2)
=========================================================

Author : A. Roopesh Reddy
Version : 2.0
"""

# =========================================================
# Imports
# =========================================================

from pathlib import Path
import json
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    ExtraTreesClassifier
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

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except:
    XGBOOST_AVAILABLE = False

# =========================================================
# Paths
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

TRAIN_FILE = (
    PROJECT_ROOT /
    "data" /
    "processed" /
    "train.csv"
)

TEST_FILE = (
    PROJECT_ROOT /
    "data" /
    "processed" /
    "test.csv"
)

MODELS_DIR = PROJECT_ROOT / "models"

MODELS_DIR.mkdir(exist_ok=True)

# =========================================================
# Load Dataset
# =========================================================

print("=" * 70)
print("Loading Datasets")
print("=" * 70)

train_df = pd.read_csv(TRAIN_FILE, low_memory=False)
test_df = pd.read_csv(TEST_FILE, low_memory=False)

print(f"Training Samples : {len(train_df)}")
print(f"Testing Samples  : {len(test_df)}")

# =========================================================
# Features & Target
# =========================================================

X_train = train_df.drop(columns=["severity"])
y_train = train_df["severity"]

X_test = test_df.drop(columns=["severity"])
y_test = test_df["severity"]

for dataset in [X_train, X_test]:
    for column in dataset.select_dtypes(include="object").columns:
        dataset[column] = dataset[column].astype(str).str.strip()

# =========================================================
# Encode Target
# =========================================================

target_encoder = LabelEncoder()

y_train = target_encoder.fit_transform(y_train)

y_test = target_encoder.transform(y_test)

# =========================================================
# Feature Lists
# =========================================================

categorical_columns = X_train.select_dtypes(
    include="object"
).columns.tolist()

numeric_columns = X_train.select_dtypes(
    exclude="object"
).columns.tolist()
print("\n===== COLUMN DTYPES =====")
print(X_train.dtypes)

print("\nCategorical Columns:")
print(categorical_columns)

print("\nNumeric Columns:")
print(numeric_columns)
for col in numeric_columns:
    bad = X_train[col].apply(lambda x: isinstance(x, str)).sum()
    if bad > 0:
        print(f"{col}: contains {bad} string values")

# =========================================================
# Feature Encoder
# =========================================================

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


print("\n===== TRAIN DTYPES =====")
print(X_train.dtypes)

print("\n===== TEST DTYPES =====")
print(X_test.dtypes)

print("\n===== AGE BAND VALUES =====")
print("Train:", X_train["age_band"].unique()[:10])
print("Test :", X_test["age_band"].unique()[:10])

X_train_encoded = feature_preprocessor.fit_transform(X_train)

print(type(X_train_encoded))
print(X_train_encoded.shape)

X_test_encoded = feature_preprocessor.transform(X_test)

# =========================================================
# Models
# =========================================================

MODELS = {

    "Random Forest": RandomForestClassifier(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    ),

    "Extra Trees": ExtraTreesClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

}

if XGBOOST_AVAILABLE:

    MODELS["XGBoost"] = XGBClassifier(
        random_state=42,
        eval_metric="mlogloss"
    )


# =========================================================
# Train Models
# =========================================================

results = {}

best_model = None
best_name = ""
best_score = 0

for name, model in MODELS.items():

    print("\n" + "=" * 70)
    print(f"Training : {name}")

    try:

        model.fit(X_train_encoded, y_train)

        predictions = model.predict(X_test_encoded)

        accuracy = accuracy_score(y_test, predictions)

        balanced = balanced_accuracy_score(y_test, predictions)

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

        print(f"Accuracy  : {accuracy:.4f}")
        print(f"F1 Score  : {f1:.4f}")

        print("\nClassification Report\n")
        print(
            classification_report(
                y_test,
                predictions,
                zero_division=0
            )
        )

        print("\nConfusion Matrix\n")
        print(
            confusion_matrix(
                y_test,
                predictions
            )
        )

        results[name] = {
            "accuracy": accuracy,
            "balanced_accuracy": balanced,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

        if f1 > best_score:
            best_score = f1
            best_model = model
            best_name = name

    except Exception as e:

        print(f"\n❌ {name} failed.")
        print(e)

        continue


# =========================================================
# Save Model
# =========================================================

joblib.dump(

    best_model,

    MODELS_DIR / "severity_model_v2.pkl"

)

joblib.dump(

    feature_preprocessor,

    MODELS_DIR / "feature_preprocessor_v2.pkl"

)

joblib.dump(

    target_encoder,

    MODELS_DIR / "target_encoder_v2.pkl"

)

# =========================================================
# Save Feature Info
# =========================================================

feature_info = {

    "input_columns": X_train.columns.tolist(),

    "categorical_columns": categorical_columns,

    "numeric_columns": numeric_columns

}

with open(

    MODELS_DIR / "feature_info_v2.json",

    "w",

    encoding="utf-8"

) as file:

    json.dump(

        feature_info,

        file,

        indent=4

    )

# =========================================================
# Save Metrics
# =========================================================

with open(

    MODELS_DIR / "model_metrics_v2.json",

    "w",

    encoding="utf-8"

) as file:

    json.dump(

        {

            "best_model": best_name,

            "results": results

        },

        file,

        indent=4

    )

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 70)

print("Training Completed")

print("=" * 70)

print(f"Best Model : {best_name}")

print(f"Weighted F1 : {best_score:.4f}")

print("\nSaved Files")

print("✔ severity_model_v2.pkl")

print("✔ feature_preprocessor_v2.pkl")

print("✔ target_encoder_v2.pkl")

print("✔ feature_info_v2.json")

print("✔ model_metrics_v2.json")