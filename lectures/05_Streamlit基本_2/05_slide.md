---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第5回：Streamlit基本 (2): レイアウト"
size: 16:9
style: |
  section {
    font-size: 25px;
  }
  h1 {
    font-size: 32px;
  }
  h2 {
    font-size: 28px;
  }
  code {
    font-size: 18px; /* コードのフォントサイズ調整 */
  }
  pre code {
    font-size: 16px; /* コードブロック内のフォントサイズ調整 */
    line-height: 1.2; /* 行間調整 */
  }

---

<!-- _class: lead -->
# 第5回 Streamlit基本 (2)
## レイアウト入門

大妻女子大学 社会情報学部 WebプログラミングI
担当：余野
出席認証コード: 1506
授業資料: https://x.gd/NoqkC (大学のアカウントでgoogleにログインしていることが必要)

---

## 本日の流れ

1.  **前回の復習** (表示系ウィジェット)
2.  **なぜレイアウト？**
3.  **サイドバー (`st.sidebar`)**
4.  **列レイアウト (`st.columns`)**
5.  **タブ表示 (`st.tabs`)**
6.  **展開可能コンテナ (`st.expander`)**
7.  **コンテナ (`st.container`)**
8.  **総合演習**
9.  **まとめと次回予告**

**目標:** Streamlit のレイアウト機能を使いこなし、見やすいアプリを作る！

---

## 1. 前回の復習

前回は Streamlit で様々な情報を「表示」する方法を学びました。

- **テキスト:** `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.text`, `st.code`
- **データ:** `st.dataframe`, `st.table`
- **数値:** `st.metric`
- **マジックコマンド:** `st.write` なしでの表示

これらを組み合わせることで、基本的な情報表示は可能です。

---

## 2. なぜレイアウト？

情報が増えてくると、ただ上から順に表示するだけでは...

- **見にくい！** どこに何があるか分かりにくい。
- **比較しにくい！** 横に並べて比べたい。
- **ごちゃごちゃする！** 関係ない情報が混ざる。
- **長い！** スクロールが多くなる。

**→ レイアウト機能を使って、情報を整理し、見やすく配置しよう！**

---

## 3. サイドバー (`st.sidebar`)

**メイン画面とは別に、左側に表示される領域**

- 用途:
    - 設定項目 (例: 表示するデータの選択、パラメータ調整)
    - ナビゲーション (例: 複数ページアプリでのページ選択)
    - アプリの説明や補足情報
- 使い方:
    - `st.ウィジェット()` の代わりに `st.sidebar.ウィジェット()` を使うだけ！

```python
import streamlit as st

# メイン画面
st.title("メインコンテンツ")
st.write("ここはメイン画面です。")

# サイドバー
st.sidebar.title("サイドバー")
st.sidebar.write("ここはサイドバーです。")
selected_option = st.sidebar.selectbox("オプション選択", ["A", "B", "C"])
st.sidebar.button("サイドバーのボタン")

st.write("サイドバーで選択されたオプション:", selected_option)
```

---

## 4. 列レイアウト (`st.columns`)

**画面を縦 (水平方向) に分割して、要素を横に並べる**

- `st.columns(分割数)`: 指定した数で等分割
- `st.columns([比率1, 比率2, ...])`: 指定した比率で分割
- `with` 構文で各列に要素を配置

```python
import streamlit as st

col1, col2 = st.columns(2) # 2列に等分割

with col1:
   st.header("列1")
   st.write("ここは左側の列です。")
   st.button("ボタン A")

with col2:
   st.header("列2")
   st.write("ここは右側の列です。")
   st.button("ボタン B")

# 比率を指定して分割 (例: 1:2)
col_a, col_b = st.columns([1, 2])
with col_a:
    st.metric("データA", 100)
with col_b:
    st.line_chart([1, 5, 2, 8])
```

---

## `st.columns` の活用例

- 画像を横に並べて比較
- 指標 (Metric) を複数並べてダッシュボード風に
- 入力フォームとプレビューを左右に表示

```python
import streamlit as st

st.header("指標を横に並べる")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# 画像を並べる (st.imageについては後日)
# col_img1, col_img2 = st.columns(2)
# with col_img1:
#    st.image("image1.jpg")
# with col_img2:
#    st.image("image2.jpg")
```
**▶ 演習: 複数のメトリックを列を使って表示してみよう！**

---

## 5. タブ表示 (`st.tabs`)

**関連する複数のコンテンツをタブで切り替えて表示**

- `st.tabs(["タブ名1", "タブ名2", ...])` でタブを作成
- `with` 構文で各タブ内に要素を配置

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [10, 20, 30]
})

tab1, tab2, tab3 = st.tabs(["📈 グラフ", "🗃 データ", "📄 説明"])

with tab1:
   st.header("グラフ表示エリア")
   st.line_chart(df)

with tab2:
   st.header("データ表示エリア")
   st.dataframe(df)

with tab3:
   st.header("補足説明")
   st.write("これはサンプルデータとそのグラフです。")
```
- 情報を整理し、画面をすっきりさせるのに有効。

---

## `st.tabs` の活用例

- 分析結果を「概要」「詳細データ」「グラフ」などで分ける
- 設定項目を種類ごとにタブでまとめる
- 機械学習モデルの評価を「精度指標」「混同行列」「特徴量重要度」などで表示

**▶ 演習: 簡単なデータフレームを作り、データとグラフをタブで表示してみよう！**

---

## 6. 展開可能コンテナ (`st.expander`)

**クリックするまで内容を隠しておける折りたたみ可能なセクション**

- `st.expander("表示ラベル")` で作成
- `with` 構文で中に要素を配置
- `expanded=True` で最初から開いた状態にもできる

```python
import streamlit as st

st.write("メインコンテンツ")

with st.expander("詳細はこちらをクリック"): # デフォルトは閉じている
     st.write("""
         ここに詳細な説明文や補足情報を書きます。
         通常は隠れているので、画面がすっきりします。
     """)
     st.button("エクスパンダ内のボタン")

with st.expander("最初から開いておく", expanded=True):
    st.write("この内容は最初から表示されています。")
```
- 長い説明、コード例、設定の詳細などを格納するのに便利。

---

## `st.expander` の活用例

- FAQ (よくある質問) の表示
- エラーメッセージやログの詳細表示
- チュートリアルや使い方の説明
- 高度な設定項目

**▶ 演習: 長めの説明文を `st.expander` に入れてみよう！**

---

## 7. コンテナ (`st.container`)

**複数の要素をグループ化するための「見えない箱」**

- `st.container()` で作成
- `with` 構文で中に要素を配置
- これ自体には枠線などの見た目はない

**主な目的:**
- **要素の配置順序の制御:** コンテナ内の要素はひとまとまりとして扱われる。
- **「Out-of-order writing」 (高度):** コンテナを使うと、定義した場所以外 (後から) でも要素を追加できる場合がある。

```python
import streamlit as st

st.header("コンテナの例")

with st.container():
   st.write("これはコンテナ内の最初の要素です。")
   st.button("コンテナ内ボタン1")

st.write("これはコンテナの外の要素です。")

with st.container():
   st.write("これは別のコンテナ内の要素です。")
   st.button("コンテナ内ボタン2")

# 高度な例 (今は理解しなくてOK)
# container = st.container()
# button_clicked = st.button("ボタン")
# if button_clicked:
#    with container: # ボタンが押されたらコンテナに書き込む
#       st.write("ボタンが押されました！")
```
- 基本的なレイアウトでは必須ではないが、複雑な配置で役立つことがある。

---

## 8. 総合演習

**課題:** これまで学んだレイアウト機能を組み合わせて、構造化されたアプリを作成しましょう。

- **テーマ例:**
    - 簡単なデータ分析ダッシュボード
    - 設定可能なプロファイルページ
    - 製品カタログ
- **使う機能 (例):**
    - `st.sidebar` に設定項目 (例: 表示するデータカテゴリ、グラフの種類)
    - `st.columns` でメイン画面を分割 (例: 左にグラフ、右にデータテーブル)
    - `st.tabs` で関連情報を整理 (例: 基本情報タブ、詳細データタブ)
    - `st.expander` で補足説明や詳細設定を格納

**▶ 色々なレイアウトを試して、見やすい配置を探してみよう！**

---

## 9. まとめ

- **サイドバー (`st.sidebar`)**: メイン画面と別の領域にウィジェットを配置。
- **列 (`st.columns`)**: 画面を縦に分割し、要素を横に並べる。
- **タブ (`st.tabs`)**: 関連コンテンツをタブで切り替えて表示。
- **エクスパンダ (`st.expander`)**: クリックで詳細を表示/非表示。
- **コンテナ (`st.container`)**: 要素をグループ化 (主に配置制御用)。

これらのレイアウト機能を組み合わせることで、情報量が多くても見やすく、使いやすい Streamlit アプリケーションを構築できます！

---

## 次回予告

**第6回: Streamlit発展 (1): 入力ウィジェット**

いよいよユーザーからの入力を受け付ける方法を学びます！

- `st.button`: クリックできるボタン
- `st.selectbox`: ドロップダウンリストからの選択
- `st.multiselect`: 複数選択可能なリスト
- `st.radio`: ラジオボタンでの選択
- `st.slider`: スライダーでの数値範囲選択
- `st.text_input`: テキスト入力 (復習＆詳細)
- `st.number_input`: 数値入力
- `st.date_input`: 日付入力

アプリがインタラクティブになります！

---

## 質疑応答

何か質問はありますか？

レイアウトの使い方、組み合わせ方など、気軽に質問してください。 