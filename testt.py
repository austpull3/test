import streamlit as st

st.markdown("# Welcome!")

st.snow() 
    
st.markdown("# Predict Your Round at Augusta National")

st.markdown("# ENJOY!")
st.sidebar.markdown("# Welcome!🎈❄️")

from PIL import Image 
image1 = Image.open('anational.webp')
st.image(image1)

st.sidebar.button("Press me!")

