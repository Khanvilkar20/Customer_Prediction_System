import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/model.pkl")

st.title("Customer Purchase Prediction")

# Inputs
age = st.number_input("Age", 18, 60)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

pages_viewed = st.number_input(
    "Pages Viewed",
    1,
    20
)

time_spent = st.number_input(
    "Time Spent",
    1,
    60
)

previous_purchases = st.number_input(
    "Previous Purchases",
    0,
    10
)

category = st.selectbox(
    "Product Category",
    ["Books", "Electronics", "Fashion", "Sports"]
)

# Encoding
gender_encoded = 1 if gender == "Male" else 0

category_map = {
    "Books": 0,
    "Electronics": 1,
    "Fashion": 2,
    "Sports": 3
}

category_encoded = category_map[category]

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender_encoded],
        "pages_viewed": [pages_viewed],
        "time_spent": [time_spent],
        "previous_purchases": [previous_purchases],
        "product_category": [category_encoded]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Customer is likely to purchase.")
    else:
        st.error("❌ Customer is unlikely to purchase.")