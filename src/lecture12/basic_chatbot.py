import streamlit as st
import google.generativeai as genai

# ページ設定
st.set_page_config(
    page_title="基本チャットボット",
    page_icon="🤖"
)

st.title("🤖 Gemini 基本チャットボット")

# Streamlit SecretsからAPIキーを取得
api_key = st.secrets["GEMINI_API_KEY"]

# Gemini APIの設定
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# メッセージ履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 過去のメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力
prompt = st.chat_input("メッセージを入力してください...")
if prompt:
    # ユーザーメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # ユーザーメッセージを履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # AI応答を生成・表示
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        
        # AI応答を履歴に追加
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response.text
        })