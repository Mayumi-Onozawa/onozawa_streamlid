import streamlit as st

st.radio("好きな食べ物は？", ("ラーメン","カレー","寿司"),horizontal = True, key = "food")
st.write(f"{st.session_state.food}が好きなんですね！")