"""
第11回 Part 5: 総合ダッシュボード作成
正解例：インタラクティブなビザ発行数分析ダッシュボード
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ページ設定
st.set_page_config(
    page_title="ビザ発行数分析ダッシュボード", 
    page_icon="🌍",
    layout="wide"
)

# データ読み込み
@st.cache_data
def load_data():
    """データを読み込み、キャッシュに保存"""
    return pd.read_csv('visa_number_in_japan.csv')

# メインタイトル
st.title('🌍 日本ビザ発行数分析ダッシュボード')
st.markdown("**Part 5: 総合ダッシュボード作成 - 正解例**")
st.markdown("---")

# データ読み込み
df = load_data()
st.success(f"✅ データ読み込み完了: {df.shape[0]:,}行 × {df.shape[1]}列")

# 国リストの取得
countries = sorted(df['Country'].unique())

# =============================================================================
# サイドバーによる操作パネル
# =============================================================================

st.sidebar.header('🎛️ 設定パネル')
st.sidebar.markdown("### ダッシュボードの設定")

# 年選択
sidebar_year = st.sidebar.slider(
    '📅 分析対象年', 
    min_value=int(df['Year'].min()), 
    max_value=int(df['Year'].max()), 
    value=2017,
    help="グラフに表示する年を選択してください"
)

# 国選択（上位国から自動選択）
top_countries_list = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(15).index.tolist()

# デフォルト値を安全に設定（存在する国のみ）
potential_defaults = ['China', 'Korea', 'South Korea', 'United States', 'USA']
safe_defaults = [country for country in potential_defaults if country in top_countries_list]
if not safe_defaults:  # 安全なデフォルト値がない場合は上位3国を使用
    safe_defaults = top_countries_list[:3]

sidebar_countries = st.sidebar.multiselect(
    '🌍 比較対象国', 
    top_countries_list, 
    default=safe_defaults[:3],  # 最大3国まで
    help="時系列比較で表示する国を選択してください"
)

# グラフタイプ設定
graph_type = st.sidebar.selectbox(
    '📈 グラフタイプ',
    ['棒グラフ', '折れ線', '円グラフ'],
    help="ランキングタブでのグラフ表示形式を選択してください"
)

# 表示件数設定
display_count = st.sidebar.selectbox(
    '🔢 ランキング表示件数',
    [5, 10, 15, 20],
    index=1,
    help="ランキングに表示する国の数を選択してください"
)

# =============================================================================
# タブによる機能分け
# =============================================================================

tab1, tab2, tab3 = st.tabs(['📊 ランキング', '📈 時系列比較', '🥧 構成比'])

# -----------------------------------------------------------------------------
# タブ1: ランキング
# -----------------------------------------------------------------------------
with tab1:
    st.subheader(f'🏆 {sidebar_year}年 国別ランキング TOP{display_count}')
    
    # その年のデータでランキング作成
    year_ranking = df[df['Year'] == sidebar_year].groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(display_count)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # グラフ表示（選択されたグラフタイプに応じて）
        if graph_type == '棒グラフ':
            fig_ranking = px.bar(
                x=year_ranking.index,
                y=year_ranking.values,
                title=f'{sidebar_year}年 国別ビザ発行数ランキング',
                labels={'x': '国名', 'y': 'ビザ発行数'},
                color=year_ranking.values,
                color_continuous_scale='Blues'
            )
            fig_ranking.update_layout(xaxis_tickangle=-45)
            
        elif graph_type == '円グラフ':
            fig_ranking = px.pie(
                values=year_ranking.values,
                names=year_ranking.index,
                title=f'{sidebar_year}年 国別ビザ発行数構成比'
            )
            
        else:  # 折れ線グラフ
            fig_ranking = px.line(
                x=year_ranking.index,
                y=year_ranking.values,
                title=f'{sidebar_year}年 国別ビザ発行数ランキング',
                markers=True
            )
            fig_ranking.update_layout(xaxis_tickangle=-45)
        
        st.plotly_chart(fig_ranking, use_container_width=True)
    
    with col2:
        # ランキングテーブル
        st.markdown("### 📋 詳細ランキング")
        ranking_df = pd.DataFrame({
            '順位': range(1, len(year_ranking) + 1),
            '国名': year_ranking.index,
            '発行数': [f"{v:,}" for v in year_ranking.values]
        })
        st.dataframe(ranking_df, use_container_width=True, hide_index=True)
        
        # 統計情報
        st.markdown("### 📊 統計情報")
        st.metric("合計発行数", f"{year_ranking.sum():,}")
        st.metric("平均発行数", f"{year_ranking.mean():.0f}")
        st.metric("最大発行数", f"{year_ranking.max():,}")

# -----------------------------------------------------------------------------
# タブ2: 時系列比較
# -----------------------------------------------------------------------------
with tab2:
    st.subheader('📈 複数国の時系列比較')
    
    if not sidebar_countries:
        st.info("📝 サイドバーから比較対象国を選択してください。")
    else:
        # 選択された国のデータを抽出
        filtered_data = df[df['Country'].isin(sidebar_countries)]
        
        # 時系列データの準備
        time_series_data = filtered_data.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
        
        # 時系列グラフ
        fig_timeseries = px.line(
            time_series_data,
            x='Year',
            y='Number of issued_numerical',
            color='Country',
            title='選択国の年次推移比較',
            markers=True,
            labels={'Number of issued_numerical': 'ビザ発行数', 'Year': '年'}
        )
        fig_timeseries.update_layout(
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_timeseries, use_container_width=True)
        
        # 年別比較表
        st.markdown("### 📊 年別比較表")
        pivot_table = time_series_data.pivot(index='Year', columns='Country', values='Number of issued_numerical').fillna(0)
        
        # 数値をカンマ区切りでフォーマット
        formatted_table = pivot_table.style.format("{:,.0f}")
        st.dataframe(formatted_table, use_container_width=True)
        
        # 各国の合計と平均
        st.markdown("### 📈 各国の統計サマリー")
        summary_stats = []
        for country in sidebar_countries:
            country_data = time_series_data[time_series_data['Country'] == country]['Number of issued_numerical']
            summary_stats.append({
                '国名': country,
                '合計発行数': f"{country_data.sum():,}",
                '平均発行数': f"{country_data.mean():.0f}",
                '最大発行数': f"{country_data.max():,}",
                '最小発行数': f"{country_data.min():,}"
            })
        
        summary_df = pd.DataFrame(summary_stats)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# タブ3: 構成比
# -----------------------------------------------------------------------------
with tab3:
    st.subheader('🥧 国別構成比分析')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 全期間の構成比
        st.markdown("#### 全期間通算 TOP10")
        total_pie_data = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
        
        fig_pie_total = px.pie(
            values=total_pie_data.values,
            names=total_pie_data.index,
            title='全期間通算 国別構成比'
        )
        fig_pie_total.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie_total, use_container_width=True)
        
        # 全期間統計
        st.markdown("##### 📊 全期間統計")
        st.metric("総発行数", f"{total_pie_data.sum():,}")
        st.metric("TOP3合計", f"{total_pie_data.head(3).sum():,}")
        st.metric("TOP3比率", f"{(total_pie_data.head(3).sum() / total_pie_data.sum() * 100):.1f}%")
    
    with col2:
        # 選択年の構成比
        st.markdown(f"#### {sidebar_year}年 TOP10")
        year_pie_data = df[df['Year'] == sidebar_year].groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
        
        fig_pie_year = px.pie(
            values=year_pie_data.values,
            names=year_pie_data.index,
            title=f'{sidebar_year}年 国別構成比'
        )
        fig_pie_year.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie_year, use_container_width=True)
        
        # 選択年統計
        st.markdown(f"##### 📊 {sidebar_year}年統計")
        st.metric("年間発行数", f"{year_pie_data.sum():,}")
        st.metric("TOP3合計", f"{year_pie_data.head(3).sum():,}")
        st.metric("TOP3比率", f"{(year_pie_data.head(3).sum() / year_pie_data.sum() * 100):.1f}%")
    
    # 年次変化の分析
    st.markdown("---")
    st.markdown("### 📈 TOP5国の年次変化")
    
    # TOP5国の年次推移
    top5_countries = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(5).index
    top5_yearly = df[df['Country'].isin(top5_countries)].groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
    
    fig_top5_trend = px.area(
        top5_yearly,
        x='Year',
        y='Number of issued_numerical',
        color='Country',
        title='TOP5国の年次推移（積み上げエリア）',
        labels={'Number of issued_numerical': 'ビザ発行数', 'Year': '年'}
    )
    st.plotly_chart(fig_top5_trend, use_container_width=True)

