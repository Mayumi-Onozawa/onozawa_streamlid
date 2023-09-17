import streamlit as st
import numpy as np
import pandas as pd

message = st.chat_message("assistant")
message.write("Hello human")

data = np.random.ramdn(30, 3)
message.write(pd.DataFrame(data))
message.bar_chart(data)