import streamlit as st

st.title("肺炎研究臨床治療存活率")
st.divider()
st.logo("images/logo.jpg",size="large")

col1,col2 =st.columns(2)

with col1:
    st.text_input("請輸入您的姓名",key="name")

with col2:
    st.text_input("請輸入您的email",key="email")

c1= st.container()
with c1:
    st.write("肺癌長年霸佔台灣癌症死亡率第 1 名。造成肺癌高死亡率的主因是早期症狀不明顯，如何能夠早期篩檢肺癌，LDCT 是什麼？肺癌的種類有哪些？台灣常見的肺腺癌又是什麼？肺癌如何診斷？目前肺癌治療策略是什麼？相關懶人包一次報你知")

st.divider()
st.header("powerBI研究畫面")
st.image("images/lung.png",caption="肺癌存活率與各期占比圖")
st.image("images/smoking_behavior.png",caption="吸菸分布圖")

    
with st.sidebar:
    with st.container():
        st.header("選單標題1")
        st.write("選單內容1")
        st.button("按鈕A1")
        st.button("按鈕K1")
    st.divider()
    with st.container():
        st.header("選單標題2")
        st.write("選單內容2")
        st.button("按鈕B")
        st.button("按鈕L")

# 任何不在 sidebar , footer 都是 Section A

# Layout (C) Footer
with st.bottom:
    st.header("關於我")
    st.text("聯絡資訊: email:")
