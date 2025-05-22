import streamlit as st

st.title("第7回 Streamlit フォーム演習 - テンプレート")
st.caption("st.form を使ってアンケートフォームを作成しましょう。")

st.markdown("---")

# 演習3.1: アンケートフォームの作成
st.write("アンケートフォームを作成し、送信ボタンでまとめて入力を処理します。")

# st.form ブロックを作成してください。keyを設定することを忘れないでください。
# with st.form(key="survey_sample_form_template"):
#     st.subheader("簡単なアンケート")
#     
#     # ここにアンケート項目を作成するコードを記述してください。
#     # 以下のウィジェットを使ってみましょう:
#     # - お名前 (st.text_input)
#     # - メールアドレス (st.text_input)
#     # - 好きな食べ物 (st.selectbox) - 選択肢をリストで定義してください (例: ["寿司", "ラーメン", ...])
#     # - ご意見・ご感想 (st.text_area)
#     # 各ウィジェットにはkeyを設定してください。
#     # s_name = st.text_input("お名前:", key="form_template_name")
#     # s_email = st.text_input("メールアドレス:", key="form_template_email")
#     # s_fav_food_options = ["", "寿司", "ラーメン", "カレー", "焼肉", "イタリアン", "その他"]
#     # s_fav_food = st.selectbox("好きな食べ物は？", options=s_fav_food_options, key="form_template_fav_food")
#     # s_feedback = st.text_area("ご意見・ご感想 (任意):", key="form_template_feedback")
#     
#     # フォーム送信ボタンを作成してください。
#     # st.form_submit_button() を使います。keyを設定してください。
#     # s_submitted_button = st.form_submit_button("アンケートを送信する", key="form_template_submit")
# 
#     # 送信ボタンが押された後の処理をここに記述してください。
#     # if s_submitted_button:
#         # st.success("アンケートへのご協力、ありがとうございました！")
#         # 入力された内容を画面に表示してみましょう。
#         # st.write(f"- お名前: {s_name if s_name else '未入力'}")
#         # st.write(f"- メールアドレス: {s_email if s_email else '未入力'}")
#         # st.write(f"- 好きな食べ物: {s_fav_food if s_fav_food else '未選択'}")
#         # if s_feedback:
#         #     st.write(f"- ご意見: {s_feedback}")
#         # else:
#         #     st.write("- ご意見: (未記入)")
#         # 必要であれば、入力チェック（必須項目の確認）や st.balloons() なども追加してみましょう。

st.markdown("---
")
st.info("フォーム演習のテンプレートファイルです。コメントに従ってコードを記述してください。") 