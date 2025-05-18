---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第8回：課題演習(1) と GitHub: 好きなテーマでアプリを作ろう！"
size: 16:9
style: |
  section {
    font-family: 'Arial', sans-serif; /* 全体のフォントを指定 */
    padding: 40px;
  }
  h1, h2, h3 {
    color: #333; /* 見出しの色 */
  }
  h1 {
    font-size: 2.5em; /* H1のフォントサイズ */
  }
  h2 {
    font-size: 1.8em; /* H2のフォントサイズ */
  }
  h3 {
    font-size: 1.4em; /* H3のフォントサイズ */
  }
  ul, ol {
    font-size: 1.1em; /* リストのフォントサイズ */
    line-height: 1.6;
  }
  code {
    font-family: 'Courier New', Courier, monospace; /* コードのフォント */
    background-color: #f4f4f4; /* コードブロックの背景色 */
    padding: 2px 4px;
    border-radius: 4px;
  }
  .lead h1 {
    color: white;
    text-align: center;
  }
  .lead p {
    text-align: center;
    color: white;
    font-size: 1.2em;
  }
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
---

<!-- _class: lead -->
# 第8回 課題演習(1) と GitHub
## 好きなテーマでアプリを作ろう！

担当: [担当者名]
**出席認証コード: 1474**
授業資料: `https://x.gd/NoqkC` (短縮URL) または Teamsで共有

---

## 今日の流れ (90分)

1.  **はじめに・課題説明 (10分)**
    *   本日の目標
    *   演習テーマの紹介
2.  **課題演習: アプリ開発 (40-50分)**
    *   好きなテーマを選んでStreamlitアプリを開発！
    *   `st.image` や `st.video` も使ってみよう
3.  **GitHub入門 (20分)**
    *   作成したアプリをGitHubに保存
4.  **まとめ・次回予告 (5-10分)**

---

## 1. 本日の目標

*   **Streamlit総合演習**:
    *   複数のテーマから1つを選び、オリジナルのStreamlitアプリを設計・実装する。
    *   ウィジェット、レイアウト、状態管理などを効果的に活用！
*   **画像・動画の活用**:
    *   `st.image` と `st.video` の使い方を理解し、アプリに組み込む。
*   **GitHub入門**:
    *   基本的な使い方を理解し、コードをGitHubに保存・管理する。

---

## 2. 演習課題: 好きなテーマを選んでアプリを開発！

**5つのテーマから1つを選んで挑戦！**
演習用テンプレートファイル (`app_テーマ名.py`) が `src/lecture08/` にあります。

1.  **今日のラッキーカラー診断アプリ** (`app_lucky_color.py`)
2.  **おすすめカフェ/ランチ スタイル診断** (`app_cafe_reco.py`)
3.  **かんたん自己紹介カード作成ツール** (`app_profile_card.py`)
4.  **シンプルなToDoリスト** (`app_todo_list.py`)
5.  **おみくじアプリ** (`app_omikuji.py`)

---

### テーマ1: 今日のラッキーカラー診断アプリ

*   **概要:** 星座や好きな数字で今日のラッキーカラーとアドバイスを表示。
*   **主な機能:** `st.selectbox`, `st.button`, `st.write`, `st.image`, `if`/`elif` や辞書。
*   **難易度:** ★★★★★ (非常に容易)
*   **演習ファイル:** `src/lecture08/app_lucky_color.py`
*   **ヒント:** 結果の対応表を辞書で作ると楽！

![ラッキーカラーイメージ](https://via.placeholder.com/300x200/FFD700/000000?Text=Lucky+Color+App)
<!-- 画像は適宜差し替え -->

---

### テーマ2: おすすめカフェ/ランチ スタイル診断

*   **概要:** 気分や予算からおすすめのカフェ/ランチスタイルと関連画像を表示。
*   **主な機能:** `st.radio`, `st.slider`, `st.button`, `st.write`, `st.image`, `if`/`elif`。
*   **難易度:** ★★★★☆ (比較的容易)
*   **演習ファイル:** `src/lecture08/app_cafe_reco.py`
*   **ヒント:** 複数の入力の組み合わせで結果を分岐。質問は3つ程度に。

![カフェイメージ](https://via.placeholder.com/300x200/8B4513/FFFFFF?Text=Cafe+Recomendation)
<!-- 画像は適宜差し替え -->

---

### テーマ3: かんたん自己紹介カード作成ツール

*   **概要:** フォームで情報入力＆画像アップロードし、カードを表示。
*   **主な機能:** `st.form`, `st.text_input`, `st.file_uploader`, `st.image`, `st.columns`。
*   **難易度:** ★★★★☆ (比較的容易。ファイルアップロードとレイアウトが鍵)
*   **演習ファイル:** `src/lecture08/app_profile_card.py`
*   **ヒント:** `st.form` で入力、`st.columns` でレイアウトを整える。

![自己紹介カードイメージ](https://via.placeholder.com/400x250/4682B4/FFFFFF?Text=Profile+Card+Creator)
<!-- 画像は適宜差し替え -->

---

### テーマ4: シンプルなToDoリスト

*   **概要:** タスク追加、完了チェック、削除ができるToDoリスト。
*   **主な機能:** `st.text_input`, `st.button`, `st.checkbox`, `st.session_state`。
*   **難易度:** ★★★☆☆ (やや注意。`st.session_state` でリスト管理がポイント)
*   **演習ファイル:** `src/lecture08/app_todo_list.py`
*   **ヒント:** タスクリストを `st.session_state` で管理。コールバック関数も活用。

![ToDoリストイメージ](https://via.placeholder.com/300x200/32CD32/FFFFFF?Text=ToDo+List)
<!-- 画像は適宜差し替え -->

---

### テーマ5: おみくじアプリ

*   **概要:** ボタンでランダムに運勢、メッセージ、関連画像を表示。
*   **主な機能:** `st.button`, `st.write`, `st.image`, `random.choice`。
*   **難易度:** ★★★★★ (非常に容易)
*   **演習ファイル:** `src/lecture08/app_omikuji.py`
*   **ヒント:** 運勢結果のリストを事前に用意し、ランダムに選択。

![おみくじイメージ](https://via.placeholder.com/300x200/FF6347/FFFFFF?Text=Omikuji+App)
<!-- 画像は適宜差し替え -->

---

### 開発の進め方 & Tips

1.  **テーマ選択**: `08_README.md` で詳細を確認し、1つ選びましょう。
2.  **ファイルを開く**: `src/lecture08/` 内の該当 `.py` ファイルを開きます。
3.  **ヒントを読む**: ファイル冒頭のコメントやヒントをチェック。
4.  **実装開始**: 少しずつ機能を実装し、`streamlit run あなたのファイル名.py` で確認。
5.  **画像/動画**: `st.image` や `st.video` でアプリを魅力的に！
    *   `st.image("画像URLやファイルパス", caption="説明", width=ピクセル数)`
    *   `st.video("動画URLやファイルパス")`
6.  **困ったら**: README、過去資料、教員へ質問！

---

## 3. GitHubであなたのアプリを保存・管理しよう！

作成した（または作成途中の）アプリのコードをGitHubに保存します。
来週、このリポジトリを使ってアプリを**世界に公開**します！

### なぜGitHub?
*   **バックアップ & バージョン管理**: コードを安全に保管、変更履歴を記録。
*   **共有 & 公開**: あなたの作品を世界に見せる第一歩。

---

### GitHub基本操作ステップ (GitHub.dev を使ってみよう)

1.  **GitHubアカウント**: 持っていますか？ (なければ [github.com/join](https://github.com/join) で作成)
2.  **新しいリポジトリ作成**:
    *   GitHub上で新しいリポジトリを作成 (例: `my-streamlit-cource`)。
    *   **Public** を選択、「Add a README file」にチェック推奨。
3.  **GitHub.devでファイル操作**:
    *   リポジトリURLの `.com` を `.dev` に変えてアクセス！
        (例: `https://github.dev/あなたのユーザー名/リポジトリ名`)
    *   エディタが開くので、`src/lecture08/` のあなたの `.py` ファイルの中身をコピー。
    *   GitHub.dev上で新しいファイルとして貼り付け、保存 (例: `app_omikuji.py`)。
    *   画像などもドラッグ＆ドロップで追加可能！
4.  **コミット & プッシュ**:
    *   左側「ソース管理」タブ → メッセージ入力 (例:「おみくじアプリ初版」) → 「コミットとプッシュ」。

---

## 4. まとめと次回予告

*   **今日やったこと**:
    *   好きなテーマを選んでStreamlitアプリ開発に挑戦！
    *   `st.image` / `st.video` の使い方を確認。
    *   GitHubに初めてのコードを保存。
*   **次回: 第9回 課題演習(2) と デプロイ**
    *   今回作ったアプリをさらにパワーアップ！
    *   **Streamlit Community Cloud** を使って、あなたのアプリを世界に公開します！

---

## 質疑応答

何か質問はありますか？

今日の演習で難しかったところ、うまくいったところなど、ぜひ教えてください。
完成したアプリをGitHubにアップロードできたら、URLを共有するのも良いでしょう！ (任意)

お疲れ様でした！ 