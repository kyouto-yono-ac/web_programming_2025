import streamlit as st
import pandas as pd

# アプリのタイトル
st.title('📊 ビザ発行数分析アプリ')
st.markdown('### 第11回演習：国別ビザ発行数の分析')

# データの読み込み
df = pd.read_csv('visa_number_in_japan.csv')
st.write(f'データを読み込みました：{df.shape[0]}行 × {df.shape[1]}列')

# --- Part 1: 第10回の補完（基本版） ---
st.header('🌏 Part 1: 国別データ表示')
st.markdown('**目標**: st.selectboxで国を選んでデータを表示しよう')

# TODO: ここを完成させよう！
# 1. 国のリストを取得する
countries = sorted(df['Country'].unique())

# 2. st.selectboxで国を選択できるようにする
selected_country = st.selectbox('国を選択してください:', countries)

# 3. 選択された国のデータをフィルタリングする
# ヒント: df[df['Country'] == selected_country]
# filtered_data = # ここを埋めよう！
filtered_data = df[df['Country'] == selected_country]  # 演習用：この行を自分で書いてみよう

# 4. フィルタリング結果を表示する
st.write(f'{selected_country}のデータ：{len(filtered_data)}件')
st.dataframe(filtered_data)

# --- Part 2: 年別ランキング（発展版） ---
st.header('🏆 Part 2: 年別ランキング')
st.markdown('**目標**: 特定の年のTOP10ランキングを表示しよう')

# 年を選択するスライダー
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
selected_year = st.slider('分析する年を選択:', min_year, max_year, max_year)

# TODO: 年別ランキングを作成しよう！
# 1. その年のデータを取得
# year_data = # ここを埋めよう！ ヒント: df[df['Year'] == selected_year]
year_data = df[df['Year'] == selected_year]  # 演習用：この行を自分で書いてみよう

# 2. 国別に集計（合計を計算）
# ヒント: year_data.groupby('Country')['Number of issued_numerical'].sum()
# country_totals = # ここを埋めよう！ 
country_totals = year_data.groupby('Country')['Number of issued_numerical'].sum()  # 演習用

# 3. 多い順にソートしてTOP10を取得
# ヒント: .sort_values(ascending=False).head(10)
# top10 = # ここを埋めよう！
top10 = country_totals.sort_values(ascending=False).head(10)  # 演習用

# 4. 結果を表示
st.write(f'{selected_year}年の国別ビザ発行数ランキング TOP10')
st.dataframe(top10)

# 簡単な棒グラフも表示してみよう（オプション）
if st.checkbox('グラフを表示'):
    st.bar_chart(top10)

# --- 発展課題のヒント ---
st.markdown('---')
st.markdown("""
💡 **発展課題のアイデア**:
1. 複数の国を比較できる機能
2. 特定の地域（アジア、ヨーロッパなど）でフィルタ
3. 年の範囲を指定して合計を計算
4. 増減率の計算
""")

# デバッグ用の情報（開発時のみ表示）
with st.expander('デバッグ情報'):
    st.write('データの列:', df.columns.tolist())
    st.write('データの形:', df.shape)
    st.write('年の範囲:', df['Year'].min(), '~', df['Year'].max())
    st.write('国数:', df['Country'].nunique()) 