import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# streamlit run main.py
st.title('Streamlit 超入門')

#インタラクティブウィジェット
st.write('Interactive Widgets')

#if st.checkbox('Show Image'):
#    img = Image.open('test.jpg')
#    st.image(img, caption='kid001',use_column_width=True) #True レイアウト幅に合わせる

option = st.selectbox(
    'あなたの好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は', option , 'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は',text,'です。'

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション',condition