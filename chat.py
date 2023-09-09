import streamlit as st

message = st.chat_message("assistant")
message.write("Hello human")
message.write("Hoe are you?")