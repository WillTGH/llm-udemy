import streamlit as st
import pandas as pd
import numpy as np

st.title('text input')

text = st.text_input('Enter text:')

number = st.slider('Pick a number', 0, 100)

option = [
    'option 1',
    'option 2',
    'option 3'
]

choice = st.selectbox('Pick an option', option)

st.write(f'You selected: {choice}')

if text:
    st.write(f'You entered: {text}')
    
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df.to_csv('data.csv')

st.write(f'data frame')
st.write(df)


chartdata = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
    )

st.line_chart(chartdata)

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)