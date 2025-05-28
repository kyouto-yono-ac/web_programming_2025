import streamlit as st

st.title("レイアウト機能 基本コード例")
st.caption("st.sidebar, st.columns, st.expander の基本的な使い方")

st.markdown("---")

# st.sidebar 例
st.markdown("**st.sidebar 例:**")
add_selectbox = st.sidebar.selectbox(
    "連絡方法を選択してください",
    ("メール", "携帯電話", "LINE")
)
st.sidebar.write(f"選択された連絡方法: {add_selectbox}")

st.markdown("---")

# st.columns 例
st.markdown("**st.columns 例:**")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

st.markdown("---")

# st.expander 例
st.markdown("**st.expander 例:**")
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("詳細を見る"):
     st.write('''
         このグラフは架空のデータを表示しています。
         詳細な分析やデータの背景については、提供元にお問い合わせください。
     ''')

st.markdown("---")
st.info("これはレイアウト機能の基本コード例です。") 