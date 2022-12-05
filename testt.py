import streamlit as st

st.markdown("# Welcome!")

st.snow() 
    
st.markdown("# Welcome to the Rent Predictor 🏘🎄")

st.markdown("# ENJOY!")
st.sidebar.markdown("# Welcome!🎈❄️")

import base64
def add_bg_from_local(image_file):
with open(image_file, "rb") as image_file:
     encoded_string = base64.b64encode(image_file.read())
     st.markdown(
     f"""
     <style>
     .stApp {{
     background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
     background-size: cover
     }}
     </style>
      """,
      unsafe_allow_html=True
        )
    add_bg_from_local('anational.webp')   


