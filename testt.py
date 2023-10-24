import streamlit as st
import pyodbc

st.markdown("# Welcome!")

st.snow() 
    
st.markdown("# Predict Your Round at Augusta National")

st.markdown("# ENJOY!")
st.sidebar.markdown("# Welcome!🎈❄️")

from PIL import Image 
image1 = Image.open('anational.webp')
st.image(image1)

st.sidebar.button("Press me!")

server = 'HOWE-ACCT-SERV\SAGE300CRE'
database = 'HoweInc'
username = 'sa'
password = 'L+S3jr3fP@*1'

# Create a connection string
connection_string = f"DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Establish a connection
conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

query = "USE [HoweInc]"
result = cursor.execute(query)
