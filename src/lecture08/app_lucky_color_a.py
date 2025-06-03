import streamlit as st

st.title("第8回 演習: ラッキーカラー診断アプリ - 解答例")
st.caption("星座や好きな数字を選んで、今日のラッキーカラーを診断しましょう。")

st.markdown("---")
st.subheader("演習: ラッキーカラー診断")
st.write("**課題**: 星座や好きな数字を選ぶと、今日のラッキーカラーとアドバイスを表示するアプリを作成する。")

# 星座のリスト
constellations = [
    "おひつじ座", "おうし座", "ふたご座", "かに座", 
    "しし座", "おとめ座", "てんびん座", "さそり座", 
    "いて座", "やぎ座", "みずがめ座", "うお座"
]

# ラッキーカラー、アドバイス、画像パスの辞書
results_data = {
    "おひつじ座": {"color": "レッド", "advice": "情熱的に行動すると良い日！", "image": "images/lucky_color/red.png"},
    "おうし座": {"color": "グリーン", "advice": "堅実さが幸運を呼ぶでしょう。", "image": "images/lucky_color/green.png"},
    "ふたご座": {"color": "イエロー", "advice": "コミュニケーションが鍵。明るく話しかけてみて。", "image": "images/lucky_color/yellow.png"},
    "かに座": {"color": "ホワイト", "advice": "優しさが周囲を癒します。", "image": "images/lucky_color/white.png"},
    "しし座": {"color": "ゴールド", "advice": "自信を持ってリーダーシップを発揮！", "image": "images/lucky_color/gold.png"},
    "おとめ座": {"color": "ネイビー", "advice": "計画通りに進めることで成果が出ます。", "image": "images/lucky_color/navy.png"},
    "てんびん座": {"color": "ピンク", "advice": "バランス感覚を大切に。", "image": "images/lucky_color/pink.png"},
    "さそり座": {"color": "パープル", "advice": "洞察力が冴える一日。", "image": "images/lucky_color/purple.png"},
    "いて座": {"color": "ブルー", "advice": "新しい挑戦が吉。", "image": "images/lucky_color/blue.png"},
    "やぎ座": {"color": "ブラウン", "advice": "努力が実を結ぶ時。", "image": "images/lucky_color/brown.png"},
    "みずがめ座": {"color": "アクア", "advice": "ひらめきを大切に。独創性を発揮して。", "image": "images/lucky_color/aqua.png"},
    "うお座": {"color": "シルバー", "advice": "直感を信じて行動しよう。", "image": "images/lucky_color/silver.png"},
}

# ユーザー入力
selected_constellation = st.selectbox("あなたの星座を選んでください", constellations)

# 診断実行ボタン
if st.button("今日のラッキーカラーを診断する！"):
    if selected_constellation in results_data:
        result = results_data[selected_constellation]
        lucky_color = result["color"]
        advice_message = result["advice"]
        image_path = result["image"]

        st.subheader(f"{selected_constellation}のあなたの今日のラッキーカラーは「{lucky_color}」です！")
        
        # 色を背景にした表示
        color_map = {
            "ホワイト": "#FFFFFF", "シルバー": "#C0C0C0", "ゴールド": "#FFD700", "アクア": "#00FFFF",
            "レッド": "red", "グリーン": "green", "イエロー": "yellow", "ピンク": "pink",
            "パープル": "purple", "ブルー": "blue", "ブラウン": "brown", "ネイビー": "navy"
        }
        
        bg_color = color_map.get(lucky_color, lucky_color.lower())
        text_color = "black" if lucky_color in ["イエロー", "ホワイト", "ピンク", "ゴールド", "アクア", "シルバー"] else "white"
        
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background-color: {bg_color}; 
            color: {text_color};
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        ">
            {lucky_color}
        </div>
        """, unsafe_allow_html=True)

        st.write("**ラッキーアドバイス:**")
        st.info(advice_message)

        # 画像表示
        try:
            st.image(image_path, caption=f"{lucky_color}のイメージ", width=250)
        except FileNotFoundError:
            st.warning(f"画像ファイル ({image_path}) が見つかりません。ダミー画像を表示します。")
            st.image("https://via.placeholder.com/250x250/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
        except Exception as e:
            st.error(f"画像表示中にエラーが発生しました: {e}")

st.markdown("---")
st.success("✅ ラッキーカラー診断アプリの解答例です。星座と結果の対応表を辞書で管理することで、簡潔に実装できます。")

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「今日のラッキーカラー診断アプリ」の解答例です。
    - 星座を選択すると、その日のラッキーカラー、アドバイス、関連画像を表示します。
    - `st.selectbox` で入力を受け付けます。
    - `st.button` で診断を実行します。
    - 結果はPythonの辞書にまとめて定義されています。
    - `st.markdown` とインラインCSSで色をスタイリッシュに表示しています。
    - `st.image` で画像を表示します (画像ファイルは別途用意が必要です)。
    """
)

# 画像についての注意書き
st.sidebar.markdown("--- ")
st.sidebar.caption(
    "画像ファイル (`red.png`, `blue.png` など) は、`src/lecture08/images/lucky_color/` "
    "というフォルダ内に配置することを想定しています。"
    "これらの画像はご自身でご用意いただくか、教員から提供されたものを使用してください。"
) 