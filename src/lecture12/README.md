# 第12回演習：データ可視化 - Streamlitアプリ

## 📁 ファイル構成

- `app_visualization.py` - **演習用テンプレート**（学生が完成させる）
- `app_answer.py` - **解答版**（講師用・最終確認用）

## 🎯 演習の流れ

### Part 1: Streamlitの基本グラフ（15分）
基本的なグラフ機能を学習します。

1. **折れ線グラフ**
   - `st.line_chart()`で年別推移を表示
   - 時系列データの可視化

2. **棒グラフ**
   - `st.bar_chart()`で国別ランキングを表示
   - カテゴリ別比較の可視化

### Part 2: Plotly Expressによる高度なグラフ（20分）
より美しく、インタラクティブなグラフを作成します。

1. **折れ線グラフの強化**
   - `px.line()`で複数国の比較
   - ホバー情報、ズーム、パン機能

2. **グラフのカスタマイズ**
   - タイトル、軸ラベルの設定
   - 色分けと凡例

### Part 3: 複数国の動的比較（15分）
ユーザーインタラクションを追加します。

1. **国選択機能**
   - `st.multiselect()`で複数国を選択
   - 動的なデータフィルタリング

2. **グラフタイプの切替**
   - 折れ線、棒グラフ、面グラフの選択
   - 同一データの異なる表現

### Part 4: 円グラフによる構成比（10分）
構成比を視覚的に表現します。

1. **円グラフの作成**
   - `px.pie()`で構成比を表示
   - 年選択機能との連携

## 🚀 実行方法

### 1. 演習用アプリの実行
```bash
cd src/lecture12
streamlit run app_visualization.py
```

### 2. 解答版アプリの実行
```bash
cd src/lecture12
streamlit run app_answer.py
```

## 📚 学習ポイント

### Streamlitの基本グラフ
- `st.line_chart()` - 時系列データの推移
- `st.bar_chart()` - カテゴリ別の比較
- `st.area_chart()` - 累積値の変化

### Plotly Expressの機能
- `px.line()` - カスタマイズ可能な折れ線グラフ
- `px.bar()` - 高度な棒グラフ
- `px.pie()` - 円グラフ
- `px.scatter()` - 散布図
- `st.plotly_chart()` - Plotlyグラフの表示

### インタラクティブ機能
- マウスホイールでズーム
- ドラッグでパン（移動）
- ホバーで詳細情報表示
- 凡例クリックで系列の表示/非表示

### UI要素
- `st.multiselect()` - 複数選択
- `st.selectbox()` - 単一選択
- `st.slider()` - 数値範囲選択
- `st.checkbox()` - オプション選択

## 💡 演習のヒント

### 基本グラフの作成
```python
# データの集計
yearly_totals = df.groupby('Year')['Number of issued_numerical'].sum()

# 折れ線グラフで表示
st.line_chart(yearly_totals)
```

### Plotlyグラフの作成
```python
# Plotlyで折れ線グラフ作成
fig = px.line(data, x='Year', y='Count', color='Country')

# カスタマイズ
fig.update_layout(title='タイトル', xaxis_title='X軸', yaxis_title='Y軸')

# Streamlitで表示
st.plotly_chart(fig, use_container_width=True)
```

### 複数国選択機能
```python
# 複数選択UI
selected_countries = st.multiselect('国を選択:', all_countries)

# 選択された国でフィルタ
if selected_countries:
    filtered_df = df[df['Country'].isin(selected_countries)]
```

## 🔧 トラブルシューティング

### よくあるエラー

1. **ModuleNotFoundError: No module named 'plotly'**
   ```bash
   pip install plotly
   ```

2. **グラフが表示されない**
   - データの形式を確認
   - 列名が正しいかチェック
   - データが空でないか確認

3. **Plotlyグラフのエラー**
   - `st.plotly_chart(fig)`の形式を確認
   - `use_container_width=True`の追加

### デバッグのコツ

1. **データの確認**
   ```python
   st.write(df.head())  # データの最初の5行を表示
   st.write(df.shape)   # データの形を確認
   ```

2. **中間結果の表示**
   ```python
   st.write("集計結果:", aggregated_data)
   ```

3. **エラーの詳細確認**
   - Streamlitのエラーメッセージを詳しく読む
   - ブラウザの開発者ツールでJavaScriptエラーを確認

## 📋 チェックリスト

### 演習完了の確認
- [ ] 年別推移が折れ線グラフで表示される
- [ ] 国別ランキングが棒グラフで表示される
- [ ] Plotlyグラフがインタラクティブに動作する
- [ ] 複数国選択でグラフが更新される
- [ ] グラフタイプを切り替えできる
- [ ] 円グラフで構成比が表示される

### 学習目標の達成確認
- [ ] Streamlitの基本グラフ機能を理解した
- [ ] Plotly Expressの基本的な使い方を覚えた
- [ ] インタラクティブ機能の価値を理解した
- [ ] 適切なグラフタイプを選択できる
- [ ] レイアウトを考えたUI設計ができる

## 🎨 発展課題

### 基本レベル
1. **グラフの装飾**
   - タイトルや軸ラベルの改善
   - 色の統一やテーマの適用

2. **追加の統計情報**
   - 平均値、最大値、最小値の表示
   - 成長率の計算と表示

### 中級レベル
1. **年範囲選択機能**
   - `st.slider()`で期間を指定
   - 選択期間での集計とグラフ表示

2. **地域別分析**
   - 地域ごとのグループ化
   - 地域別比較グラフ

### 上級レベル
1. **ヒートマップ**
   - 年・国の2次元データ表示
   - `px.imshow()`の活用

2. **アニメーション機能**
   - 年ごとの変化を動画で表示
   - `px.bar(animation_frame='Year')`

3. **ダッシュボード統合**
   - 複数のグラフを組み合わせ
   - レスポンシブレイアウト

## 📖 参考資料

### 公式ドキュメント
- [Streamlit Charts](https://docs.streamlit.io/library/api-reference/charts)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Plotly Graph Objects](https://plotly.com/python/graph-objects/)

### 学習リソース
- [データ可視化のベストプラクティス](https://www.tableau.com/learn/articles/data-visualization)
- [色理論とアクセシビリティ](https://webaim.org/articles/contrast/)
- [Streamlit Gallery](https://streamlit.io/gallery)

### 次回への準備
第13回では、これまでの知識を統合した総合的なWebアプリケーション開発を行います。
- 今回作成したグラフ機能
- 第11回の集計・ランキング機能
- 第10回のデータ処理機能

すべてを組み合わせた実用的なアプリケーションを完成させましょう！ 