import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

st.title("第13回 最終課題: パーソナル学習アシスタント - 解答例")
st.caption("AIがあなたの学習をサポートする個人専用の学習アシスタントです。")

st.markdown("---")

# データ読み込み
@st.cache_data
def load_learning_resources():
    df = pd.read_csv("data/learning_resources.csv")
    return df

resources_df = load_learning_resources()

# API設定
api_key = st.text_input(
    "Gemini API キーを入力してください:",
    type="password",
    help="Google AI StudioでAPIキーを取得してください"
)

if api_key:
    genai.configure(api_key=api_key)

# セッション状態の初期化
if "learning_history" not in st.session_state:
    st.session_state.learning_history = []
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {
        "name": "",
        "grade": 1,
        "subjects": []
    }

# サイドバー: ユーザープロフィール設定
st.sidebar.header("👤 ユーザープロフィール")

st.session_state.user_profile["name"] = st.sidebar.text_input(
    "名前",
    value=st.session_state.user_profile["name"]
)

st.session_state.user_profile["grade"] = st.sidebar.selectbox(
    "学年",
    [1, 2, 3, 4],
    index=st.session_state.user_profile["grade"] - 1
)

subject_options = resources_df["科目"].unique().tolist()

st.session_state.user_profile["subjects"] = st.sidebar.multiselect(
    "学習中の科目",
    subject_options,
    default=st.session_state.user_profile["subjects"]
)

# 学習記録表示
st.sidebar.header("📚 学習記録")
if st.session_state.learning_history:
    recent_sessions = st.session_state.learning_history[-3:]
    for session in reversed(recent_sessions):
        st.sidebar.text(f"• {session['subject']} ({session['date'].strftime('%m/%d')})")
else:
    st.sidebar.text("まだ学習記録がありません")

# メインエリア: タブ構成
tab1, tab2, tab3 = st.tabs(["🎯 今日の学習", "❓ 質問・解説", "📊 学習進捗"])

with tab1:
    st.subheader("今日の学習プラン")
    
    if not api_key:
        st.warning("Gemini API キーを設定してください。")
    else:
        # 科目選択
        if st.session_state.user_profile["subjects"]:
            selected_subject = st.selectbox(
                "今日学習する科目を選択",
                st.session_state.user_profile["subjects"]
            )
        else:
            selected_subject = st.selectbox(
                "今日学習する科目を選択",
                subject_options
            )
        
        # 関連リソース表示
        if selected_subject:
            st.subheader(f"{selected_subject}の学習リソース")
            subject_resources = resources_df[resources_df["科目"] == selected_subject]
            
            if not subject_resources.empty:
                for idx, row in subject_resources.iterrows():
                    with st.expander(f"{row['リソース名']} ({row['レベル']}) {row['難易度']}"):
                        st.write(f"**タイプ**: {row['タイプ']}")
                        st.write(f"**説明**: {row['説明']}")
        
        # トピック入力
        topic = st.text_input(
            "学習トピック",
            placeholder="例: Python の関数について、統計の基礎概念"
        )
        
        # 学習レベル選択
        level = st.selectbox(
            "学習レベル",
            ["初級", "中級", "上級"]
        )
        
        if st.button("学習プランを作成", use_container_width=True):
            if selected_subject and topic:
                model = genai.GenerativeModel('gemini-2.0-flash-lite')
                
                prompt = f"""
                学習者プロフィール:
                - 名前: {st.session_state.user_profile['name']}
                - 学年: {st.session_state.user_profile['grade']}年生
                
                科目: {selected_subject}
                トピック: {topic}
                レベル: {level}
                
                上記の情報を元に、学習プランを作成してください。
                以下の要素を含めてください：
                1. 学習目標
                2. 学習手順（3ステップ）
                3. 練習問題（1問）
                4. 理解度チェック項目
                
                親しみやすい文章でお願いします。
                """
                
                response = model.generate_content(prompt)
                
                st.success("学習プランが作成されました！")
                st.markdown(response.text)
                
                # 学習セッションを記録
                st.session_state.learning_history.append({
                    "subject": selected_subject,
                    "topic": topic,
                    "level": level,
                    "date": datetime.now()
                })
            else:
                st.warning("科目とトピックを入力してください。")

with tab2:
    st.subheader("質問・解説サポート")
    
    if not api_key:
        st.warning("Gemini API キーを設定してください。")
    else:
        # 質問内容入力
        question = st.text_area(
            "質問内容",
            placeholder="わからないことを詳しく書いてください...",
            height=150
        )
        
        if st.button("AIに質問する", use_container_width=True):
            if question:
                model = genai.GenerativeModel('gemini-2.0-flash-lite')
                
                context = f"""
                学習者情報:
                - 学年: {st.session_state.user_profile['grade']}年生
                - 得意科目: {', '.join(st.session_state.user_profile['subjects'])}
                
                以下の質問に、学習者のレベルに合わせて分かりやすく回答してください。
                
                質問: {question}
                """
                
                response = model.generate_content(context)
                
                st.success("回答が完成しました！")
                
                # 質問と回答を表示
                st.markdown("### 📝 質問")
                st.write(question)
                
                st.markdown("### 🤖 AI回答")
                st.markdown(response.text)
            else:
                st.warning("質問内容を入力してください。")

with tab3:
    st.subheader("学習進捗ダッシュボード")
    
    if st.session_state.learning_history:
        # 学習データの準備
        df = pd.DataFrame(st.session_state.learning_history)
        
        # 基本統計
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("総学習セッション数", len(df))
        
        with col2:
            unique_subjects = df['subject'].nunique()
            st.metric("学習科目数", unique_subjects)
        
        with col3:
            recent_sessions = len(df[df['date'] > datetime.now() - pd.Timedelta(days=7)])
            st.metric("今週の学習回数", recent_sessions)
        
        # 科目別学習回数
        st.subheader("科目別学習回数")
        subject_counts = df['subject'].value_counts()
        st.bar_chart(subject_counts)
        
    else:
        st.info("まだ学習記録がありません。「今日の学習」タブから学習を始めてみましょう！")

st.markdown("---")
st.success("✅ パーソナル学習アシスタントの解答例です。CSVファイルから学習リソースを読み込み、Gemini APIを活用しています。") 