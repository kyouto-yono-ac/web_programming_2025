---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第14回：最終課題演習(2) - 制作完成・デプロイ"
size: 16:9
style: |
  section { font-size: 1.2em; }
  h1 { font-size: 1.8em; }
  h2 { font-size: 1.5em; }
  h3 { font-size: 1.3em; }
  table { font-size: 0.9em; }
  code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 0.8em;
    background-color: #f0f0f0;
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
  pre code {
    display: block;
    padding: 0.5em;
    overflow-x: auto;
    font-size: 0.7em;
  }
  .lead h1 {
    font-size: 2.4em;
  }
  .lead h2 {
    font-size: 1.8em;
  }
  .lead p {
    font-size: 1.4em;
  }
  .small {
    font-size: 0.8em;
  }
  .highlight {
    background-color: #ffeb3b;
    padding: 0.2em 0.4em;
    border-radius: 3px;
  }
  ul, ol {
    font-size: 1.0em;
  }
  li {
    margin-bottom: 0.3em;
  }
---

<!-- _class: lead -->

# 第14回
## 最終課題演習(2)
### 制作完成・デプロイ

**アプリを完成させ、公開しよう！**

出席認証コード: **4495**

---

## 📋 本日の目標

1. **機能完成**: 前回から続けて、アプリの機能を完成させる
2. **デプロイ**: GitHubアップロード → Streamlit Community Cloudでの公開
3. **動作確認**: 公開されたアプリの動作テスト・バグ修正

---

## 🎯 今日の授業の流れ

### タイムスケジュール
| 時間 | 内容 |
|------|------|
| 00:00-00:05 | 前回の進捗確認・本日の目標説明 |
| 00:05-01:10 | 制作の続行・機能完成 |
| 01:10-01:20 | GitHubアップロード・デプロイ |
| 01:20-01:25 | 動作確認・バグ修正 |
| 01:25-01:30 | 次回準備・まとめ |

### 本日の成果物
- **完成したアプリ**: 全機能が動作するアプリ
- **公開URL**: 誰でもアクセスできるWebアプリ
- **アプリの説明シート**: [アプリの説明シート](https://forms.gle/AYQNMr4Apck77H3p7)に記入してください：


---

## 🚀 GitHubアップロード手順

### 1. リポジトリの準備
1. **GitHub.com**で新しいリポジトリを作成
   - リポジトリ名: `web-programming-2025-final-project`（中間の区別できれば何でも大丈夫です）
   - **Public設定**
   - 「Add a README file」にチェック

### 2. 必要ファイルの準備（※必ずしもこの構成でなくてもいいです）
```
your-project/
├── app.py              # メインアプリファイル
├── requirements.txt    # 依存ライブラリ
├── data/              # データファイル（必要に応じて）
│   └── your_data.csv
└── README.md          # プロジェクト説明
```

### 3. requirements.txtの作成
```txt
streamlit
pandas
plotly
google-generativeai
```

---

## 🌐 Streamlit Community Cloudでのデプロイ

### 1. デプロイ手順
1. **Streamlit Community Cloud**（https://share.streamlit.io/）にアクセス
2. GitHubアカウントでログイン
3. 「New app」をクリック
4. リポジトリ・ブランチ・メインファイルを選択
5. 「Deploy!」をクリック

### 2. 設定項目
- **Repository**: 作成したGitHubリポジトリ
- **Branch**: main（通常はデフォルト）
- **Main file path**: app.py（メインファイル名）
- **App URL**: 自動生成される公開URL　**URLはわかりやすいものに変えてください**

### 3. Secretsの設定（Gemini API使用の場合）
1. デプロイ後の設定画面で「Secrets」を選択
2. 以下の形式でAPIキーを設定：
```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

deployは以前の授業資料を参考にしてください：
**https://docs.google.com/document/d/1jCVlQHL6o425FxVXUZdZk-LgYa5wydISlqu52cbkbyk/edit?usp=drive_link**


---

## 🔧 よくある問題と解決方法

### 問題1: モジュールが見つからない
```
ModuleNotFoundError: No module named 'plotly'
```
**解決方法**: `requirements.txt`に必要なライブラリを追加

### 問題2: APIキーが読み込めない
```
KeyError: 'GEMINI_API_KEY'
```
**解決方法**: Streamlit Community CloudのSecretsを正しく設定

### 問題3: データファイルが見つからない
```
FileNotFoundError: No such file or directory: 'data.csv'
```
**解決方法**: データファイルをリポジトリに含める、またはパスを確認

### 問題4: アプリが起動しない
**解決方法**: 
- アプリログを確認
- 最小限のコードで動作確認
- エラーメッセージを詳しく確認

---

## 📞 サポート・質問

### 授業中のサポート
- **技術的な問題**: デプロイやエラーの解決
- **機能改善**: UI/UXの向上アドバイス
- **最終調整**: 完成度を高めるための助言

### 質問・相談方法
- **授業中の質問**: 制作中の直接質問
- **manabaの掲示板**: スレッドを立てて質問
- **スレッドでの情報共有**: 他の学生との情報交換

### 次回の準備
- **発表準備**: 3分間の発表内容を考える
- **デモ練習**: アプリの操作を練習する
- **発表資料**: 必要に応じて補助資料を準備

---

## 🎉 お疲れ様でした！

### 本日の達成事項
- ✅ **アプリ完成**: 全機能が動作するアプリが完成
- ✅ **Web公開**: 誰でもアクセスできるURLが生成
- ✅ **実践経験**: 実際の開発・デプロイ経験を積んだ

### 次回に向けて
- **発表準備**: 3分間で魅力的にアプリを紹介
- **デモ練習**: スムーズな操作ができるよう練習
- **工夫点整理**: 技術的な工夫や苦労した点を整理

### 素晴らしい作品の完成を楽しみにしています！

**次回は皆さんの作品発表会です。お疲れ様でした！**

---

## 📝 授業アンケートのお願い

### 授業評価アンケートの実施
- **実施場所**: **UNIPA**の授業評価画面
- **所要時間**: **約10分**で完了
- **回答期限**: 授業終了後、速やかに回答をお願いします

### アンケートの目的
- **授業改善**: 皆さんの意見を今後の授業に反映
- **学習効果**: 授業内容や進行方法の改善点を把握
- **サポート向上**: より良い学習環境の提供

### 回答方法
1. **UNIPA**にログイン
2. **授業評価**のメニューを選択
3. **WebプログラミングI**の評価を選択
4. 各項目について率直な意見を記入

### 特に評価いただきたい点
- **最終課題演習**: 3回構成の演習の有効性
- **技術統合**: 学んだ技術を組み合わせる学習効果
- **デプロイ体験**: 実際にWebアプリを公開する経験
- **サポート体制**: 質問・相談のしやすさ

### お願い
- **率直な意見**: 良い点・改善点を遠慮なく記入
- **具体的な内容**: 具体的な改善提案があれば記入
- **建設的な意見**: 今後の授業向上につながる内容

**皆さんの貴重な意見をお待ちしています！** 