import streamlit as st
# import pandas as pd # 発展課題で使用する場合はコメントを解除してください

st.title("第7回 Streamlit ファイルアップロード演習 - テンプレート")
st.caption("st.file_uploader を使ってファイルをアップロードしましょう。")

st.markdown("---")

# 演習4.1: ファイルアップローダーの設置
st.write("画像ファイルまたはCSVファイルをアップロードし、その情報を表示します。")

# ここにファイルアップローダーを作成するコードを記述してください。
# st.file_uploader() を使います。
# - ラベルは「ここにファイルをアップロード (画像 or CSV)」などとしましょう。
# - type=[...] で許可するファイル形式 (png, jpg, jpeg, gif, csv) を指定してください。
# - accept_multiple_files=False に設定してください。
# - key を設定することを推奨します (例: key="file_uploader_template")
# uploaded_file_data_template = st.file_uploader(
#     "ここにファイルをアップロード (画像 or CSV)", 
#     type=["png", "jpg", "jpeg", "gif", "csv"],
#     accept_multiple_files=False,
#     key="file_uploader_template"
# )

# ファイルがアップロードされたかを確認し、アップロード後の処理を記述してください。
# if uploaded_file_data_template is not None:
#     st.success(f"ファイル「{uploaded_file_data_template.name}」がアップロードされました！")
#     st.write("**ファイル情報:**")
#     # アップロードされたファイルのファイル名、タイプ、サイズを表示しましょう。
#     # st.write(f"- ファイル名: {uploaded_file_data_template.name}")
#     # st.write(f"- ファイルタイプ: {uploaded_file_data_template.type}")
#     # st.write(f"- ファイルサイズ: {uploaded_file_data_template.size} バイト")

#     # 演習4.2: アップロードされたファイルの種類に応じて処理を分岐
#     # アップロードされたファイルのタイプ (uploaded_file_data_template.type) をチェックして、表示方法を切り替えましょう。
#     # 画像ファイル (例: type.startswith("image/")) の場合
#     # if uploaded_file_data_template.type.startswith("image/"):
#         # st.subheader("アップロードされた画像:")
#         # st.image() を使って画像を表示しましょう。キャプションや use_column_width=True も設定できます。
#         # st.image(uploaded_file_data_template, caption=f"{uploaded_file_data_template.name}", use_column_width=True)
#     # CSVファイル (type == "text/csv") の場合
#     # elif uploaded_file_data_template.type == "text/csv":
#         # st.subheader("アップロードされたCSV (先頭5行):")
#         # 発展課題: Pandasを使ってCSVを読み込み表示
#         # 上の import pandas as pd のコメントを解除してください。
#         # try-except ブロックを使ってエラー処理を行うことを推奨します。
#         # try:
#             # pd.read_csv() で uploaded_file_data_template を読み込み、データフレームを作成します。
#             # df = pd.read_csv(uploaded_file_data_template)
#             # st.dataframe(df.head()) # データフレームの先頭5行を表示します。
#         # except Exception as e:
#             # st.error(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
#             # st.info("エラーが発生した場合でも、ファイル情報自体は上に表示されています。CSVの内容が正しいかご確認ください。")
#     # その他のファイルタイプの場合
#     # else:
#         # st.warning("対応していないファイルタイプです。画像(png, jpg等)またはCSVファイルをアップロードしてください。")
# else:
#     # ファイルがアップロードされていない場合の表示
#     st.info("まだファイルはアップロードされていません。")

st.markdown("---")
st.info("ファイルアップロード演習のテンプレートファイルです。コメントに従ってコードを記述してください。") 