---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第5回：Streamlit基本(1) と状態管理入門"
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
    font-size: 18px;
  }
  pre code {
    font-size: 16px;
    line-height: 1.2;
  }
  table {
    font-size: 20px;
  }
---

<!-- _class: lead -->
# 第5回 Streamlit基本(1) と状態管理入門
## `st.session_state` でインタラクティブなアプリを作ろう

**担当:** [担当者名]
**授業資料:** `https://x.gd/NoqkC`
**出席認証コード:** `1506`

---

## 今日の目標

1.  Streamlitの基本的な表示ウィジェットを理解し、使用できるようになる
2.  `st.session_state` の概念と基本的な使い方を習得する
3.  インタラクティブなリスト管理（アイテムの追加など）ができるアプリを作成する
4.  Pythonの関数と辞書の基本的な概念を理解する

---

## 本日の流れ (90分)

| 時間        | 内容                                                            | 形式          |
| ----------- | --------------------------------------------------------------- | ------------- |
| 00:00-00:10 | 前回の復習と本日の課題提示                                      | 講義          |
| 00:10-00:30 | **Streamlitの状態管理: `st.session_state` 入門**                | 講義 + デモ   |
| 00:30-00:55 | **演習1: `st.session_state`を使った動的持ち物リスト**         | 演習 (Streamlit)|
| 00:55-01:10 | **Streamlit基本ウィジェット (表示系)**                          | 講義 + デモ   |
| 01:10-01:20 | **Python基礎: 関数 (`def`) と辞書 (`dict`) の初歩**             | 講義          |
| 01:20-01:30 | まとめ、質疑応答、次回予告                                      | 講義          |

---

## 前回の復習: 持ち物チェックリスト

```python
# 持ち物リスト
items = ["PC", "充電器", "スマートフォン", "財布", "筆記用具", "ノート", "ハンカチ", "ティッシュ"]

st.subheader("必須アイテム:")

# for ループを使って items の各要素を st.checkbox で表示
for item in items:
    st.checkbox(item)
```

**課題:** このリストに新しいアイテムを追加できるようにするには？

---

## Streamlitの状態管理: `st.session_state` 入門

### なぜ `st.session_state` が必要か？

- Streamlitのスクリプトは、ユーザーの操作（ボタンクリックなど）があるたびに**最初から最後まで再実行**される
- 通常の変数は再実行時に**リセット**される
- ユーザーの操作やデータの変更を**保持**するには、特別な仕組みが必要

→ `st.session_state` の出番！

---

## `st.session_state` とは？

- アプリケーションのセッション間で**持続する**辞書型のオブジェクト
- キーと値のペアでデータを保存
- ブラウザを閉じるまで値が保持される

```python
# 基本的な使い方
if 'count' not in st.session_state:
    st.session_state.count = 0  # 初期化

st.session_state.count += 1  # 値の更新
st.write(f"カウント: {st.session_state.count}")  # 値の参照
```

---

## 簡単なデモ: カウンターアプリ

```python
import streamlit as st

# カウンターの初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

# カウントアップボタン
if st.button('カウントアップ'):
    st.session_state.count += 1

# カウンターの表示
st.write(f"現在のカウント: {st.session_state.count}")

# リセットボタン
if st.button('リセット'):
    st.session_state.count = 0
```

---

## 演習1: 動的持ち物リスト

**目標:** 第4回の持ち物リストを改造し、ユーザーが新しいアイテムを追加できるようにする

**ステップ:**
1.  持ち物リストを `st.session_state` で初期化
2.  `st.text_input` で新しいアイテム名を入力
3.  `st.button` でアイテムをリストに追加
4.  `for` ループでリストを表示
5.  (発展) アイテムの削除機能

---

## 演習1: コードのひな形

```python
import streamlit as st

# 持ち物リストの初期化
if 'items' not in st.session_state:
    st.session_state.items = ["PC", "充電器", "スマートフォン", "財布"]

# 新しいアイテムの入力
new_item = st.text_input("新しいアイテムを入力:")

# 追加ボタン
if st.button("追加"):
    # ここに追加のロジックを書く
    pass

# リストの表示
st.subheader("持ち物リスト:")
for item in st.session_state.items:
    st.checkbox(item)
```

---

## Streamlit基本ウィジェット (表示系)

### `st.write()`
- 最も汎用的な表示コマンド
- 文字列、数値、データフレームなど、様々なデータを表示

```python
st.write("Hello, World!")  # 文字列
st.write(42)  # 数値
st.write(["apple", "banana", "orange"])  # リスト
```

---

## Streamlit基本ウィジェット (表示系)

### テキストフォーマット
```python
st.header("大見出し")
st.subheader("中見出し")
st.caption("キャプション（小さな説明文）")
```

### Markdown
```python
st.markdown("""
# Markdown見出し
これは **太字** で、これは *イタリック* です。
- リスト項目1
- リスト項目2
""")
```

---

## Streamlit基本ウィジェット (表示系)

### `st.button()`
- クリック可能なボタンを表示
- クリックイベントで条件分岐を実行

```python
if st.button("クリックしてください"):
    st.write("ボタンがクリックされました！")
```

---

## Python基礎: 関数 (`def`)

### 関数とは？
- 同じ処理をまとめて再利用しやすくする
- コードの可読性を向上させる

### 基本的な使い方
```python
# 関数の定義
def greet(name):
    return f"こんにちは、{name}さん！"

# 関数の呼び出し
message = greet("太郎")
st.write(message)  # 出力: こんにちは、太郎さん！
```

---

## Python基礎: 辞書 (`dict`)

### 辞書とは？
- キー(key)と値(value)のペアでデータを格納するデータ型
- `st.session_state` も辞書のように振る舞う

### 基本的な使い方
```python
# 辞書の作成
person = {
    "name": "太郎",
    "age": 20,
    "city": "東京"
}

# 値へのアクセス
st.write(person["name"])  # 出力: 太郎
st.write(person["age"])   # 出力: 20
```

---

## まとめ

1.  **Streamlitの状態管理:**
    - `st.session_state` でユーザーの操作やデータの変更を保持
    - 辞書型のオブジェクトとして扱う

2.  **Streamlit基本ウィジェット:**
    - `st.write()`: 汎用的な表示
    - `st.header()`, `st.subheader()`, `st.caption()`: テキストフォーマット
    - `st.markdown()`: Markdown記法での表示
    - `st.button()`: クリックイベントの処理

3.  **Python基礎:**
    - 関数 (`def`): 処理のまとめ、再利用
    - 辞書 (`dict`): キーと値のペアでデータを管理

---

## 次回予告

**第6回: Streamlit基本(2) 多様な入力ウィジェット**

- `st.selectbox`: ドロップダウンリスト
- `st.multiselect`: 複数選択
- `st.slider`: スライダー
- `st.number_input`: 数値入力
- `st.text_input`: テキスト入力（より詳しく）

より複雑なユーザー入力を受け付ける方法を学びます！

---

## 質疑応答

ご質問はありますか？

---

## 付録: 演習1の解答例

```python
import streamlit as st

# 持ち物リストの初期化
if 'items' not in st.session_state:
    st.session_state.items = ["PC", "充電器", "スマートフォン", "財布"]

# 新しいアイテムの入力
new_item = st.text_input("新しいアイテムを入力:")

# 追加ボタン
if st.button("追加") and new_item:  # new_itemが空でない場合のみ追加
    st.session_state.items.append(new_item)

# リストの表示
st.subheader("持ち物リスト:")
for item in st.session_state.items:
    st.checkbox(item)
``` 