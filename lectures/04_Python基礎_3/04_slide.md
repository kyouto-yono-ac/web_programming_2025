---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第4回：Python基礎(3) 制御構造(ループ復習)とStreamlit応用"
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
# 第4回 Python基礎(3)
## 制御構造(ループ復習)とStreamlit応用

**担当:** [担当者名]
**授業資料:** `https://x.gd/NoqkC` (大学のアカウントでgoogleにログインしていることが必要)
**出席認証コード:** `0707`

---

## 今日の目標

1.  Pythonの `for` ループと `while` ループの使い方を**復習**し、Colabで問題を解く。
2.  簡単な Streamlit アプリで `for` ループと `if` 文を**実際に使ってみる**。

---

## 本日の流れ (90分)

| 時間        | 内容                                        | 形式          |
| ----------- | ------------------------------------------- | ------------- |
| 00:00-00:30 | **ループ (`for`/`while`) の復習**         | 講義 + Colab  |
| 00:30-00:50 | **演習1: ループ復習 (Colab)**             | 演習 (Colab)  |
| 00:50-01:00 | Streamlit演習の準備・説明                 | 講義          |
| 01:00-01:25 | **演習2: Streamlitアプリ (for/if)**       | 演習 (Streamlit)|
| 01:25-01:30 | まとめと次回予告                            | 講義          |

---

## 1. ループ (`for`/`while`) の復習

前回学んだループ構文を思い出しましょう。

- **`for` ループ:**
    - `range()` で回数指定
    - リスト (`list`) の要素を順番に処理
- **`while` ループ:**
    - 条件式が `True` の間繰り返す
    - 無限ループに注意！
- ループ制御 (`break`, `continue`)

**詳細な構文やコード例が必要な場合:**
👉 Google Colab `03_lecture.ipynb` の「4. 繰り返し (ループ)」セクションを再度確認してください。

---

## 2. 演習1: ループ復習 (Colab)

**時間:** 20分

**内容:**
前回 (第3回) の Colab 演習ノートブックにある `for` ループと `while` ループの問題を解いて、使い方に慣れましょう。

**ファイル:**
👉 Google Colab `03_exercises.ipynb` の問題 3, 4, 5 あたり

---

## 3. Streamlit演習 の準備

**今日のテーマ:**
前回学んだループ (`for`) と条件分岐 (`if`) を、Streamlit アプリの中で実際に使ってみよう！

**使うファイル (`src/lecture04/app.py`):**
- 課題1: `for` ループを使った「持ち物チェックリスト」
- 課題2: `if` 文を使った「今日のコーデ提案」

---

## 4. 演習2: Streamlit アプリ (for/if)

**時間:** 25分

**ファイル:**
- 演習用: `src/lecture04/app.py`
- 解答例: `src/lecture04/app_a.py`

**手順:**
1.  `src/lecture04/app.py` を開く。
2.  コメント (`# --- ここに ...`) を参考に、課題1(`for`)と課題2(`if`)のコードを完成させる。
3.  ターミナルで `streamlit run src/lecture04/app.py` を実行して動作確認。

---

### 課題1: 持ち物チェックリスト (for)

**目標:** `for` ループを使って、リスト `items` の各要素を `st.checkbox` で表示する。

**`app.py` の該当箇所:**
```python
# --- 課題1: 持ち物チェックリスト (forループ) ---
items = ["PC", "充電器", ...] # 持ち物リスト
st.subheader("必須アイテム:")
# --- ここに for ループを使って items の各要素を
# --- st.checkbox で表示するコードを書いてください ---

# (ここに for item in items: ... を書く)

# --- ここまで (課題1) ---
```
ヒント: `for item in items:` で要素を取り出し、`st.checkbox(item)` で表示。

---

### 課題2: 今日のコーデ提案 (if)

**目標:** `if`/`elif`/`else` を使って、選択された天気と気温に応じて、適切な服装のアドバイスを `st.info()` などで表示する。

**`app.py` の該当箇所:**
```python
# --- 課題2: 今日のコーデ提案 (if文) ---
weather = st.selectbox(...)
temperature = st.slider(...)
if st.button("コーデを提案する"):
    st.subheader("おすすめコーデ:")
    # --- ここに if/elif/else を使って天気と気温に応じた
    # --- メッセージを表示するコードを書いてください ---
    # (コメントのヒントも参考に！↓)
    # ＜考え方のヒント (箇条書き)＞
    # - まず「天気」で大きく場合分け...
    # (ここにif/elif/elseの条件分岐を書く)
    # --- ここまで (課題2) ---
```
ヒント: `if "晴れ" in weather and temperature >= 25:` のように条件を組み合わせる。

---

### Streamlit アプリの実行方法

1.  **VS Code の場合:**
    *   メニュー「ターミナル」>「新しいターミナル」
    *   `streamlit run src/lecture04/app.py` と入力して実行
2.  **GitHub Codespaces / GitHub.dev の場合:**
    *   codespacesを立ち上げる
    *   `streamlit run src/lecture04/app.py` を実行
    *   表示されるURLを開くか、ポート転送機能を使う

アプリがブラウザで起動したら、課題1と課題2が正しく動作するか確認しましょう。

---

## まとめ

- ループ (`for`, `while`) は処理の繰り返しに使う (復習)
- **Streamlit応用:**
    - `for` + リスト + `st.checkbox` → リスト項目の動的表示
    - `if` + 条件 + `st.info` → ユーザー入力に応じた表示変更
- Pythonの基本構文が Streamlit アプリの動作の核となる！

---

## 次回予告

**第5回: Python基礎(4) 関数と辞書 + Streamlit基本(1)**

- **関数 (`def`)**: 処理をまとめて再利用しやすくする
- **辞書 (`dict`)**: キーと値のペアでデータを扱う
- **Streamlit 基本 (`st.write`, `st.button` など)**: アプリの基本的な表示と操作

今日作ったアプリを関数で整理したり、より複雑なデータを扱えるようにします。

---

## 付録: Streamlit 解答例 (課題1: 持ち物チェックリスト)

```python
# --- 課題1: 持ち物チェックリスト (forループ) ---
st.write("---")
st.header("課題1: 🎒 持ち物チェックリスト")
st.write("Pythonのリストと `for` ループを使って、持ち物リストをチェックボックスで表示しましょう。")

# 持ち物リスト
items = ["PC", "充電器", "スマートフォン", "財布", "筆記用具", "ノート", "ハンカチ", "ティッシュ"]

st.subheader("必須アイテム:")

# --- ここに for ループを使って items の各要素を st.checkbox で表示するコードを書いてください ---
for item in items:
    st.checkbox(item)
# --- ここまで (課題1) ---

st.caption("ヒント: `for item in items:` でリスト要素を繰り返し、`st.checkbox(item)` で表示します。")
```

---

## 付録: Streamlit 解答例 (課題2: 今日のコーデ提案)

```python
if st.button("コーデを提案する"):
    st.write(f"天気: {weather}, 気温: {temperature}°C")
    st.subheader("おすすめコーデ:")
    if "☀️ 晴れ" in weather:
        if temperature >= 25:
            st.info("半袖やノースリーブで涼しく過ごそう！ Tシャツ、ワンピースなどがおすすめ。帽子もあると良いかも？👒")
        elif temperature >= 15:
            st.info("長袖シャツやブラウスがちょうどいいかも。薄手のカーディガンがあると安心。😊")
        else:
            st.info("少し肌寒いかも。ニットやパーカーに、ジャケットやコートを羽織るのがおすすめ。🧥")
    elif "☁️ 曇り" in weather:
        if temperature >= 20:
            st.info("過ごしやすい気温だけど、羽織ものがあると安心。長袖Tシャツやシャツにカーディガンなど。🌥️")
        else:
            st.info("少し肌寒いかも。セーターやトレーナーに、軽めのコートやジャケットを合わせると良さそう。")
    elif "☔ 雨" in weather:
        if temperature >= 20:
            st.info("雨だけど蒸し暑いかも。半袖や長袖シャツに、撥水性のある羽織もの。傘と濡れても良い靴を忘れずに！🌂")
        else:
            st.info("雨で肌寒いかも。長袖にジャケットやコート、そして傘は必須！足元も防水の靴がおすすめ。👢")
    else:
        st.write("状況に応じて調整してくださいね。")

``` 