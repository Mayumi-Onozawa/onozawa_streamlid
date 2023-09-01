import streamlit as st
from datetime import date

title = st.text_input("好きな映画は？", "Back to the future")
st.write("入力された映画：", title)