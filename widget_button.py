import streamlit as st

account = st.text_input("Accoiunt", "0000000")
pw = st.text_input("password", "12345")

if pw == "streamlit":
    st.write("Login success")
else:
    st.write("Error")