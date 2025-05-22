import streamlit as st

st.title("第7回 Streamlit フォーム演習 - 解答")
st.caption("st.form を使ってアンケートフォームを作成しましょう。")

st.markdown("---")

# 演習3.1: アンケートフォームの作成
st.write("アンケートフォームを作成し、送信ボタンでまとめて入力を処理します。")

# st.form ブロックを開始し、keyを指定します
with st.form(key="survey_sample_form_ans"):
    st.subheader("簡単なアンケート")
    # 各入力ウィジェット (text_input, selectbox, text_area) をフォーム内に配置します
    # keyはフォーム内でも一意である必要があります
    s_name = st.text_input("お名前:", value="山田 太郎", key="form_ans_name")
    s_email = st.text_input("メールアドレス:", value="yamada.taro@example.com", key="form_ans_email")
    s_fav_food_options = ["", "寿司", "ラーメン", "カレー", "焼肉", "イタリアン", "その他"]
    s_fav_food = st.selectbox("好きな食べ物は？", options=s_fav_food_options, index=2, key="form_ans_fav_food") # indexで初期選択肢を設定
    s_feedback = st.text_area("ご意見・ご感想 (任意):", value="Streamlitは楽しく学べます！", key="form_ans_feedback")
    
    # フォーム送信ボタンを作成します
    s_submitted_button = st.form_submit_button("アンケートを送信する", key="form_ans_submit")

    # 送信ボタンが押されたかを確認します
    if s_submitted_button:
        # 入力内容をチェックし、必須項目が入力されているか確認します
        all_filled = True
        if not s_name: 
            st.warning("お名前を入力してください。")
            all_filled = False
        if not s_email: 
            st.warning("メールアドレスを入力してください。")
            all_filled = False
        # 好きな食べ物は未選択の場合空文字列になるのでチェック
        if not s_fav_food: 
             st.warning("好きな食べ物を選択してください。")
             all_filled = False
        
        # 全て入力されていれば成功メッセージと入力内容を表示します
        if all_filled:
            st.success("アンケートへのご協力、ありがとうございました！")
            st.markdown("**送信内容:**")
            st.write(f"- お名前: {s_name}")
            st.write(f"- メールアドレス: {s_email}")
            st.write(f"- 好きな食べ物: {s_fav_food}")
            if s_feedback:
                st.write(f"- ご意見: {s_feedback}")
            else:
                st.write("- ご意見: (未記入)")
            st.balloons() # お祝いのアニメーション
        else:
            st.error("未入力の項目があります。ご確認ください。")

st.markdown("---")
st.success("フォーム演習の解答例です。") 