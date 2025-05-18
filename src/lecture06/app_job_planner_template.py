import streamlit as st

st.title("理想のバイトプランナー")
st.write("あなたの希望するアルバイトの条件を入力して、理想のバイトを見つけるためのプランを立てましょう！")

# --- 入力セクション ---
st.header("あなたの希望条件")

# 1. 希望職種（キーワード） (st.text_input)
# TODO: 希望職種（キーワード）を入力するtext_inputを配置してください。
# 例: "カフェ", "塾講師", "データ入力"
job_keywords = "" # 仮の値

# 2. 希望時給 (st.number_input)
# TODO: 希望時給を入力するnumber_inputを配置してください。
# min_value=800, value=1000, step=50
desired_wage = 1000 # 仮の値

# 3. 週の希望勤務時間 (st.slider)
# TODO: 週の希望勤務時間を入力するsliderを配置してください。
# min_value=0, max_value=40, value=15, step=1
desired_hours_weekly = 15 # 仮の値

# 4. 希望勤務曜日 (st.multiselect)
# TODO: 希望勤務曜日を複数選択するmultiselectを配置してください。
# options: ["月", "火", "水", "木", "金", "土", "日"]
preferred_days = [] # 仮の値

# 5. 重視する点 (st.selectbox)
# TODO: バイト選びで重視する点を選択するselectboxを配置してください。
# options: ["給与", "楽しさ", "スキルアップ", "通いやすさ", "シフトの柔軟性", "職場の雰囲気"]
priority_point = None # 仮の値

# --- プランニングロジックセクション ---
if st.button("プランニング開始"):
    st.header("あなたへのバイトプランニング")

    if job_keywords and desired_wage and preferred_days and priority_point: # 簡単な入力チェック
        st.subheader("あなたの希望まとめ:")
        st.write(f"- **希望職種:** {job_keywords}")
        st.write(f"- **希望時給:** {desired_wage}円以上")
        st.write(f"- **週の勤務時間:** {desired_hours_weekly}時間程度")
        st.write(f"- **希望勤務曜日:** {', '.join(preferred_days)}")
        st.write(f"- **最も重視する点:** {priority_point}")

        st.subheader("アドバイスとおすすめアクション:")
        advice = []
        
        # TODO: 希望時給に基づくアドバイス
        # 例: if desired_wage >= 1500: advice.append("時給1500円以上を目指すなら、専門スキルや経験が求められることが多いです。...")
        
        # TODO: 勤務時間や曜日に基づくアドバイス
        # 例: if desired_hours_weekly <= 10: advice.append("週10時間以内なら、学業との両立もしやすい短期・単発のバイトも視野に入れてみては？")
        
        # TODO: 重視する点に基づくアドバイス
        # 例: if priority_point == "スキルアップ": advice.append("スキルアップ重視なら、インターンシップや専門知識が活かせるバイトを探しましょう。...")

        if not advice:
            st.info("具体的な条件に合わせて、求人サイトで検索してみましょう！")
        else:
            for item in advice:
                st.markdown(f"- {item}")
        
        # (架空のおすすめバイト情報を表示するのも面白いかもしれません)
        # st.subheader("こんなバイトはどうでしょう？（架空）")
        # if "カフェ" in job_keywords:
        #    st.write("- **おしゃれカフェA店:** 時給1050円、週2日からOK、シフト柔軟！")

    else:
        st.error("すべての項目を入力・選択してください。")

st.write("---")
st.caption("これは演習用のサンプルアプリです。") 