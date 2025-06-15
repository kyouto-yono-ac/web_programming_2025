---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第11回：実践データ分析 (集計とランキング)"
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

# 第11回
## 実践データ分析 (集計とランキング)

出席認証コード: **6549**

---

## 本日の流れ

1. **前回の復習とイントロダクション** (約10分)
2. **第10回の補完：Streamlitとの基本連携** (約20分)
   - `st.selectbox`で国を選んでデータ表示
3. **講義：複数条件フィルタリングとデータ集計** (約20分)
   - AND/OR条件、`groupby`による集計
4. **講義：ランキング作成とStreamlit連携** (約20分)
   - `sort_values`でのソート、`st.slider`との連携
5. **演習：インタラクティブ分析アプリの作成** (約15分)
6. **まとめと次回予告** (約5分)

---

## 1. 前回の復習とイントロダクション

### 第10回で学んだこと
- Pandasライブラリの基本：`import pandas as pd`
- CSVファイルの読み込み：`pd.read_csv()`
- データの観察：`df.head()`, `df.info()`
- 基本的なフィルタリング：`df[df['Country'] == 'China']`

### 本日のゴール
第10回の基本操作 → **Streamlitアプリ** → **高度な分析** → **ランキング作成**

---

## 2. 第10回の補完：Streamlitとの基本連携 (20分)

### 目標：`st.selectbox`で国を選んでデータ表示

```python
import streamlit as st
import pandas as pd

# データの読み込み
df = pd.read_csv('visa_number_in_japan.csv')

# 国のリストを取得
countries = df['Country'].unique()

# セレクトボックスで国を選択
selected_country = st.selectbox('国を選択してください', countries)

# 選択された国のデータをフィルタリング
filtered_data = df[df['Country'] == selected_country]

# 結果を表示
st.dataframe(filtered_data)
```

---

### Colabで演習：基本的なStreamlit連携
`11_lecture.ipynb`を開いてください。

**Step 1: 基本アプリの作成**
- データ読み込み
- `st.selectbox`での国選択
- `st.dataframe`での表示

**Step 2: 動作確認**
- 異なる国を選択してデータが変わることを確認
- データの内容を観察

---

## 3. 講義：複数条件フィルタリングとデータ集計 (20分)

### 複数条件の指定方法

**AND条件（両方の条件を満たす）**
```python
# 2023年かつ中国のデータ
df_china_2023 = df[(df['Year'] == 2023) & (df['Country'] == 'China')]
```

**OR条件（いずれかの条件を満たす）**
```python
# 中国または韓国のデータ
df_china_or_korea = df[(df['Country'] == 'China') | (df['Country'] == 'Korea')]
```

**`isin()`メソッド（複数の値のいずれかに一致）**
```python
# 中国、韓国、アメリカのいずれかのデータ
countries_list = ['China', 'Korea', 'United States']
df_selected = df[df['Country'].isin(countries_list)]
```

---

### データ集計 (`groupby`)

**国別の合計発行数**
```python
country_totals = df.groupby('Country')['Number of issued_numerical'].sum()
print(country_totals.head())
```

**年・国別の集計**
```python
year_country_totals = df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum()
```

**集計結果をDataFrameに変換**
```python
summary_df = df.groupby('Country')['Number of issued_numerical'].sum().reset_index()
```

---

## 4. 講義：ランキング作成とStreamlit連携 (20分)

### ランキング作成 (`sort_values`)

**降順ソート（多い順）**
```python
ranking = df.sort_values('Number of issued_numerical', ascending=False)
```

**TOP10の抽出**
```python
top10 = ranking.head(10)
```

**国別合計でのランキング**
```python
country_ranking = df.groupby('Country')['Number of issued_numerical'].sum().sort_values(ascending=False).head(10)
```

---

### Streamlitとの連携

**年選択スライダー**
```python
selected_year = st.slider('年を選択', 
                         min_value=int(df['Year'].min()), 
                         max_value=int(df['Year'].max()), 
                         value=2023)
```

**選択された年のTOP10表示**
```python
# その年のデータをフィルタ
year_data = df[df['Year'] == selected_year]

# 国別集計
country_totals = year_data.groupby('Country')['Number of issued_numerical'].sum()

# TOP10作成
top10 = country_totals.sort_values(ascending=False).head(10).reset_index()

# 結果表示
st.dataframe(top10)
```

---

### パフォーマンス向上：`st.cache_data`

```python
@st.cache_data  # データの読み込みを高速化
def load_data():
    return pd.read_csv('visa_number_in_japan.csv')

df = load_data()  # キャッシュされたデータを使用
```

- 初回読み込み後はメモリにキャッシュ
- アプリの動作が高速化
- データが変更されない限り再読み込みしない

---

## 5. 演習：インタラクティブ分析アプリの作成 (15分)

### 段階的な実装

**Step 1: 基本版（第10回の補完）**
`st.selectbox`で国を選んでデータ表示

**Step 2: 発展版**
`st.slider`で年を選択→その年の国別TOP10を表示

### 実装手順
1. データの読み込み（`st.cache_data`使用）
2. `st.slider`での年選択UI
3. 選択された年でのデータフィルタリング
4. 国別集計とランキング作成
5. `st.dataframe`での結果表示

---

### Colabで演習：ランキングアプリの作成
`11_lecture.ipynb`の続きです。

**完成形のイメージ:**
- 年をスライダーで選択（例：2019〜2023）
- その年の国別ビザ発行数TOP10を自動表示
- リアルタイムで結果が更新される

**発展課題:**
- 表示件数を選択可能にする（TOP5, TOP10, TOP20）
- 特定地域のみのランキング
- 複数年の比較表示

---

## 6. まとめと次回予告

### 本日のまとめ
- **第10回の補完**: `st.selectbox`での基本的なStreamlit連携を完成
- **複数条件フィルタリング**: AND/OR条件、`isin()`メソッド
- **データ集計**: `groupby()`を使った国別・年別の統計
- **ランキング作成**: `sort_values()`でのソート、TOP10抽出
- **高速化**: `st.cache_data`によるパフォーマンス向上

### 今日学んだ主要な関数・メソッド
- 複数条件：`&`, `|`, `isin()`
- 集計：`groupby()`, `sum()`, `reset_index()`
- ソート：`sort_values()`, `head()`
- Streamlit：`st.cache_data`, `st.slider`, `st.selectbox`

---

### 次回予告: 第12回 データ可視化 (グラフ作成)
- **グラフ作成**: `st.line_chart`, `st.bar_chart`での可視化
- **Plotly Express**: より高度でインタラクティブなグラフ
- **時系列分析**: 複数国の時系列比較グラフ
- **総合アプリ**: `st.multiselect`で複数国を選んでグラフ比較

今回作成したランキングデータを、視覚的に美しいグラフで表現します！

---

<!-- _class: lead -->

## Q & A

質疑応答

お疲れ様でした！ 