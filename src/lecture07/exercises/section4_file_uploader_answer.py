import streamlit as st
import pandas as pd # 発展課題で使用

st.title("第7回 Streamlit ファイルアップロード演習 - 解答")
st.caption("st.file_uploader を使ってファイルをアップロードしましょう。")

st.markdown("---")

# 演習4.1: ファイルアップローダーの設置
st.write("画像ファイルまたはCSVファイルをアップロードし、その情報を表示します。")

# ファイルアップローダーウィジェットを作成します。
# typeで許可するファイル形式をリストで指定します。
# accept_multiple_files=Falseで単一ファイルのみを受け付けます。
# keyを設定します。
uploaded_file_data_ans = st.file_uploader(
    "ここにファイルをアップロード (画像 or CSV)", 
    type=["png", "jpg", "jpeg", "gif", "csv"],
    accept_multiple_files=False, 
    key="file_uploader_ans_main"
)

# ファイルがアップロードされたかを確認します。
if uploaded_file_data_ans is not None:
    st.success(f"ファイル「{uploaded_file_data_ans.name}」がアップロードされました！")
    st.write("**ファイル情報:**")
    st.write(f"- ファイル名: {uploaded_file_data_ans.name}")
    st.write(f"- ファイルタイプ: {uploaded_file_data_ans.type}")
    st.write(f"- ファイルサイズ: {uploaded_file_data_ans.size} バイト")

    # 演習4.2: アップロードされたファイルの種類に応じて処理を分岐
    # ファイルタイプ (uploaded_file_data_ans.type) を確認し、処理を分岐させます。
    # 画像ファイルの場合
    if uploaded_file_data_ans.type.startswith("image/"):
        st.subheader("アップロードされた画像:")
        st.image(uploaded_file_data_ans, caption=f"{uploaded_file_data_ans.name}", use_column_width=True)
    # CSVファイルの場合
    elif uploaded_file_data_ans.type == "text/csv":
        st.subheader("アップロードされたCSV (先頭5行):")
        # 発展課題: Pandasを使ってCSVを読み込み表示
        # try-exceptブロックでエラーハンドリングを行います。
        try:
            # pd.read_csv() でファイルを読み込み、st.dataframe() で表示します。
            df = pd.read_csv(uploaded_file_data_ans)
            st.dataframe(df.head()) # 先頭5行を表示
        except Exception as e:
            st.error(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
            st.info("エラーが発生した場合でも、ファイル情報自体は上記に表示されています。CSVの内容が正しいかご確認ください。")
    # その他のファイルタイプの場合
    else:
        st.warning("対応していないファイルタイプです。画像(png, jpg等)またはCSVファイルをアップロードしてください。")
else:
    st.info("まだファイルはアップロードされていません。")

st.markdown("---")
st.success("ファイルアップロード演習の解答例です。") 