import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


