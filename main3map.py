import streamlit as st
import numpy as np
import pandas as pd

# streamlit run main.py
st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns = ['lat','lon']
)
#地図表示
st.map(df)
