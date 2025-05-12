# 第5回 Streamlit基本(1) と状態管理入門 (`st.session_state`)

**授業の目標:**
- Streamlitの基本的な表示ウィジェット（`st.write`, `st.header`, `st.markdown`, `st.button`）を理解し、使用できるようになる。
- Streamlitアプリケーション内でユーザーの操作やデータの変更を保持するための `st.session_state` の概念と基本的な使い方を習得する。
- `st.session_state` を活用して、インタラクティブなリスト管理（アイテムの追加など）ができる簡単なアプリケーションを作成できるようになる。
- Pythonの関数 (`def`) の基本的な定義と呼び出し方を理解し、コードの整理に役立つことを知る。
- Pythonの辞書 (`dict`) の基本的な概念を理解する。

**対象:** 大妻女子大学 社会情報学部 社会情報学科 社会生活情報学専攻 3・4年生
**前提知識:** 第4回までのPython基礎（変数、データ型、演算、if文、for/whileループ）、Streamlitの基本的な実行方法と `st.checkbox`, `st.text_input` の利用経験。
**授業時間:** 90分 (実質 70-80分程度)
**形式:** 講義 + Streamlit演習
**必要機材:** ノートPC、インターネット接続環境、(Streamlit実行環境 - GitHub.dev推奨)

## タイムスケジュール (目安)

| 時間        | 内容                                                            | 形式          | 詳細                                                                                                |
| ----------- | --------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| 00:00-00:10 | 前回の復習と本日の課題提示                                      | 講義          | 第4回「持ち物チェックリスト」の振り返り、動的にリストを更新する課題の提示                             |
| 00:10-00:30 | **Streamlitの状態管理: `st.session_state` 入門**                | 講義 + デモ   | `st.session_state`の必要性、初期化、値の読み書き、簡単なカウンターアプリ例                          |
| 00:30-00:55 | **演習1: `st.session_state`を使った動的持ち物リスト**         | 演習 (Streamlit)| `st.text_input` で項目追加、ボタンで `st.session_state` 内のリストを更新、表示                    |
| 00:55-01:10 | **Streamlit基本ウィジェット (表示系)**                          | 講義 + デモ   | `st.write`, `st.header`, `st.subheader`, `st.markdown`, `st.button` (復習と役割) の使い方と例   |
| 01:10-01:20 | **Python基礎: 関数 (`def`) と辞書 (`dict`) の初歩**             | 講義          | 関数の定義と呼び出し、辞書の基本構造と利用例（`st.session_state`との関連も）                       |
| 01:20-01:30 | まとめ、質疑応答、次回予告                                      | 講義          |                                                                                                     |

## 授業内容の詳細

1.  **前回の復習と本日の課題:**
    *   第4回の「持ち物チェックリスト」演習（`st.checkbox` で静的リストを表示）を簡単に振り返る。
    *   課題の提示: チェックリストにユーザーが新しい持ち物を追加できるようにするにはどうすれば良いか？ (→ `st.session_state` の導入へ)

2.  **Streamlit の状態管理: `st.session_state` 入門:**
    *   **なぜ `st.session_state` が必要か:** Streamlitのスクリプト再実行モデルと状態保持の課題。
    *   **`st.session_state` とは:** アプリケーションのセッション間で持続する辞書型のオブジェクト。
    *   **基本的な使い方:**
        *   存在確認と初期化: `if 'key' not in st.session_state:`
        *   値の代入: `st.session_state.key = value` or `st.session_state['key'] = value`
        *   値の参照: `st.session_state.key` or `st.session_state['key']`
    *   簡単なデモ: 数値をカウントアップするボタンとカウンター表示。

3.  **演習1: `st.session_state` を使った動的持ち物リスト (`src/lecture05/app_checklist.py`):**
    *   **目標:** 第4回の持ち物リストを改造し、ユーザーが新しいアイテムを追加できるようにする。
    *   **ステップ:**
        1.  持ち物リストを `st.session_state` で初期化する (例: `st.session_state.items = ["PC", "充電器"]`)。
        2.  `st.text_input` で新しいアイテム名を入力させる。
        3.  `st.button` を配置し、クリックされたら入力されたアイテムを `st.session_state.items` (リスト) に追加するロジックを実装する。
        4.  `st.session_state.items` を `for` ループで反復処理し、各アイテムを `st.checkbox` で表示する。
        5.  (発展) アイテムの削除機能 (例: 各チェックボックスの隣に削除ボタンを配置)。

4.  **Streamlit 基本ウィジェット (表示系):**
    *   `st.write()`: 最も汎用的な表示コマンド。文字列、数値、データフレームなどを表示。
    *   `st.header("ヘッダー")`, `st.subheader("サブヘッダー")`, `st.caption("キャプション")`: テキストに見出しや説明を追加。
    *   `st.markdown()`: Markdown記法を使って、太字、イタリック、リスト、リンク、画像などを表示。
        *   例: `st.markdown("これは **太字** で、これは *イタリック* です。詳細は[こちら](URL)。")`
    *   `st.button("ボタンラベル")`: アクションをトリガーする。クリックイベントで条件分岐 (`if`) を実行 (今回は `st.session_state` の更新と連動)。

5.  **Python基礎: 関数 (`def`) と辞書 (`dict`) の初歩:**
    *   **関数 (`def`):**
        *   同じ処理をまとめるメリット（再利用性、可読性向上）。
        *   簡単な関数の定義: `def function_name(arguments):`
        *   関数の呼び出し: `function_name(values)`
        *   例: 持ち物リストにアイテムを追加する処理を関数化する。
    *   **辞書 (`dict`):**
        *   キー(key)と値(value)のペアでデータを格納するデータ型: `{key1: value1, key2: value2}`。
        *   値へのアクセス: `my_dict[key1]`
        *   `st.session_state` も辞書のように振る舞うことを軽く説明。

## 準備物

*   **教員:**
    *   授業用スライド (`05_slide.md`, `05_slide.pdf`)
    *   Streamlit演習用スクリプト (`src/lecture05/app_checklist.py`, `src/lecture05/app_checklist_a.py`)
    *   出席認証コード (事前に`assets/CODE.csv`から取得)
*   **学生:**
    *   ノートPC
    *   インターネット接続
    *   Streamlit実行環境 (GitHubアカウント推奨、GitHub.devを使う場合)
    *   第4回までの演習ファイル (特に `src/lecture04/app.py`)

## 配布資料

*   講義スライド PDF (`lectures/05_Streamlit基本1_状態管理/05_slide.pdf`)
*   Streamlit演習スクリプト:
    *   `src/lecture05/app_checklist.py` (演習用スケルトン)
    *   `src/lecture05/app_checklist_a.py` (解答例)

## 次回予告

次回は、「Streamlit基本 (2): 多様な入力ウィジェット」として、`st.selectbox`, `st.multiselect`, `st.slider`, `st.number_input`, `st.text_input` (より詳しく) などを学び、ユーザーからの多様なデータ入力を受け付ける方法を探求します。また、Pythonの「関数」についてもさらに詳しく学びます。 