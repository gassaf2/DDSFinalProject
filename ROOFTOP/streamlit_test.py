import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')

# Add a text input field
user_input = st.text_input("Enter some text:", "Default text")

# Display the entered text
st.write("You entered:", user_input)