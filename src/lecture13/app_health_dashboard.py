import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from datetime import datetime

st.title("第13回 最終課題: パーソナル健康管理ダッシュボード")
st.caption("健康データの記録・分析とAIによる健康アドバイスを提供するダッシュボードを作成しましょう。")

st.markdown("---")
st.subheader("最終課題: パーソナル健康管理ダッシュボード")
st.write("**課題**: 健康データの記録・可視化・分析機能とGemini APIを活用したAIアドバイス機能を持つダッシュボードを作成する。")

# ここに最終課題のコードを記述してください
# ヒント: st.session_state で健康データ管理、st.form でデータ入力、px.line でグラフ表示、genai で健康アドバイス


st.markdown("---")
st.info("💡 健康の基準値は data/health_tips.csv から読み込み、データ入力・可視化・AIアドバイスをタブで分けて表示しましょう。") 