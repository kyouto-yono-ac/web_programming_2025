import streamlit as st
import random

st.title("第8回 演習: おみくじアプリ - 解答例")
st.caption("ボタンを押してランダムに運勢・メッセージ・画像を表示しましょう。")

st.markdown("---")
st.subheader("演習: おみくじアプリ")
st.write("**課題**: ボタンを押すとランダムに運勢・メッセージ・画像を表示するアプリを作成する。")

# おみくじデータの定義
omikuji_data = [
    {
        "fortune": "大吉",
        "message": "素晴らしい一日になりそう！新しいことに挑戦してみて。",
        "image": "images/omikuji/daikichi.png",
        "color": "#FFD700"
    },
    {
        "fortune": "中吉", 
        "message": "良いことが待っています。周りの人を大切にしましょう。",
        "image": "images/omikuji/chukichi.png", 
        "color": "#FFA500"
    },
    {
        "fortune": "小吉",
        "message": "小さな幸せを見つけられる日。感謝の気持ちを忘れずに。",
        "image": "images/omikuji/shokichi.png",
        "color": "#98FB98"
    },
    {
        "fortune": "吉",
        "message": "穏やかに過ごすのが吉。無理せずマイペースで。",
        "image": "images/omikuji/kichi.png",
        "color": "#87CEEB"
    },
    {
        "fortune": "末吉",
        "message": "後半に良いことがありそう。諦めずに頑張って！",
        "image": "images/omikuji/suekichi.png",
        "color": "#DDA0DD"
    },
    {
        "fortune": "凶",
        "message": "今日は慎重に。でも明日はきっと良い日になります。",
        "image": "images/omikuji/kyo.png",
        "color": "#F0F0F0"
    }
]

# おみくじを引くボタン
st.subheader("🏮 おみくじを引いてみましょう")

if st.button("🎯 おみくじを引く", use_container_width=True):
    # ランダムに結果を選択
    result = random.choice(omikuji_data)
    
    # 結果表示
    st.markdown(f"""
    <div style="
        text-align: center;
        padding: 30px;
        border-radius: 15px;
        background-color: {result['color']};
        border: 3px solid #333;
        margin: 20px 0;
    ">
        <h1 style="
            font-size: 48px;
            margin: 0;
            color: #333;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        ">
            {result['fortune']}
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # メッセージ表示
    st.info(f"📖 **今日のメッセージ**: {result['message']}")
    
    # 画像表示
    try:
        st.image(result['image'], caption=f"{result['fortune']}のイメージ", width=300)
    except FileNotFoundError:
        st.warning(f"画像ファイル ({result['image']}) が見つかりません。")
        # 運勢に応じたemoji表示
        emoji_map = {"大吉": "🌟", "中吉": "🌈", "小吉": "🍀", "吉": "😊", "末吉": "🌸", "凶": "🌧️"}
        st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji_map.get(result['fortune'], '🎋')}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"画像表示中にエラーが発生しました: {e}")
    
    # おまけ情報
    if result['fortune'] == "大吉":
        st.balloons()
        st.success("🎉 大吉おめでとうございます！今日は特別な日になりそうです！")
    elif result['fortune'] == "凶":
        st.warning("💪 凶が出ても大丈夫！きっと良いことが待っています。前向きに過ごしましょう！")

else:
    st.write("上のボタンを押して、今日の運勢を占ってみてください！")

st.markdown("---")
st.success("✅ おみくじアプリの解答例です。random.choice()でランダム選択し、結果に応じて表示を変えています。")

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「おみくじアプリ」の解答例です。
    - ボタンを押すと、ランダムに運勢、メッセージ、関連画像を表示します。
    - `random.choice()` を使って、事前に定義した運勢結果のリストからランダムに一つを選びます。
    - 結果は辞書のリストとして定義されています。
    - `st.image` で画像を表示し、結果に応じて `st.balloons()` や `st.snow()` のアニメーションを実行します。
    - メッセージは運勢の良し悪しに応じて `st.success`, `st.info`, `st.error` で色分けしています。
    - `st.session_state` を使って、最後に引いたおみくじの結果を保持し、ボタンクリック時のみ更新・表示するようにしています。
    """
)
st.sidebar.markdown("--- ")
st.sidebar.caption(
    "画像ファイル (例: `daikichi.png`) は、`src/lecture08/images/omikuji/` "
    "フォルダ内に配置することを想定しています。"
    "これらの画像はご自身でご用意いただくか、教員から提供されたものを使用してください。"
) 