import streamlit as st
# import random # おみくじで使用しないのでコメントアウト

st.title("第4回 Pythonループと条件分岐 演習 (Streamlit)")
st.write("以下の課題に挑戦してみましょう！")

# --- 課題1: 持ち物チェックリスト (forループ) ---
st.write("---")
st.header("課題1: 🎒 持ち物チェックリスト")
st.write("Pythonのリストと `for` ループを使って、持ち物リストをチェックボックスで表示しましょう。")

# 持ち物リスト
items = []

st.subheader("必須アイテム:")

# --- ここに for ループを使って items の各要素を st.checkbox で表示するコードを書いてください ---

# (ここにfor item in items: ... を書く)


# --- ここまで (課題1) ---

st.caption("ヒント: `for item in items:` でリスト要素を繰り返し、`st.checkbox(item)` で表示します。")

# --- 課題2: 今日のコーデ提案 (if文) ---
st.write("---")
st.header("課題2: 👚 今日のコーデ提案")
st.write("天気と気温を選んで、おすすめの服装を `if` 文で表示しましょう。")

# 天気を選択
weather = st.selectbox(
    "今日の天気は？",
    ("☀️ 晴れ", "☁️ 曇り", "☔ 雨")
)

# 気温を選択
temperature = st.slider(
    "予想最高気温は？ (°C)",
    min_value=-5, max_value=40, value=25
)

# ボタン
if st.button("コーデを提案する"):
    st.write(f"天気: {weather}, 気温: {temperature}°C")
    st.subheader("おすすめコーデ:")
    # --- ここに if/elif/else を使って天気と気温に応じたメッセージを表示するコードを書いてください ---

    # 例: if "晴れ" in weather and temperature >= 25: ...
    #     elif "雨" in weather: ...
    #     else: ...

    # ＜考え方のヒント (箇条書き)＞
    # - まず「天気」で大きく場合分け (if "晴れ" in weather: ... elif "曇り" in weather: ... else: ...)
    # - 次に、それぞれの天気の中で「気温」でさらに場合分け (if temperature >= 25: ... elif temperature >= 15: ... else: ...)
    # - どんなメッセージを表示するか？
    #   - 晴れ & 25度以上 → 「半袖でOK！涼しい格好で！👒」
    #   - 晴れ & 15度～24度 → 「長袖シャツがちょうどいいかも？😊」
    #   - 晴れ & 15度未満 → 「ニットやジャケットが必要かも🧥」
    #   - 曇り & 20度以上 → 「長袖Tシャツに羽織ものがあると安心🌥️」
    #   - 曇り & 20度未満 → 「セーターや軽めのコートが良いかも」
    #   - 雨 & 20度以上 → 「蒸し暑いかも？半袖に撥水の上着、傘必須！🌂」
    #   - 雨 & 20度未満 → 「肌寒い雨。しっかり防寒と傘、防水の靴も！👢」

    # (ここにif/elif/elseの条件分岐を書く)


    # --- ここまで (課題2) ---

st.caption("ヒント: `if \"晴れ\" in weather and temperature >= 25:` のように条件を組み合わせます。")

st.write("---")
st.info("解答例は `app_a.py` を見てください。") 