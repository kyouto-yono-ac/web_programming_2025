import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("第9回 データ可視化デモ")
st.caption("Streamlitで作成できるグラフとチャートの例")

st.markdown("---")

# サンプルデータの準備
np.random.seed(42)

# 1. 棒グラフの例
st.subheader("1. 棒グラフ (st.bar_chart)")
st.write("おみくじアプリの結果統計の例")

omikuji_data = pd.DataFrame({
    '運勢': ['大吉', '中吉', '小吉', '吉', '末吉', '凶'],
    '今月の出現回数': [5, 8, 12, 15, 7, 3]
})

st.bar_chart(omikuji_data.set_index('運勢'))

# データも表示
with st.expander("データを確認"):
    st.dataframe(omikuji_data)

st.markdown("---")

# 2. 線グラフの例
st.subheader("2. 線グラフ (st.line_chart)")
st.write("カフェ満足度の推移例")

chart_data = pd.DataFrame(
    np.random.randn(20, 3) + [1, 2, 3],
    columns=['気分', '予算満足度', '味の評価']
)

st.line_chart(chart_data)

st.markdown("---")

# 3. メトリクス表示
st.subheader("3. メトリクス表示 (st.metric)")
st.write("ToDoリストの進捗状況例")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="完了率",
        value="75%",
        delta="15%",
        delta_color="normal"
    )

with col2:
    st.metric(
        label="今日のタスク数",
        value=8,
        delta=2,
        delta_color="normal"
    )

with col3:
    st.metric(
        label="平均所要時間",
        value="25分",
        delta="-5分",
        delta_color="inverse"
    )

st.markdown("---")

# 4. 円グラフ (Plotly使用)
st.subheader("4. 円グラフ (st.plotly_chart)")
st.write("自己紹介カードの趣味分布例")

hobby_data = pd.DataFrame({
    'カテゴリ': ['読書', '映画鑑賞', 'スポーツ', '料理', 'ゲーム', 'その他'],
    '人数': [12, 8, 6, 10, 15, 4]
})

fig = px.pie(hobby_data, values='人数', names='カテゴリ', title="趣味の分布")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 5. 散布図
st.subheader("5. 散布図 (st.plotly_chart)")
st.write("カフェ診断結果の相関例")

cafe_data = pd.DataFrame({
    '予算': np.random.randint(500, 3000, 50),
    '満足度': np.random.randint(1, 6, 50),
    'カテゴリ': np.random.choice(['がっつり', 'ヘルシー', 'おしゃれ', '静か'], 50)
})

fig2 = px.scatter(cafe_data, x='予算', y='満足度', color='カテゴリ', title="予算と満足度の関係")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 6. ヒストグラム
st.subheader("6. ヒストグラム (st.plotly_chart)")
st.write("ラッキーカラー診断の利用時間分布例")

time_data = np.random.normal(14, 3, 100)  # 平均14時、標準偏差3時間
time_df = pd.DataFrame({'利用時間': time_data})

fig3 = px.histogram(time_df, x='利用時間', bins=20, title="アプリ利用時間の分布")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# 7. インタラクティブな例
st.subheader("7. インタラクティブなグラフ")
st.write("スライダーでデータを変更できる例")

# スライダーでデータ数を調整
data_points = st.slider("データ数を選択", 10, 100, 50)

# ランダムデータ生成
interactive_data = pd.DataFrame({
    'x': np.random.randn(data_points),
    'y': np.random.randn(data_points),
    'カテゴリ': np.random.choice(['A', 'B', 'C'], data_points)
})

fig4 = px.scatter(interactive_data, x='x', y='y', color='カテゴリ', 
                  title=f"インタラクティブ散布図 (データ数: {data_points})")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# 8. 実装のヒント
st.subheader("8. 実装のヒント")

with st.expander("グラフをアプリに追加する方法"):
    st.markdown("""
    ### 基本的な手順
    1. **データの準備**: pandas DataFrameを作成
    2. **グラフの選択**: 表示したいデータに適したグラフを選ぶ
    3. **Streamlit関数の使用**: `st.bar_chart()`, `st.line_chart()`, `st.plotly_chart()`など
    
    ### よく使う組み合わせ
    - **ToDoリスト**: 進捗率のメトリクス + 完了状況の棒グラフ
    - **診断アプリ**: 結果分布の円グラフ + 傾向の線グラフ
    - **カード作成**: 入力データの統計をメトリクスで表示
    
    ### 注意点
    - データが空の場合のエラーハンドリング
    - グラフのサイズ調整 (`use_container_width=True`)
    - 色やスタイルの統一
    """)

st.success("💡 これらのグラフを参考に、自分のアプリにも可視化機能を追加してみましょう！") 