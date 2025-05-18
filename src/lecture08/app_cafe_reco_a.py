import streamlit as st

# アプリのタイトル
st.title("おすすめカフェ/ランチ スタイル診断")
st.write("いくつかの質問に答えて、あなたにピッタリのカフェやランチのスタイルを見つけましょう！")

# 質問項目
st.subheader("あなたの好みや気分を教えてください")

# 1. 今日の気分は？
mood_options = {
    "しっかり食べたい": "しっかり",
    "軽めに済ませたい": "軽め",
    "おしゃれな雰囲気を楽しみたい": "おしゃれ",
    "静かに過ごしたい": "静か"
}
selected_mood_display = st.radio(
    "Q1. 今日の気分は？",
    list(mood_options.keys())
)
selected_mood = mood_options[selected_mood_display]

# 2. 予算は？
budget_options = {
    "〜1000円": "リーズナブル", 
    "1000円〜1800円": "標準", 
    "1800円〜": "贅沢"
}
selected_budget_display = st.selectbox(
    "Q2. ランチの予算はどれくらい？",
    list(budget_options.keys())
)
selected_budget = budget_options[selected_budget_display]

# 3. 誰と行きますか？
companion_options = {
    "ひとりで": "ひとり",
    "友達や同僚と (2〜4人)": "少人数",
    "大人数で (5人以上)": "大人数"
}
selected_companion_display = st.radio(
    "Q3. 誰と行きますか？",
    list(companion_options.keys())
)
selected_companion = companion_options[selected_companion_display]


# 診断結果のデータ (ここに診断ロジックと結果を定義)
# キーは (気分, 予算, 同行者) のタプル
recommendations = {
    # しっかり x リーズナブル
    ("しっかり", "リーズナブル", "ひとり"): {"title": "定食屋でがっつり一人飯", "desc": "コスパ抜群の定食屋で、栄養満点のがっつりランチをどうぞ。午後の活力になります！", "img": "images/cafe_reco/teishoku_hitori.png"},
    ("しっかり", "リーズナブル", "少人数"): {"title": "仲間とわいわい大衆食堂", "desc": "友達や同僚と、安くて美味しい大衆食堂へ！豊富なメニューから好きなものを選んで楽しもう。", "img": "images/cafe_reco/taishu_shokudo.png"},
    ("しっかり", "リーズナブル", "大人数"): {"title": "食べ放題でみんな満足！", "desc": "大人数ならやっぱり食べ放題！お財布に優しく、みんなでお腹いっぱいになれます。", "img": "images/cafe_reco/tabehoudai_reasonable.png"},
    # しっかり x 標準
    ("しっかり", "標準", "ひとり"): {"title": "話題のラーメン店で一杯", "desc": "ちょっと贅沢に、行列のできるラーメン店や専門店の味を堪能。自分へのご褒美に。", "img": "images/cafe_reco/ramen_hitori.png"},
    ("しっかり", "標準", "少人数"): {"title": "人気の洋食屋さんでランチセット", "desc": "ハンバーグやオムライスなど、みんな大好きな洋食屋さんのランチセットで、会話も弾みます。", "img": "images/cafe_reco/yoshoku_friends.png"},
    ("しっかり", "標準", "大人数"): {"title": "多国籍料理ビュッフェ", "desc": "色々な国の料理が楽しめるビュッフェなら、大人数でもそれぞれの好みに合わせられます。", "img": "images/cafe_reco/buffet_standard.png"},
    # おしゃれ x 標準 (一例)
    ("おしゃれ", "標準", "ひとり"): {"title": "ブックカフェで読書ランチ", "desc": "おしゃれなブックカフェで、美味しいコーヒーと共に静かな読書時間を。軽食も楽しめます。", "img": "images/cafe_reco/book_cafe.png"},
    ("おしゃれ", "標準", "少人数"): {"title": "テラス席のあるカフェレストラン", "desc": "開放的なテラス席で、おしゃれなランチプレートを囲んで、友人との会話を楽しんで。", "img": "images/cafe_reco/terrace_cafe.png"},
    # ... 他の組み合わせも追加 (以下はデフォルト的なもの)
}

default_recommendation = {"title": "あなたにぴったりのスタイルを探索中...", "desc": "もう少し条件を変えて試してみてね！", "img": "images/cafe_reco/default.png"}

# 診断実行ボタン
if st.button("おすすめスタイルを診断する！"):
    st.header("診断結果")
    # 選択された条件に一致する結果を探す
    result_key = (selected_mood, selected_budget, selected_companion)
    recommendation = recommendations.get(result_key, default_recommendation)

    st.subheader(recommendation["title"])
    
    # 画像表示 (画像ファイルは src/lecture08/images/cafe_reco/ に配置想定)
    try:
        # プロジェクトルートから streamlit run src/lecture08/app_cafe_reco_a.py で実行する場合を考慮
        # (演習テンプレートと同じパス構造を想定)
        full_image_path = recommendation["img"]
        st.image(full_image_path, caption=recommendation["title"], use_column_width=True)
    except FileNotFoundError:
        st.warning(f"画像ファイル ({full_image_path}) が見つかりません。ダミー画像を表示します。")
        st.image("https://via.placeholder.com/400x250/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
    except Exception as e:
        st.error(f"画像表示中にエラーが発生しました: {e}")

    st.info(recommendation["desc"])
    
    if recommendation == default_recommendation and result_key not in recommendations:
        st.caption(f"(デバッグ情報: 検索キー {result_key} は定義されていませんでした)")

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