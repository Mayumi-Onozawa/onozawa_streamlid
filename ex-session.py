import streamlit as st

st.multiselect(
    "好きなスポーツは？",
    ["野球","サッカー","バレーボール","テニス","水泳", "その他"],
    key = "suport"
)

st.json(f"{st.session_state.suport}")