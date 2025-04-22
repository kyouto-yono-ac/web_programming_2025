---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第6回：Streamlit発展 (1): 入力ウィジェット"
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
# 第6回 Streamlit発展 (1)
## 入力ウィジェット入門

大妻女子大学 社会情報学部 WebプログラミングI
担当：余野
出席認証コード: 1887
授業資料: https://x.gd/NoqkC (大学のアカウントでgoogleにログインしていることが必要)

---

## 本日の流れ

1.  **前回の復習** (レイアウト機能)
2.  **インタラクティブなアプリへ**
3.  **ボタン (`st.button`)**
4.  **単一選択 (`st.selectbox`, `st.radio`)**
5.  **複数選択 (`st.multiselect`)**
6.  **数値入力 (`st.slider`, `st.number_input`)**
7.  **テキスト入力 (`st.text_input`, `st.text_area`)**
8.  **日付入力 (`st.date_input`)**
9.  **総合演習**
10. **まとめと次回予告**

**目標:** Streamlit の入力ウィジェットを使いこなし、ユーザーと対話できるアプリを作る！

---

## 1. 前回の復習

前回は Streamlit アプリの見た目を整理するレイアウト機能を学びました。

- **`st.sidebar`**: サイドバーに要素を配置
- **`st.columns`**: 画面を列に分割
- **`st.tabs`**: タブでコンテンツを切り替え
- **`st.expander`**: クリックで詳細を表示/非表示
- **`st.container`**: 要素をグループ化

これらで見やすいアプリの「骨格」を作れるようになりました。

---

## 2. インタラクティブなアプリへ

これまでのアプリは、主に情報を**表示**するだけでした。

今回は、**ユーザーからの入力**を受け取り、それに応じてアプリの動作を変える方法を学びます。

- ユーザーがボタンをクリックしたら処理を実行
- ユーザーが選択肢を選んだら表示を更新
- ユーザーが数値を入力したら計算結果を表示

→ これが**インタラクティブ (対話的)** なアプリです！

---

## 入力ウィジェットの基本

Streamlit の入力ウィジェットは、基本的に以下の流れで使います。

1.  **ウィジェット関数を呼び出す:** `st.button("ラベル")`, `st.selectbox(...)` など。
2.  **戻り値を受け取る:** ユーザーが入力した値や、操作の状態 (ボタンが押されたかなど) が関数の戻り値として返ってくる。
3.  **戻り値を利用する:** `if` 文でボタンのクリックを判定したり、選択された値を表示したり、計算に使ったりする。

```python
import streamlit as st

# 1. ウィジェット呼び出し & 2. 戻り値受け取り
user_name = st.text_input("お名前を入力してください")

# 3. 戻り値を利用
if user_name:
    st.write(f"こんにちは、{user_name}さん！")
```

---

## 3. ボタン (`st.button`)

**クリックできるボタンを作成**

- `st.button("ラベル")`
- **戻り値:**
    - ボタンが**クリックされた瞬間**の再実行で `True` を返す。
    - それ以外 (クリックされていない、他のウィジェット操作での再実行) では `False` を返す。

```python
import streamlit as st

if st.button("クリックしてね！"):
    st.write("ボタンがクリックされました！")
else:
    st.write("ボタンはまだ押されていません。")
```
- 何かのアクションを開始するトリガーとしてよく使う。

---

## 4. 単一選択 (`st.selectbox`, `st.radio`)

**複数の選択肢から一つだけ選ばせる**

- **`st.selectbox("ラベル", [選択肢リスト], index=0)`**: ドロップダウンリスト
- **`st.radio("ラベル", [選択肢リスト], index=0, horizontal=False)`**: ラジオボタン
- **戻り値:** ユーザーが選択した選択肢の値。
- `index`: デフォルトで選択される要素のインデックス。
- `horizontal=True` (radioのみ): ラジオボタンを横に並べる。

```python
import streamlit as st

options = ["りんご", "バナナ", "オレンジ"]

selected_fruit = st.selectbox("好きな果物を選んでください (Selectbox):", options)
st.write(f"あなたが選んだ果物 (Selectbox): {selected_fruit}")

selected_color = st.radio("好きな色を選んでください (Radio):", ["赤", "青", "黄"], horizontal=True)
st.write(f"あなたが選んだ色 (Radio): {selected_color}")
```
- 見た目とスペース効率で使い分ける。

---

## 5. 複数選択 (`st.multiselect`)

**複数の選択肢を同時に選ばせる**

- `st.multiselect("ラベル", [選択肢リスト], default=[デフォルト選択肢])`
- **戻り値:** ユーザーが選択した選択肢の**リスト**。

```python
import streamlit as st

toppings = ["チーズ", "ペパロニ", "マッシュルーム", "オリーブ"]

selected_toppings = st.multiselect(
    "ピザのトッピングを選んでください (複数可):",
    toppings,
    default=["チーズ"] # デフォルトでチーズを選択
)

st.write("選択したトッピング:", selected_toppings)

if selected_toppings:
    st.write("あなたは", ", ".join(selected_toppings), "を選びました。")
else:
    st.write("トッピングが選択されていません。")
```
- 複数のカテゴリ選択やタグ付けなどに使う。

---

## 6. 数値入力 (`st.slider`, `st.number_input`)

**数値を入力させる**

- **`st.slider("ラベル", min_value, max_value, value, step)`**: スライダーで範囲選択
    - `value`: 初期値。範囲 (タプル) を指定すると範囲スライダーになる。
- **`st.number_input("ラベル", min_value, max_value, value, step)`**: 入力ボックス
- **戻り値:** ユーザーが選択/入力した数値 (または範囲タプル)。

```python
import streamlit as st

age = st.slider("年齢を選択してください:", 0, 100, 25) # 最小, 最大, 初期値
st.write(f"あなたの年齢: {age} 歳")

price_range = st.slider("価格帯を選択してください:", 0.0, 1000.0, (100.0, 500.0), step=10.0)
st.write(f"選択した価格帯: {price_range[0]:.1f} 円 〜 {price_range[1]:.1f} 円")

quantity = st.number_input("数量を入力してください:", min_value=0, max_value=50, value=1, step=1)
st.write(f"入力された数量: {quantity}")
```
- 直感的な範囲選択なら `slider`、正確な数値入力なら `number_input`。

---

## 7. テキスト入力 (`st.text_input`, `st.text_area`)

**テキストを入力させる**

- **`st.text_input("ラベル", value="", max_chars=None, placeholder="")`**: 一行入力
    - `value`: 初期値
    - `max_chars`: 最大文字数
    - `placeholder`: 入力例などのヒント表示
- **`st.text_area("ラベル", value="", height=None, max_chars=None, placeholder="")`**: 複数行入力
    - `height`: ボックスの高さ (ピクセル数)
- **戻り値:** 入力された文字列。

```python
import streamlit as st

user_name = st.text_input("お名前:", placeholder="山田 太郎")
if user_name:
    st.write(f"ようこそ、{user_name}さん")

comment = st.text_area("コメント (複数行可):", height=150)
if comment:
    st.write("入力されたコメント:")
    st.write(comment)
```

---

## 8. 日付入力 (`st.date_input`)

**日付を入力させる**

- `st.date_input("ラベル", value=None, min_value=None, max_value=None)`
- **戻り値:** Python の `datetime.date` オブジェクト。
- `value`: 初期値 ( `datetime.date` オブジェクトまたは `None`)
- `min_value`, `max_value`: 選択可能な日付の範囲 (`datetime.date` オブジェクト)

```python
import streamlit as st
import datetime

today = datetime.date.today()
start_date = st.date_input(
    "開始日を選択してください:",
    value=today, # デフォルトは今日
    min_value=today - datetime.timedelta(days=30), # 30日前から
    max_value=today + datetime.timedelta(days=30)  # 30日後まで
)

st.write(f"選択された開始日: {start_date}")

# 時刻も入力させたい場合は st.time_input
selected_time = st.time_input("時刻を選択:", datetime.time(12, 00))
st.write(f"選択された時刻: {selected_time}")
```

---

## 9. 総合演習

**課題:** これまで学んだ入力ウィジェットを組み合わせて、ユーザーの入力に応じて結果が変わる簡単なアプリを作成しましょう。

- **テーマ例:**
    - 簡単なアンケートフォーム (名前、年齢、好きなものなど)
    - BMI 計算機 (身長と体重を入力)
    - 旅行プランナー (目的地、日付、人数を選択)
- **使う機能 (例):**
    - `st.text_input` で名前入力
    - `st.slider` または `st.number_input` で年齢や数値入力
    - `st.selectbox` や `st.radio` で選択肢入力
    - `st.multiselect` で複数選択
    - `st.date_input` で日付入力
    - `st.button` で結果表示のトリガー
    - 入力された値を使って `st.write` や `st.metric` で結果を表示

**▶ 色々なウィジェットを試して、インタラクティブな動作を確認しよう！**

---

## 10. まとめ

- Streamlit の**入力ウィジェット**を使うことで、ユーザーからの入力を受け付け、アプリをインタラクティブにできる。
- **主要なウィジェット:**
    - `st.button`: クリックイベント
    - `st.selectbox`, `st.radio`: 単一選択
    - `st.multiselect`: 複数選択
    - `st.slider`, `st.number_input`: 数値入力
    - `st.text_input`, `st.text_area`: テキスト入力
    - `st.date_input`: 日付入力
- 各ウィジェットは**戻り値**としてユーザーの入力や状態を返す。
- その戻り値を使って、アプリの表示や処理を変化させる。

---

## 次回予告

**第7回: Streamlit発展 (2): 状態管理 (`st.session_state`)**

複数のウィジェット操作や画面遷移をまたいで情報を保持するには？

- Streamlit の再実行の仕組みと課題
- `st.session_state` の導入
- `st.session_state` を使ったウィジェット間の連携
- `st.session_state` を使ったカウンターや累積処理

より複雑なインタラクションを実現するための重要な概念です！

---

## 質疑応答

何か質問はありますか？

入力ウィジェットの使い方、組み合わせ方、エラーなど、気軽に質問してください。 