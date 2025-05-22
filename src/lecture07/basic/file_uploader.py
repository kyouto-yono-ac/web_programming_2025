import streamlit as st

st.title("ファイルアップロード機能 基本コード例")
st.caption("st.file_uploader の基本的な使い方")

st.markdown("---")

# st.file_uploader 例
st.markdown("**st.file_uploader 例:**")
uploaded_file_basic = st.file_uploader("ファイルを選択してください (PNG or JPG)", type=["png", "jpg"], key="file_uploader_basic_file") # Add key

if uploaded_file_basic is not None:
    # ファイル詳細の表示
    st.write("**ファイル情報:**")
    st.write("ファイル名:", uploaded_file_basic.name)
    st.write("ファイルタイプ:", uploaded_file_basic.type)
    st.write("ファイルサイズ:", uploaded_file_basic.size, "bytes")

    # 画像ファイルなら表示
    if uploaded_file_basic.type.startswith("image/"):
        st.image(uploaded_file_basic, caption='アップロードされた画像', use_column_width=True)

st.markdown("---")
st.info("これはファイルアップロード機能の基本コード例です。") 