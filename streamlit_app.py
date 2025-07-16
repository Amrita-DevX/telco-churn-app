import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime
from utils import add_custom_features

#  Automatically Load the Latest Model
model_dir = "models"
model_files = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]
model_files.sort(key=lambda x: os.path.getmtime(os.path.join(model_dir, x)), reverse=True)
latest_model_path = os.path.join(model_dir, model_files[0])

model = joblib.load(latest_model_path)

st.title("📊 Telco Customer Churn Prediction App")

st.markdown("Enter customer information to predict whether they will churn or not.")

#  Input Fields for All 19 Features (except customerID & TotalCharges)
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("senior citizen?", ["Yes", "No"])
Partner = st.selectbox("Has Partner?", ["Yes", "No"])
Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)

#  Predict Button
if st.button("Predict Churn"):
    input_data = pd.DataFrame([{
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges
    }])

    prediction = model.predict(input_data)[0]
    churn_label = "Churn" if prediction == 1 else "No Churn"

    st.success(f"✅ Prediction: **{churn_label}**")

    # Show probabilities
    prob = model.predict_proba(input_data)[0]
    st.write(f"📈 Churn Probability: {prob[1]*100:.2f}%")
    st.write(f"📉 No Churn Probability: {prob[0]*100:.2f}%")