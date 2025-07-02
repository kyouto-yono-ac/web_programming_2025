# 第12回 授業概要：LLM活用 - Gemini APIとチャットボット開発

## 1. 基本情報
- **授業回:** 第12回
- **タイトル:** LLM活用 - Gemini APIとチャットボット開発
- **認証コード:** 4802
- **時間:** 90分
- **形式:** 講義 + 実習
- **必要機材:**
    - **教員:** PC、プロジェクター
    - **学生:** PC (Streamlit実行環境、インターネット接続)

## 2. 授業の目標
### 🎯 最終的な成果物
**「忍者キャラクターチャットボット」**
- Gemini APIを活用したAI搭載チャットボット
- 個性豊かなキャラクター設定による差別化された会話
- 既存アプリケーションへのAI機能統合

### 具体的な学習目標
1. **Gemini API**: Google AI Studioでの取得方法とAPIキー管理
2. **チャットボット基礎**: Streamlitでの基本的なチャットインターフェース構築
3. **プロンプトエンジニアリング**: キャラクター設定による一貫性のある応答生成
4. **既存アプリ改良**: 外部リポジトリをベースにした機能拡張
5. **セキュリティ**: APIキーの安全な管理とベストプラクティス

## 3. タイムスケジュール（90分）
| 時間 | 内容 | 詳細 |
| --- | --- | --- |
| 20分 | **Part 1: Gemini API取得と設定** | Google AI Studio、APIキー取得、セキュリティ説明、基本的な使い方 |
| 35分 | **Part 2: 基本チャットボットの作成** | Streamlitチャット機能、メッセージ履歴管理、エラーハンドリング |
| 35分 | **Part 3: キャラクターチャット機能の実装** | リポジトリクローン、プロンプトエンジニアリング、キャラクター実装 |

## 4. 授業内容の詳細

### Part 1: Gemini API取得と設定（20分）
#### 目標：Gemini APIの基本環境を構築し、安全に使用できる

**1-1. Google AI Studio の利用（8分）**
- LLM（大規模言語モデル）とGeminiの概要説明
- Google AI Studio（https://aistudio.google.com/）アクセス
- Googleアカウントでのログイン
- 講師によるAPIキー取得のデモンストレーション

**1-2. セキュリティベストプラクティス（7分）**
```bash
# 1. .streamlit/secrets.tomlファイルを作成
mkdir .streamlit
echo 'GEMINI_API_KEY = "your_api_key_here"' > .streamlit/secrets.toml
```

```python
# 2. Streamlit Secretsでの管理（推奨）
import streamlit as st
api_key = st.secrets["GEMINI_API_KEY"]

# 絶対にやってはいけないこと
api_key = "AIzaSy..."  # コードに直接書く
```

**重要:** `.streamlit/secrets.toml`ファイルは自動的に`.gitignore`に含まれるため、安全です。

**1-3. 基本的な使い方（5分）**
```python
import google.generativeai as genai

# API設定
genai.configure(api_key=api_key)

# モデル初期化とテキスト生成
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("こんにちは")
print(response.text)
```

### Part 2: 基本チャットボットの作成（35分）
#### 目標：Streamlitで動作するシンプルなチャットボットを完成させる

**2-1. Streamlitチャット機能の実装（15分）**
```python
import streamlit as st

# セッション状態でメッセージ履歴を管理
if "messages" not in st.session_state:
    st.session_state.messages = []

# 過去のメッセージを表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザー入力
prompt = st.chat_input("メッセージを入力")
if prompt:
    # ユーザーメッセージを追加・表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
```

**2-2. AI応答の生成と統合（12分）**
```python
# AI応答の生成・表示
with st.chat_message("assistant"):
    response = model.generate_content(prompt)
    ai_response = response.text
    st.markdown(ai_response)

# AI応答を履歴に追加
st.session_state.messages.append({"role": "assistant", "content": ai_response})
```

**2-3. エラーハンドリングとUI改善（8分）**
```python
try:
    response = model.generate_content(prompt)
    ai_response = response.text
except Exception as e:
    ai_response = "申し訳ありません。エラーが発生しました。"
    st.error(f"エラー: {e}")

# UIの改善
with st.sidebar:
    if st.button("会話履歴をクリア"):
        st.session_state.messages = []
        st.rerun()
```

### Part 3: キャラクターチャット機能の実装（35分）
#### 目標：既存リポジトリを拡張し、個性的なキャラクターとの会話を実現

**3-1. リポジトリの理解と準備（10分）**
```bash
# streamlit_2025 リポジトリのクローン
git clone https://github.com/OWU131323104/streamlit_2025.git
cd streamlit_2025

# 既存アプリケーションの確認
streamlit run app.py
```

**3-2. プロンプトエンジニアリングの実装（15分）**
```python
# キャラクター設定データ
CHARACTERS = {
    "danzou": {
        "name": "段蔵",
        "personality": "クールで寡黙だが、心は優しい忍者",
        "speech_style": "「〜だ」「〜である」という武士的な口調",
        "specialty": "隠密行動、手裏剣術",
        "image": "danzou.webp"
    }
}

# システムプロンプトの生成
def create_character_prompt(character_key):
    char = CHARACTERS[character_key]
    return f"""
あなたは「{char['name']}」として会話してください。

【設定】
- 性格: {char['personality']}
- 口調: {char['speech_style']}
- 得意分野: {char['specialty']}

この設定を一貫して保ってください。
"""
```

**3-3. キャラクター選択とUI統合（10分）**
```python
# キャラクター選択
selected_char = st.sidebar.selectbox(
    "キャラクターを選択:",
    options=list(CHARACTERS.keys()),
    format_func=lambda x: CHARACTERS[x]["name"]
)

# キャラクター情報表示
char_info = CHARACTERS[selected_char]
st.sidebar.image(char_info["image"], width=150)
st.sidebar.write(f"**性格**: {char_info['personality']}")

# キャラクター応答の生成
character_prompt = create_character_prompt(selected_char)
full_prompt = character_prompt + f"\n\nユーザー: {prompt}\n{char_info['name']}:"
response = model.generate_content(full_prompt)
```

## 5. 準備物
- **教員側:**
    - Google AI Studio アカウント（デモ用）
    - `src/lecture12/` 内の実習ファイル
    - `lectures/12_LLM活用_GeminiAPI/12_slide.md` (授業スライド)
- **学生側:**
    - PC、Googleアカウント
    - インターネット接続環境
    - Streamlit実行環境
    - **`.streamlit/secrets.toml`ファイルの準備**（APIキー設定用）

## 6. 配布資料
- `src/lecture12/basic_chatbot.py` (基本チャットボット)
- `src/lecture12/character_chat_template.py` (キャラクターチャット・テンプレート)
- `src/lecture12/character_chat_answer.py` (キャラクターチャット・解答版)
- `src/lecture12/README.md` (実習ガイド)

## 7. 使用技術・ライブラリ
```bash
# 必要なライブラリのインストール
pip install google-generativeai streamlit pillow
```

### 主要な新機能
- `google.generativeai`: Gemini API操作
- `st.chat_message()`: チャットメッセージ表示
- `st.chat_input()`: チャット入力フィールド
- `st.session_state`: セッション状態管理（履歴保持）

## 8. 評価ポイント
### 基本要件（60%）
- [ ] Gemini APIが正常に動作する
- [ ] 基本的なチャット機能が実装されている
- [ ] エラーハンドリングが適切に行われている

### 応用要件（40%）
- [ ] キャラクター設定が適切に反映されている
- [ ] UI/UXが使いやすく設計されている
- [ ] プロンプトエンジニアリングに工夫が見られる

## 9. セキュリティ注意事項
⚠️ **重要なセキュリティ要件**
- APIキーは絶対にコードに直接記述しない
- **`.streamlit/secrets.toml`ファイルを使用**（自動的に`.gitignore`に含まれる）
- GitHubなどの公開リポジトリにAPIキーを含めない
- 使用量制限を適切に設定する
- APIキーは他人と共有しない

✅ **Streamlit Secretsの利点**
- ファイルが自動的にGitで無視される
- ローカルとクラウドの両方で動作
- 設定が簡単で管理しやすい

## 10. 次回予告
第13回では、今回作成したLLM機能と、これまでに学習したデータ分析・可視化機能を組み合わせた総合的なアプリケーション開発を行います。

**予定内容:**
- データ分析結果の自動解説機能
- グラフの説明文生成
- インサイトの自動抽出
- 総合ダッシュボードの完成

データとAIの融合による実用的なWebアプリケーションを完成させましょう！ 