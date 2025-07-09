import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

st.title("第13回 最終課題: パーソナル学習アシスタント")
st.caption("AIがあなたの学習をサポートする個人専用の学習アシスタントを作成しましょう。")

st.markdown("---")
st.subheader("最終課題: パーソナル学習アシスタント")
st.write("**課題**: Gemini APIを活用して学習プラン作成・質問応答・進捗管理機能を持つ学習アシスタントを作成する。")

# ここに最終課題のコードを記述してください
# ヒント: genai.configure でAPI設定、st.session_state で学習履歴管理、st.tabs で機能分け


st.markdown("---")
st.info("💡 Gemini APIキーをst.text_inputで入力し、学習リソースは data/learning_resources.csv から読み込みましょう。") 