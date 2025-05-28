import streamlit as st

st.title("第8回 演習: 自己紹介カード作成ツール - 解答例")
st.caption("フォームで情報を入力し、整形して自己紹介カードを表示しましょう。")

st.markdown("---")
st.subheader("演習: 自己紹介カード作成")
st.write("**課題**: フォームで情報を入力し、整形して自己紹介カードを表示するアプリを作成する。")

# フォームでユーザー情報を入力
with st.form("profile_form"):
    st.subheader("自己紹介情報を入力してください")
    
    # 基本情報
    name = st.text_input("名前", placeholder="大妻 花子")
    nickname = st.text_input("ニックネーム", placeholder="はなちゃん")
    
    # 所属情報
    department_options = [
        "社会情報学科 社会生活情報学専攻",
        "社会情報学科 環境情報学専攻", 
        "社会情報学科 情報デザイン専攻",
        "その他"
    ]
    department = st.selectbox("所属学科・専攻", department_options)
    grade = st.slider("学年", 1, 4, 2)
    
    # 自己紹介
    hobbies = st.text_area("趣味・特技", placeholder="読書、映画鑑賞、プログラミングなど")
    introduction = st.text_area("自己紹介・一言", placeholder="よろしくお願いします！")
    
    # アイコン画像
    icon_image = st.file_uploader(
        "プロフィール画像をアップロード（任意）", 
        type=['png', 'jpg', 'jpeg'],
        help="PNG、JPG、JPEG形式の画像をアップロードできます"
    )
    
    # カスタマイズオプション
    col1, col2 = st.columns(2)
    with col1:
        card_color = st.color_picker("カードの背景色", "#E6F3FF")
    with col2:
        favorite_color = st.color_picker("アクセントカラー", "#4A90E2")
    
    # フォーム送信ボタン
    submitted = st.form_submit_button("自己紹介カードを作成！", use_container_width=True)

# カード表示エリア
st.markdown("---")
st.subheader("完成した自己紹介カード")

if submitted:
    if not name:
        st.error("名前は必須項目です。入力してください。")
    else:
        st.success("自己紹介カードが作成されました！")
        
        # カードスタイル
        st.markdown(f"""
        <div style="
            border: 3px solid {favorite_color};
            border-radius: 15px;
            padding: 25px;
            margin: 20px 0;
            background: linear-gradient(135deg, {card_color} 0%, {card_color}88 100%);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        ">
        """, unsafe_allow_html=True)
        
        # レイアウト: 画像とテキスト情報を2列に分割
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if icon_image is not None:
                st.image(icon_image, caption="プロフィール画像", width=150)
            else:
                # デフォルト画像の代わりにアイコン表示
                st.markdown(f"""
                <div style="
                    width: 150px;
                    height: 150px;
                    background-color: {favorite_color};
                    border-radius: 75px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 60px;
                    color: white;
                    margin: 10px auto;
                ">
                    👤
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # 名前（メイン表示）
            display_name = f"{name} ({nickname})" if nickname else name
            st.markdown(f"""
            <h2 style="
                color: {favorite_color};
                margin-bottom: 10px;
                font-size: 28px;
            ">
                {display_name}
            </h2>
            """, unsafe_allow_html=True)
            
            # 所属情報
            st.write(f"**🎓 所属**: {department}")
            st.write(f"**📚 学年**: {grade}年生")
            
            # 趣味・特技
            if hobbies:
                st.write(f"**🎨 趣味・特技**: {hobbies}")
            
            # 自己紹介
            if introduction:
                st.write(f"**💭 自己紹介**: {introduction}")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ダウンロード機能のヒント
        st.info("💡 このカードのスクリーンショットを撮って保存できます！")
        
else:
    st.info("上記フォームに情報を入力して「自己紹介カードを作成！」ボタンを押してください。")

st.markdown("---")
st.success("✅ 自己紹介カードアプリの解答例です。st.formで入力をまとめ、st.columnsでレイアウトを整えています。")

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「自己紹介カード作成ツール」の解答例です。
    - `st.form` を使って複数の入力項目をまとめて処理します。
    - `st.file_uploader` でプロフィール画像をアップロードできます。
    - `st.columns` を使って画像とテキスト情報を2列レイアウトで表示します。
    - `st.color_picker` でカードの色をカスタマイズできます。
    - HTMLとCSSを使ってカードのデザインを装飾しています。
    """
) 