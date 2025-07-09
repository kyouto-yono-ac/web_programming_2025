import streamlit as st
import pandas as pd
import plotly.express as px

st.title("第13回 最終課題: 美容・コスメ商品比較ダッシュボード")
st.caption("様々な美容・コスメ商品を比較・分析できるインタラクティブなダッシュボードを作成しましょう。")

st.markdown("---")
st.subheader("最終課題: 美容・コスメ商品比較ダッシュボード")
st.write("**課題**: CSVファイルからコスメ商品データを読み込み、フィルタリング・可視化・分析機能を持つダッシュボードを作成する。")

# ここに最終課題のコードを記述してください
# ヒント: pd.read_csv でデータ読み込み、st.sidebar でフィルタ、st.tabs でタブ分け、px.bar や px.scatter で可視化


st.markdown("---")
st.info("💡 CSVファイルは data/cosmetic_products.csv から読み込み、サイドバーでフィルタリング、メインエリアでタブ分けして表示しましょう。") 