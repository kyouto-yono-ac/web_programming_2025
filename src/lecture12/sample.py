import google.generativeai as genai

# API設定
genai.configure(api_key="YOUR_API_KEY")

# モデルの初期化
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# テキスト生成
response = model.generate_content("こんにちは！元気ですか？")
print(response.text)
