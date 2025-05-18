import streamlit as st

st.title("大学生活充実度チェッカー")

st.write("あなたの大学生活について教えてください。簡単なフィードバックをします。")

# --- 入力セクション ---
st.header("あなたの情報")

# 1. 学部
faculties = ["文学部", "経済学部", "理工学部", "社会情報学部", "国際学部", "その他"]
faculty = st.selectbox("あなたの学部を選択してください:", faculties)

# 2. 週の平均勉強時間
study_hours = st.slider("週の平均勉強時間 (時間):", min_value=0, max_value=50, value=10, step=1)

# 3. 所属しているサークル・部活動
activity_options = ["運動系サークル", "文化系サークル", "学生団体", "部活動", "インターンシップ", "特になし", "その他"]
activities = st.multiselect("所属しているサークル・部活動・その他活動 (複数選択可):", activity_options, default=["特になし"])

# 4. 友人関係の満足度
satisfaction_levels = ["大変満足", "満足", "普通", "少し不満", "不満"]
social_satisfaction = st.radio("現在の友人関係についての満足度:", satisfaction_levels, index=2)

# 5. 平均睡眠時間
sleep_hours = st.number_input("1日の平均睡眠時間 (時間):", min_value=0.0, max_value=12.0, value=7.0, step=0.5)

# --- 診断ロジックセクション ---
if st.button("診断する"):
    st.header("診断結果")
    
    feedback = []
    
    # 勉強時間に基づくフィードバック
    if study_hours < 10:
        feedback.append(f"週の平均勉強時間が{study_hours}時間ですね。もう少し時間を増やして、授業の予習復習や課題に取り組むと、より学びが深まるかもしれません。")
    elif study_hours > 30:
        feedback.append(f"週に{study_hours}時間も勉強していて素晴らしいです！ただ、息抜きも大切にしてくださいね。")
    else:
        feedback.append(f"週に{study_hours}時間の勉強、バランスが取れていますね。この調子で頑張りましょう！")

    # サークル活動に基づくフィードバック
    if "特になし" in activities and len(activities) == 1:
        feedback.append("サークルや部活動、学生団体などに参加すると、新しい友達ができたり、視野が広がったりするかもしれません。何か興味のある活動を探してみてはいかがでしょうか？")
    elif len(activities) > 2:
        feedback.append(f"{len(activities)}つも活動していてアクティブですね！時間管理をしっかりして、学業との両立も頑張ってください。")
    
    # 友人関係の満足度に基づくフィードバック
    if social_satisfaction == "大変満足" or social_satisfaction == "満足":
        feedback.append("友人関係に満足しているのは素晴らしいことです！これからも良い関係を築いていってください。")
    elif social_satisfaction == "普通":
        feedback.append("友人関係が「普通」と感じるのですね。新しいコミュニティに参加してみるなど、少し変化を加えてみるのも良いかもしれません。")
    elif social_satisfaction == "少し不満" or social_satisfaction == "不満":
        feedback.append("友人関係で悩みがあるのですね。一人で抱え込まず、信頼できる人（友人、家族、大学の相談窓口など）に話してみることを考えてみてください。")

    # 睡眠時間に基づくフィードバック
    if sleep_hours < 6.0:
        feedback.append(f"平均睡眠時間が{sleep_hours}時間ですか。健康のためにも、もう少し睡眠時間を確保することをおすすめします。最低でも6-7時間は目指しましょう。")
    elif sleep_hours > 9.0:
        feedback.append(f"平均睡眠時間が{sleep_hours}時間と十分取れているようですね。質の高い睡眠は日中のパフォーマンス向上に繋がります。")
    else:
        feedback.append("睡眠時間は適切ですね。規則正しい生活を心がけましょう。")

    # 総合的なフィードバック
    if not feedback: # Should not happen with current logic, but as a fallback
        st.success("あなたの大学生活は充実しているようです！この調子で楽しんでください。")
    else:
        st.subheader("あなたへのアドバイス:")
        for i, item in enumerate(feedback):
            st.markdown(f"{i+1}. {item}")
            
    if study_hours > 15 and ("特になし" not in activities or len(activities) > 1) and social_satisfaction in ["大変満足", "満足"] and sleep_hours >= 6.5 :
        st.balloons()
        st.success("全体的にバランスの取れた素晴らしい大学生活を送っていますね！")

st.write("---")
st.caption("これは演習用のサンプルアプリ（解答例）です。") 