import streamlit as st

st.title("PowerBI 簡報說明")

tab1,tab2 =st.tabs("肺癌存活率與各期占比圖","吸菸分布圖")

with tab1:
    st.header("肺癌存活率與各期占比圖")
    st.image("imges/lung.png",caption="肺癌存活率與各期占比圖")

with tab2:
    st.header("吸菸分布圖")
    st.image("images/smoking_behavior.png",caption="吸菸分布圖")