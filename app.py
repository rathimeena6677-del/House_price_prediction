import streamlit as st
import pickle
import numpy as np

# Load model
with open("model_pickle (1)", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq.ft)", min_value=100.0, value=1000.0)
bedrooms = st.number_input("Bedrooms", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)

if st.button("Predict Price"):
    data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(data)
    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
