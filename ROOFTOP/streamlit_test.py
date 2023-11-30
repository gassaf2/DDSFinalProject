import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')


# Create tabs using beta_columns
tabs = st.beta_columns(3)

# Add content to each tab
with tabs[0]:
    st.header("Tab 1")
    st.write("This is the content of Tab 1")

with tabs[1]:
    st.header("Tab 2")
    st.write("This is the content of Tab 2")

with tabs[2]:
    st.header("Tab 3")
    st.write("This is the content of Tab 3")

# Add a text input field
user_input = st.text_input("Enter some text:", "Default text")

# Display the entered text
st.write("You entered:", user_input)