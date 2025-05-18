import streamlit as st
import random

# アプリのタイトル
st.title("今日のラッキーカラー診断アプリ")

# 説明
st.write("あなたの今日のラッキーカラーを占います！")

# ---ここからコードを書いてみましょう---

# TODO: ユーザーからの入力を受け付けるウィジェットを配置する
# 例: st.selectboxで星座を選んでもらう、st.text_inputで好きな数字を入力してもらうなど
# input_value = st.selectbox("あなたの星座を選んでください", ["おひつじ座", "おうし座", ...]) # 残りの星座も追加してください
# lucky_number_str = st.text_input("好きな数字を1つ入力してください (例: 7)")

# TODO: 診断実行のボタンを配置する
# if st.button("ラッキーカラーを診断する！"):
    # TODO: 入力値に基づいてラッキーカラーとアドバイスを決定するロジック
    # ヒント: 星座や数字と結果（色、アドバイスメッセージ、表示する画像ファイル名など）の
    #       対応表をPythonの辞書で事前に作っておくと簡単です。
    # colors = {"おひつじ座": "赤", "おうし座": "緑", ...} # 他の星座と色も追加
    # advice = {"おひつじ座": "情熱的に過ごせる一日！", "おうし座": "落ち着いて物事に取り組もう", ...} # 他も追加
    # images = {"おひつじ座": "images/red_gem.png", ...} # ダミーの画像パス、適宜用意・変更

    # selected_color = "未選択"
    # selected_advice = "まだ占っていません"
    # selected_image_path = None

    # if input_value in colors: # selectboxの場合
    #     selected_color = colors[input_value]
    #     selected_advice = advice[input_value]
    #     # selected_image_path = images[input_value] # 画像パスも設定
    # else: # 何か他の入力やエラー処理
    #     st.error("有効な星座を選んでください。")


    # TODO: 診断結果（ラッキーカラー、アドバイス、関連画像）を表示する
    # st.subheader(f"今日のあなたのラッキーカラーは「{selected_color}」です！")
    # st.write(selected_advice)
    # if selected_image_path:
    #     try:
    #         st.image(selected_image_path, caption=f"{selected_color}に関連するイメージ")
    #     except FileNotFoundError:
    #         st.warning(f"画像ファイル {selected_image_path} が見つかりません。ダミー画像を表示します。")
    #         st.image("https://via.placeholder.com/150/FF0000/FFFFFF?Text=No+Image", caption="画像が見つかりません")
    #     except Exception as e:
    #         st.error(f"画像表示中にエラーが発生しました: {e}")
    # else:
    #     # 画像がない場合の代替表示やメッセージ
    #     st.info("この結果に関連する特別な画像はありません。")

    # CSS風に色を表示する例 (st.markdown を使う)
    # st.markdown(f"""
    # <div style="
    #     text-align: center;
    #     padding: 20px;
    #     border-radius: 10px;
    #     background-color: {selected_color.lower()};
    #     color: white;
    #     font-size: 24px;
    #     font-weight: bold;
    # ">
    #     {selected_color}
    # </div>
    # """, unsafe_allow_html=True)


# ---ここまで---

st.sidebar.header("ヒント")
st.sidebar.info(
    """
- 星座や好きな数字などを選ぶと、今日のラッキーカラー、アドバイス、関連画像を表示します。
- `st.selectbox` で選択肢を提示したり、`st.text_input` で自由入力を受け付けます。
- `st.button` を押したら、入力に基づいて結果を決定するロジックを作ります。
- Pythonの辞書を使って、入力と結果（色名、メッセージ、画像パスなど）を対応付けると便利です。
- `st.image` で結果に関連する画像を表示してみましょう。
- `st.markdown` を使うと、HTMLやCSSを少し使ってリッチな表示も可能です。
"""
)

# 画像を配置するフォルダの例 (実際に`src/lecture08/images`フォルダを作成し、画像を格納してください)
# 例: images/red_gem.png, images/blue_sky.png など
# (このテンプレートでは画像ファイル自体は含みません) 