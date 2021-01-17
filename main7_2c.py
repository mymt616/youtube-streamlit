import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

# streamlit run main.py
st.title('Streamlit 超入門')

#インタラクティブウィジェット
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # pirnt (i)
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.2)



#if st.checkbox('Show Image'):
#    img = Image.open('test.jpg')
#    st.image(img, caption='kid001',use_column_width=True) #True レイアウト幅に合わせる


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ解答')


# option = st.selectbox(
#     'あなたの好きな数字を教えて下さい。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は', option , 'です。'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は',text,'です。'

# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション',condition