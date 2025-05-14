import streamlit as st

# 持ち物リスト
items = ["PC", "充電器", "スマートフォン", "財布", "筆記用具", "ノート", "ハンカチ", "ティッシュ"]

# リストの表示
st.subheader("持ち物リスト:")
for item in items:
    st.checkbox(item) 