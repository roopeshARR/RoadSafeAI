<div align="center">

# 🚗 RoadSafe AI

### AI-Powered Indian Road Accident Analysis & Severity Prediction Platform

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=24&duration=3500&pause=1000&color=2F81F7&center=true&vCenter=true&width=800&lines=Road+Accident+Analysis+using+Machine+Learning;Accident+Severity+Prediction;Interactive+Analytics+Dashboard;Built+with+Python+%7C+Streamlit+%7C+Scikit-Learn" />
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![GitHub Repo stars](https://img.shields.io/github/stars/roopeshARR/RoadSafeAI?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/roopeshARR/RoadSafeAI?style=for-the-badge)

</p>

<p align="center">
An intelligent Machine Learning platform that analyzes Indian road accident data, predicts accident severity, and provides interactive dashboards for data-driven road safety insights.
</p>

</div>

---

# 📖 Overview

RoadSafe AI is an end-to-end Machine Learning application developed to analyze Indian road accident datasets and predict accident severity. The project combines data preprocessing, feature engineering, model training, evaluation, and an interactive Streamlit dashboard into one platform.

The objective is to help researchers, students, and transportation authorities understand accident patterns and generate actionable insights using AI.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 Interactive Dashboard | Visualize accident statistics and trends |
| 🤖 Severity Prediction | Predict accident severity using ML |
| 📈 Data Analytics | Generate insights through charts and graphs |
| 🧹 Data Preprocessing | Automated cleaning and feature engineering |
| 🧠 Machine Learning | Model training and evaluation |
| 📂 Dataset Management | Support for multiple accident datasets |
| ⚡ Fast Web Interface | Streamlit-powered interactive application |

---

# 🏗️ System Architecture

```mermaid
flowchart LR

A[Indian Road Accident Dataset]
--> B[Data Cleaning]

B --> C[Feature Engineering]

C --> D[Machine Learning Models]

D --> E[Model Evaluation]

E --> F[Saved Model]

F --> G[Streamlit Dashboard]

G --> H[Severity Prediction]

G --> I[Analytics Dashboard]
```

---

# 🤖 Machine Learning Pipeline

```mermaid
graph LR

Dataset --> Cleaning

Cleaning --> Encoding

Encoding --> FeatureEngineering

FeatureEngineering --> TrainTestSplit

TrainTestSplit --> ModelTraining

ModelTraining --> Evaluation

Evaluation --> Prediction

Prediction --> Dashboard
```

---

# 📂 Project Structure

```text
RoadSafeAI
│
├── assets
│
├── components
│
├── pages
│
├── services
│
├── training
│
├── models
│
├── data
│   ├── raw
│   └── processed
│
├── Home.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-Learn |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Model Serialization | Joblib |
| Version Control | Git & GitHub |

---

# 📸 Application Preview

## 🏠 Dashboard

<p align="center">
<img src="assets/screenshots/dashboard.png" width="95%">
</p>

---

## 🤖 Prediction Page

<p align="center">
<img src="assets/screenshots/prediction.png" width="95%">
</p>

---

## 📊 Analytics

<p align="center">
<img src="assets/screenshots/analytics.png" width="95%">
</p>

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/roopeshARR/RoadSafeAI.git
```

## Navigate to Project

```bash
cd RoadSafeAI
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run Home.py
```

---

# 📊 Workflow

```text
Indian Road Accident Dataset
            │
            ▼
     Data Preprocessing
            │
            ▼
   Feature Engineering
            │
            ▼
 Machine Learning Models
            │
            ▼
    Model Evaluation
            │
            ▼
    Severity Prediction
            │
            ▼
 Interactive Dashboard
```

---

# 📈 Dashboard Modules

- 🏠 Home Dashboard
- 📊 Accident Analytics
- 🤖 Severity Prediction
- 📈 Trend Analysis
- 📉 Risk Assessment
- 📋 Machine Learning Insights

---

# 📂 Dataset

The project is designed to work with Indian road accident datasets.

Datasets are processed through:

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Model Training
- Severity Prediction

> **Note:** Large datasets may not be included in the repository because of GitHub storage limits. Replace them with your own datasets if necessary.

---

# 🎯 Future Roadmap

- ✅ Interactive Dashboard
- ✅ Accident Severity Prediction
- ✅ Machine Learning Pipeline
- ✅ Data Analytics
- 🔲 Deep Learning Models
- 🔲 Explainable AI (XAI)
- 🔲 Real-Time Traffic Integration
- 🔲 Weather API Integration
- 🔲 Cloud Deployment
- 🔲 Mobile Application

---

# 👨‍💻 Author

### **Avuthu Roopesh Reddy**

🎓 B.Tech Electronics & Communication Engineering  
🏫 Anurag University

📧 **Email**  
avuthuroopeshreddy@gmail.com

💻 **GitHub**  
https://github.com/roopeshARR

🔗 **LinkedIn**  
https://www.linkedin.com/in/avuthu-roopesh-reddy-09938b315/

---


<div align="center">

### 🚗 Building Safer Roads Through Artificial Intelligence

**Made with ❤️ by Avuthu Roopesh Reddy**

</div>
