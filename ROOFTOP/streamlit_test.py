import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st

st.header('Roof Top Detection', divider='blue',help='This is an application where user can drop an image and the system will detect the roof top  using deep learning model')
st.header('Deep Learning application is :blue[cool] :sunglasses:')

st.caption(' Introduction: The usage of this application is free of cost')

"""
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
"""
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
uploaded_file = st.file_uploader("Choose an image...", type="jpg, jpeg, tiff")
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
