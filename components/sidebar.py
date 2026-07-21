"""
=========================================================
Sidebar Component
=========================================================
"""

import streamlit as st

from config import PROJECT_NAME


def show_sidebar():

    st.sidebar.title(PROJECT_NAME)

    st.sidebar.markdown("---")

    st.sidebar.info(
        "AI-Powered Road Accident Analysis & Severity Prediction Platform"
    )