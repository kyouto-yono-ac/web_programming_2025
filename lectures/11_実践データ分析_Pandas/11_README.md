# 第11回 授業概要：データ処理・分析・可視化の総合実践 (Pandas)

## 1. 基本情報
- **授業回:** 第11回
- **タイトル:** データ処理・分析・可視化の総合実践 (Pandas)
- **時間:** 90分
- **形式:** 講義 + 演習
- **必要機材:**
    - **教員:** PC、プロジェクター
    - **学生:** PC (Google Colab, Streamlit実行環境)

## 2. 授業の目標
### 🎯 最終的な成果物
**「インタラクティブなビザ発行数分析ダッシュボード」**
- データの読み込み・加工・集計・ランキング
- 様々なグラフによる可視化
- ユーザーが操作できるWebアプリケーション

### 具体的な学習目標
1. **Pandasの基礎**: CSVファイルの読み込み、データの基本操作
2. **データ分析**: 集計、フィルタリング、ランキング作成
3. **Streamlit連携**: インタラクティブなUI作成
4. **データ可視化**: 複数のグラフタイプによる表現
5. **総合的なダッシュボード**: 全機能を統合したアプリケーション

## 3. タイムスケジュール（90分）
| 時間 | 内容 | 詳細 |
| --- | --- | --- |
| 5分 | イントロダクション | 本日完成させるアプリのデモ、ゴール説明 |
| 15分 | **Part 1: Pandas基礎** | データ読み込み、基本操作、シンプルなフィルタリング |
| 20分 | **Part 2: データ分析** | 複数条件、集計（groupby）、ランキング作成 |
| 20分 | **Part 3: Streamlit連携** | selectbox、slider、基本的なインタラクティブUI |
| 20分 | **Part 4: データ可視化** | 基本グラフ、Plotly Express、インタラクティブグラフ |
| 8分 | **Part 5: 総合ダッシュボード作成** | 全機能を統合した最終アプリ |
| 2分 | まとめと振り返り | 作成物の確認、次回予告 |

## 4. 授業内容の詳細

### イントロダクション（5分）
- **完成版アプリのデモンストレーション**
  - 年選択 → 国別ランキング表示
  - 複数国選択 → 時系列グラフ比較
  - 様々なグラフタイプの切り替え
- **本日のロードマップ説明**

### Part 1: Pandas基礎（15分）
#### 目標：データをプログラムに読み込み、基本操作ができる

**1-1. 環境準備とデータ読み込み（5分）**
```python
import pandas as pd
import streamlit as st

# CSVファイルの読み込み
df = pd.read_csv('visa_number_in_japan.csv')
```

**1-2. データの観察（5分）**
```python
# データの概要を把握
df.head()      # 最初の5行
df.info()      # データ型と欠損値の確認
df.shape       # 行数と列数
```

**1-3. 基本的なフィルタリング（5分）**
```python
# 単一条件でのデータ抽出
china_data = df[df['Country'] == 'China']
year_2023 = df[df['Year'] == 2023]
```

### Part 2: データ分析（20分）
#### 目標：複雑な条件でのデータ抽出と集計ができる

**2-1. 複数条件フィルタリング（8分）**
```python
# AND条件
china_2023 = df[(df['Country'] == 'China') & (df['Year'] == 2023)]

# OR条件
china_or_korea = df[(df['Country'] == 'China') | (df['Country'] == 'Korea')]

# isin()を使った複数選択
selected_countries = df[df['Country'].isin(['China', 'Korea', 'United States'])]
```

**2-2. データ集計（groupby）（7分）**
```python
# 国別の合計発行数
country_totals = df.groupby('Country')['Number of issued_numerical'].sum()

# 年別の合計発行数
yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()

# 年・国別の集計
year_country_totals = df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum()
```

**2-3. ランキング作成（5分）**
```python
# 国別ランキング（降順）
country_ranking = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False)

# TOP10の抽出
top10_countries = country_ranking.head(10)
```

### Part 3: Streamlit連携（20分）
#### 目標：データ分析結果をインタラクティブなWebアプリにする

**3-1. 基本的なUI要素（8分）**
```python
# セレクトボックス
countries = df['Country'].unique()
selected_country = st.selectbox('国を選択', countries)

# スライダー
selected_year = st.slider('年を選択', 
                         min_value=int(df['Year'].min()), 
                         max_value=int(df['Year'].max()), 
                         value=2023)

# マルチセレクト
selected_countries = st.multiselect('複数国を選択', countries, default=['China', 'Korea'])
```

**3-2. インタラクティブなデータ表示（7分）**
```python
# 選択された年のデータを表示
year_data = df[df['Year'] == selected_year]
st.dataframe(year_data)

# 選択された国のデータを表示
country_data = df[df['Country'] == selected_country]
st.dataframe(country_data)
```

**3-3. パフォーマンス最適化（5分）**
```python
# データキャッシュで高速化
@st.cache_data
def load_data():
    return pd.read_csv('visa_number_in_japan.csv')

df = load_data()
```

### Part 4: データ可視化（20分）
#### 目標：データを視覚的に分かりやすく表現する

**4-1. Streamlitの基本グラフ（7分）**
```python
# 年別推移の折れ線グラフ
yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()
st.line_chart(yearly_totals)

# 国別ランキングの棒グラフ
top10_2023 = df[df['Year'] == 2023].groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top10_2023)
```

**4-2. Plotly Expressによる高度なグラフ（10分）**
```python
import plotly.express as px

# インタラクティブな折れ線グラフ
fig_line = px.line(df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index(),
                   x='Year', y='Number of issued_numerical', color='Country',
                   title='国別年次推移')
st.plotly_chart(fig_line)

# 円グラフ
top10_data = df[df['Year'] == 2023].groupby('Country')['Number of issued_numerical'].sum().head(10).reset_index()
fig_pie = px.pie(top10_data, values='Number of issued_numerical', names='Country',
                 title='2023年 国別構成比')
st.plotly_chart(fig_pie)
```

**4-3. 複数国の時系列比較（3分）**
```python
# ユーザーが選択した複数国の推移を表示
selected_countries = st.multiselect('比較したい国を選択', countries, default=['China', 'Korea'])
filtered_data = df[df['Country'].isin(selected_countries)]
comparison_data = filtered_data.groupby(['Year', 'Country'])['Number of issued_numerical'].sum().reset_index()

fig_comparison = px.line(comparison_data, x='Year', y='Number of issued_numerical', 
                        color='Country', title='選択国の年次推移比較')
st.plotly_chart(fig_comparison)
```

### Part 5: 総合ダッシュボード作成（8分）
#### 目標：全機能を統合した完成版アプリケーション

**統合アプリの構成**
1. **サイドバーでの操作パネル**
2. **メインエリアでの結果表示**
3. **複数のタブによる機能分け**

```python
# サイドバー
st.sidebar.header('設定パネル')
selected_year = st.sidebar.slider('年を選択', 2015, 2023, 2023)
selected_countries = st.sidebar.multiselect('国を選択', countries, default=['China', 'Korea'])

# タブによる機能分け
tab1, tab2, tab3 = st.tabs(['📊 ランキング', '📈 時系列比較', '🥧 構成比'])

with tab1:
    # 年別ランキング表示
    
with tab2:
    # 複数国の時系列比較
    
with tab3:
    # 円グラフによる構成比表示
```

## 5. 使用技術・ライブラリ

### 主要ライブラリ
- **pandas**: データ処理・分析
- **streamlit**: Webアプリケーション構築
- **plotly.express**: 高度なデータ可視化

### 重要な関数・メソッド
#### Pandas
- `pd.read_csv()` - データ読み込み
- `df.head()`, `df.info()` - データ観察
- `df[条件式]` - フィルタリング
- `df.groupby()` - データ集計
- `df.sort_values()` - ソート

#### Streamlit
- `st.selectbox()`, `st.multiselect()` - 選択UI
- `st.slider()` - 数値選択UI
- `st.dataframe()` - データ表示
- `st.line_chart()`, `st.bar_chart()` - 基本グラフ
- `st.plotly_chart()` - Plotlyグラフ表示
- `st.cache_data` - パフォーマンス最適化

#### Plotly Express
- `px.line()` - 折れ線グラフ
- `px.bar()` - 棒グラフ
- `px.pie()` - 円グラフ
- `px.scatter()` - 散布図

## 6. 準備物
### 教員側
- `11_lecture.ipynb` (講義用Colabノートブック)
- `visa_number_in_japan.csv` (ビザ発行データ)
- 完成版Streamlitアプリのデモ
- 段階別の中間版アプリ

### 学生側
- PC、Googleアカウント
- `visa_number_in_japan.csv` のダウンロード準備

## 7. 配布資料
- `lectures/11_実践データ分析_Pandas/11_lecture.ipynb`
- `lectures/11_実践データ分析_Pandas/11_exercises.ipynb`
- `src/lecture11/app_dashboard.py` (最終版統合アプリ)
- `src/lecture11/app_step1.py` (Part1用基礎アプリ)
- `src/lecture11/app_step2.py` (Part2用分析アプリ)
- `src/lecture11/app_step3.py` (Part3用UI統合アプリ)
- `src/lecture11/app_step4.py` (Part4用可視化アプリ)

## 8. 期待される成果物

### 基本達成目標
1. **データ読み込み・観察**: CSVファイルを読み込み、基本情報を把握
2. **フィルタリング**: 単一・複数条件でのデータ抽出
3. **集計・ランキング**: groupbyによる集計とソート
4. **基本的なStreamlitアプリ**: selectbox、sliderを使ったUI
5. **基本グラフ**: line_chart、bar_chartによる可視化

### 発展達成目標
1. **高度な可視化**: Plotly Expressによるインタラクティブグラフ
2. **複数国比較**: multiselectによる動的な比較分析
3. **統合ダッシュボード**: タブ機能を使った多機能アプリ
4. **パフォーマンス最適化**: cache_dataによる高速化

### 最終成果物
**「ビザ発行数分析ダッシュボード」**
- 年選択によるランキング表示
- 複数国選択による時系列比較
- 様々なグラフタイプでの可視化
- 直感的で美しいユーザーインターフェース

## 9. 学習効果を高めるポイント

### 段階的な実装
1. **小さく始める**: 最初は単純な機能から
2. **徐々に拡張**: 各Partで機能を追加
3. **統合して完成**: 最後に全機能を組み合わせ

### 実践的な学習
- **実際のデータ使用**: 日本政府の公開データを活用
- **実用的なアプリ作成**: 実際に使える分析ツール
- **視覚的な理解**: グラフによる直感的な把握

### 次回以降への接続
- 本授業で作成したダッシュボードは、今後の授業でも拡張可能
- 他のデータセットでも同じ手法が応用可能
- データサイエンスの基礎スキルとして活用可能 