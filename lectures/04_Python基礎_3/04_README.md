# 第4回 Python基礎(3): 制御構造(for/while ループ) と Streamlit応用

**授業の目標:**
- Pythonの `for` ループと `while` ループの基本的な使い方を理解し、記述できるようになる。
- ループ構造を用いてリストなどの反復処理や条件に基づく処理を実装できるようになる。
- 簡単な Streamlit アプリケーションの中でループや条件分岐 (`if`) を活用する方法を体験する。

**対象:** 大妻女子大学 社会情報学部 社会情報学科 社会生活情報学専攻 3・4年生
**前提知識:** 第3回までのPython基礎（変数、データ型、演算、if文）
**授業時間:** 90分 (実質 70-80分程度)
**形式:** 講義 + Google Colab演習 + Streamlit演習
**必要機材:** ノートPC、インターネット接続環境、Googleアカウント、(Streamlit実行環境 - GitHub.dev推奨)

## タイムスケジュール (目安)

| 時間        | 内容                                        | 形式          | 詳細                                                                      |
| ----------- | ------------------------------------------- | ------------- | ------------------------------------------------------------------------- |
| 00:00-00:30 | **for/whileループの解説 (復習含む)**        | 講義 + Colab  | `for` (`range`, リスト反復), `while` の基本、`break`/`continue` (Colab: `03_lecture.ipynb` 参照) |
| 00:30-00:50 | **演習1: for/whileループ (Colab)**        | 演習 (Colab)  | Colab (`03_exercises.ipynb`) のループ関連問題を解く                      |
| 00:50-01:00 | Streamlit演習の準備・説明                 | 講義          | 今回の演習アプリ (`src/lecture04/app.py`) の概要説明                      |
| 01:00-01:25 | **演習2: Streamlitアプリ (ループと条件分岐)** | 演習 (Streamlit)| Streamlit (`src/lecture04/app.py`) の課題1(for)と課題2(if) を実装       |
| 01:25-01:30 | まとめと次回予告                            | 講義          | 次回 (関数、辞書、Streamlit基本) の紹介                                  |

## 授業内容の詳細

1.  **制御構造 (ループ) - 復習と解説:** (Colab `03_lecture.ipynb` を参照)
    *   **`for` ループ:**
        *   指定した回数繰り返す (`range`)
        *   リストや文字列の要素を順番に取り出して繰り返す (`in`)
    *   **`while` ループ:**
        *   条件が真の間、処理を繰り返す
        *   カウンター変数を使ったループ制御、無限ループの注意点
    *   **`break` と `continue` (軽く触れる)**
2.  **Colab演習:** (Colab `03_exercises.ipynb` のループ関連問題を使用)
    *   基本的な `for`, `while` を使った問題演習
3.  **Streamlit演習 (`src/lecture04/app.py`):**
    *   **課題1: 持ち物チェックリスト:**
        *   Pythonリストの定義
        *   `for` ループを使ってリストの各要素を `st.checkbox` で表示する
    *   **課題2: 今日のコーデ提案:**
        *   `st.selectbox`, `st.slider` での入力取得
        *   `if`/`elif`/`else` を使った条件分岐 (天気 `and` 気温)
        *   条件に応じたメッセージ表示 (`st.info` など)

## 準備物

*   **教員:**
    *   授業用スライド (`04_slide.md`, `04_slide.pdf`) - **今回の内容に合わせて作成**
    *   Colabノートブック (前回の `03_lecture.ipynb`, `03_exercises.ipynb`, `03_answers.ipynb` を主に利用)
    *   Streamlit演習用スクリプト (`src/lecture04/app.py`, `src/lecture04/app_a.py`) - **作成済み**
    *   出席認証コード (事前に`assets/CODE.csv`から取得)
*   **学生:**
    *   ノートPC
    *   Googleアカウント (Colab利用のため)
    *   インターネット接続
    *   Streamlit実行環境 (GitHubアカウント推奨、GitHub.devを使う場合)

## 配布資料

*   講義スライド PDF (`lectures/04_Python基礎_3/04_slide.pdf`)
*   Colabノートブック (第3回のものを再利用):
    *   `lectures/03_Python基礎_2/03_lecture.ipynb` (ループ部分)
    *   `lectures/03_Python基礎_2/03_exercises.ipynb` (ループ問題)
    *   `lectures/03_Python基礎_2/03_answers.ipynb` (ループ解答)
*   Streamlit演習スクリプト:
    *   `src/lecture04/app.py` (演習用)
    *   `src/lecture04/app_a.py` (解答例)

## 次回予告

次回は、今回扱えなかった「関数」と「辞書」、そして「Streamlit基本 (1): 基本表示とインタラクション」を学びます。Pythonのコードを整理する方法や、より複雑なデータを扱う方法、そしてStreamlitでの基本的なアプリ画面の作り方を学びます。 