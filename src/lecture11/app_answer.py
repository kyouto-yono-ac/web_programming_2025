import streamlit as st
import pandas as pd

# ページ設定
st.set_page_config(page_title="ビザ発行数分析アプリ", page_icon="📊")

# アプリのタイトル
st.title('📊 ビザ発行数分析アプリ（解答版）')
st.markdown('### 第11回解答：実践データ分析 - 集計とランキング')

# データの読み込み（キャッシュ付き）
@st.cache_data
def load_data():
    return pd.read_csv('visa_number_in_japan.csv')

df = load_data()
st.success(f'✅ データを読み込みました: {df.shape[0]}行 × {df.shape[1]}列')

# サイドバーで分析タイプを選択
st.sidebar.header('📋 分析メニュー')
analysis_type = st.sidebar.radio(
    '分析タイプを選択:',
    ['🌏 国別データ表示', '🏆 年別ランキング', '📈 複数年比較']
)

# --- Part 1: 国別データ表示 ---
if analysis_type == '🌏 国別データ表示':
    st.header('🌏 国別データ表示')
    
    # 国のリストを取得
    countries = sorted(df['Country'].unique())
    selected_country = st.selectbox('国を選択してください:', countries)
    
    # 選択された国のデータをフィルタリング
    filtered_data = df[df['Country'] == selected_country]
    
    # 基本統計の表示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('📊 データ件数', len(filtered_data))
    with col2:
        st.metric('📅 年の範囲', f"{filtered_data['Year'].min()}-{filtered_data['Year'].max()}")
    with col3:
        st.metric('🎫 総発行数', f"{filtered_data['Number of issued_numerical'].sum():,}")
    
    # データテーブル表示
    st.subheader(f'📋 {selected_country}のデータ')
    st.dataframe(filtered_data, use_container_width=True)
    
    # 年別トレンドグラフ
    if len(filtered_data) > 1:
        st.subheader(f'📈 {selected_country}の年別トレンド')
        yearly_data = filtered_data.groupby('Year')['Number of issued_numerical'].sum().reset_index()
        st.line_chart(yearly_data.set_index('Year'))

# --- Part 2: 年別ランキング ---
elif analysis_type == '🏆 年別ランキング':
    st.header('🏆 年別ランキング')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 年を選択
        min_year = int(df['Year'].min())
        max_year = int(df['Year'].max())
        selected_year = st.slider('分析する年:', min_year, max_year, max_year)
    
    with col2:
        # 表示件数を選択
        top_n = st.selectbox('表示する上位件数:', [5, 10, 15, 20], index=1)
    
    # その年のデータを取得
    year_data = df[df['Year'] == selected_year]
    
    if len(year_data) > 0:
        # 国別集計
        country_totals = year_data.groupby('Country')['Number of issued_numerical'].sum()
        
        # TOP N作成
        top_countries = country_totals.sort_values(ascending=False).head(top_n).reset_index()
        top_countries['順位'] = range(1, len(top_countries) + 1)
        top_countries = top_countries[['順位', 'Country', 'Number of issued_numerical']]
        top_countries.columns = ['順位', '国名', 'ビザ発行数']
        
        # ランキング表示
        st.subheader(f'🏆 {selected_year}年 国別ビザ発行数ランキング TOP{top_n}')
        st.dataframe(top_countries, use_container_width=True)
        
        # 棒グラフ表示
        st.subheader('📊 ランキンググラフ')
        chart_data = country_totals.sort_values(ascending=False).head(top_n)
        st.bar_chart(chart_data)
        
        # 統計情報
        st.subheader('📈 統計情報')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('🎫 総発行数', f"{year_data['Number of issued_numerical'].sum():,}")
        with col2:
            st.metric('🌍 対象国数', len(country_totals))
        with col3:
            st.metric('🥇 1位の発行数', f"{top_countries['ビザ発行数'].iloc[0]:,}")
    else:
        st.warning(f'{selected_year}年のデータが見つかりません。')

# --- Part 3: 複数年比較 ---
elif analysis_type == '📈 複数年比較':
    st.header('📈 複数年比較')
    
    # 比較する年を選択
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    years_to_compare = st.multiselect(
        '比較する年を選択（2年以上選択）:',
        range(min_year, max_year + 1),
        default=[max_year - 1, max_year]
    )
    
    # 比較する国を選択
    top_countries = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10).index.tolist()
    countries_to_compare = st.multiselect(
        '比較する国を選択:',
        top_countries,
        default=top_countries[:5]
    )
    
    if len(years_to_compare) >= 2 and len(countries_to_compare) >= 1:
        # データをフィルタリング
        filtered_df = df[
            (df['Year'].isin(years_to_compare)) & 
            (df['Country'].isin(countries_to_compare))
        ]
        
        # 年・国別集計
        comparison_data = filtered_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
        
        # ピボットテーブルを作成
        pivot_data = comparison_data.pivot(index='Country', columns='Year', values='Number of issued_numerical').fillna(0)
        
        st.subheader('📊 年別・国別比較表')
        st.dataframe(pivot_data, use_container_width=True)
        
        # 折れ線グラフで推移を表示
        st.subheader('📈 年別推移グラフ')
        for country in countries_to_compare:
            country_data = comparison_data[comparison_data['Country'] == country]
            if len(country_data) > 0:
                chart_data = country_data.set_index(['Year'])['Number of issued_numerical']
                st.line_chart(chart_data, use_container_width=True)
    else:
        st.info('比較するには2年以上と1カ国以上を選択してください。')

# フッター
st.markdown('---')
st.markdown("""
### 🎯 学習ポイント
1. **`st.selectbox`**: 選択肢から1つを選ぶ
2. **`st.slider`**: 数値の範囲から値を選ぶ
3. **`st.multiselect`**: 複数の選択肢を選ぶ
4. **`st.cache_data`**: データ読み込みの高速化
5. **`groupby()`**: データの集計
6. **`sort_values()`**: データの並び替え
""")

# データの基本情報
with st.expander('📋 データ情報'):
    st.write('**データの形:**', df.shape)
    st.write('**列名:**', df.columns.tolist())
    st.write('**年の範囲:**', df['Year'].min(), '〜', df['Year'].max())
    st.write('**国数:**', df['Country'].nunique())
    st.write('**データ例:**')
    st.dataframe(df.head()) 