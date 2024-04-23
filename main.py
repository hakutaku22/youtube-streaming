import streamlit as st
import time
  
st.title('streamlit入門')
st.write('Display image')

'START'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iteration.text(f'Iteration{i+1}')
   bar.progress(i+1)
   time.sleep(0.1)

left_column,right_column = st.columns(2)
left_column.button('右に文字を表示')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
#option = st.text_input(
#    'あなたが趣味'
#)
#'あなたの好きな数字は',option,'です'


#if st.checkbox('show image'):
#    img = Image.open('jpg-vs-jpeg.jpg')
#    st.image(img,caption='aaa',use_column_width=True)
