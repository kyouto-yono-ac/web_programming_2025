import streamlit as st

st.title("Streamlit入力ウィジェット演習")

st.write('''
このアプリでは、Streamlitの様々な入力ウィジェットを使って、簡単なアンケートフォームを作成します。
以下のフォームに必要事項を入力してください。
''')

# フォームの作成
with st.form("survey_form"):
    # テキスト入力
    name = st.text_input("お名前")
    email = st.text_input("メールアドレス")
    
    # 数値入力
    age = st.slider("年齢", 0, 100, 20)
    height = st.number_input("身長 (cm)", 100.0, 200.0, 160.0, 0.1)
    
    # 選択
    gender = st.selectbox(
        "性別",
        ["男性", "女性", "その他", "回答しない"]
    )
    
    # 複数選択
    hobbies = st.multiselect(
        "趣味（複数選択可）",
        ["読書", "スポーツ", "音楽", "旅行", "料理", "ゲーム", "その他"]
    )
    
    # その他の趣味の入力（条件付き表示）
    if "その他" in hobbies:
        other_hobby = st.text_input("その他の趣味を入力してください")
    else:
        other_hobby = ""
    
    # 送信ボタン
    submitted = st.form_submit_button("送信")
    
    # フォーム送信時の処理
    if submitted:
        if not name:
            st.error("名前を入力してください")
        elif not email:
            st.error("メールアドレスを入力してください")
        else:
            st.success("フォームが送信されました！")
            
            # 入力内容の表示
            st.write("### 入力内容")
            st.write(f"**名前:** {name}")
            st.write(f"**メールアドレス:** {email}")
            st.write(f"**年齢:** {age}歳")
            st.write(f"**身長:** {height}cm")
            st.write(f"**性別:** {gender}")
            
            st.write("**趣味:**")
            for hobby in hobbies:
                if hobby == "その他" and other_hobby:
                    st.write(f"- {other_hobby}")
                else:
                    st.write(f"- {hobby}")
            
            # 身長と年齢に基づくメッセージ
            if height > 170 and age < 30:
                st.info("背が高くて若いですね！")
            elif height < 160 and age > 50:
                st.info("経験豊富な方ですね！")
            
            # 趣味の数に基づくメッセージ
            hobby_count = len(hobbies)
            if hobby_count == 0:
                st.warning("趣味を1つは見つけてみましょう！")
            elif hobby_count >= 3:
                st.success("多趣味で素晴らしいですね！") 