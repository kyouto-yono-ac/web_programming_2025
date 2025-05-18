import streamlit as st

# アプリのタイトル
st.title("おすすめカフェ/ランチ スタイル診断")

st.write("いくつかの質問に答えて、あなたにピッタリのカフェやランチのスタイルを見つけましょう！")

# ---ここからコードを書いてみましょう---

# TODO: ユーザーからの入力を受け付けるウィジェットを配置する
# 例1: 気分 (st.radio)
# mood_options = ["がっつり食べたい", "ヘルシー志向", "おしゃれな空間で過ごしたい", "静かに集中したい"]
# selected_mood = st.radio("今の気分は？", mood_options)

# 例2: 予算 (st.slider または st.selectbox)
# budget = st.slider("ランチの予算は？ (円)", min_value=500, max_value=3000, step=100, value=1000)
# budget_options = ["〜1000円", "1000円〜1500円", "1500円〜2000円", "2000円〜"]
# selected_budget_range = st.selectbox("予算帯は？", budget_options)

# 例3: ジャンル (st.multiselect または st.selectbox)
# genre_options = ["和食", "洋食", "中華", "イタリアン", "カフェごはん", "エスニック"]
# selected_genres = st.multiselect("気になるジャンルは？ (複数選択可)", genre_options)

# TODO: 診断実行のボタンを配置する
# if st.button("おすすめスタイルを診断する！"):
    # TODO: 入力値に基づいておすすめのスタイル名と関連画像、簡単な説明を決定するロジック
    # ヒント: 複数の入力の組み合わせから、おすすめのスタイル名（例：「隠れ家風カフェでのんびり読書ランチ」）と、
    #       それっぽい画像ファイル名、説明文を決定するルールを if/elif/else 文で作ります。
    #       あまり複雑にしすぎず、3つ程度の質問に絞ると管理しやすいです。

    # recommendation_title = "診断結果のタイトル"
    # recommendation_description = "ここに診断結果の説明文が入ります。"
    # recommendation_image_path = "images/cafe_reco/default.png" # ダミーの画像パス

    # # --- 診断ロジックの例 (selected_mood と selected_budget_range を使う場合) ---
    # if selected_mood == "がっつり食べたい":
    #     if selected_budget_range == "〜1000円":
    #         recommendation_title = "コスパ最強！満腹ランチスタイル"
    #         recommendation_description = "お手頃価格でお腹いっぱいになれる、ボリューム満点のランチがおすすめです。定食屋や大盛り無料のお店を探してみては？"
    #         recommendation_image_path = "images/cafe_reco/gutsuri_cheap.png"
    #     elif selected_budget_range == "1000円〜1500円":
    #         recommendation_title = "大満足！がっつり贅沢ランチ"
    #         recommendation_description = "ちょっと奮発して、お肉料理や話題の丼ものなど、食べ応えのあるランチを楽しみましょう。"
    #         recommendation_image_path = "images/cafe_reco/gutsuri_mid.png"
    #     else:
    #         recommendation_title = "超豪華！自分にご褒美がっつり飯"
    #         recommendation_description = "特別な日や自分へのご褒美に、高級焼肉やステーキなど、普段は食べられないような豪華ながっつり飯はいかがですか。"
    #         recommendation_image_path = "images/cafe_reco/gutsuri_expensive.png"
    # elif selected_mood == "ヘルシー志向":
    #     # ... 他の気分の分岐も同様に作成 ...
    #     recommendation_title = "からだ想いのヘルシーランチスタイル"
    #     recommendation_description = "野菜たっぷりのサラダランチや、バランスの取れた定食がおすすめです。"
    #     recommendation_image_path = "images/cafe_reco/healthy.png"
    # # --- 他の条件分岐も追加してください ---
    # else:
    #     recommendation_title = "あなたにぴったりのスタイルを探求中..."
    #     recommendation_description = "いくつかの質問に答えて、あなたに最適なカフェやランチのスタイルを見つけましょう。"
    #     recommendation_image_path = "images/cafe_reco/default.png"


    # TODO: 診断結果（スタイル名、説明、関連画像）を表示する
    # st.subheader(recommendation_title)
    # st.write(recommendation_description)
    # try:
    #     st.image(recommendation_image_path, caption=recommendation_title)
    # except FileNotFoundError:
    #     st.warning(f"画像ファイル {recommendation_image_path} が見つかりません。ダミー画像を表示します。")
    #     st.image("https://via.placeholder.com/300x200/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
    # except Exception as e:
    #     st.error(f"画像表示中にエラーが発生しました: {e}")

# ---ここまで---

st.sidebar.header("ヒント")
st.sidebar.info(
    """
- 気分（例：がっつり、ヘルシー）、予算、ジャンルなどの質問に答えると、おすすめのカフェやランチの「スタイル」と関連画像を表示します。
- `st.radio` や `st.slider`, `st.selectbox` などでユーザーに質問します。
- `st.button` を押したら、入力の組み合わせに基づいて `if`/`elif` 文で条件分岐させ、おすすめのスタイル名、説明文、画像パスを決定します。
- 質問項目は3つ程度に絞ると、分岐の管理がしやすくなります。
- `st.image` で結果の画像を表示します。
- 画像は `src/lecture08/images/cafe_reco/` フォルダに配置することを想定しています (例: `gutsuri.png`, `healthy_cafe.png` など)。
"""
)

# 画像を配置するフォルダの例 (実際に`src/lecture08/images/cafe_reco`フォルダを作成し、画像を格納してください)
# (このテンプレートでは画像ファイル自体は含みません) 