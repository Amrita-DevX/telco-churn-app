import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned dataset
df = pd.read_csv("data/cleaned_churn_data.csv")

# Page config
st.set_page_config(page_title="📊 Churn Dashboard", layout="wide")
st.title("📊 Telco Customer Churn Dashboard")

# KPI Section
st.subheader("Churn Overview")
col1, col2, col3 = st.columns(3)

total_customers = len(df)
total_churned = df[df['Churn'] == 'Yes'].shape[0]
churn_rate = round((total_churned / total_customers) * 100, 2)

col1.metric("Total Customers", f"{total_customers}")
col2.metric("Churned Customers", f"{total_churned}")
col3.metric("Churn Rate", f"{churn_rate}%")

# Donut Chart
churn_counts = df['Churn'].value_counts().reset_index()
churn_counts.columns = ['Churn', 'count']  # Rename columns

fig_donut = px.pie(
    churn_counts,
    names='Churn',        # Now refers to 'Yes' / 'No'
    values='count',       # Refers to how many in each
    hole=0.5, 
    title="Churn vs Non-Churn Customers",
    color_discrete_sequence=['tomato', 'mediumseagreen']
)

fig_donut.update_layout(margin=dict(t=50, b=0, l=0, r=0))

st.subheader("Churn vs Non-Churn Customers")
st.plotly_chart(fig_donut, use_container_width=True)

# Churn by Contract Type
st.subheader("Churn by Contract Type")
contract_churn = df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
fig_contract = px.bar(contract_churn, x='Contract', y='Count', color='Churn', barmode='group')
st.plotly_chart(fig_contract, use_container_width=True)

# Churn by Tenure
st.subheader("Tenure Distribution by Churn")
fig_tenure = px.box(df, x='Churn', y='tenure', color='Churn', title="Tenure Distribution")
st.plotly_chart(fig_tenure, use_container_width=True)

# Churn by Monthly Charges
st.subheader("Monthly Charges vs Churn")
fig_monthly = px.histogram(df, x='MonthlyCharges', color='Churn', barmode='overlay')
st.plotly_chart(fig_monthly, use_container_width=True)

# Churn by Services Used
st.subheader("Churn by Services Used")
services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport']
for service in services:
    st.markdown(f"**{service}**")
    temp = df.groupby([service, 'Churn']).size().reset_index(name='Count')
    fig = px.bar(temp, x=service, y='Count', color='Churn', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

# Churn by Demographics
st.subheader("Churn by Demographics")
demographics = ['gender', 'SeniorCitizen', 'Dependents']
for demo in demographics:
    st.markdown(f"**{demo}**")
    fig = px.histogram(df, x=demo, color='Churn', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

# Churn by Payment Method
st.subheader("Churn by Payment Method")
payment = df.groupby(['PaymentMethod', 'Churn']).size().reset_index(name='Count')
fig_payment = px.bar(payment, x='PaymentMethod', y='Count', color='Churn', barmode='group')
st.plotly_chart(fig_payment, use_container_width=True)

# Actionable Segments
st.subheader("Actionable Segments")
segment = df[(df['Churn'] == 'Yes') & 
             (df['Contract'] == 'Month-to-month') &
             (df['TechSupport'] == 'No') & 
             (df['MonthlyCharges'] > 80) & 
             (df['tenure'] < 6)]
st.markdown(f"🔍 **High-Risk Segment (Churned, No TechSupport, High Charges, Low Tenure)**: {segment.shape[0]} customers")
st.dataframe(segment[['gender', 'SeniorCitizen', 'tenure', 'Contract', 'TechSupport', 'MonthlyCharges']])
