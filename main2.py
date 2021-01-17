import streamlit as st
import numpy as np
import pandas as pd

# streamlit run main.py
st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)
#折れ線
st.line_chart(df)
#折れ線 色で埋める
st.area_chart(df)
#棒グラフ
st.bar_chart(df)

