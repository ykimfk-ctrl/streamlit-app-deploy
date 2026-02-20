import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def ask_llm(user_text: str, expert: str) -> str:
    if expert == "専門家A":
        system_msg = "あなたは厳格な専門家Aです。結論→根拠→指摘を箇条書きで短く答えてください。"
    else:
        system_msg = "あなたは優しい専門家Bです。初心者向けに、手順を小さく分けて答えてください。"

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "{text}")
    ])

    llm = ChatOpenAI(model="gpt-4o-mini")

    chain = prompt | llm
    result = chain.invoke({"text": user_text})
    return result.content


st.title("LLMアプリ（練習）")
st.write("専門家A/Bを切り替えて、入力文に応答します（まずはダミー返答）。")

expert = st.radio("専門家を選んでください", ["専門家A", "専門家B"])
user_text = st.text_area("入力", placeholder="ここに文章を入れてください")

if st.button("実行"):
    if not user_text.strip():
        st.warning("入力が空です。文章を入れてください。")
        st.stop()

    st.divider()
    st.write("選択:", expert)
    st.write("入力:", user_text)

    # まずはダミー（LLMにする前の段階）
    response = ask_llm(user_text, expert)
    st.success(response)    

