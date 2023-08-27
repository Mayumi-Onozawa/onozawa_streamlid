import streamlit as st

options = st.multiselect(
    "What are your favorite fruits?",
    ["Apple","Orange","Melon","Peach"],
    ["Apple","Meoln"]
)

st.write("You selscted: ", options)