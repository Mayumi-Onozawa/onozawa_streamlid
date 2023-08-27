import streamlit as st

apple = st.checkbox("apple")
oraneg = st.checkbox("orange")
melon = st.checkbox("melon")

fruits = []
if apple:
    fruits.append("apple")
if orange:
    fruits.append("orange")
if melon:
    fruits.append("melon")

st.write(f'You selected{fruits}')