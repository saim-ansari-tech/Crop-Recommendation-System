import streamlit as st
import joblib
import pandas as pd
st.title("Crop Recommendation System")
model = joblib.load('model/crop_recommendation.pkl')
encoder = joblib.load('model/encoder.pkl')
features = joblib.load('model/features.pkl')

st.header('Enter your Land details')
usr_input = {}



usr_input['N'] = st.number_input('Nitrogen (N)', 0.0, 140.0, 50.0)
usr_input['P'] = st.number_input('Phosphorus (P)', 5.0, 145.0, 50.0)
usr_input['K'] = st.number_input('Potassium (K)', 5.0, 205.0, 40.0)
usr_input['temperature'] = st.number_input('temperature', min_value=0.0, max_value=50.0, value=0.0)
usr_input['humidity'] = st.number_input('humidity', min_value=0.0, max_value=100.0, value=0.0)
usr_input['ph'] = st.number_input('ph', min_value=0.0, max_value=14.0, value=6.5)
usr_input['rainfall'] = st.number_input('rainfall', min_value=0.0, max_value=300.0, value=0.0)





if usr_input['rainfall'] > 300:
    st.warning("Rainfall seems outside normal range. Prediction may be unreliable.")
button = st.button('Predict')
if button == True:
    df = pd.DataFrame([usr_input])
    pred = model.predict(df)
    crop = encoder.inverse_transform(pred)
    st.success(f"Recommended Crop: {crop[0]}")

