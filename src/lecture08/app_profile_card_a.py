import streamlit as st

st.set_page_config(layout="wide")

st.title("課題演習: かんたん自己紹介カード作成ツール - 解答例")
st.subheader("Streamlitの機能を使って、オリジナルの自己紹介カードを作ってみましょう！")

st.markdown("---")

# 1. フォームを作成します (st.form)
with st.form(key="profile_form_solution"):
    st.header("自己紹介情報を入力してください")
    name = st.text_input("名前 (Name)", placeholder="大妻 花子", value="大妻 トトロ")
    nickname = st.text_input("ニックネーム (Nickname)", placeholder="はなちゃん", value="トトちゃん")
    
    department_options = [
        "社会情報学科 社会生活情報学専攻", 
        "社会情報学科 環境情報学専攻", 
        "社会情報学科 情報デザイン専攻", 
        "その他"
    ]
    department = st.selectbox("所属 (Department/Major)", department_options, index=0)
    grade = st.slider("学年 (Grade)", 1, 4, 3)
    
    free_text = st.text_area(
        "ひとこと・趣味など (About me / Hobbies)", 
        placeholder="趣味は読書と旅行です。よろしくお願いします！", 
        value="となりのトトロが大好きです！どんぐり集めと森の探検が趣味。最近はStreamlitの勉強も頑張っています。どうぞよろしく！",
        height=150
    )

    icon_image = st.file_uploader(
        "アイコン画像を選択 (Upload Icon Image)", 
        type=['png', 'jpg', 'jpeg'], 
        help="PNG, JPG, JPEG形式の画像をアップロードできます (推奨サイズ: 200x200px程度)"
    )
    
    st.markdown("--- Optional Fields ---")
    video_url = st.text_input("好きなYouTube動画のURL (任意)", placeholder="例: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    card_color = st.color_picker("カードのテーマカラー (Card Theme Color)", "#A9DBCB") # Slightly desaturated green

    # フォームの送信ボタン
    submitted = st.form_submit_button("自己紹介カードを作成する！ (Generate Profile Card)")

st.markdown("---")
st.header("完成した自己紹介カードプレビュー")

if submitted:
    if not name:
        st.error("名前は必須項目です。入力してください。")
    else:
        st.success("自己紹介カードが作成されました！")
        
        # カードのスタイルを動的に生成
        # より洗練されたデザインにするために、HTML/CSSを少し活用
        card_html_style = f"""
        <div style="
            border: 3px solid {card_color};
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            background-color: {card_color}33; /* 20% opacity */
            box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
            overflow: hidden; /* clearfix for floated elements if any */
        ">
        """
        st.markdown(card_html_style, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2.5]) # アイコン列 : テキスト列

        with col1:
            if icon_image is not None:
                st.image(icon_image, caption="アイコン", use_column_width=True)
            else:
                # Placeholder icon if no image is uploaded (using a simple emoji or text)
                st.markdown("<div style='font-size: 80px; text-align: center; padding: 20px; background-color: #eee; border-radius: 10px;'>👤</div>", unsafe_allow_html=True)
                st.caption("_(アイコン未設定)_ ")
            
            # Display color picker selection for reference (optional)
            st.markdown(f"<div style='margin-top:10px; padding:5px; background-color:{card_color}; color:white; text-align:center; border-radius:5px;'>テーマカラー</div>", unsafe_allow_html=True)

        with col2:
            st.subheader(f"{name} ({nickname})" if nickname else name)
            st.markdown(f"**<span style='color:{card_color};'>所属:</span>** {department} - {grade}年生", unsafe_allow_html=True)
            st.markdown("--- --- ---") # Divider
            st.markdown(f"**<span style='color:{card_color};'>自己紹介・趣味:</span>**", unsafe_allow_html=True)
            st.markdown(f"<div style='padding:10px; background-color:white; border-radius:5px; min-height:80px;'>{free_text}</div>", unsafe_allow_html=True)
            
            if video_url:
                st.markdown("--- --- ---")
                st.markdown(f"**<span style='color:{card_color};'>お気に入りの動画:</span>**", unsafe_allow_html=True)
                # Check if it's a YouTube URL for potential embedding, otherwise link
                if "youtube.com/watch?v=" in video_url or "youtu.be/" in video_url:
                    st.video(video_url)
                else:
                    st.link_button("動画を見る (外部サイト)", video_url)
        
        st.markdown("</div>", unsafe_allow_html=True) # Close card_html_style div
        st.balloons()

else:
    st.info("上記フォームに情報を入力して「自己紹介カードを作成する！」ボタンを押してください。サンプルデータが入力済みです。")

st.markdown("---")
st.header("補足: `st.image` と `st.video` の簡単な使用例")

if st.checkbox("画像 (st.image) の例を表示"):
    st.subheader("st.image のデモ")
    st.image("https://static.streamlit.io/examples/owl.jpg", caption="フクロウ (URLから表示)", width=300)
    # ローカルファイルの例は、実行環境にファイルがないとエラーになるためコメントアウト
    # try:
    #     st.image("dummy_image.jpg", caption="ローカル画像 (dummy_image.jpg)")
    # except Exception as e:
    #     st.warning(f"ローカル画像表示エラー: {e} (dummy_image.jpg が必要です)")

if st.checkbox("動画 (st.video) の例を表示"):
    st.subheader("st.video のデモ")
    st.video("https://storage.googleapis.com/streamlit-official-media/videos/cat.mp4", format="video/mp4")
    st.caption("猫の動画 (MP4 URLから表示)")

st.markdown("---")
st.caption("解答例は以上です。これを参考に、さらに機能を拡張したり、デザインを工夫したりしてみてください！") 