import streamlit as st

st.title("用streamlit架站")

with st.sidebar:
    st.header("選單標題")
    st.write("選單內容")
    st.button("按鈕A")
    st.button("按鈕B")

    st.bottom.header("關於我")
    st.text("聯絡資訊: email: norn_chang@hotmail.com")