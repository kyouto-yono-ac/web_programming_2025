import streamlit as st

# タイトル
st.title("動的持ち物チェックリスト")
st.write("このアプリでは、持ち物リストに新しいアイテムを追加できます。")

# 持ち物リストの初期化
if 'items' not in st.session_state:
    st.session_state.items = ["PC", "充電器", "スマートフォン", "財布"]

# 新しいアイテムの入力
new_item = st.text_input("新しいアイテムを入力:")

# 追加ボタン
if st.button("追加"):
    # ここに追加のロジックを書く
    pass

# リストの表示
st.subheader("持ち物リスト:")
for item in st.session_state["items"]:
    st.checkbox(item)

# ヒント
st.caption("ヒント: `st.session_state.items.append(new_item)` でリストに追加できます。") 