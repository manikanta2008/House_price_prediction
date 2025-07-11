import streamlit as st
import numpy as np
import joblib

# Load your saved model
model = joblib.load('house_price_model.pkl')

st.title('House Price Prediction')

st.write('Enter the details below to predict the house price:')

# Input fields matching your columns
MedInc = st.number_input('Median Income (10k USD)', min_value=0.0, max_value=20.0, value=3.0, step=0.1)
HouseAge = st.number_input('House Age (years)', min_value=0, max_value=100, value=20)
AveRooms = st.number_input('Average Rooms', min_value=0.0, max_value=20.0, value=5.0)
AveBedrms = st.number_input('Average Bedrooms', min_value=0.0, max_value=10.0, value=1.0)
Population = st.number_input('Population', min_value=1, max_value=50000, value=1000)
AveOccup = st.number_input('Average Occupancy', min_value=0.0, max_value=10.0, value=3.0)
Latitude = st.number_input('Latitude', min_value=30.0, max_value=50.0, value=35.0)
Longitude = st.number_input('Longitude', min_value=-125.0, max_value=-100.0, value=-120.0)

# Predict button
if st.button('Predict House Price'):
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(input_data)
    st.success(f'🏠 Predicted House Price: ${prediction[0]:,.2f}')
