import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.sidebar.write('Dataframe')

#df=pd.DataFrame({
#    '1列目':[1,2,3,4],
#    '2列目':[10,20,30,40]
#})

#st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)
#st.table(df.style.highlight_max(axis=0))

#df=pd.DataFrame(
#    np.random.rand(20,3),
#    columns=['a','b','c']
#)

#st.line_chart(df)


#df=pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon']
#)

#st.map(df)

#if st.checkbox('Show Image'):
#    img=Image.open('main.JPG')
#    st.image(img,caption='aquaponi',use_column_width=True)

#option=st.selectbox(
#    'あなたの好きな数字を教えてください。',
#    list(range(1,11))
#)

#'あなたの好きな数字は',option,'です'

text=st.text_input('あなたの趣味を教えてください')
'あなたの趣味は：',text

condition=st.slider('あなたの今の調子は',0,100,50)
'コンディション：',condition



