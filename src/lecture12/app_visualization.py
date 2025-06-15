import streamlit as st
import pandas as pd
import plotly.express as px

# アプリのタイトル
st.title('📊 データ可視化アプリ')
st.markdown('### 第12回演習：グラフ作成とインタラクティブ可視化')

# データの読み込み
df = pd.read_csv('visa_number_in_japan.csv')
st.write(f'データを読み込みました：{df.shape[0]}行 × {df.shape[1]}列')

# --- Part 1: Streamlitの基本グラフ ---
st.header('📈 Part 1: Streamlitの基本グラフ')
st.markdown('**目標**: 基本的なグラフ機能を使ってデータを可視化しよう')

# TODO: 年別総ビザ発行数の推移を折れ線グラフで表示
st.subheader('年別総ビザ発行数の推移')

# 1. 年別集計データを作成
# ヒント: df.groupby('Year')['Number of issued_numerical'].sum()
# yearly_totals = # ここを埋めよう！
yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()  # 演習用

# 2. 折れ線グラフで表示
# ヒント: st.line_chart(yearly_totals)
# ここを埋めよう！
st.line_chart(yearly_totals)  # 演習用

# TODO: 特定年の国別ランキングを棒グラフで表示
st.subheader('2023年 国別ランキング TOP10')

# 1. 2023年のデータを取得
year_2023 = df[df['Year'] == 2023]

# 2. 国別集計してTOP10を作成
# ヒント: .groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
# top10_2023 = # ここを埋めよう！
top10_2023 = year_2023.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)  # 演習用

# 3. 棒グラフで表示
# ヒント: st.bar_chart(top10_2023)
# ここを埋めよう！
st.bar_chart(top10_2023)  # 演習用

# --- Part 2: Plotly Expressによる高度なグラフ ---
st.header('✨ Part 2: Plotly Expressによる高度なグラフ')
st.markdown('**目標**: より美しく、インタラクティブなグラフを作成しよう')

# 上位5カ国の年別推移データを準備
top_countries = ['China', 'Korea', 'United States', 'Thailand', 'Vietnam']
filtered_df = df[df['Country'].isin(top_countries)]
yearly_by_country = filtered_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()

st.subheader('上位5カ国の年別推移比較')

# TODO: Plotlyで折れ線グラフを作成
# ヒント: px.line(yearly_by_country, x='Year', y='Number of issued_numerical', color='Country')
# fig_line = # ここを埋めよう！
fig_line = px.line(yearly_by_country, x='Year', y='Number of issued_numerical', color='Country', markers=True)  # 演習用

# グラフのカスタマイズ
fig_line.update_layout(
    title='上位5カ国の年別ビザ発行数推移',
    xaxis_title='年',
    yaxis_title='ビザ発行数'
)

# Streamlitで表示
# ヒント: st.plotly_chart(fig_line, use_container_width=True)
# ここを埋めよう！
st.plotly_chart(fig_line, use_container_width=True)  # 演習用

# --- Part 3: 複数国の動的比較 ---
st.header('🌍 Part 3: 複数国の動的比較')
st.markdown('**目標**: ユーザーが国を選択して比較できる機能を作ろう')

# 国選択UI
all_countries = sorted(df['Country'].unique())
selected_countries = st.multiselect(
    '比較する国を選択してください（複数選択可）:',
    all_countries,
    default=['China', 'Korea', 'United States']
)

if selected_countries:
    # 選択された国のデータを準備
    comparison_df = df[df['Country'].isin(selected_countries)]
    comparison_data = comparison_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
    
    # グラフタイプ選択
    chart_type = st.selectbox('グラフタイプを選択:', ['折れ線グラフ', '棒グラフ', '面グラフ'])
    
    # TODO: 選択されたグラフタイプに応じてグラフを作成
    if chart_type == '折れ線グラフ':
        fig = px.line(comparison_data, x='Year', y='Number of issued_numerical', color='Country', markers=True)
    elif chart_type == '棒グラフ':
        fig = px.bar(comparison_data, x='Year', y='Number of issued_numerical', color='Country')
    else:  # 面グラフ
        fig = px.area(comparison_data, x='Year', y='Number of issued_numerical', color='Country')
    
    # グラフを表示
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("比較する国を選択してください")

# --- Part 4: 円グラフによる構成比表示 ---
st.header('🥧 Part 4: 円グラフによる構成比表示')

# 年選択
selected_year = st.slider('年を選択:', 
                         min_value=int(df['Year'].min()), 
                         max_value=int(df['Year'].max()), 
                         value=2023)

# その年のTOP10
year_data = df[df['Year'] == selected_year]
top10_pie = year_data.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10).reset_index()

# TODO: 円グラフを作成
# ヒント: px.pie(top10_pie, values='Number of issued_numerical', names='Country')
# fig_pie = # ここを埋めよう！

fig_pie.update_layout(title=f'{selected_year}年 国別ビザ発行数の構成比 (TOP10)')

# 円グラフを表示
st.plotly_chart(fig_pie, use_container_width=True)

# --- 発展課題のヒント ---
st.markdown('---')
st.markdown("""
💡 **発展課題のアイデア**:
1. 年の範囲を指定して期間別の比較
2. 地域別（アジア、ヨーロッパなど）でのグループ化
3. 増減率を計算して変化率のグラフ
4. ヒートマップによる年・国の2次元表示
5. アニメーション機能（年ごとの変化を動画で表示）
""")

# デバッグ情報
with st.expander('デバッグ情報'):
    st.write('利用可能な国:', df['Country'].unique()[:10], '...など')
    st.write('データの年範囲:', df['Year'].min(), '~', df['Year'].max())
    st.write('上位5カ国データ例:')
    st.dataframe(yearly_by_country.head()) 