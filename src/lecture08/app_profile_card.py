import streamlit as st

st.set_page_config(layout="wide") # ページレイアウトをワイドに設定

st.title("課題演習: かんたん自己紹介カード作成ツール")
st.subheader("Streamlitの機能を使って、オリジナルの自己紹介カードを作ってみましょう！")

st.info("""
**目標:**
- `st.form` を使って情報を入力する。
- `st.file_uploader` でアイコン画像をアップロードする。
- `st.image` でアップロードした画像を表示する。
- `st.columns` やその他のレイアウト機能を活用して、見やすいカードデザインにする。
- `st.video` や `st.color_picker` など、学んだ他の機能も自由に追加してみよう！
""")

st.markdown("---")

# --- ここから演習スタート！ --- #

# 1. フォームを作成します (st.form)
# `with st.form(key="profile_form")` のように書きます。
# この中に、自己紹介情報を入力するためのウィジェットを配置しましょう。

# 例: st.text_input, st.selectbox, st.text_area, st.file_uploader

# --- フォームのウィジェット配置場所 --- #
# name = st.text_input("名前 (Name)", placeholder="大妻 花子")
# nickname = st.text_input("ニックネーム (Nickname)", placeholder="はなちゃん")
# department_options = ["社会情報学科 社会生活情報学専攻", "その他"] # 必要に応じて選択肢を編集
# department = st.selectbox("所属 (Department/Major)", department_options)
# grade = st.slider("学年 (Grade)", 1, 4, 3)
# free_text = st.text_area("ひとこと・趣味など (About me / Hobbies)", placeholder="趣味は読書と旅行です。よろしくお願いします！")

# icon_image = st.file_uploader("アイコン画像を選択 (Upload Icon Image)", type=['png', 'jpg', 'jpeg'], help="PNG, JPG, JPEG形式の画像をアップロードできます")

# video_url = st.text_input("好きなYouTube動画のURL (任意)", placeholder="例: https://www.youtube.com/watch?v=XXXX")
# card_color = st.color_picker("カードの背景色 (Card Background Color)", "#FFC0CB") # デフォルトはピンク

# フォームの送信ボタン (st.form_submit_button)
# submitted = st.form_submit_button("自己紹介カードを作成する！ (Generate Profile Card)")


st.markdown("---")
# 2. カード表示エリア
st.header("完成した自己紹介カードプレビュー")

# フォームが送信されたら (if submitted: のブロック内)、入力内容を使ってカードを表示します。
# ここで st.columns や st.image などを使ってレイアウトを工夫しましょう。

# --- カード表示ロジック --- #
# if submitted:
#     if not name:
#         st.error("名前は必須項目です。入力してください。")
#     else:
#         st.success("自己紹介カードが作成されました！")
        
#         # カードのスタイルを動的に生成 (背景色など)
#         # card_style = f"""
#         # border: 2px solid {card_color};
#         # border-radius: 10px;
#         # padding: 20px;
#         # margin: 10px;
#         # background-color: {card_color}20; /* 透明度を追加 */
#         # """
        
#         # st.markdown(f'<div style="{card_style}">' , unsafe_allow_html=True)

#         # 2列レイアウト (アイコン画像とテキスト情報)
#         # col1, col2 = st.columns([1, 2]) # アイコンの列を少し狭く

#         # with col1:
#         #     if icon_image is not None:
#         #         st.image(icon_image, caption="アイコン", width=150)
#         #     else:
#         #         st.markdown("_(アイコンなし)_ ")

#         # with col2:
#         #     st.subheader(f"{name} ({nickname})" if nickname else name)
#         #     st.write(f"**所属:** {department} - {grade}年生")
#         #     st.write(f"**ひとこと:** {free_text}")
            
#         #     if video_url:
#         #         st.write("**好きな動画:**")
#         #         # st.video(video_url) # 直接URLで動作しない場合があるので注意。テスト用のmp4等推奨。
#         #         st.link_button("動画を見る", video_url)

#         # st.markdown('</div>', unsafe_allow_html=True)
# else:
#     st.info("上記フォームに情報を入力して「自己紹介カードを作成する！」ボタンを押してください。")


st.markdown("---")
st.caption("演習はここまでです。不明な点は質問してください。GitHubへのアップロードも挑戦しましょう！") 