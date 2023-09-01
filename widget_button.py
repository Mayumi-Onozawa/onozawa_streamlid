import streamlit as st

number = st.number_input("insert a number", step=1)
st.write("The current number is ", number)