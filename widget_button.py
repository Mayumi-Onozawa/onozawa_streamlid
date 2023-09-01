import streamlit as st

txt = st.text_area("Test to analyze", '''Hello World, This is Streamlit. This is Text_area widget.''')
st.write(f'単語数={len(txt.split(" "))}単語')