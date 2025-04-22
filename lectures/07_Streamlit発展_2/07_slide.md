---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第7回：Streamlit発展 (2): 状態管理 (st.session_state)"
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
# 第7回 Streamlit発展 (2)
## 状態管理 (st.session_state)

大妻女子大学 社会情報学部 WebプログラミングI
担当：余野
出席認証コード: 2242
授業資料: https://x.gd/NoqkC (大学のアカウントでgoogleにログインしていることが必要)

---

## 本日の流れ

1.  **前回の復習** (入力ウィジェット)
2.  **Streamlit の再実行モデルと「状態」の問題**
3.  **`st.session_state` の基本**
4.  **ウィジェットと `st.session_state` の連携 (`key`)**
5.  **コールバック関数 (`on_change`, `args`)**
6.  **応用例と実践演習 (カウンター, ToDoリスト)**
7.  **まとめとベストプラクティス**
8.  **次回予告**

**目標:** `st.session_state` を使いこなし、インタラクション間で情報を保持する！

---

## 1. 前回の復習

前回はユーザーからの入力を受け取るウィジェットを学びました。

- **`st.button`**: クリック検知
- **`st.selectbox`, `st.radio`**: 単一選択
- **`st.multiselect`**: 複数選択
- **`st.slider`, `st.number_input`**: 数値入力
- **`st.text_input`, `st.text_area`**: テキスト入力
- **`st.date_input`**: 日付入力

これらの戻り値を使って、入力に応じた表示変化が可能になりました。

---

## 2. Streamlit の再実行モデルと「状態」の問題

**Streamlit の重要な特徴 (おさらい):**
ユーザーがウィジェットを操作する (ボタンを押す、値を変えるなど) たびに、**Python スクリプト全体が最初から最後まで再実行される**。

**これにより、困ったことが起こる場合があります...**

```python
import streamlit as st

st.title("カウンターアプリ (?)")

count = 0 # スクリプト実行のたびに 0 にリセットされる

if st.button("カウントアップ"):
    count += 1

st.write(f"現在のカウント: {count}")
```
**▶ このコードを実行してボタンを押しても、カウントは増えません！**

なぜなら、ボタンを押してスクリプトが再実行されるたびに `count = 0` が実行されてしまうからです。
インタラクション間で値 (状態) を保持できていません。

---

## 「状態 (State)」とは？

- アプリケーションが動作する中で、**保持・記憶しておく必要のある情報** のこと。
    - ユーザーの入力値
    - 計算結果
    - アプリの設定
    - ログイン状態 など

- Streamlit の再実行モデルでは、通常の Python 変数は状態を保持するのには使えません。

**そこで登場するのが `st.session_state` です！**

---

## 3. `st.session_state` の基本

**スクリプトの再実行をまたいで情報を保持するための特別な仕組み**

- Streamlit アプリの**各ユーザーセッションごと**に用意される。
- Python の**辞書 (dictionary)** のように使える。

**使い方:**
1.  **初期化:** そのキーがまだ存在しない場合のみ、初期値を設定する。
2.  **参照:** 値を読み出す。
3.  **更新:** 値を書き換える。

```python
import streamlit as st

# 1. 初期化 (初回実行時 or キーが存在しない場合のみ実行される)
if 'count' not in st.session_state:
    st.session_state.count = 0

# ボタンが押されたらカウントアップ
if st.button("カウントアップ"):
    # 3. 更新
    st.session_state.count += 1

# 2. 参照
st.write(f"現在のカウント: {st.session_state.count}")
```
**▶ これならカウントが増える！**

---

## `st.session_state` の操作方法

辞書と同じように、いくつかの方法でアクセスできます。

```python
import streamlit as st

# キー 'my_variable' で状態を管理

# 初期化 (推奨される方法)
if 'my_variable' not in st.session_state:
    st.session_state.my_variable = "初期値"

# 参照
value1 = st.session_state.my_variable  # 属性アクセス (Attribute access)
value2 = st.session_state['my_variable'] # 辞書アクセス (Dictionary access)
st.write(f"現在の値 (属性): {value1}")
st.write(f"現在の値 (辞書): {value2}")

# 更新
st.session_state.my_variable = "新しい値"
st.session_state['my_variable'] = "さらに新しい値"

# 存在確認
if 'another_key' in st.session_state:
    st.write("another_key は存在します")
else:
    st.write("another_key は存在しません")

# キーと値を一覧表示 (デバッグ用)
st.write("現在の Session State:", st.session_state)
```
- 基本的には属性アクセス (`st.session_state.キー名`) がシンプルで推奨されます。
- キー名にスペースや特殊文字を含めたい場合は辞書アクセスを使います。

---

## 4. ウィジェットと `st.session_state` の連携 (`key`)

入力ウィジェットの値を簡単に `st.session_state` に保存する方法があります。

**ウィジェット関数の `key` 引数を使う！**

- `key="キー名"` を指定すると、ウィジェットの値が自動的に `st.session_state.キー名` に格納される。

```python
import streamlit as st

# key を指定して text_input を作成
st.text_input("テキストを入力してください", key="user_text")

# Session State を介して値にアクセス
if 'user_text' in st.session_state:
    st.write("入力されたテキスト (Session State経由):", st.session_state.user_text)

# ウィジェットの戻り値でもアクセス可能 (従来通り)
# text_value = st.text_input("...")
# st.write(text_value)
```
- `key` を使うと、コードの異なる場所からでも同じ入力値に簡単にアクセスできる。
- 状態管理がしやすくなる。

---

## `key` 引数の注意点

- `key` を指定したウィジェットの戻り値と、`st.session_state[key]` は常に同じ値になる。
- `key` はアプリ全体で **ユニーク (一意)** である必要がある。同じ `key` を複数のウィジェットで使うとエラーになる。

```python
import streamlit as st

# key を使ってスライダーの値を取得
st.slider("値を選択", 0, 10, key="my_slider")
st.write("スライダーの値:", st.session_state.my_slider)

# Session State を直接更新することも可能 (ただし非推奨な場合も)
if st.button("値を5にセット"):
    st.session_state.my_slider = 5
    # この後、スライダーの表示も自動的に 5 に更新される！
```
**▶ 演習: `selectbox` の選択値を `key` を使って Session State に保存し、表示してみよう！**

---

## 5. コールバック関数 (`on_change`, `args`)

ウィジェットの値が変更されたとき (またはボタンが押されたとき) に、**特定の処理 (関数) を自動的に実行したい** 場合に使います。

- **`on_change` 引数:** ウィジェットの値が変わったときに呼び出す関数を指定。
- **`args` 引数:** そのコールバック関数に渡す引数をタプルで指定。

**なぜ使う？**
- 状態の更新ロジックを関数としてまとめることができる。
- 複雑な状態遷移を管理しやすくなる。

---

## コールバック関数の例 (カウンター)

```python
import streamlit as st

# コールバック関数: カウンターを増やす
def increment_counter():
    st.session_state.count += 1

# コールバック関数: カウンターを減らす
def decrement_counter():
    st.session_state.count -= 1

# 状態の初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(f"現在のカウント: {st.session_state.count}")

# ボタンにコールバック関数を登録
st.button("＋", on_change=increment_counter)
st.button("－", on_change=decrement_counter)

# --- 引数を渡す例 --- 
def add_value(value_to_add):
    st.session_state.count += value_to_add

st.button("+5", on_change=add_value, args=(5,))
```
- `on_change` に指定した関数は、ウィジェット操作による **再実行の前に** 呼び出される。
- 関数内で `st.session_state` を更新しておけば、再実行後のスクリプトでその新しい値を使える。

---

## 6. 応用例と実践演習

**演習1: 単位変換アプリ**
- `st.number_input` で数値を入力 (例: 摂氏温度)。
- `st.radio` で変換先の単位を選択 (例: 華氏)。
- 変換結果を表示する。
- 入力値や選択肢を `st.session_state` (key引数) で管理してみよう。

**演習2: 簡単な ToDo リスト**
- `st.session_state` に ToDo リスト (Python のリスト) を保存する。
- `st.text_input` で新しいタスクを入力。
- `st.button` (またはコールバック) でタスクをリストに追加。
- 現在の ToDo リストを `st.write` や `for` ループで表示。
- (発展) チェックボックスで完了状態を管理したり、削除ボタンを追加したり。

**▶ Session State を使って、状態を保持するアプリを作ってみよう！**

---

## 7. まとめとベストプラクティス

- **Streamlit はウィジェット操作で再実行される。**
- **`st.session_state`**: 再実行をまたいで状態を保持する辞書ライクなオブジェクト。
    - **初期化:** `if 'key' not in st.session_state:` パターンが重要。
    - **アクセス:** `st.session_state.key` or `st.session_state['key']`
    - **ウィジェット連携:** `key="my_key"` 引数で自動的に値を格納。
- **コールバック関数 (`on_change`)**: ウィジェット操作時に状態を更新するロジックをまとめるのに便利。

**使い方のヒント:**
- 必要な状態だけを `st.session_state` で管理する。
- キー名は分かりやすく、一意にする。
- 複雑な処理はコールバック関数にまとめる。

`st.session_state` をマスターすれば、本格的なインタラクティブアプリが作れます！

---

## 8. 次回予告

**第8回: データ処理入門 (Pandas)**

いよいよデータ分析の世界へ！

- Python の強力なデータ分析ライブラリ **Pandas** の基本を学びます。
    - **DataFrame**, **Series** とは？
    - データの読み込み (CSV, Excel ...)
    - データの選択、フィルタリング
    - 簡単な集計
- Streamlit の **`st.file_uploader`** を使って、ユーザーがファイルをアップロードできるようにします。

---

## 質疑応答

何か質問はありますか？

`st.session_state` の挙動、コールバック、エラーなど、気軽に質問してください。 