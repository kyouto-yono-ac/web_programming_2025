import streamlit as st

st.title("第7回 Streamlit レイアウト演習 - 解答例")
st.caption("st.sidebar, st.columns, st.expander を使ってみましょう。")

st.markdown("---")
st.subheader("演習1: サイドバー (st.sidebar)")
st.write("**課題**: サイドバーに自分の名前と学籍番号を表示するテキスト入力を配置。")

st.sidebar.title("自己紹介")
user_name = st.sidebar.text_input("お名前を入力してください:", value="大妻 花子", key="layout_ans_name")
user_id = st.sidebar.text_input("学籍番号を入力してください:", value="21XX000", key="layout_ans_id")
if user_name and user_id:
    st.sidebar.write(f"名前: {user_name}")
    st.sidebar.write(f"学籍番号: {user_id}")

st.markdown("---")
st.subheader("演習2: カラムレイアウト (st.columns)")
st.write("**課題**: メインエリアを2列に分け、左列に好きなものの画像、右列にその説明文を表示。")

col1, col2 = st.columns(2)
with col1:
    st.header("好きなもの")
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="可愛いネコ", use_column_width=True)
    
with col2:
    st.header("説明文")
    st.write("ネコが大好きです。自由気ままで愛らしい性格に癒されます。")
    st.write("毛がふわふわで、見ているだけで幸せな気持ちになります。")

st.markdown("---")
st.subheader("演習3: エキスパンダー (st.expander)")
st.write("**課題**: 説明文の下にエキスパンダーを設け、さらに詳細な情報を隠して表示できるようにする。")

with st.expander("詳細情報を見る"):
    st.write("ネコについてのさらに詳しい情報：")
    st.write("- 睡眠時間は1日12-16時間")
    st.write("- 優れた聴覚と夜間視力を持つ")
    st.write("- 喉を鳴らすゴロゴロ音は癒し効果がある")
    st.image("https://static.streamlit.io/examples/dog.jpg", caption="犬も可愛いです", width=300)

st.markdown("---")
st.success("✅ レイアウト演習の解答例です。各機能を組み合わせることで、見やすく整理されたアプリが作成できます。") 