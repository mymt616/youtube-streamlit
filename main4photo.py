import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# streamlit run main.py
st.title('Streamlit 超入門')

#インタラクティブウィジェット
st.write('Interactive Widgets')

if st.checkbox('Show Image'):
    img = Image.open('test.jpg')
    st.image(img, caption='kid001',use_column_width=True) #True レイアウト幅に合わせる


