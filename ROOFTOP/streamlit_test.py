import streamlit as st
import pandas as pd
import numpy as np


st.title('Roof Top Detection')




# Add a text input field
user_input = st.text_input("Enter some text:", "Default text")

# Display the entered text
st.write("You entered:", user_input)


our_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h



if st.checkbox('Parameters of model'):
    st.subheader('Raw data')
    st.write("test test test test test test \n test test test test test")
    
    
    
animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'    
    
    
# stateful button     
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
    
"""    
# Toggle button    
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
    
"""