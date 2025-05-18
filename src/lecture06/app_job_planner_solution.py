import streamlit as st

st.title("理想のバイトプランナー")
st.write("あなたの希望するアルバイトの条件を入力して、理想のバイトを見つけるためのプランを立てましょう！")

# --- 入力セクション ---
st.header("あなたの希望条件")

# 1. 希望職種（キーワード）
job_keywords = st.text_input("希望職種（キーワード、例: カフェ, 事務, プログラミング）:", placeholder="例: カフェ")

# 2. 希望時給
desired_wage = st.number_input("希望時給 (円):", min_value=800, value=1000, step=50)

# 3. 週の希望勤務時間
desired_hours_weekly = st.slider("週の希望勤務時間 (時間):", min_value=0, max_value=40, value=15, step=1)

# 4. 希望勤務曜日
days_options = ["月", "火", "水", "木", "金", "土", "日"]
preferred_days = st.multiselect("希望勤務曜日 (複数選択可):", days_options)

# 5. 重視する点
priority_options = ["給与の高さ", "仕事の楽しさ・やりがい", "スキルアップ・成長できる", "通いやすさ（場所・時間）", "シフトの柔軟性", "職場の雰囲気の良さ", "将来へのつながり"]
priority_point = st.selectbox("バイト選びで最も重視する点は何ですか？:", priority_options)

# --- プランニングロジックセクション ---
if st.button("プランニング開始"):
    st.header("あなたへのバイトプランニング")

    all_fields_filled = True
    if not job_keywords:
        st.warning("希望職種を入力してください。")
        all_fields_filled = False
    if not preferred_days:
        st.warning("希望勤務曜日を1つ以上選択してください。")
        all_fields_filled = False
    if not priority_point:
        st.warning("重視する点を選択してください。") # Selectboxはデフォルトで値が入るが念のため
        all_fields_filled = False

    if all_fields_filled:
        st.subheader("あなたの希望まとめ:")
        st.write(f"- **希望職種（キーワード）:** {job_keywords}")
        st.write(f"- **希望時給:** {desired_wage}円以上")
        st.write(f"- **週の希望勤務時間:** {desired_hours_weekly}時間程度")
        st.write(f"- **希望勤務曜日:** {', '.join(preferred_days)}")
        st.write(f"- **最も重視する点:** {priority_point}")

        st.subheader("📝 アドバイスとおすすめアクション")
        advice = []
        
        # 希望時給に基づくアドバイス
        if desired_wage >= 1500:
            advice.append(f"時給{desired_wage}円は魅力的ですね！このレベルの時給を目指す場合、プログラミング、家庭教師、専門知識を活かした翻訳・通訳、高時給のイベントスタッフなどが考えられます。ご自身のスキルや経験を棚卸しして、合致する求人を探してみましょう。求人サイトで「高時給」フィルターをかけるのも有効です。")
        elif desired_wage >= 1200:
            advice.append(f"時給{desired_wage}円は比較的高水準です。塾講師、コールセンター、スキルが求められるオフィスワーク、一部の飲食店などで見つかる可能性があります。未経験でも研修制度が充実しているところを選ぶと良いでしょう。")
        else:
            advice.append(f"時給{desired_wage}円からスタートする場合、未経験者歓迎の求人が多く見つかります。まずは経験を積むことを重視するのも良いでしょう。")

        # 勤務時間や曜日に基づくアドバイス
        if desired_hours_weekly == 0 and preferred_days:
             advice.append("勤務時間は0時間ですが、希望曜日が選択されていますね。短期・単発のバイトや、自分のペースで働ける業務委託（クラウドソーシングなど）を検討してみてはいかがでしょうか？")
        elif desired_hours_weekly <= 10 and desired_hours_weekly > 0:
            advice.append(f"週{desired_hours_weekly}時間程度の勤務なら、学業との両立もしやすいですね。大学の授業スケジュールに合わせてシフトを組める短期・単発バイトや、週1-2日からOKの求人を探してみましょう。")
        elif len(preferred_days) <= 2 and desired_hours_weekly > 0:
            advice.append(f"希望勤務曜日が{len(preferred_days)}日と限られているのですね。週末のみOKのイベントスタッフや、特定の曜日に集中して働けるシフト制のバイトを探すと見つかりやすいかもしれません。")
        
        # 重視する点に基づくアドバイス
        if priority_point == "スキルアップ・成長できる":
            advice.append("スキルアップを重視するなら、インターンシップへの参加がおすすめです。また、IT系（プログラミング学習支援など）、教育系（塾講師、採点業務）、専門スキルが身につくオフィスワーク（英語使用、デザインアシスタントなど）も良いでしょう。求人情報で「未経験者歓迎」かつ「研修制度あり」の記載があるか確認しましょう。")
        elif priority_point == "仕事の楽しさ・やりがい":
            advice.append(f"楽しさややりがいを重視するなら、あなたの趣味や興味関心に近い職種が良いでしょう。例えば、音楽が好きならライブスタッフやCDショップ、動物が好きならペットショップや動物病院の補助など、{job_keywords}に関連するキーワードで具体的に探してみましょう。")
        elif priority_point == "将来へのつながり":
            advice.append(f"将来のキャリアに繋げたいなら、希望する業界や職種でのインターンシップやアルバイト経験が重要です。{job_keywords}に関連する企業で、アシスタント業務や雑務からでも良いので、まずは業界に飛び込んでみることをお勧めします。OB/OG訪問などで情報収集するのも有効です。")
        elif priority_point == "給与の高さ" and desired_wage < 1200:
            advice.append(f"給与の高さを重視しつつ、希望時給が{desired_wage}円の場合、まずは経験を積んで昇給を目指せるバイトや、インセンティブ制度のあるバイトも検討してみましょう。")
        elif priority_point == "シフトの柔軟性":
            advice.append("シフトの柔軟性を重視するなら、登録制の派遣バイト（イベントスタッフ、試験監督など）や、週ごとのシフト提出が可能な飲食店・小売店、在宅でできるデータ入力などが考えられます。求人票の「シフト自己申告制」「週1日～OK」などの記載をチェックしましょう。")

        if not advice:
            st.info("素晴らしい！あなたの希望に合うバイトが見つかるよう、求人サイトで早速検索を開始しましょう！「Indeed」や「マイナビバイト」などが有名です。大学のキャリアセンターにも相談してみるのも良いでしょう。")
        else:
            for i, item in enumerate(advice):
                st.markdown(f"<div style='padding: 10px; border-left: 5px solid #4CAF50; margin-bottom: 10px; background-color: #f9f9f9;'>{i+1}. {item}</div>", unsafe_allow_html=True)
        
        # 架空のおすすめバイト情報
        st.subheader("💡 こんなバイトはどうでしょう？（架空の提案）")
        if "カフェ" in job_keywords or "飲食" in job_keywords:
           st.markdown("- **「陽だまりカフェ」:** 時給1050円～、週2日・1日3時間～OK、シフト柔軟、美味しいまかない付き！お洒落な空間で楽しく働けます。接客スキルも身につきます。")
        if "事務" in job_keywords or "データ入力" in job_keywords:
            st.markdown("- **「株式会社オフィスサポート」:** 時給1100円～、週3日～、PC基本操作できればOK。丁寧な研修があるので未経験でも安心。コツコツ作業が得意な方におすすめ。")
        if "プログラミング" in job_keywords or "IT" in job_keywords:
            st.markdown("- **「スタートアップTech」:** 時給1300円～（スキルにより応相談）、週2日～、リモートワークも一部可。実践的な開発経験を積みたい学生エンジニア募集！")
        if not ("カフェ" in job_keywords or "飲食" in job_keywords or "事務" in job_keywords or "データ入力" in job_keywords or "プログラミング" in job_keywords or "IT" in job_keywords):
            st.write("具体的な職種キーワードに合わせて、さらに絞り込んだ提案が可能です。")

    else:
        st.error("すべての必須項目を入力・選択してください。")

st.write("---")
st.caption("これは演習用のサンプルアプリ（解答例）です。提供される情報は架空のものです。") 