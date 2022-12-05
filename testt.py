import streamlit as st

st.markdown("# Welcome!")
def main_page():
    st.snow() 
    
    st.markdown("# Welcome to the Rent Predictor 🏘🎄")
    st.markdown("### In the sidebar to the left there are several pages that can take you through the machine learning side of the predictor.")
    st.markdown("### If you wish to go straight to the predictor select that page.")
    from PIL import Image 
    image1 = Image.open('/Users/austinpullar/Desktop/house3.jpeg')
    st.image(image1)

    st.markdown("# ENJOY!")
    st.sidebar.markdown("# Welcome!🎈❄️")
    
    page_names_to_funcs = {
    "Welcome Page": main_page,
    }

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
