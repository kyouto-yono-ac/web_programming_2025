---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第4回：Streamlit基本 (1): テキストとデータ表示"
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
  table {
    font-size: 20px; /* テーブルのフォントサイズ調整 */
  }

---

<!-- _class: lead -->
# 第4回 Streamlit基本 (1)
## テキストとデータ表示

大妻女子大学 社会情報学部 WebプログラミングI
担当：余野
出席認証コード: 0707
授業資料: https://x.gd/NoqkC (大学のアカウントでgoogleにログインしていることが必要)　

---

## 本日の流れ

1.  **前回の復習と Streamlit 概要**
2.  **基本的なテキスト表示** (`st.title`, `st.header`, `st.write`...)
3.  **Markdown とコードの表示** (`st.markdown`, `st.code`)
4.  **マジックコマンド**
5.  **データフレームとテーブル表示** (`st.dataframe`, `st.table`)
6.  **メトリック表示** (`st.metric`)
7.  **総合演習**
8.  **まとめと次回予告**

**目標:** Streamlit で様々な情報を効果的に表示できるようになる！

---

## 1. 前回の復習と Streamlit 概要

- **Python 基礎 (復習):**
    - 制御構造: `if`, `for`, `while`
    - 関数: `def`, 引数, 戻り値, デフォルト引数, キーワード引数, Docstring
    - これらを組み合わせて処理の流れを作る
- **Streamlit とは？ (再確認)**
    - Python だけで簡単に Web アプリを作成できるフレームワーク
    - データ分析・可視化アプリのプロトタイピングに強い
- **アプリの実行方法 (復習):**
    - ターミナルで `streamlit run ファイル名.py`

---

## Streamlit アプリの基本構造

```python
# 1. ライブラリのインポート
import streamlit as st
import pandas as pd # データ表示でよく使う

# 2. アプリのタイトル設定 (例)
st.title("はじめての Streamlit アプリ")

# 3. 表示したい内容を記述 (ここからが本番！)
st.write("Hello, Streamlit!")

# これだけで Web アプリが動く！
```
- 基本的に上から下にコードが実行され、対応する要素が Web ページに表示される。
- ファイルを保存すると、ブラウザの表示も自動で更新されることが多い (便利！)

---

## 2. 基本的なテキスト表示

様々なテキスト表示用コマンドがあります。

- `st.title("メインタイトル")`: 最も大きな見出し (通常1ページに1つ)
- `st.header("セクション見出し")`: やや大きな見出し
- `st.subheader("サブセクション見出し")`: 中くらいの見出し
- `st.write("汎用的なテキストや変数")`: 文字列、数値、変数の中身など、多くを表示可能。
- `st.text("固定幅フォントのテキスト")`: 整形済みテキストや短いメッセージに。

```python
st.title("アプリのタイトル")
st.header("これはヘッダーです")
st.subheader("これはサブヘッダーです")
st.write("st.write は色々なものを表示できます。例えば数値:", 123)
st.text("st.text はシンプルなテキスト表示用です。")
```
**▶ 実際にコードを書いて試してみよう！**

---

## 3. Markdown とコードの表示

**`st.markdown()`: もっと表現力豊かなテキストを！**
- Markdown 記法が使える。
    - `**太字**` → **太字**
    - `*イタリック*` → *イタリック*
    - `- リスト`
    - `[リンクテキスト](URL)`
    - `![画像ALT](画像URL)` など

```python
st.markdown("## Markdown が使えます！")
st.markdown("- **太字** も *イタリック* もリストも OK")
st.markdown("Streamlit 公式ドキュメントは [こちら](https://docs.streamlit.io/)")
```

**`st.code()`: コードを見やすく表示！**
```python
code = '''
def hello():
    print("Hello, Streamlit!")
'''
st.code(code, language='python')
```

---

## 4. マジックコマンド

**`st.write()` を書かなくても表示できる！？**

Streamlit では、Python の変数やリテラル（文字列、数値など）をスクリプト内に直接記述するだけで、自動的に `st.write()` で表示してくれる機能があります。

```python
import streamlit as st
import pandas as pd

st.title("マジックコマンドの例")

# st.write を使わずに表示
"""
## Markdown もそのまま書ける！
- マジック！
- すごい！
"""

x = 10
x # これだけで x の値 (10) が表示される

df = pd.DataFrame({
    '列1': [1, 2, 3],
    '列2': [10, 20, 30]
})
df # DataFrame も表示される！
```
- 簡単な値の確認やデバッグに便利。
- 長いスクリプトでは、何が表示されているか分かりにくくなる可能性も。

---

## 5. データフレームとテーブル表示

**Pandas DataFrame を使って表データを表示**

(事前に `import pandas as pd` が必要)

```python
import pandas as pd

data = {
    '商品': ['りんご', 'バナナ', 'オレンジ'],
    '価格': [120, 100, 150],
    '在庫': [30, 50, 20]
}
df = pd.DataFrame(data)
```

**`st.dataframe(df)`: インタラクティブなテーブル**
- スクロール可能
- 列でソート可能
- 大きなデータセットの表示に適している

**`st.table(df)`: 静的なテーブル**
- シンプルな表示
- 基本的に全データが表示される (大きなデータには不向き)
- デザインが少し異なる

---

## `st.dataframe()` vs `st.table()`

```python
import streamlit as st
import pandas as pd

data = {
    '商品': ['りんご', 'バナナ', 'オレンジ', 'ぶどう', 'もも'],
    '価格': [120, 100, 150, 300, 250],
    '在庫': [30, 50, 20, 15, 25]
}
df = pd.DataFrame(data)

st.header("st.dataframe の例 (インタラクティブ)")
st.dataframe(df)

st.header("st.table の例 (静的)")
st.table(df)
```
**▶ 用途に応じて使い分けよう！**
(一般的には `st.dataframe` の方が高機能で便利)

---

## 6. メトリック表示 (`st.metric`)

**主要な数値 (KPI など) を分かりやすく表示したい！**

`st.metric(label="ラベル", value=現在の値, delta=変化量)`

- `label`: 数値の意味を示すテキスト
- `value`: 表示したい主要な数値
- `delta` (任意): 以前の値との差分。正なら緑▲、負なら赤▼で表示されることが多い。

```python
st.metric(label="気温", value="25 °C", delta="1.5 °C")
st.metric(label="湿度", value="60 %", delta="-5 %")
st.metric(label="売上", value="1,200,000 円", delta="50,000 円")
```
- ダッシュボードなどで重要な指標を目立たせるのに便利。

---

## 7. 総合演習

**課題:** これまで学んだ表示ウィジェットを使って、簡単な自己紹介ページ、または好きなテーマの情報ページを作成してみましょう。

- **含める要素 (例):**
    - `st.title` でページタイトル
    - `st.header` / `st.subheader` でセクション分け
    - `st.markdown` で自己紹介文や説明文 (リストやリンクも活用)
    - `st.code` で好きなコードスニペット
    - `st.dataframe` または `st.table` で簡単な表 (例: 好きなものリスト、スキル一覧)
    - `st.metric` で何か面白い数値 (例: 今年の目標達成度、お気に入りの数値)

**▶ GitHub Codespaces (またはローカル) で `app.py`