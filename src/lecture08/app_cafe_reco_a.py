import streamlit as st

st.title("第8回 演習: カフェ/ランチ診断アプリ - 解答例")
st.caption("気分・予算・同行者を選んで、おすすめのカフェスタイルを診断しましょう。")

st.markdown("---")
st.subheader("演習: カフェ/ランチ診断")
st.write("**課題**: 気分・予算・同行者を選ぶと、おすすめのカフェスタイルを診断するアプリを作成する。")

# ユーザー入力
mood_options = ["がっつり食べたい", "ヘルシー志向", "おしゃれな空間で過ごしたい", "静かに集中したい"]
selected_mood = st.radio("今の気分は？", mood_options)

budget = st.slider("ランチの予算は？ (円)", min_value=500, max_value=3000, step=100, value=1000)

companion_options = ["一人で", "友達と", "家族と", "デート"]
selected_companion = st.selectbox("誰と行きますか？", companion_options)

# 診断実行ボタン
if st.button("おすすめスタイルを診断する！"):
    # 診断ロジック
    if selected_mood == "がっつり食べたい":
        if budget < 1000:
            title = "コスパ最強！満腹ランチスタイル"
            description = "お手頃価格でお腹いっぱいになれる、ボリューム満点のランチがおすすめです。"
            image_path = "images/cafe_reco/gutsuri_cheap.png"
        elif budget < 1500:
            title = "大満足！がっつり贅沢ランチ"
            description = "ちょっと奮発して、お肉料理や話題の丼ものなど、食べ応えのあるランチを楽しみましょう。"
            image_path = "images/cafe_reco/gutsuri_mid.png"
        else:
            title = "超豪華！自分にご褒美がっつり飯"
            description = "特別な日や自分へのご褒美に、高級焼肉やステーキなど、普段は食べられないような豪華ながっつり飯はいかがですか。"
            image_path = "images/cafe_reco/gutsuri_expensive.png"
    elif selected_mood == "ヘルシー志向":
        title = "からだ想いのヘルシーランチスタイル"
        description = "野菜たっぷりのサラダランチや、バランスの取れた定食がおすすめです。"
        image_path = "images/cafe_reco/healthy.png"
    elif selected_mood == "おしゃれな空間で過ごしたい":
        title = "インスタ映え♪おしゃれカフェスタイル"
        description = "トレンドのカフェで、おしゃれな料理と空間を楽しみましょう。SNSでシェアしたくなる素敵な時間を。"
        image_path = "images/cafe_reco/stylish.png"
    else:  # 静かに集中したい
        title = "隠れ家風カフェでのんびり集中タイム"
        description = "落ち着いた雰囲気のカフェで、読書や作業に集中できる環境がおすすめです。"
        image_path = "images/cafe_reco/quiet.png"

    # 結果表示
    st.subheader(f"🎯 {title}")
    st.write(description)
    
    # 同行者に応じた追加コメント
    if selected_companion == "友達と":
        st.info("👥 友達とのランチなら、シェアできるメニューがあるお店もおすすめです！")
    elif selected_companion == "デート":
        st.info("💕 デートなら、雰囲気の良い個室やテラス席のあるお店を選んでみてはいかがでしょう。")
    elif selected_companion == "一人で":
        st.info("🧘‍♀️ 一人時間を大切に。カウンター席のあるお店もゆっくりできて良いですね。")

    # 画像表示
    try:
        st.image(image_path, caption=title, width=300)
    except FileNotFoundError:
        st.warning(f"画像ファイル ({image_path}) が見つかりません。ダミー画像を表示します。")
        st.image("https://via.placeholder.com/300x200/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
    except Exception as e:
        st.error(f"画像表示中にエラーが発生しました: {e}")

st.markdown("---")
st.success("✅ カフェ/ランチ診断アプリの解答例です。複数の入力を組み合わせて結果を分岐させています。")

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「おすすめカフェ/ランチ スタイル診断」の解答例です。
    - 3つの質問（気分、予算、同行者）に答えると、おすすめのスタイルと関連画像を表示します。
    - `st.radio` と `st.selectbox` で入力を受け付けます。
    - `st.button` で診断を実行します。
    - 診断ロジックはPythonの辞書に条件と結果をマッピングしています。
    - `st.image` で画像を表示します (画像ファイルは別途用意が必要です)。
    """
)
st.sidebar.markdown("--- ")
st.sidebar.caption(
    "画像ファイルは、`src/lecture08/images/cafe_reco/` フォルダ内に配置することを想定しています。"
    "(例: `teishoku_hitori.png`, `book_cafe.png` など)"
    "これらの画像はご自身でご用意いただくか、教員から提供されたものを使用してください。"
) 