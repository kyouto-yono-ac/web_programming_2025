import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("第13回 最終課題: 美容・コスメ商品比較ダッシュボード - 解答例")
st.caption("様々な美容・コスメ商品を比較・分析できるインタラクティブなダッシュボードです。")

st.markdown("---")

# データ読み込み
@st.cache_data
def load_data():
    df = pd.read_csv("data/cosmetic_products_scraped.csv")
    # データクリーニング
    df = df.dropna(subset=['商品名', 'ブランド名', '口コミ点', '口コミ件数'])
    df = df[df['カテゴリ名'] != '注目のアイテム']  # 注目のアイテムは除外
    
    # 税込価格を数値に変換
    df['価格'] = df['税込価格'].str.replace('円', '').str.replace(',', '').str.replace('オープン価格', '0')
    df['価格'] = pd.to_numeric(df['価格'], errors='coerce')
    df = df.dropna(subset=['価格'])
    df = df[df['価格'] > 0]
    
    # カラム名を統一
    df = df.rename(columns={
        'カテゴリ名': 'カテゴリ',
        'ブランド名': 'ブランド',
        '口コミ点': '総合評価',
        '口コミ件数': '口コミ数'
    })
    
    return df

df = load_data()

# サイドバーでフィルタリング
st.sidebar.header("🔍 商品フィルタ")

# ブランドフィルタ
brand_options = df["ブランド"].unique()
selected_brands = st.sidebar.multiselect(
    "ブランドを選択",
    options=brand_options,
    default=brand_options[:5] if len(brand_options) > 5 else brand_options
)

# カテゴリフィルタ
category_options = df["カテゴリ"].unique()
selected_categories = st.sidebar.multiselect(
    "カテゴリを選択",
    options=category_options,
    default=category_options[:3] if len(category_options) > 3 else category_options
)

# 価格帯フィルタ
if not df.empty:
    price_range = st.sidebar.slider(
        "価格帯 (円)",
        min_value=int(df["価格"].min()),
        max_value=int(df["価格"].max()),
        value=(int(df["価格"].min()), int(df["価格"].max()))
    )
else:
    price_range = (0, 100000)

# 評価フィルタ
rating_range = st.sidebar.slider(
    "評価範囲",
    min_value=1.0,
    max_value=6.0,
    value=(1.0, 6.0),
    step=0.1
)

# データフィルタリング
filtered_df = df[
    (df["ブランド"].isin(selected_brands)) &
    (df["カテゴリ"].isin(selected_categories)) &
    (df["価格"] >= price_range[0]) &
    (df["価格"] <= price_range[1]) &
    (df["総合評価"] >= rating_range[0]) &
    (df["総合評価"] <= rating_range[1])
]

# メイン表示エリア
if not filtered_df.empty:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("商品数", len(filtered_df))
    with col2:
        st.metric("平均価格", f"¥{filtered_df['価格'].mean():.0f}")
    with col3:
        st.metric("平均評価", f"{filtered_df['総合評価'].mean():.1f}")
    with col4:
        st.metric("総口コミ数", f"{filtered_df['口コミ数'].sum()}")
    
    # タブで表示を切り替え
    tab1, tab2, tab3 = st.tabs(["📊 概要分析", "🔍 商品一覧", "💰 価格分析"])
    
    with tab1:
        st.subheader("ブランド別商品数")
        brand_counts = filtered_df["ブランド"].value_counts().head(10)
        fig1 = px.bar(
            x=brand_counts.index,
            y=brand_counts.values,
            title="ブランド別商品数 (上位10位)",
            labels={"x": "ブランド", "y": "商品数"}
        )
        fig1.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig1, use_container_width=True)
        
        st.subheader("カテゴリ別評価分布")
        fig2 = px.box(
            filtered_df,
            x="カテゴリ",
            y="総合評価",
            title="カテゴリ別評価分布"
        )
        fig2.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig2, use_container_width=True)
        
        st.subheader("価格帯別商品数")
        filtered_df_copy = filtered_df.copy()
        filtered_df_copy['価格帯'] = pd.cut(filtered_df_copy['価格'], bins=5, labels=['低価格', '中低価格', '中価格', '中高価格', '高価格'])
        price_counts = filtered_df_copy['価格帯'].value_counts()
        fig3 = px.pie(
            values=price_counts.values,
            names=price_counts.index,
            title="価格帯別商品数分布"
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab2:
        st.subheader("商品一覧")
        
        # 並び替えオプション
        sort_by = st.selectbox(
            "並び替え",
            ["価格（安い順）", "価格（高い順）", "評価（高い順）", "口コミ数（多い順）", "ランキング順"]
        )
        
        if sort_by == "価格（安い順）":
            display_df = filtered_df.sort_values("価格")
        elif sort_by == "価格（高い順）":
            display_df = filtered_df.sort_values("価格", ascending=False)
        elif sort_by == "評価（高い順）":
            display_df = filtered_df.sort_values("総合評価", ascending=False)
        elif sort_by == "口コミ数（多い順）":
            display_df = filtered_df.sort_values("口コミ数", ascending=False)
        else:
            display_df = filtered_df.sort_values("ランキング")
        
        # 商品表示
        for idx, row in display_df.head(20).iterrows():
            with st.container():
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    st.write(f"**{row['商品名']}**")
                    st.write(f"ブランド: {row['ブランド']} | カテゴリ: {row['カテゴリ']} | ランキング: {row['ランキング']}")
                    st.write(f"価格: ¥{row['価格']:,} | 発売日: {row['発売日']}")
                    st.write(f"⭐ {row['総合評価']:.1f} ({row['口コミ数']:.0f}件)")
                    if pd.notna(row['商品URL']):
                        st.write(f"[商品詳細]({row['商品URL']})")
                
                with col2:
                    st.metric("メーカー", row['メーカー'])
                    if pd.notna(row['注目人数']):
                        st.metric("注目人数", f"{row['注目人数']:.0f}")
                
                st.markdown("---")
    
    with tab3:
        st.subheader("価格 vs 評価")
        fig4 = px.scatter(
            filtered_df,
            x="価格",
            y="総合評価",
            color="カテゴリ",
            size="口コミ数",
            hover_data=['商品名', 'ブランド'],
            title="価格と評価の関係"
        )
        st.plotly_chart(fig4, use_container_width=True)
        
        st.subheader("コスパ分析")
        # コスパ指数計算（評価/価格×10000）
        filtered_df = filtered_df.copy()
        filtered_df["コスパ指数"] = (filtered_df["総合評価"] / filtered_df["価格"]) * 10000
        
        # 上位10位のコスパ商品
        top_cospa = filtered_df.nlargest(10, "コスパ指数")
        
        fig5 = px.bar(
            top_cospa,
            x="コスパ指数",
            y="商品名",
            orientation="h",
            title="コスパ上位10商品",
            hover_data=['価格', '総合評価']
        )
        st.plotly_chart(fig5, use_container_width=True)
        
        # ブランド別平均価格
        st.subheader("ブランド別平均価格")
        brand_avg_price = filtered_df.groupby('ブランド')['価格'].mean().sort_values(ascending=False).head(10)
        
        fig6 = px.bar(
            x=brand_avg_price.index,
            y=brand_avg_price.values,
            title="ブランド別平均価格 (上位10位)",
            labels={"x": "ブランド", "y": "平均価格 (円)"}
        )
        fig6.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig6, use_container_width=True)
else:
    st.info("選択した条件に該当する商品がありません。フィルタ条件を変更してください。")

st.markdown("---")
st.success("✅ 美容・コスメ商品比較ダッシュボードの解答例です。@cosmeのランキングデータを使用し、Plotlyを使った可視化機能を実装しています。") 