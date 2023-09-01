import streamlit as st
import datetime

name = st.text_input("氏名", "")
mail = st.text_input("メールアドレス", "")
day = st.date_input("誕生日")
sex =  st.radio("性別", ("男","女","その他"))
job = st.selectbox(
    "職業",("会社員","アルバイト","派遣","その他")
)
hobby = st.multiselect(
    "趣味",["読書","スポーツ","ゲーム","料理","音楽","ショッピング","その他"]
)
if st.button("submit"):
    st.json(
        {
            "name" : name,
            "mail" : mail,
            "birthday": day,
            "gender" : sex,
            "occupation": job,
            "hobby": hobby,
        }
    )