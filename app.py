import streamlit as st
import pickle
import numpy as np

# Load model

model = pickle.load(open("heart_model.pkl", "rb"))

st.set_page_config(
page_title="Heart Disease Predictor",
page_icon="❤️"
)

st.title("❤️ Heart Disease Prediction")

st.write("Enter patient information below.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox(
"Sex",
["Female", "Male"]
)

cp = st.selectbox(
"Chest Pain Type",
[0, 1, 2, 3]
)

trestbps = st.number_input(
"Resting Blood Pressure",
min_value=50,
max_value=250,
value=120
)

chol = st.number_input(
"Cholesterol",
min_value=50,
max_value=700,
value=200
)

fbs = st.selectbox(
"Fasting Blood Sugar > 120 mg/dl",
[0, 1]
)

restecg = st.selectbox(
"Resting ECG",
[0, 1, 2]
)

thalach = st.number_input(
"Maximum Heart Rate Achieved",
min_value=50,
max_value=250,
value=150
)

exang = st.selectbox(
"Exercise Induced Angina",
[0, 1]
)

oldpeak = st.number_input(
"Old Peak",
min_value=0.0,
max_value=10.0,
value=1.0
)

slope = st.selectbox(
"Slope",
[0, 1, 2]
)

ca = st.selectbox(
"Number of Major Vessels",
[0, 1, 2, 3, 4]
)

thal = st.selectbox(
"Thal",
[0, 1, 2, 3]
)

if st.button("Predict"):

```
sex_value = 1 if sex == "Male" else 0

features = np.array([[
    age,
    sex_value,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal
]])

prediction = model.predict(features)

if prediction[0] == 1:
    st.error("⚠️ Heart Disease Detected")
else:
    st.success("✅ No Heart Disease Detected")
```
