"""
=========================================================
RoadSafe AI
Configuration File
=========================================================
"""

from pathlib import Path

# -------------------------------------------------------
# Project Information
# -------------------------------------------------------

PROJECT_NAME = "RoadSafe AI"

PROJECT_TAGLINE = "AI-Powered Road Accident Analysis & Severity Prediction Platform"

VERSION = "1.0.0"

AUTHOR = "A. Roopesh Reddy"

# -------------------------------------------------------
# Base Paths
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

REPORT_DIR = BASE_DIR / "reports"

LOG_DIR = BASE_DIR / "logs"

ASSET_DIR = BASE_DIR / "assets"

# -------------------------------------------------------
# Dataset Paths
# -------------------------------------------------------

DATASET_ANALYTICS = RAW_DATA_DIR / "22-25.csv"

DATASET_PREDICTION = RAW_DATA_DIR / "17-22.csv"

CLEAN_ANALYTICS = PROCESSED_DATA_DIR / "clean_22_25.csv"

CLEAN_PREDICTION = PROCESSED_DATA_DIR / "clean_17_22.csv"

# -------------------------------------------------------
# Model Files
# -------------------------------------------------------

MODEL_FILE = MODEL_DIR / "random_forest.pkl"

SCALER_FILE = MODEL_DIR / "scaler.pkl"

ENCODER_FILE = MODEL_DIR / "label_encoders.pkl"

# -------------------------------------------------------
# Dashboard Settings
# -------------------------------------------------------

PAGE_TITLE = PROJECT_NAME

PAGE_ICON = "🚗"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

# -------------------------------------------------------
# Theme Colors
# -------------------------------------------------------

PRIMARY_COLOR = "#1976D2"

SUCCESS_COLOR = "#2E7D32"

WARNING_COLOR = "#FB8C00"

DANGER_COLOR = "#D32F2F"

BACKGROUND_COLOR = "#F5F7FA"

TEXT_COLOR = "#212121"