import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from datetime import datetime

st.title("第13回 最終課題: パーソナル健康管理ダッシュボード - 解答例")
st.caption("健康データの記録・分析とAIによる健康アドバイスを提供するダッシュボードです。")

st.markdown("---")

# データ読み込み
@st.cache_data
def load_health_tips():
    df = pd.read_csv("data/health_tips.csv")
    return df

tips_df = load_health_tips()

# セッション状態の初期化
if "health_data" not in st.session_state:
    st.session_state.health_data = []
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {
        "name": "",
        "age": 20,
        "height": 160,
        "target_weight": 50
    }

# サイドバー: プロフィール設定
st.sidebar.header("👤 プロフィール")
st.session_state.user_profile["name"] = st.sidebar.text_input("名前", value=st.session_state.user_profile["name"])
st.session_state.user_profile["age"] = st.sidebar.slider("年齢", 15, 80, st.session_state.user_profile["age"])
st.session_state.user_profile["height"] = st.sidebar.slider("身長 (cm)", 140, 200, st.session_state.user_profile["height"])
st.session_state.user_profile["target_weight"] = st.sidebar.slider("目標体重 (kg)", 40, 100, st.session_state.user_profile["target_weight"])

# API キー設定
api_key = st.sidebar.text_input("Gemini API キー", type="password")
if api_key:
    genai.configure(api_key=api_key)

# 健康の基準値表示
st.sidebar.header("📋 健康の基準値")
for idx, row in tips_df.iterrows():
    st.sidebar.text(f"{row['項目']}: {row['推奨値']}")

# タブ構成
tab1, tab2, tab3 = st.tabs(["📊 ダッシュボード", "📝 データ入力", "💡 AIアドバイス"])

with tab1:
    st.subheader("健康状態概要")
    
    if st.session_state.health_data:
        df = pd.DataFrame(st.session_state.health_data)
        latest_data = df.iloc[-1]
        
        # 基本メトリクス
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("現在の体重", f"{latest_data['weight']:.1f} kg")
        
        with col2:
            bmi = latest_data['weight'] / (st.session_state.user_profile["height"] / 100) ** 2
            st.metric("BMI", f"{bmi:.1f}")
        
        with col3:
            target_diff = latest_data['weight'] - st.session_state.user_profile["target_weight"]
            st.metric("目標まで", f"{target_diff:+.1f} kg")
        
        with col4:
            st.metric("記録日数", len(df))
        
        # 体重変化グラフ
        st.subheader("体重変化")
        fig_weight = px.line(df, x='date', y='weight', title='体重の変化', markers=True)
        fig_weight.add_hline(
            y=st.session_state.user_profile["target_weight"],
            line_dash="dash",
            annotation_text="目標体重"
        )
        st.plotly_chart(fig_weight, use_container_width=True)
        
        # 統計サマリー
        st.subheader("統計サマリー")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**体重**")
            st.write(f"平均: {df['weight'].mean():.1f} kg")
            st.write(f"変動: {df['weight'].max() - df['weight'].min():.1f} kg")
        
        with col2:
            st.write("**生活習慣**")
            st.write(f"平均運動時間: {df['exercise_minutes'].mean():.0f} 分")
            st.write(f"平均睡眠時間: {df['sleep_hours'].mean():.1f} 時間")
            st.write(f"平均体調スコア: {df['condition_score'].mean():.1f}")
        
        # 生活習慣のグラフ
        st.subheader("生活習慣の推移")
        
        fig_exercise = px.line(df, x='date', y='exercise_minutes', title='運動時間の推移')
        st.plotly_chart(fig_exercise, use_container_width=True)
        
        fig_sleep = px.line(df, x='date', y='sleep_hours', title='睡眠時間の推移')
        st.plotly_chart(fig_sleep, use_container_width=True)
        
    else:
        st.info("まだデータがありません。「データ入力」タブから健康データを記録してください。")

with tab2:
    st.subheader("今日の健康データ入力")
    
    with st.form("health_input_form"):
        st.write("**基本データ**")
        weight = st.number_input("体重 (kg)", min_value=30.0, max_value=150.0, value=50.0, step=0.1)
        
        st.write("**生活習慣**")
        col1, col2 = st.columns(2)
        
        with col1:
            exercise_minutes = st.number_input("運動時間 (分)", min_value=0, max_value=300, value=0)
            sleep_hours = st.number_input("睡眠時間 (時間)", min_value=0.0, max_value=12.0, value=7.0, step=0.5)
        
        with col2:
            condition_score = st.slider("体調スコア", 1, 5, 3, help="1:悪い, 5:とても良い")
        
        memo = st.text_area("今日のメモ", placeholder="食事内容、気になることなど")
        
        submitted = st.form_submit_button("記録する", use_container_width=True)
        
        if submitted:
            new_record = {
                "date": datetime.now().date(),
                "weight": weight,
                "exercise_minutes": exercise_minutes,
                "sleep_hours": sleep_hours,
                "condition_score": condition_score,
                "memo": memo
            }
            
            st.session_state.health_data.append(new_record)
            st.success("健康データを記録しました！")
            st.rerun()

with tab3:
    st.subheader("AIによる健康アドバイス")
    
    if not api_key:
        st.warning("AIアドバイスを利用するには、サイドバーでGemini API キーを設定してください。")
    elif not st.session_state.health_data:
        st.info("健康データを記録してからAIアドバイスをご利用ください。")
    else:
        if st.button("AIアドバイスを取得", use_container_width=True):
            model = genai.GenerativeModel('gemini-2.0-flash-lite')
            df = pd.DataFrame(st.session_state.health_data)
            latest_data = df.iloc[-1]
            
            prompt = f"""
            以下の健康データを基に、パーソナライズされた健康アドバイスを提供してください。

            プロフィール:
            - 年齢: {st.session_state.user_profile['age']}歳
            - 身長: {st.session_state.user_profile['height']}cm
            - 目標体重: {st.session_state.user_profile['target_weight']}kg

            最新の健康データ:
            - 現在の体重: {latest_data['weight']}kg
            - 運動時間: {latest_data['exercise_minutes']}分
            - 睡眠時間: {latest_data['sleep_hours']}時間
            - 体調スコア: {latest_data['condition_score']}/5

            以下の観点からアドバイスを提供してください:
            1. 体重管理について
            2. 運動習慣について
            3. 睡眠の質について
            4. 健康維持のための提案

            親しみやすく、実践しやすいアドバイスをお願いします。
            """
            
            response = model.generate_content(prompt)
            
            st.success("AIアドバイスが完成しました！")
            st.markdown(response.text)

st.markdown("---")
st.success("✅ パーソナル健康管理ダッシュボードの解答例です。CSVファイルから健康の基準値を読み込み、データ分析とAIアドバイスを組み合わせています。") 