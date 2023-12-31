import streamlit as st
import time, random
st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user", "content":prompt})

    with st.chat_message("assistant"):
        message_pleceholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?","Hi, human! Is there anything I can help you with?","Do you need help?"
            ]
        )

        for chunk in assistant_response.split():
           full_response += chunk + " "
           time.sleep(0.1)

           message_pleceholder.markdown(full_response + " ")

        message_pleceholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant","content":full_response})
       