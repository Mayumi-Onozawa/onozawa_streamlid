import streamlit as st

promt = st.chat_input("ここに入力してください")
if promt:
    st.write(f"入力内容: {promt}")