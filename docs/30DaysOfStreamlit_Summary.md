# #30DaysOfStreamlit チャレンジ概要 (Day 1-3)

## Day 1: ローカル開発環境の設定

*   **内容:** 
    *   Conda を使用した Python 仮想環境の作成 (`conda create`, `conda activate`)
    *   Streamlit ライブラリのインストール (`pip install streamlit`)
    *   Streamlit デモアプリの起動 (`streamlit hello`)
*   **主な Streamlit 関数/コマンド:** `streamlit hello` (Streamlit CLI コマンド)

## Day 2: 最初のStreamlitアプリの構築

*   **内容:** 
    *   IDE (統合開発環境) で Python ファイル (`streamlit_app.py`) を作成
    *   "Hello world!" を表示する簡単な Streamlit アプリを作成し実行 (`streamlit run`)
*   **主な Streamlit 関数:** `st.write`

## Day 3: `st.button`

*   **内容:** 
    *   ボタンウィジェット (`st.button`) を使用
    *   ボタンが押されたかどうか (`if st.button(...)`) で表示するメッセージを条件分岐 (`if`/`else`) させるアプリを作成
*   **主な Streamlit 関数:** `st.button`, `st.write`, `st.header` 

## Day 4: Ken Jee と一緒に Streamlit アプリを構築

*   **内容:** 
    *   データサイエンティスト Ken Jee 氏の YouTube 動画 ([https://www.youtube.com/watch?v=Yk-unX4KnV4](https://www.youtube.com/watch?v=Yk-unX4KnV4)) を視聴し、Streamlit アプリ構築プロセスを学ぶ。
*   **主な Streamlit 関数:** (動画内で紹介される関数に依存)

## Day 5: `st.write`

*   **内容:** 
    *   `st.write` を使ってテキスト、数値、Pandas DataFrame、Altair チャートなどを表示する様々な方法を試す。
*   **主な Streamlit 関数:** `st.write`, `st.header`

## Day 6: Streamlit アプリを GitHub にアップロード

*   **内容:** 
    *   GitHub アカウントの作成またはサインイン。
    *   新しい GitHub リポジトリを作成。
    *   作成した Streamlit アプリのファイル (例: `streamlit_app.py`, `requirements.txt`) を GitHub リポジトリにアップロードする手順。
*   **主な Streamlit 関数:** (Streamlit 関数は直接使用しないが、デプロイの準備段階)

## Day 7: Streamlit Community Cloud を使ってアプリをデプロイ

*   **内容:** 
    *   Streamlit Community Cloud ([https://streamlit.io/cloud](https://streamlit.io/cloud)) の概要とサインアップ方法。
    *   GitHub リポジトリを選択し、ブランチとファイルを選んでデプロイする手順。
*   **主な Streamlit 関数:** (Streamlit 関数は直接使用しない) 

## Day 8: `st.slider`

*   **内容:** 
    *   スライダーウィジェット (`st.slider`) を使って、数値（整数、浮動小数点数）、日付、時間、日時データを受け付ける方法を学ぶ。
    *   単一の値のスライダー、範囲（最小値・最大値）を指定するスライダー、時間範囲のスライダー、日時スライダーの例を試す。
*   **主な Streamlit 関数:** `st.slider`, `st.write`, `st.header`, `st.subheader` 

## Day 9: `st.line_chart`

*   **内容:** 
    *   `st.line_chart` を使って折れ線グラフを表示する方法を学ぶ。
    *   NumPy でランダムな数値を生成し、Pandas DataFrame を作成して、それを `st.line_chart` に渡してグラフを表示する。
    *   `st.altair_chart` との関係性（`st.line_chart` は `st.altair_chart` の簡易版であること）に触れる。
*   **主な Streamlit 関数:** `st.line_chart`, `st.header` 

## Day 10: `st.selectbox`

*   **内容:** 
    *   セレクトボックスウィジェット (`st.selectbox`) を使って、定義済みの選択肢（例: 'Blue', 'Red', 'Green'）からユーザーに1つ選ばせる方法を学ぶ。
    *   選択された値を `st.write` で表示する。
*   **主な Streamlit 関数:** `st.selectbox`, `st.write`, `st.header` 

## Day 11: `st.multiselect`

*   **内容:** 
    *   マルチセレクトウィジェット (`st.multiselect`) を使って、定義済みの選択肢（例: 色）からユーザーに複数選択させる方法を学ぶ。
    *   デフォルトで選択されている項目を指定する方法も含む。
    *   選択されたオプションのリストを `st.write` で表示する。
*   **主な Streamlit 関数:** `st.multiselect`, `st.write`, `st.header`

## Day 12: `st.checkbox`

*   **内容:**
    *   チェックボックスウィジェット (`st.checkbox`) を表示する方法を学ぶ。
    *   チェックボックスの状態 (`True`/`False`) を使用して、条件に応じて異なるメッセージを表示する。
*   **主な Streamlit 関数:** `st.checkbox`, `st.write`, `st.header`

## Day 13: クラウド開発環境の利用

*   **内容:**
    *   GitPod などのクラウド開発環境を紹介。
    *   GitHub リポジトリから直接開発環境を立ち上げる方法について説明。
*   **主な Streamlit 関数:** (Streamlit 関数は直接使用しない)

## Day 14: Streamlit Components

*   **内容:**
    *   Streamlit の機能を拡張するサードパーティ製 Python モジュールである Streamlit Components を紹介。
    *   `streamlit-pandas-profiling` コンポーネントを例に、インストールと使用方法を説明。
*   **主な Streamlit 関数:** `st.header` (およびコンポーネント固有の関数 `st_profile_report`)

## Day 15: `st.latex`

*   **内容:**
    *   LaTeX 形式で数式を表示する `st.latex` コマンドの使用方法を学ぶ。
*   **主な Streamlit 関数:** `st.latex`, `st.header`

## Day 16: Streamlit アプリのテーマカスタマイズ

*   **内容:**
    *   `.streamlit/config.toml` ファイルを使用して Streamlit アプリのテーマ（色、フォントなど）をカスタマイズする方法を学ぶ。
*   **主な Streamlit 関数:** `st.title`, `st.write`, `st.code`, `st.sidebar.slider`

## Day 17: `st.secrets`

*   **内容:**
    *   API キーやデータベースパスワードなどの機密情報を安全に管理するための `st.secrets` の使い方を学ぶ。
    *   Streamlit Community Cloud でのシークレット管理と、ローカルでの `.streamlit/secrets.toml` ファイルの使用について説明。
*   **主な Streamlit 関数:** `st.secrets`, `st.title`, `st.write`

## Day 18: `st.file_uploader`

*   **内容:**
    *   ファイルアップロードウィジェット (`st.file_uploader`) を表示し、ユーザーがアップロードしたファイル（例: CSV）を処理する方法を学ぶ。
    *   アップロードされた CSV ファイルを Pandas DataFrame として読み込み、表示および記述統計量を計算する例。
*   **主な Streamlit 関数:** `st.file_uploader`, `st.title`, `st.subheader`, `st.write`, `st.info`

## Day 19: Streamlit アプリのレイアウト

*   **内容:**
    *   Streamlit アプリのレイアウトを構成するためのコマンドを学ぶ:
        *   `st.set_page_config(layout="wide")`: ページ幅を広げる
        *   `st.sidebar`: サイドバーにウィジェットを配置
        *   `st.expander`: 折りたたみ可能なコンテナを作成
        *   `st.columns`: カラム（列）を作成してコンテンツを配置
*   **主な Streamlit 関数:** `st.set_page_config`, `st.sidebar.header`, `st.sidebar.text_input`, `st.sidebar.selectbox`, `st.expander`, `st.columns`, `st.write`, `st.image`, `st.header`, `st.title`

## Day 20: Streamlit に関する Tech Twitter Space

*   **内容:**
    *   Francesco Ciulla 氏がホストする Streamlit に関する Twitter Space の告知。
*   **主な Streamlit 関数:** (Streamlit 関数は直接使用しない)

## Day 21: `st.progress`

*   **内容:**
    *   処理の進行状況を視覚的に表示するプログレスバー (`st.progress`) の使い方を学ぶ。
    *   `time.sleep` とループを使ってプログレスバーが更新される様子をデモンストレーション。
*   **主な Streamlit 関数:** `st.progress`, `st.title`, `st.expander`, `st.write`, `st.balloons`

## Day 22: `st.form`

*   **内容:**
    *   複数のウィジェット入力をまとめて送信ボタンで処理するフォーム (`st.form`) の作成方法を学ぶ。
    *   `with` 記法とオブジェクト記法でのフォームの使い方。
    *   フォーム内のウィジェット操作ではアプリが再実行されず、送信ボタンが押されたときにまとめて処理される利点を説明。
    *   フォーム内では `st.form_submit_button` が必須であること、`st.button` などは配置できない制約に触れる。
*   **主な Streamlit 関数:** `st.form`, `st.form_submit_button`, `st.selectbox`, `st.select_slider`, `st.checkbox`, `st.slider`, `st.title`, `st.header`, `st.subheader`, `st.markdown`, `st.write`

## Day 23: `st.experimental_get_query_params`

*   **内容:**
    *   ユーザーのブラウザ URL から直接クエリパラメータを取得する `st.experimental_get_query_params` (実験的機能) の使い方を学ぶ。
    *   URL にパラメータを追加してアプリの動作を変える例。
*   **主な Streamlit 関数:** `st.experimental_get_query_params`, `st.title`, `st.expander`, `st.write`, `st.header`, `st.markdown`

## Day 24: `st.cache`

*   **内容:**
    *   アプリのパフォーマンスを最適化するためのキャッシュ機能 (`st.cache` デコレータ) を学ぶ。
    *   関数の入力、外部変数、関数本体などを基に結果をキャッシュし、次回呼び出し時に再計算をスキップする仕組みを説明。
    *   キャッシュを使用した場合としない場合の実行速度の違いを比較。
*   **主な Streamlit 関数:** `st.cache`, `st.title`, `st.subheader`, `st.write`, `st.info`

## Day 25: `st.session_state`

*   **内容:**
    *   ユーザーセッション内で変数を保持し、再実行間で状態を共有するための `st.session_state` を学ぶ。
    *   コールバック関数と組み合わせて状態を操作する方法。
    *   ポンドとキログラムの重量変換アプリを例に、入力ウィジェットの `on_change` コールバックで `st.session_state` を更新する実装を説明。
*   **主な Streamlit 関数:** `st.session_state`, `st.number_input`, `st.title`, `st.header`, `st.columns`, `st.write`

## Day 26: API を利用したアプリ構築 (Bored API)

*   **内容:**
    *   外部 API (Bored API) を利用して Streamlit アプリを構築する方法を学ぶ。
    *   `requests` ライブラリを使って API からデータを取得し、その結果をアプリに表示する。
    *   ユーザー入力に基づいて API リクエストを動的に変更する例。
*   **主な Streamlit 関数:** `st.title`, `st.sidebar.header`, `st.sidebar.selectbox`, `st.columns`, `st.expander`, `st.write`, `st.header`, `st.info`, `st.metric`

## Day 27: Streamlit Elements を使ったダッシュボード構築

*   **内容:**
    *   サードパーティコンポーネント `streamlit-elements` を紹介。
    *   Material UI ウィジェット、Monaco エディタ、Nivo チャートなどを使って、ドラッグ＆ドロップやリサイズが可能なインタラクティブなダッシュボードを作成する方法を学ぶ。
    *   `dashboard.Grid`, `mui.Card`, `editor.Monaco`, `nivo.Bump`, `sync`, `lazy` などの `streamlit-elements` の主要な機能を使用。
*   **主な Streamlit 関数:** `st.set_page_config`, `st.sidebar.title`, `st.sidebar.header`, `st.sidebar.write`, `st.sidebar.text_input`, `st.session_state` (および `streamlit-elements` の関数群)

## Day 28: `streamlit-shap`

*   **内容:**
    *   SHAP (SHapley Additive exPlanations) プロットを Streamlit アプリ内で表示するためのコンポーネント `streamlit-shap` を紹介。
    *   機械学習モデル (XGBoost) の予測結果を説明するために、SHAP 値を計算し、Waterfall プロット、Beeswarm プロット、Force プロットを表示する方法を学ぶ。
*   **主な Streamlit 関数:** `st.set_page_config`, `st.experimental_memo`, `st.title`, `st.expander`, `st.markdown`, `st.header`, `st.dataframe`, `st.write`, `st_shap` (コンポーネント関数)

## Day 29: Hugging Face を使ったゼロショットテキスト分類器

*   **内容:**
    *   Hugging Face の API Inference と Distilbart モデルを利用して、事前学習なしでテキスト分類を行うゼロショット学習分類器を Streamlit で構築する方法を紹介 (外部ブログ記事へのリンク)。
    *   ユーザーが定義したラベルに基づいてテキストを分類する。
*   **主な Streamlit 関数:** (外部ブログ記事の内容による)

## Day 30: Streamlit アプリ作成の技術 (YouTube サムネイル抽出)

*   **内容:**
    *   これまでの学習内容を応用し、実用的な Streamlit アプリ (`yt-img-app`) を作成するプロセスを示す。
    *   YouTube 動画の URL からサムネイル画像を取得するアプリを構築。
    *   ユーザー入力の受け付け、URL の処理、カスタム関数による画像取得と表示の手順を説明。
*   **主な Streamlit 関数:** `st.title`, `st.header`, `st.expander`, `st.write`, `st.sidebar.header`, `st.sidebar.selectbox`, `st.text_input`, `st.image`