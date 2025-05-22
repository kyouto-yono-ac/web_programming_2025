import streamlit as st

st.title("第7回 Streamlit レイアウト演習 - 解答")
st.caption("st.sidebar, st.columns, st.expander を使ってみましょう。")

st.markdown("---\n\n**演習1.1: サイドバー (st.sidebar)**")
st.sidebar.title("自己紹介入力")
user_name = st.sidebar.text_input("お名前を入力してください:", value="大妻 花子", key="layout_ans_name")
user_id = st.sidebar.text_input("学籍番号を入力してください:", value="XXYYZZ", key="layout_ans_id")
if user_name and user_id:
    st.sidebar.success(f"名前: {user_name}\n学籍番号: {user_id}")
else:
    st.sidebar.info("サイドバーから名前と学籍番号を入力してください。")

st.markdown("---\n\n**演習1.2: カラムレイアウト (st.columns)**")
st.subheader("好きなものを2列で紹介")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**好きな動物**")
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="ネコ", use_column_width=True)
    st.write("猫は自由気ままで可愛らしいです。")

with col2:
    st.markdown("**好きな食べ物**")
    st.image("https://static.streamlit.io/examples/dog.jpg", caption="イヌ (例: こちらも可愛い)", use_column_width=True)
    st.write("お寿司やラーメンが好きです。")

st.markdown("---\n\n**演習1.3: エキスパンダー (st.expander)**")
st.subheader("詳細情報")
with st.expander("ここをクリックして詳細を表示"):
    st.write("エキスパンダーは、通常は隠しておきたい補足情報や詳細設定を表示するのに便利です。")
    st.warning("この情報はエキスパンダー内にあります。")
    st.image("https://static.streamlit.io/examples/owl.jpg", caption="フクロウもいます")

st.markdown("---
")
st.success("レイアウト演習の解答例です。") 