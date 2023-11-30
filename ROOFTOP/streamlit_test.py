import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')




# Add a text input field
user_input = st.text_input("Enter some text:", "Default text")

# Display the entered text
st.write("You entered:", user_input)


our_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h



if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)