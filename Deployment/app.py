import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load model and scaler
model = tf.keras.models.load_model("csat_ann_model.keras")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="CSAT Prediction App", layout="centered")

st.title("Customer Satisfaction Score Prediction")
st.write("Predict CSAT score based on customer support interaction details.")

st.subheader("Enter Interaction Details")

channel = st.number_input("Channel Name (Encoded)", min_value=0)
category = st.number_input("Category (Encoded)", min_value=0)
subcategory = st.number_input("Sub Category (Encoded)", min_value=0)
agent = st.number_input("Agent Name (Encoded)", min_value=0)
supervisor = st.number_input("Supervisor (Encoded)", min_value=0)
manager = st.number_input("Manager (Encoded)", min_value=0)
tenure = st.number_input("Tenure Bucket (Encoded)", min_value=0)
shift = st.number_input("Agent Shift (Encoded)", min_value=0)

if st.button("Predict CSAT Score"):

    input_data = np.array([[channel, category, subcategory,
                            agent, supervisor, manager,
                            tenure, shift]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    csat_score = round(prediction[0][0])

    st.success(f"Predicted CSAT Score: {csat_score}")