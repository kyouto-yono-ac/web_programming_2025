import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ページ設定
st.set_page_config(
    page_title="データ可視化アプリ",
    page_icon="📊",
    layout="wide"
)

# アプリのタイトル
st.title('📊 データ可視化アプリ（解答版）')
st.markdown('### 第12回解答：グラフ作成とインタラクティブ可視化')

# データの読み込み（キャッシュ付き）
@st.cache_data
def load_data():
    return pd.read_csv('visa_number_in_japan.csv')

df = load_data()
st.success(f'✅ データを読み込みました: {df.shape[0]}行 × {df.shape[1]}列')

# サイドバーで表示モードを選択
st.sidebar.header('📋 表示モード')
display_mode = st.sidebar.radio(
    '表示するグラフを選択:',
    ['📈 基本グラフ', '✨ 高度なグラフ', '🌍 複数国比較', '📊 総合ダッシュボード']
)

# --- 基本グラフモード ---
if display_mode == '📈 基本グラフ':
    st.header('📈 Streamlitの基本グラフ機能')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('年別総ビザ発行数の推移')
        yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()
        st.line_chart(yearly_totals)
        
        st.subheader('累積推移（面グラフ）')
        st.area_chart(yearly_totals)
    
    with col2:
        st.subheader('2023年 国別ランキング TOP10')
        year_2023 = df[df['Year'] == 2023]
        top10_2023 = year_2023.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(top10_2023)
        
        # 統計情報
        st.metric('2023年総発行数', f"{year_2023['Number of issued_numerical'].sum():,}")
        st.metric('TOP3の合計', f"{top10_2023.head(3).sum():,}")

# --- 高度なグラフモード ---
elif display_mode == '✨ 高度なグラフ':
    st.header('✨ Plotly Expressによる高度なグラフ')
    
    # 上位5カ国の年別推移
    st.subheader('上位5カ国の年別推移比較')
    top_countries = ['China', 'Korea', 'United States', 'Thailand', 'Vietnam']
    filtered_df = df[df['Country'].isin(top_countries)]
    yearly_by_country = filtered_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
    
    fig_line = px.line(yearly_by_country, 
                      x='Year', 
                      y='Number of issued_numerical', 
                      color='Country',
                      title='上位5カ国の年別ビザ発行数推移',
                      markers=True)
    
    fig_line.update_layout(
        xaxis_title='年',
        yaxis_title='ビザ発行数',
        legend_title='国名',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    # 棒グラフとの比較表示
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('2023年 TOP10（棒グラフ）')
        year_2023 = df[df['Year'] == 2023]
        top10_bar = year_2023.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10).reset_index()
        
        fig_bar = px.bar(top10_bar, 
                        x='Number of issued_numerical', 
                        y='Country', 
                        orientation='h',
                        title='2023年 国別ビザ発行数 TOP10')
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.subheader('2023年 TOP10（円グラフ）')
        fig_pie = px.pie(top10_bar, 
                        values='Number of issued_numerical', 
                        names='Country',
                        title='2023年 構成比')
        st.plotly_chart(fig_pie, use_container_width=True)

# --- 複数国比較モード ---
elif display_mode == '🌍 複数国比較':
    st.header('🌍 複数国の動的比較')
    
    # 国選択UI
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.multiselect(
        '比較する国を選択してください（複数選択可）:',
        all_countries,
        default=['China', 'Korea', 'United States', 'Thailand']
    )
    
    if selected_countries:
        # グラフオプション
        col1, col2, col3 = st.columns(3)
        
        with col1:
            chart_type = st.selectbox('グラフタイプ:', ['折れ線グラフ', '棒グラフ', '面グラフ', '散布図'])
        
        with col2:
            year_range = st.slider('年の範囲:', 
                                  min_value=int(df['Year'].min()),
                                  max_value=int(df['Year'].max()),
                                  value=(int(df['Year'].min()), int(df['Year'].max())))
        
        with col3:
            show_total = st.checkbox('合計値も表示')
        
        # データ準備
        comparison_df = df[
            (df['Country'].isin(selected_countries)) & 
            (df['Year'] >= year_range[0]) & 
            (df['Year'] <= year_range[1])
        ]
        comparison_data = comparison_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
        
        # グラフ作成
        if chart_type == '折れ線グラフ':
            fig = px.line(comparison_data, x='Year', y='Number of issued_numerical', 
                         color='Country', markers=True, title='選択した国々の年別推移比較')
        elif chart_type == '棒グラフ':
            fig = px.bar(comparison_data, x='Year', y='Number of issued_numerical', 
                        color='Country', title='選択した国々の年別比較（棒グラフ）')
        elif chart_type == '面グラフ':
            fig = px.area(comparison_data, x='Year', y='Number of issued_numerical', 
                         color='Country', title='選択した国々の年別推移（面グラフ）')
        else:  # 散布図
            fig = px.scatter(comparison_data, x='Year', y='Number of issued_numerical', 
                           color='Country', size='Number of issued_numerical',
                           title='選択した国々の年別推移（散布図）')
        
        fig.update_layout(xaxis_title='年', yaxis_title='ビザ発行数')
        st.plotly_chart(fig, use_container_width=True)
        
        # 合計値の表示
        if show_total:
            st.subheader('📈 期間中の合計値')
            total_by_country = comparison_df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                fig_total = px.bar(x=total_by_country.values, y=total_by_country.index, 
                                  orientation='h', title=f'{year_range[0]}-{year_range[1]}年 期間合計')
                fig_total.update_layout(yaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig_total, use_container_width=True)
            
            with col2:
                st.dataframe(total_by_country.reset_index(), use_container_width=True)
    
    else:
        st.info("比較する国を選択してください")

# --- 総合ダッシュボードモード ---
elif display_mode == '📊 総合ダッシュボード':
    st.header('📊 総合ダッシュボード')
    
    # 全体概要
    st.subheader('🌐 全体概要')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric('総データ数', f"{len(df):,}")
    with col2:
        st.metric('総発行数', f"{df['Number of issued_numerical'].sum():,}")
    with col3:
        st.metric('対象国数', df['Country'].nunique())
    with col4:
        st.metric('対象年数', df['Year'].nunique())
    
    # メイングラフエリア
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader('📈 年別推移とトレンド')
        yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum().reset_index()
        
        # トレンドライン付きの折れ線グラフ
        fig_trend = px.line(yearly_totals, x='Year', y='Number of issued_numerical',
                           title='年別総ビザ発行数推移', markers=True)
        
        # トレンドラインを追加
        fig_trend.add_traces(px.scatter(yearly_totals, x='Year', y='Number of issued_numerical',
                                       trendline='ols').data[1:])
        
        fig_trend.update_layout(showlegend=False)
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col2:
        st.subheader('🏆 最新年ランキング')
        latest_year = df['Year'].max()
        latest_data = df[df['Year'] == latest_year]
        top5_latest = latest_data.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(5)
        
        fig_top5 = px.pie(values=top5_latest.values, names=top5_latest.index,
                         title=f'{latest_year}年 TOP5')
        st.plotly_chart(fig_top5, use_container_width=True)
    
    # 詳細分析
    st.subheader('🔍 詳細分析')
    
    # ヒートマップ
    st.subheader('国・年別ヒートマップ（TOP10国）')
    
    # TOP10国を選択
    top10_countries = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10).index
    heatmap_data = df[df['Country'].isin(top10_countries)]
    heatmap_pivot = heatmap_data.pivot_table(index='Country', columns='Year', 
                                           values='Number of issued_numerical', 
                                           aggfunc='sum', fill_value=0)
    
    fig_heatmap = px.imshow(heatmap_pivot, 
                           title='年別・国別ビザ発行数ヒートマップ',
                           labels=dict(x="年", y="国", color="発行数"))
    st.plotly_chart(fig_heatmap, use_container_width=True)

# フッター
st.markdown('---')
st.markdown("""
### 🎯 第12回で学んだポイント
1. **Streamlitの基本グラフ**: `st.line_chart()`, `st.bar_chart()`, `st.area_chart()`
2. **Plotly Express**: `px.line()`, `px.bar()`, `px.pie()`, `px.scatter()`
3. **インタラクティブ操作**: ズーム、パン、ホバー情報
4. **動的なグラフ**: ユーザー選択に応じたリアルタイム更新
5. **レイアウト設計**: `st.columns()`による効果的な画面分割
6. **データ可視化のベストプラクティス**: 適切なグラフタイプの選択

💡 **可視化の原則**: データの性質に応じた適切なグラフ選択、色使い、レイアウトが重要です。
""")

# 使用データの情報
with st.expander('📋 データ情報'):
    st.write('**データソース**: visa_number_in_japan.csv')
    st.write('**データの形:**', df.shape)
    st.write('**列名:**', df.columns.tolist())
    st.write('**年の範囲:**', df['Year'].min(), '〜', df['Year'].max())
    st.write('**国数:**', df['Country'].nunique())
    
    st.subheader('データサンプル')
    st.dataframe(df.head(), use_container_width=True) 