import streamlit as st

st.title("第7回 Streamlit レイアウト演習 - テンプレート")
st.caption("st.sidebar, st.columns, st.expander を使ってみましょう。")

st.markdown("---\n\n**演習1.1: サイドバー (st.sidebar)**")
st.write("サイドバーに自分の名前と学籍番号を表示するテキスト入力を配置し、入力があれば表示しましょう。")

# ここに演習1.1のコードを記述してください
# ヒント: st.sidebar.text_input() を使います
# st.sidebar.title("自己紹介入力")
# user_name = st.sidebar.text_input("お名前を入力してください:")
# user_id = st.sidebar.text_input("学籍番号を入力してください:")
# if user_name and user_id:
#     st.sidebar.success(f"名前: {user_name}\n学籍番号: {user_id}")
# else:
#     st.sidebar.info("サイドバーから名前と学籍番号を入力してください。")

st.markdown("---\n\n**演習1.2: カラムレイアウト (st.columns)**")
st.write("メインエリアを2列に分け、左列に好きなものの画像、右列にその説明文を表示しましょう。")

# ここに演習1.2のコードを記述してください
# ヒント: st.columns(2) で列を作成し、with col1: や with col2: ブロック内で要素を配置します。st.image() も使ってみましょう。
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("**好きな動物**")
#     # st.image("画像URL", caption="キャプション", use_column_width=True)
#     st.write("ここに好きな動物の説明を追加...")

# with col2:
#     st.markdown("**好きな食べ物**")
#     # st.image("画像URL", caption="キャプション", use_column_width=True)
#     st.write("ここに好きな食べ物の説明を追加...")

st.markdown("---\n\n**演習1.3: エキスパンダー (st.expander)**")
st.write("説明文の下にエキスパンダーを設け、さらに詳細な情報を隠して表示できるようにしましょう。")

# ここに演習1.3のコードを記述してください
# ヒント: with st.expander("ここをクリック") といった形でブロックを作成します。中に st.write() や st.image() などを配置してみましょう。
# st.subheader("詳細情報")
# with st.expander("ここをクリックして詳細を表示"):
#     st.write("ここに普段は隠しておきたい詳細な情報を記述します。")
#     # st.image("画像URL")

st.markdown("---
")
st.info("レイアウト演習のテンプレートファイルです。コメントに従ってコードを記述してください。") 