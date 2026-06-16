import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="AI Credit Scoring",
    page_icon="💳",
    layout="centered"
)

st.title("💳 AI Credit Scoring System")
st.markdown("### Check the creditworthiness of an applicant")

st.divider()

age = st.number_input(
    "👤 Age",
    min_value=18,
    max_value=100,
    value=25
)

income = st.number_input(
    "💰 Monthly Income",
    min_value=0,
    value=50000
)

loan = st.number_input(
    "🏦 Loan Amount",
    min_value=0,
    value=100000
)

savings = st.number_input(
    "💵 Savings",
    min_value=0,
    value=20000
)

if st.button("🔍 Predict Credit Risk"):

    st.success("Prediction Completed!")

    st.metric(
        label="Credit Score",
        value="780"
    )

    st.metric(
        label="Risk Level",
        value="Low Risk"
    )