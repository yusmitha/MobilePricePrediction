import streamlit as st
import pickle
import numpy as np
import os
 
# Fix file paths for deployment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pipe = pickle.load(open(os.path.join(BASE_DIR, 'pipe.pkl'), 'rb'))
df = pickle.load(open(os.path.join(BASE_DIR, 'df.pkl'), 'rb'))
 
st.title("Mobile Price Predictor")
 
# brand
Mobile_Brand = st.selectbox('Brand', df['Brand'].unique())
 
# Ram
Ram = st.selectbox('RAM(in GB)', [1, 2, 3, 4, 6, 8, 12, 16])
 
# Storage
Storage = st.selectbox('Storage(in GB)', [8, 16, 32, 64, 128, 256, 512, 1024])
 
# BackCameras
Number_Of_Cameras = st.selectbox('Number of Back Cameras', [1, 2, 3, 4])
 
# Primary Camera Pixels
Primary_Camera = st.selectbox('Primary Camera(in MP)', [5, 8, 12, 13, 16, 48, 50, 64, 100, 108, 200])
 
# Display Type
Display_Type = st.selectbox('Display Type', df['Display Type'].unique())
 
# screen size
screen_size = st.selectbox('Screen Size(in inches)', df['Screen Size(in)'].unique())
 
# Android
Android = st.selectbox('Android Version(in V)', df['Android Version'].unique())
 
# Battery
Battery = st.selectbox('Battery(in mAh)', df['Battery(mAh)'].unique())
 
# Number Of Cores
Cores = st.selectbox('Number of Cores', df['Number of Cores'].unique())
 
# Processor
Processor = st.selectbox('Processor', df['Processor Brand'].unique())
 
 
if st.button('Predict Price'):
    query = np.array([Mobile_Brand, Ram, Storage, Number_Of_Cameras, Primary_Camera,
                      Display_Type, screen_size, Android, Battery, Cores, Processor])
    query = query.reshape(1, 11)
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    st.success(f"💰 Estimated Price: ₹{predicted_price:,}")