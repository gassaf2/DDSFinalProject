import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from io import StringIO
import streamlit as st

st.header('Roof Top Detection', divider='blue',help='This is an application where user can drop an image and the system will detect the roof top  using deep learning model')
st.header('Deep Learning application is :blue[cool] :sunglasses:')

st.caption(' Introduction: The usage of this application is free of cost')

"""
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
"""
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

static_folder_path = "ROOFTOP/test_streamlit"
# Get the image file path within the static folder
image_filename = "austin1__tile_0_0.png"
image_path = f"{static_folder_path}/{image_filename}"

# Read the image using PIL (Python Imaging Library)
image = Image.open(image_path)

# Display the image in your Streamlit app
st.image(image, caption="Example Image", use_column_width=True)
    
    
    
    
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
