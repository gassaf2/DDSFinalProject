import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')


# Create tabs
tabs = ["Tab 1", "Tab 2", "Tab 3"]
selected_tab = st.radio("Select a tab:", tabs)

# Add content based on the selected tab
if selected_tab == "Tab 1":
    st.header("Tab 1")
    st.write("This is the content of Tab 1")

elif selected_tab == "Tab 2":
    st.header("Tab 2")
    st.write("This is the content of Tab 2")

elif selected_tab == "Tab 3":
    st.header("Tab 3")
    st.write("This is the content of Tab 3")