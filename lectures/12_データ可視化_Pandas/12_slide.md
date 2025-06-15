---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第12回：データ可視化（グラフ作成）"
size: 16:9
style: |
  section { font-size: 1.4em; }
  h1 { font-size: 2.0em; }
  h2 { font-size: 1.7em; }
  h3 { font-size: 1.5em; }
  code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 0.9em;
    background-color: #f0f0f0;
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
  pre code {
    display: block;
    padding: 0.5em;
    overflow-x: auto;
    font-size: 0.8em;
  }
  .lead h1 {
    font-size: 2.8em;
  }
  .lead h2 {
    font-size: 2.0em;
  }
  .lead p {
    font-size: 1.6em;
  }
---

<!-- _class: lead -->

# 第12回
## データ可視化（グラフ作成）

出席認証コード: **4827**

---

## 本日の流れ

1. **前回の復習とイントロダクション** (約10分)
2. **Streamlitの基本グラフ機能** (約20分)
   - `st.line_chart`, `st.bar_chart`, `st.area_chart`
3. **Plotly Expressによる高度なグラフ** (約25分)
   - `px.line`, `px.bar`, `px.scatter`, `px.pie`
4. **複数国の時系列比較** (約20分)
   - `st.multiselect`による複数選択
5. **総合演習：可視化ダッシュボード** (約10分)
6. **まとめと次回予告** (約5分)

---

## 1. 前回の復習とイントロダクション

### 第11回で学んだこと
- データの**集計**：`groupby()`で国別・年別の統計
- **ランキング作成**：`sort_values()`でTOP10抽出
- **Streamlit連携**：`st.selectbox`, `st.slider`でインタラクティブUI
- **パフォーマンス向上**：`st.cache_data`でデータキャッシュ

### 今日のゴール
データ集計結果 → **視覚的に美しいグラフ** → **理解しやすい情報伝達**

---

### なぜグラフが重要？データ可視化の意義

**数字の羅列** vs **グラフによる視覚化**

| 年 | 中国 | 韓国 | アメリカ |
|----|------|------|----------|
| 2019 | 432,879 | 89,045 | 145,323 |
| 2020 | 156,789 | 45,623 | 98,456 |
| 2021 | 278,234 | 67,891 | 123,789 |

↓ **グラフ化すると...**

一目で**トレンド**、**比較**、**パターン**が分かる！

---

## 2. Streamlitの基本グラフ機能 (20分)

### 基本的な3つのグラフタイプ

**折れ線グラフ（時系列データの推移）**
```python
st.line_chart(data)
```

**棒グラフ（カテゴリ別の比較）**
```python
st.bar_chart(data)
```

**面グラフ（累積値の変化）**
```python
st.area_chart(data)
```

---

### 実例：年別総ビザ発行数の推移

```python
import streamlit as st
import pandas as pd

# データの読み込み
df = pd.read_csv('visa_number_in_japan.csv')

# 年別集計
yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()

# 折れ線グラフで表示
st.line_chart(yearly_totals)
```

**ポイント**：
- データは自動的にインデックス（年）をX軸、値をY軸とする
- シンプルで高速
- 基本的な見た目で十分な場合に最適

---

### 演習：第11回のランキング結果をグラフ化

```python
# 2023年の国別TOP10をグラフ化
year_2023 = df[df['Year'] == 2023]
top10_2023 = year_2023.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)

# 棒グラフで表示
st.bar_chart(top10_2023)
```

`12_lecture.ipynb`を開いて実際にやってみましょう！

---

## 3. Plotly Expressによる高度なグラフ (25分)

### Plotly Expressとは？
- **より美しく**、**カスタマイズ性の高い**グラフライブラリ
- **インタラクティブ機能**（ズーム、パン、ホバー）
- **豊富なグラフタイプ**

### インストールと基本的な使い方
```python
# Colabでのインストール
!pip install plotly

# インポート
import plotly.express as px

# Streamlitでの表示
st.plotly_chart(fig)
```

---

### 主要なPlotly Expressのグラフタイプ

**折れ線グラフ**
```python
fig = px.line(data, x='Year', y='Count', color='Country')
st.plotly_chart(fig)
```

**棒グラフ**
```python
fig = px.bar(data, x='Country', y='Count', title='国別ランキング')
st.plotly_chart(fig)
```

**円グラフ**
```python
fig = px.pie(data, values='Count', names='Country')
st.plotly_chart(fig)
```

---

### Plotlyの強力な機能

**1. インタラクティブ操作**
- マウスホイールでズーム
- ドラッグでパン（移動）
- ホバーで詳細情報表示

**2. 美しいデザイン**
- 自動的な色分け
- プロフェッショナルな見た目
- カスタマイズ可能

**3. 豊富なオプション**
- タイトル、軸ラベル
- 凡例の位置
- 色の指定

---

### 実例：複数国の年別推移（Plotly版）

```python
# 上位5カ国の年別推移データを準備
top_countries = ['China', 'Korea', 'United States', 'Thailand', 'Vietnam']
filtered_df = df[df['Country'].isin(top_countries)]
yearly_by_country = filtered_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()

# Plotlyで折れ線グラフ作成
fig = px.line(yearly_by_country, 
             x='Year', 
             y='Number of issued_numerical', 
             color='Country',
             title='上位5カ国の年別ビザ発行数推移',
             markers=True)

st.plotly_chart(fig, use_container_width=True)
```

---

## 4. 複数国の時系列比較 (20分)

### 目標：ユーザーが国を選んで比較できるアプリ

**主要機能**：
1. `st.multiselect`で複数国を選択
2. 選択された国々の年別推移を同時表示
3. 色分けで区別、凡例で識別

### ステップ1：国選択UI

```python
# 国のリスト取得
all_countries = sorted(df['Country'].unique())

# 複数選択UI
selected_countries = st.multiselect(
    '比較する国を選択してください（複数選択可）:',
    all_countries,
    default=['China', 'Korea', 'United States']  # デフォルト選択
)
```

---

### ステップ2：選択された国のデータ準備

```python
if selected_countries:  # 国が選択されている場合のみ
    # 選択された国のデータをフィルタ
    filtered_df = df[df['Country'].isin(selected_countries)]
    
    # 年・国別に集計
    comparison_data = filtered_df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()
    
    # Plotlyグラフ作成
    fig = px.line(comparison_data, 
                 x='Year', 
                 y='Number of issued_numerical', 
                 color='Country',
                 title='選択した国々の年別推移比較',
                 markers=True)
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("比較する国を選択してください")
```

---

### さらなる機能追加

**グラフタイプの選択**
```python
chart_type = st.selectbox('グラフタイプを選択:', ['折れ線グラフ', '棒グラフ', '面グラフ'])

if chart_type == '折れ線グラフ':
    fig = px.line(data, x='Year', y='Count', color='Country')
elif chart_type == '棒グラフ':
    fig = px.bar(data, x='Year', y='Count', color='Country')
else:  # 面グラフ
    fig = px.area(data, x='Year', y='Count', color='Country')
```

**年の範囲選択**
```python
year_range = st.slider('年の範囲を選択:', 
                      min_value=int(df['Year'].min()),
                      max_value=int(df['Year'].max()),
                      value=(2019, 2023))
```

---

## 5. 総合演習：可視化ダッシュボード (10分)

### 目標：様々なグラフを組み合わせた総合的なダッシュボード

**組み合わせる要素**：
- 全体の年別推移（折れ線）
- 特定年のランキング（棒グラフ）
- 地域別分布（円グラフ）
- 複数国比較（インタラクティブ）

### レイアウトの工夫

```python
# 2列レイアウト
col1, col2 = st.columns(2)

with col1:
    st.subheader('📈 年別推移')
    st.line_chart(yearly_data)

with col2:
    st.subheader('🏆 国別ランキング')
    st.bar_chart(ranking_data)
```

---

### 演習：統合ダッシュボードの作成
`12_lecture.ipynb`の最終セクションで実装します。

**含める機能**：
1. **概要セクション** - 基本統計情報
2. **推移グラフ** - 年別全体トレンド
3. **ランキング** - インタラクティブな年選択
4. **比較分析** - 複数国の同時比較
5. **詳細分析** - 地域別・カテゴリ別

---

## Plotlyのグラフカスタマイズ

### 基本的なカスタマイズ

```python
fig = px.line(data, x='Year', y='Count', color='Country')

# タイトルと軸ラベル
fig.update_layout(
    title='ビザ発行数の年別推移',
    xaxis_title='年',
    yaxis_title='ビザ発行数',
    legend_title='国名'
)

# 軸の書式設定
fig.update_yaxis(tickformat=',')  # 数字にカンマ
```

### 色とスタイルの調整

```python
# カスタム色の指定
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
fig.update_traces(line=dict(width=3))

# 背景色
fig.update_layout(plot_bgcolor='white')
```

---

## データ可視化のベストプラクティス

### 1. 適切なグラフタイプの選択
- **時系列データ** → 折れ線グラフ
- **カテゴリ比較** → 棒グラフ
- **構成比** → 円グラフ
- **相関関係** → 散布図

### 2. 色使いの原則
- **意味のある色分け**（例：国ごとに固定色）
- **カラーバリアフリー**への配慮
- **背景との十分なコントラスト**

### 3. 情報の階層化
- **最も重要な情報**を目立たせる
- **詳細情報**はホバーやクリックで表示
- **説明文**は簡潔に

---

## 6. まとめと次回予告

### 本日のまとめ
- **Streamlitの基本グラフ**: `st.line_chart`, `st.bar_chart`, `st.area_chart`
- **Plotly Express**: より美しく高機能なグラフ作成
- **インタラクティブ機能**: ズーム、パン、ホバー情報
- **複数国比較**: `st.multiselect`による動的な比較分析
- **総合ダッシュボード**: 様々なグラフの効果的な組み合わせ

### 今日学んだ主要な関数・メソッド
- グラフ作成：`px.line()`, `px.bar()`, `px.pie()`, `px.scatter()`
- 表示：`st.plotly_chart()`
- UI：`st.multiselect()`, `st.selectbox()`
- カスタマイズ：`fig.update_layout()`, `fig.update_traces()`

---

### 次回予告: 第13回 総合演習・アプリ開発
- **総合プロジェクト**: これまでの知識を統合した本格的なWebアプリ開発
- **ユーザーインターフェース**: より洗練されたUI/UXデザイン
- **データ分析ワークフロー**: データ取得→処理→分析→可視化の完全な流れ
- **デプロイメント**: 作成したアプリを実際にWeb上で公開

第10-12回で学んだ全ての技術を組み合わせて、実用的なデータ分析アプリケーションを完成させます！

---

<!-- _class: lead -->

## Q & A

質疑応答

お疲れ様でした！ 