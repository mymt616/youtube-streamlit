import streamlit as st
import numpy as np
import pandas as pd

# streamlit run main.py
st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#st.write(df)
#st.datafremeは表の高さと幅を指定できる
#axis 0 は列　1　は 行
st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)

#静的
st.table(df.style.highlight_max(axis=0))

#マジックコマンド
# バッククォートは　SHIFT + @で出る
"""
# 章
## 節
### 項目

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
