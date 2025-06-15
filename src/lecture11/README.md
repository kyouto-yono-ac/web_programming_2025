# 第11回演習：実践データ分析 - Streamlitアプリ

## 📁 ファイル構成

- `app_ranking.py` - **演習用テンプレート**（学生が完成させる）
- `app_answer.py` - **解答版**（講師用・最終確認用）

## 🎯 演習の流れ

### Part 1: 基本演習（10-15分）
`app_ranking.py`を使用して、第10回の補完を行います。

1. **国選択機能の実装**
   - `st.selectbox`で国を選択
   - 選択された国のデータをフィルタリング
   - `st.dataframe`で結果を表示

### Part 2: 発展演習（15-20分）
年別ランキング機能を実装します。

1. **年選択機能の追加**
   - `st.slider`で年を選択
   - 選択された年のデータを取得

2. **ランキング作成**
   - `groupby()`で国別集計
   - `sort_values()`でランキング作成
   - TOP10を表示

## 🚀 実行方法

### 1. 演習用アプリの実行
```bash
cd src/lecture11
streamlit run app_ranking.py
```

### 2. 解答版アプリの実行
```bash
cd src/lecture11
streamlit run app_answer.py
```

## 📚 学習ポイント

### Streamlitの基本操作
- `st.selectbox()` - 選択肢から1つを選ぶ
- `st.slider()` - 数値範囲から値を選ぶ
- `st.dataframe()` - データフレームの表示
- `st.bar_chart()` - 簡単な棒グラフ

### Pandasの集計操作
- `df.groupby()` - グループ化
- `.sum()` - 合計値の計算
- `.sort_values()` - 並び替え
- `.head()` - 上位N件の取得

### データフィルタリング
- `df[df['列名'] == 値]` - 条件フィルタ
- `df['列名'].unique()` - ユニークな値の取得

## 💡 演習のヒント

### 国別データの取得
```python
# 国のリストを取得
countries = df['Country'].unique()

# 選択された国のデータをフィルタ
filtered_data = df[df['Country'] == selected_country]
```

### 年別ランキングの作成
```python
# その年のデータを取得
year_data = df[df['Year'] == selected_year]

# 国別合計を計算
country_totals = year_data.groupby('Country')['Number of issued_numerical'].sum()

# 降順でソートしてTOP10を取得
top10 = country_totals.sort_values(ascending=False).head(10)
```

## 🔧 トラブルシューティング

### よくあるエラー

1. **ModuleNotFoundError: No module named 'streamlit'**
   ```bash
   pip install streamlit
   ```

2. **FileNotFoundError: visa_number_in_japan.csv**
   - CSVファイルが同じディレクトリにあることを確認
   - Google Colabの場合は適切にアップロード

3. **SyntaxError**
   - コメントアウトされた行を確認
   - `# ここを埋めよう！` の部分を適切なコードに置き換え

## 📋 チェックリスト

### 演習完了の確認
- [ ] 国を選択すると該当国のデータが表示される
- [ ] 年スライダーを動かすとランキングが更新される
- [ ] TOP10が正しく表示される
- [ ] グラフが適切に表示される

### 学習目標の達成確認
- [ ] `st.selectbox`の基本的な使い方を理解した
- [ ] `groupby()`による集計ができる
- [ ] `sort_values()`による並び替えができる
- [ ] 条件フィルタリングができる 