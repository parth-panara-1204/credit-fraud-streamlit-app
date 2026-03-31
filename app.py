import streamlit as st
import numpy as np
import joblib

pipeline = joblib.load("pipeline_model.pkl")

st.title("Credit Card Fraud Detection")

features = []

time = st.number_input("Time")
features.append(time)

for i in range(1, 29):
    val = st.number_input(f"V{i}")
    features.append(val)

amount = st.number_input("Amount")
features.append(amount)

if st.button("Predict"):

    features = np.array(features).reshape(1, -1)

    prediction = pipeline.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")