"""
=========================================================
RoadSafe AI
Data Service
=========================================================
"""

import pandas as pd
import streamlit as st

from config import (
    CLEAN_ANALYTICS,
    CLEAN_PREDICTION,
    DATASET_ANALYTICS,
    DATASET_PREDICTION
)

from utils.logger import logger


# =========================================================
# Analytics Dataset
# =========================================================

@st.cache_data
def load_analytics_dataset():

    try:

        df = pd.read_csv(CLEAN_ANALYTICS)

        logger.info("Processed Analytics Dataset Loaded")

        return df

    except FileNotFoundError:

        logger.warning("Processed Analytics Dataset Not Found")

        logger.warning("Loading Raw Analytics Dataset")

        return pd.read_csv(DATASET_ANALYTICS)


# =========================================================
# Prediction Dataset
# =========================================================

@st.cache_data
def load_prediction_dataset():

    try:

        df = pd.read_csv(CLEAN_PREDICTION)

        logger.info("Processed Prediction Dataset Loaded")

        return df

    except FileNotFoundError:

        logger.warning("Processed Prediction Dataset Not Found")

        logger.warning("Loading Raw Prediction Dataset")

        return pd.read_csv(DATASET_PREDICTION)