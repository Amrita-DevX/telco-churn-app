# 📉 Telco Customer Churn Prediction App

An end-to-end machine project that predicts whether a customer is likely to churn based on their usage behavior, contract type, and demographics. Built with **Python**, **Scikit-learn**, and **Streamlit**, this app helps telecom companies understand and visualize churn patterns interactively.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Cloud-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Model-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Status-Deployed-brightgreen" />
</p>

---

## 🔍 Project Overview

This project analyzes the **Telco Customer Churn** dataset, performs feature engineering and ML modeling to predict customer churn, and provides a user-friendly **dashboard** with rich visualizations and insights.

The app allows:
- Live predictions
- Visual churn analysis
- Business-friendly insights

---

## 🚀 Features

✅ Data Cleaning & EDA  
✅ Versioned ML Model Training  
✅ Streamlit Dashboard & Inference UI  
✅ Donut charts, bar plots, KPIs, filters  
✅ Git + GitHub + Streamlit Cloud deployment  

---

## 📊 Streamlit app

**🧾  User Input Interface &  Churn Prediction Output**

**📈  Business Dashboard**

The dashboard provides answers to the following:

1. **Churn Distribution** – % of customers churned  
2. **Contract Type** – Month-to-month vs 1/2-year contracts  
3. **Tenure Analysis** – Are new users more likely to churn?  
4. **Charges Impact** – Monthly vs Total Charges  
5. **Services Used** – Internet, Online Backup, Streaming, etc.  
6. **Demographics** – Gender, Senior Citizens, Dependents  
7. **Payment Method** – Is auto-pay safer?  
8. **Actionable Segments** – High-risk customer profiles

---

## 🧠 Tech Stack

| Layer          | Technology         |
|----------------|--------------------|
| Data Handling  | Pandas, NumPy      |
| Visualization  | Plotly             |
| Model Building | Scikit-learn       |
| App Framework  | Streamlit          |
| Deployment     | Streamlit Cloud    |
| Versioning     | Git + GitHub       |

---

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Amrita-DevX/telco-churn-app.git
cd telco-churn-app

# Optional: create virtual environment
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

```
---

▶️ **Run the App Locally**

To run the app on your local machine:
```
streamlit run streamlit_app.py
```
Once it starts, open the provided URL in the browser.

---


🚫 **Deployment Note**

Due to compatibility issues on Streamlit Cloud and Render, we were unable to deploy this app online.

❌ **Common Deployment Errors Faced:**

- ModuleNotFoundError: No module named 'distutils'

- numpy==1.26.0 not compatible with Python 3.13

- pip._vendor.pyproject_hooks._impl.BackendUnavailable

🔹 **Why This Happened:**

These platforms currently use Python 3.13, while some packages (e.g., NumPy, Pandas, Scikit-learn) are not fully stable or compatible with this version yet.

🔧 **Advice for Anyone Using This Repo:**

If you want to deploy this project on Render or Streamlit Cloud, we recommend:

- Setting your Python version to 3.10 or 3.9

- Using numpy==1.24.3, pandas==1.5.3, and scikit-learn==1.3.2 wihch is compatible 

- Including a runtime.txt file (if needed )with this line:
```
python-3.10
```

- Avoiding large files like videos in the repo

This project is 100% working locally and produces reliable results and visualizations. Just not yet cloud-deployed due to external dependency conflicts.
You can check out the a preview of the app, Go to 
```
telco-churn-app/
│
├── data/churn_app_video.mp4     

```

---


## 📁 Project Structure

```
telco-churn-app/
│
├── data/                    # Dataset (optional local copy)
├── models/                  # Trained model files (.pkl)
├── pages/                   # Dashboard sub-pages (1_Dashboard.py etc.)
├── docs/                    # Documentation
├── eda_model_building.py    # EDA
├── model_training.py        # Train ML model
├── utils.py                 # Helper function
├── streamlit_app.py         # Main Streamlit entrypoint
├── requirements.txt         # All project dependencies
└── README.md                # Project documentation

```
---

## ✨ Future Enhancements
 
- Add SHAP or LIME for model interpretability
- Build retraining pipeline for new data
- Export charts from dashboard
- Add login/authentication for private dashboards
- Deploy to Hugging Face Spaces or Docker

---

## 📜 License

- This project is licensed under the MIT License.
- Feel free to use, share, and improve upon it!




