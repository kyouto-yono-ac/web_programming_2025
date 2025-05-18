import streamlit as st
import random

# アプリのタイトル
st.title("おみくじアプリ")

st.write("今日の運勢を占ってみましょう！ボタンを押してください。")

# ---ここからコードを書いてみましょう---

# TODO: おみくじの結果（運勢、メッセージ、画像パスなど）のリストや辞書を事前に定義する
# 例: fortune_results = [
#     {"name": "大吉", "message": "最高の1日！何をやってもうまくいく！", "image": "images/omikuji/daikichi.png"},
#     {"name": "中吉", "message": "なかなか良い日。小さな幸せを見つけよう。", "image": "images/omikuji/chukichi.png"},
#     {"name": "小吉", "message": "まあまあの日。油断は禁物だけど、前向きに！", "image": "images/omikuji/shokichi.png"},
#     {"name": "吉",   "message": "平穏な一日。日々の感謝を忘れずに。", "image": "images/omikuji/kichi.png"},
#     {"name": "末吉", "message": "努力が報われる兆し。諦めないで！", "image": "images/omikuji/suekichi.png"},
#     {"name": "凶",   "message": "ちょっと注意が必要な日。慎重に行動しよう。", "image": "images/omikuji/kyo.png"},
#     {"name": "大凶", "message": "今日は控えめに。明日に期待！", "image": "images/omikuji/daikyo.png"}
# ]

# TODO: おみくじを引くボタン (st.button) を配置する
# if st.button("おみくじを引く"):
    # TODO: ボタンが押されたら、上記で定義した結果リストからランダムに1つ選ぶ (random.choice)
    # selected_result = random.choice(fortune_results)

    # TODO: 選ばれた結果（運勢名、メッセージ、画像）を表示する
    # st.header(f"今日のあなたの運勢は...「{selected_result['name']}」です！")
    # st.balloons() # お祝いの風船！

    # # 画像表示
    # try:
    #     st.image(selected_result["image"], caption=selected_result["name"])
    # except FileNotFoundError:
    #     st.warning(f"画像ファイル {selected_result['image']} が見つかりません。")
    #     st.image("https://via.placeholder.com/300x300/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
    # except Exception as e:
    #     st.error(f"画像表示中にエラーが発生しました: {e}")
    
    # st.write(selected_result["message"])
    
    # (オプション) st.info, st.success, st.warning, st.error などでメッセージの見た目を変える
    # if selected_result["name"] in ["大吉", "中吉"]:
    #     st.success(selected_result["message"])
    # elif selected_result["name"] in ["凶", "大凶"]:
    #     st.error(selected_result["message"])
    # else:
    #     st.info(selected_result["message"])

# ---ここまで---

st.sidebar.header("ヒント")
st.sidebar.info(
    """
- ボタンを押すと、ランダムに今日の運勢（大吉、中吉、小吉など）、一言メッセージ、関連する画像を表示します。
- `random.choice()` を使って、事前に定義した運勢結果のリストからランダムに一つを選びます。
- 運勢結果は、運勢名、メッセージ、画像ファイルパスなどをひとまとめにした辞書とし、その辞書のリストを準備すると管理しやすいです。
- `st.button` でおみくじを引くトリガーを作ります。
- `st.image` で運勢に関連する画像を表示してみましょう。
- `st.balloons()` や `st.snow()` でお祝いや雰囲気を出すエフェクトも使えます。
- 画像は `src/lecture08/images/omikuji/` フォルダに配置することを想定しています (例: `daikichi.png`, `kyo.png` など)。
"""
)

# 画像を配置するフォルダの例 (実際に`src/lecture08/images/omikuji`フォルダを作成し、画像を格納してください)
# (このテンプレートでは画像ファイル自体は含みません) 