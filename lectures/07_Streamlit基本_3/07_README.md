# 第7回 Streamlit基本(3): レイアウト、状態管理、ファイル入力

## 1. 基本情報
- **時間:** 90分 (講義・演習含む、実質60-70分程度)
- **形式:** 講義 + ハンズオン演習
- **必要機材:** ノートPC、インターネット接続、Googleアカウント、GitHubアカウント

## 2. 授業の目標
- Streamlitのレイアウト機能 (`st.columns`, `st.expander`, `st.sidebar`) を理解し、使いこなせるようになる。
- Streamlitのセッション状態管理 (`st.session_state`) の概念と使い方を習得する。
- Streamlitのフォーム機能 (`st.form`, `st.form_submit_button`) を理解し、複数の入力をまとめて扱えるようになる。
- Streamlitのファイルアップロード機能 (`st.file_uploader`) を用いて、ユーザーがファイルをアップロードし、その情報を表示できるようになる。

## 3. タイムスケジュール (目安)
| 時間          | 内容                                     | 詳細                                                                                               |
|---------------|------------------------------------------|----------------------------------------------------------------------------------------------------|
| 00:00 - 00:05 | 前回の復習と本日の目標                     | Streamlitウィジェットの振り返り、本日のゴール説明                                                        |
| 00:05 - 00:25 | レイアウト機能                           | `st.sidebar`, `st.columns`, `st.expander` の使い方デモと解説、簡単な演習                               |
| 00:25 - 00:45 | 状態管理 (`st.session_state`)             | `st.session_state` の必要性、基本的な使い方（初期化、値の更新、コールバック関数との連携の初歩）、演習           |
| 00:45 - 01:05 | フォーム (`st.form`)                      | `st.form` と `st.form_submit_button` を使った複数入力の一括処理、演習                                  |
| 01:05 - 01:20 | ファイルアップロード (`st.file_uploader`)    | `st.file_uploader` を使ったファイル選択、アップロードされたファイル情報の表示（ファイル名、種類、サイズ）、簡単な演習 |
| 01:20 - 01:25 | 質疑応答と次回予告                       |                                                                                                    |
| 01:25 - 01:30 | まとめと演習課題の提示                   |                                                                                                    |

## 4. 授業内容の詳細

### a. レイアウト機能
- **`st.sidebar`**: アプリケーションの主要なコンテンツから分離して、ナビゲーションやコントロールを配置するためのサイドバーを作成します。
- **`st.columns`**: 画面を複数の列に分割し、コンテンツを並べて表示します。各列の幅も調整可能です。
- **`st.expander`**: クリックすることでコンテンツの表示/非表示を切り替えられるコンテナを作成します。詳細情報やオプション設定を隠しておくのに便利です。

### b. 状態管理 (`st.session_state`)
- Streamlitアプリはスクリプトが上から下に再実行されるたびに変数が初期化されてしまうため、ユーザーの操作や入力値を保持するためには状態管理が必要です。
- `st.session_state` は、ウィジェットの値やアプリ内の変数をインタラクション間で保持するための仕組みです。
- 値の初期化、アクセス、更新方法、コールバック関数と連携した状態更新の基本を学びます。

### c. フォーム (`st.form`)
- 複数の入力ウィジェットをグループ化し、送信ボタン (`st.form_submit_button`) が押されたときに一度に全ての入力値を処理するための仕組みです。
- フォーム外のウィジェット操作では再実行がトリガーされますが、フォーム内のウィジェットは送信ボタンが押されるまで再実行をトリガーしません。これにより、意図しない再実行を防ぎ、ユーザー体験を向上させます。

### d. ファイルアップロード (`st.file_uploader`)
- ユーザーがローカルからファイルをアップロードできるようにするウィジェットです。
- アップロードされたファイルは `UploadedFile` オブジェクトとして扱われ、ファイル名、ファイルタイプ、サイズなどの情報を取得したり、内容を読み取ったりすることができます。
- 簡単な例として、アップロードされたファイル名やサイズを表示する方法を学びます。

## 5. 準備物
- **教員側:**
    - 講義スライド (`07_slide.md`, `07_slide.pdf`)
    - Colab講義ノートブック (`07_lecture.ipynb`)
    - Colab演習ノートブック (`07_exercises.ipynb`)
    - Colab解答ノートブック (`07_answers.ipynb`)
    - Streamlit演習用スクリプト (`src/lecture07/app_layout.py`, `src/lecture07/app_session.py`, `src/lecture07/app_form.py`, `src/lecture07/app_upload.py`)
    - Streamlit解答用スクリプト (`src/lecture07/app_layout_a.py`, `src/lecture07/app_session_a.py`, `src/lecture07/app_form_a.py`, `src/lecture07/app_upload_a.py`)
- **学生側:**
    - ノートPC
    - Googleアカウント (Google Colaboratory用)
    - GitHubアカウント (Streamlit Cloud連携用、またはコード共有用)
    - Webブラウザ (Google Chrome推奨)
    - 事前インストール済みのPython環境 (ローカルでStreamlitを動かす場合)

## 6. 配布資料
- `lectures/07_Streamlit基本_3/07_README.md` (このファイル)
- `lectures/07_Streamlit基本_3/07_slide.pdf`
- `lectures/07_Streamlit基本_3/07_lecture.ipynb` (作成しない場合は削除)
- `lectures/07_Streamlit基本_3/07_exercises.ipynb` (作成しない場合は削除)
- `lectures/07_Streamlit基本_3/07_answers.ipynb` (作成しない場合は削除)
- `src/lecture07/app_lecture.py`
- `src/lecture07/app_lecture_a.py`

## 7. 次回予告
- **第8回: 課題演習 (1) と GitHub**
    - これまでの知識を活用した総合的なStreamlitアプリ作成演習
    - 作成したアプリをGitHubへアップロードする方法
    - 補足: `st.image`, `st.video` の使い方 