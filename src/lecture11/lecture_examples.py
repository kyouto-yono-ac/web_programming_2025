"""
第11回：データ処理・分析・可視化の総合実践 (Pandas)
Streamlit連携とデータ可視化の例
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(
    page_title="第11回 Streamlit例", 
    page_icon="🎮",
    layout="wide"
)

# データ読み込み
@st.cache_data
def load_data():
    """データを読み込み、キャッシュに保存"""
    return pd.read_csv('visa_number_in_japan.csv')

# メインタイトル
st.title('🎮 第11回：Streamlit連携とデータ可視化')
st.markdown("**授業で扱ったStreamlitの例**")
st.markdown("---")

# データ読み込み
df = load_data()
st.success(f"✅ データ読み込み完了: {df.shape[0]:,}行 × {df.shape[1]}列")

# =============================================================================
# Part 3: Streamlit連携
# =============================================================================

st.header("🎮 Part 3: Streamlit連携")

# 3-1. 基本的なUI要素
st.subheader("3-1. 基本的なUI要素")

countries = df['Country'].unique()

col1, col2 = st.columns(2)

with col1:
    st.write("**セレクトボックス（ドロップダウン）**")
    selected_country = st.selectbox('国を選択', countries)
    
    # 選択された国のデータを表示
    country_data = df[df['Country'] == selected_country]
    st.write(f"**{selected_country}のデータ件数:** {len(country_data)}件")
    st.dataframe(country_data.head())

with col2:
    st.write("**スライダー（数値選択）**")
    selected_year = st.slider('年を選択', 
                             min_value=int(df['Year'].min()), 
                             max_value=int(df['Year'].max()), 
                             value=2017)
    
    # その年のデータを表示
    year_data = df[df['Year'] == selected_year]
    st.write(f"**{selected_year}年のデータ件数:** {len(year_data)}件")

st.write("**マルチセレクト（複数選択）**")
selected_countries = st.multiselect(
    '複数国を選択', 
    countries, 
    default=['China', 'South Korea']
)

if selected_countries:
    multi_data = df[df['Country'].isin(selected_countries)]
    st.write(f"**選択された{len(selected_countries)}カ国のデータ件数:** {len(multi_data)}件")
    st.dataframe(multi_data.head())

# 3-2. インタラクティブなデータ表示
st.subheader("3-2. インタラクティブなデータ表示")

# 年選択 → その年のランキング表示
display_year = st.slider('ランキング表示年を選択', 2006, 2017, 2017)

# その年のデータを抽出
year_ranking_data = df[df['Year'] == display_year]

# 国別集計とランキング
ranking = year_ranking_data.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)

# 結果を表示
st.write(f'**{display_year}年 国別TOP10**')
st.dataframe(ranking)

st.markdown("---")

# =============================================================================
# Part 4: データ可視化
# =============================================================================

st.header("📈 Part 4: データ可視化")

# 4-1. Streamlitの基本グラフ
st.subheader("4-1. Streamlitの基本グラフ")

col1, col2 = st.columns(2)

with col1:
    st.write("**年別推移の折れ線グラフ**")
    yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()
    st.line_chart(yearly_totals)

with col2:
    st.write("**国別ランキングの棒グラフ**")
    top10_2017 = df[df['Year'] == 2017].groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top10_2017)

# 4-2. Plotly Expressによる高度なグラフ
st.subheader("4-2. Plotly Expressによる高度なグラフ")

st.write("**インタラクティブな折れ線グラフ**")
line_data = df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
top5_countries = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(5).index
line_data_top5 = line_data[line_data['Country'].isin(top5_countries)]

fig_line = px.line(line_data_top5, 
                   x='Year', 
                   y='Number of issued_numerical', 
                   color='Country',
                   title='上位5カ国の年次推移')
st.plotly_chart(fig_line, use_container_width=True)

st.write("**美しい棒グラフ**")
top10_data = df[df['Year'] == 2017].groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10).reset_index()

fig_bar = px.bar(top10_data, 
                 x='Country', 
                 y='Number of issued_numerical',
                 title='2017年 国別ビザ発行数 TOP10',
                 color='Number of issued_numerical',
                 color_continuous_scale='Blues')
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar, use_container_width=True)

st.write("**円グラフで構成比を表示**")
pie_data = df[df['Year'] == 2017].groupby('Country')['Number of issued_numerical'].sum().head(10).reset_index()

fig_pie = px.pie(pie_data, 
                 values='Number of issued_numerical', 
                 names='Country',
                 title='2017年 国別構成比 (TOP10)')
st.plotly_chart(fig_pie, use_container_width=True)

# 4-3. 複数国の時系列比較
st.subheader("4-3. 複数国の時系列比較")

st.write("**ユーザー選択による動的グラフ**")
comparison_countries = st.multiselect('比較したい国を選択', 
                                    countries, 
                                    default=['China', 'South Korea', 'united states of america'],
                                    key='comparison')

if comparison_countries:
    # 選択された国のデータを抽出
    filtered_data = df[df['Country'].isin(comparison_countries)]
    comparison_data = filtered_data.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
    
    # 比較グラフを作成
    fig_comparison = px.line(comparison_data, 
                            x='Year', 
                            y='Number of issued_numerical', 
                            color='Country',
                            title='選択国の年次推移比較')
    st.plotly_chart(fig_comparison, use_container_width=True)

st.markdown("---")

