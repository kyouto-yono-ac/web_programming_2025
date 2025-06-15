# 第11回 授業概要：実践データ分析 (集計とランキング)

## 1. 基本情報
- **授業回:** 第11回
- **タイトル:** 実践データ分析 (集計とランキング)
- **時間:** 90分
- **形式:** 講義 + 演習
- **必要機材:**
    - **教員:** PC、プロジェクター
    - **学生:** PC (Google Colab, Streamlit実行環境)

## 2. 授業の目標
1. **第10回の補完**: `st.selectbox`で国を選んでデータを表示するアプリを作成できる
2. 複数条件でのデータフィルタリング（AND/OR条件）ができる
3. `groupby`を使ってデータを集計し、国別・年別の統計を計算できる
4. `sort_values`を使ってランキングを作成し、TOP10などの順位付けができる
5. `st.cache_data`を使ったStreamlitアプリの高速化ができる
6. インタラクティブなデータ分析アプリ（年選択→ランキング表示）を作成できる

## 3. タイムスケジュール
| 時間 | 内容 | 詳細 |
| --- | --- | --- |
| 10分 | 前回の復習とイントロダクション | 第10回の基本操作の復習、本日の目標説明 |
| 20分 | 第10回の補完：Streamlitとの基本連携 | `st.selectbox`で国を選んでデータ表示、`st.dataframe`の活用 |
| 20分 | 講義：複数条件フィルタリングとデータ集計 | AND/OR条件、`groupby`による集計処理 |
| 20分 | 講義：ランキング作成とStreamlit連携 | `sort_values`でのソート、`st.slider`との連携 |
| 15分 | 演習：インタラクティブ分析アプリの作成 | 年選択→国別TOP10表示アプリの実装 |
| 5分 | まとめと次回予告 | 本日の振り返り、次回（データ可視化）の予告 |

## 4. 授業内容の詳細

### 前回の復習とイントロダクション
- 第10回で学んだPandasの基本操作（`read_csv`, `head`, `info`, 単一条件フィルタ）の復習
- 本日完成させるアプリのデモンストレーション（第10回からの発展）

### 第10回の補完：Streamlitとの基本連携
- **目標:** `st.selectbox`で国を選んでデータを表示するアプリを完成させる
- **基本的なStreamlit連携:**
  - `st.dataframe()`でのデータ表示
  - `st.selectbox()`での国選択UI
  - 選択された国のデータフィルタリング
  - フィルタ結果の表示
- **実装例:**
  ```python
  import streamlit as st
  import pandas as pd
  
  df = pd.read_csv('visa_number_in_japan.csv')
  countries = df['Country'].unique()
  selected_country = st.selectbox('国を選択してください', countries)
  filtered_data = df[df['Country'] == selected_country]
  st.dataframe(filtered_data)
  ```

### 講義：複数条件フィルタリングとデータ集計
- **複数条件の指定方法:**
  - AND条件：`df[(df['Year'] == 2023) & (df['Country'] == 'China')]`
  - OR条件：`df[(df['Country'] == 'China') | (df['Country'] == 'Korea')]`
  - `isin()`メソッドの活用：`df[df['Country'].isin(['China', 'Korea'])]`
- **データ集計 (`groupby`):**
  - 国別の合計発行数：`df.groupby('Country')['Number of issued_numerical'].sum()`
  - 年・国別の集計：`df.groupby(['Year', 'Country'])['Number of issued_numerical'].sum()`
  - 集計結果のDataFrameへの変換：`.reset_index()`

### 講義：ランキング作成とStreamlit連携
- **ランキング作成 (`sort_values`):**
  - 降順ソート：`df.sort_values('Number of issued_numerical', ascending=False)`
  - TOP10の抽出：`.head(10)`
- **Streamlitとの連携:**
  - `st.slider`で年を選択
  - `st.selectbox`で表示する上位件数を選択
  - `st.dataframe`で結果を表示
- **パフォーマンス向上:**
  - `st.cache_data`を使ったデータ読み込みの高速化

### 演習：インタラクティブ分析アプリの作成
- **段階的な実装:**
  1. 基本版：`st.selectbox`で国を選んでデータ表示（第10回の補完）
  2. 発展版：`st.slider`で年を選択→その年の国別TOP10を表示
- **実装手順:**
  1. データの読み込みと前処理（`st.cache_data`使用）
  2. `st.slider`での年選択UI
  3. 選択された年でのデータフィルタリング
  4. 国別集計とランキング作成
  5. `st.dataframe`での結果表示
- **発展課題:** 複数年の比較、特定地域のフィルタリングなど

## 5. 準備物
- **教員側:**
  - `11_lecture.ipynb` (講義用Colabノートブック)
  - `visa_number_in_japan.csv` (ビザ発行データ)
  - 完成版のStreamlitアプリデモ
- **学生側:**
  - PC、Googleアカウント
  - 前回アップロードした`visa_number_in_japan.csv`

## 6. 配布資料
- `lectures/11_実践データ分析_Pandas/11_lecture.ipynb`
- `lectures/11_実践データ分析_Pandas/11_exercises.ipynb`
- `src/lecture11/app_ranking.py` (演習用Streamlitアプリ)
- `src/lecture11/app_ranking_a.py` (解答用Streamlitアプリ)

## 7. 次回予告
- 第12回: データ可視化 (グラフ作成)
- 今回作成したランキングデータを、`st.line_chart`、`st.bar_chart`、Plotly Expressを使って視覚的に表現します。複数国の時系列比較グラフや、インタラクティブなグラフ作成を学びます。

## 8. 使用するデータとライブラリ
- **データセット:** `visa_number_in_japan.csv` (第10回と同じ)
- **主要なライブラリ:**
  - `pandas` (データ処理)
  - `streamlit` (Web UI)
- **新しく学ぶ主要な関数/メソッド:**
  - 複数条件：`&`, `|`, `isin()`
  - 集計：`groupby()`, `sum()`, `count()`, `mean()`
  - ソート：`sort_values()`
  - Streamlit：`st.cache_data`, `st.slider`, `st.selectbox` 