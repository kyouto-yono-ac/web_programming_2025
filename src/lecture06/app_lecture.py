import streamlit as st

st.title("Streamlit基本 (2): 多様な入力ウィジェット")

# --- 表示系ウィジェットの復習 ---
st.header("表示系ウィジェットの復習 (st.write, st.header, st.markdownなど)")

st.subheader("st.write の使用例")
st.write("Hello, Streamlit World! これは st.write() を使った基本的なテキスト表示です。")
st.write("数値も表示できます:", 12345)
st.write("リストも表示できます:", ["りんご", "バナナ", "みかん"])
df_example = {"列1": [1, 2, 3], "列2": [10, 20, 30]}
st.write("簡単なデータフレームも表示できます:", df_example)

st.subheader("その他のテキスト表示")
st.text("これは st.text() を使った表示です。st.write と似ていますが、主に固定幅フォントで表示されます。")
st.caption("これは st.caption() で表示したキャプションです。小さな説明文などに使います。")

st.subheader("st.markdown の使用例")
st.markdown("""
### Markdown見出し (H3)
Markdown記法を使って、**太字** や *イタリック*、箇条書きリストなどが表現できます。

- アイテム1
- アイテム2
  - サブアイテム2.1

[Streamlit公式サイトへのリンク](https.streamlit.io)
""")

st.info("st.info: 情報メッセージを表示します。")
st.success("st.success: 成功メッセージを表示します。")
st.warning("st.warning: 警告メッセージを表示します。")
st.error("st.error: エラーメッセージを表示します。")

st.subheader("インタラクション系ウィジェットの復習 (st.button, st.checkbox)")

# st.button の例
st.write("st.button の使用例:")
if st.button("ここをクリック！"):
    st.write("ボタンがクリックされました！")
else:
    st.write("ボタンはまだクリックされていません。")

# st.checkbox の例
st.write("st.checkbox の使用例:")
show_message = st.checkbox("メッセージを表示する")

if show_message:
    st.info("チェックボックスがオンになっているので、このメッセージが表示されています。")
else:
    st.warning("チェックボックスはオフです。")


# 前回の復習
st.header("前回の復習")
st.write("""
前回は以下の内容を学びました：
- 基本的な表示関数（`st.write`, `st.header`, `st.markdown`）
- 基本的なインタラクション（`st.button`, `st.checkbox`）
""")

st.divider()
# 入力ウィジェットの基本パラメータ
st.header("入力ウィジェットの基本パラメータ")
st.write("""
Streamlitの入力ウィジェットには、共通の基本パラメータがあります：

1. `label`: ウィジェットのラベル（表示名）
2. `help`: ヘルプテキスト（?マークをクリックすると表示）
3. `key`: ウィジェットの一意の識別子
""")

# 選択型ウィジェット
st.header("選択型ウィジェット")

## selectbox
st.subheader("1. st.selectbox")
st.write("""
`st.selectbox`は、ドロップダウンリストで単一の選択肢を選ぶウィジェットです。
""")

# 例：好きな果物を選択
fruits = ["りんご", "バナナ", "オレンジ", "ぶどう", "メロン"]
selected_fruit = st.selectbox(
    "好きな果物を選んでください",
    fruits,
    help="ドロップダウンリストから選択してください"
)
st.write(f"選択された果物: {selected_fruit}")

# 条件分岐の例
if selected_fruit == "りんご":
    st.write("りんごは健康に良い果物です！")
elif selected_fruit == "バナナ":
    st.write("バナナはエネルギー補給に最適です！")

st.divider()
## multiselect
st.subheader("2. st.multiselect")
st.write("""
`st.multiselect`は、複数の選択肢を選べるリストです。
""")

# 例：好きな果物を複数選択
selected_fruits = st.multiselect(
    "好きな果物を選んでください（複数選択可）",
    fruits,
    help="Ctrlキー（Macの場合はCommandキー）を押しながらクリックで複数選択できます"
)

# 選択結果の表示
if selected_fruits:
    st.write("選択された果物:")
    for fruit in selected_fruits:
        st.write(f"- {fruit}")
else:
    st.write("果物が選択されていません")

st.divider()
# 数値入力ウィジェット
st.header("数値入力ウィジェット")

## slider
st.subheader("1. st.slider")
st.write("""
`st.slider`は、スライダーを使って数値を選択するウィジェットです。
""")

# 基本的なスライダー
age = st.slider(
    "年齢を選択してください",
    min_value=0,
    max_value=100,
    value=20,
    step=1,
    help="スライダーを動かして年齢を選択してください"
)
st.write(f"選択された年齢: {age}歳")

# 範囲選択の例
st.write("""
範囲を選択するスライダーの例：
""")
age_range = st.slider(
    "年齢範囲を選択してください",
    min_value=0,
    max_value=100,
    value=(20, 40),
    help="スライダーの両端を動かして範囲を選択してください"
)
st.write(f"選択された年齢範囲: {age_range[0]}歳から{age_range[1]}歳まで")

st.divider()
## number_input
st.subheader("2. st.number_input")
st.write("""
`st.number_input`は、直接数値を入力できるフィールドです。
""")

# 基本的な数値入力
number = st.number_input(
    "数値を入力してください",
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    help="数値を直接入力するか、上下の矢印で調整してください"
)
st.write(f"入力された数値: {number}")

# 計算例
st.write("""
入力された数値を使った計算例：
""")
st.write(f"2倍の値: {number * 2}")
st.write(f"平方根: {number ** 0.5:.2f}")

st.divider()
# テキスト入力ウィジェット
st.header("テキスト入力ウィジェット")

## text_input
st.subheader("st.text_input")
st.write("""
`st.text_input`は、テキストを入力できるフィールドです。
""")

# 基本的なテキスト入力
name = st.text_input(
    "名前を入力してください",
    help="あなたの名前を入力してください"
)

# 入力値の検証
if name:
    st.write(f"こんにちは、{name}さん！")
    st.write(f"名前の長さ: {len(name)}文字")
else:
    st.write("名前が入力されていません")

st.divider()
# 総合演習
st.header("総合演習：簡単なアンケートアプリ")
st.write("""
これまで学んだ入力ウィジェットを組み合わせて、簡単なアンケートアプリを作成してみましょう。
""")

# アンケートフォーム
st.subheader("アンケート")

# テキスト入力
name = st.text_input("お名前を入力してください")

# 数値入力
age = st.slider("年齢を選択してください", 0, 100, 20)

# 選択
gender = st.selectbox(
    "性別を選択してください",
    ["男性", "女性", "その他"]
)

# 複数選択
hobbies = st.multiselect(
    "趣味を選択してください（複数選択可）",
    ["読書", "スポーツ", "音楽", "旅行", "料理", "ゲーム"]
)

# 送信ボタン
if st.button("アンケートを送信"):
    if name:
        st.write("### アンケート結果")
        st.write(f"**名前:** {name}")
        st.write(f"**年齢:** {age}歳")
        st.write(f"**性別:** {gender}")
        st.write("**趣味:**")
        for hobby in hobbies:
            st.write(f"- {hobby}")
    else:
        st.error("名前を入力してください")

st.divider()
# まとめ
st.header("まとめ")
st.write("""
今回学んだ内容：
1. 選択型ウィジェット
   - `st.selectbox`: 単一選択のドロップダウンリスト
   - `st.multiselect`: 複数選択可能なリスト

2. 数値入力ウィジェット
   - `st.slider`: スライダーによる数値選択
   - `st.number_input`: 直接数値を入力

3. テキスト入力ウィジェット
   - `st.text_input`: テキスト入力フィールド

これらのウィジェットを組み合わせることで、様々なインタラクティブなアプリケーションを作成できます。
""")

st.divider()
# 次回予告
st.header("次回予告")
st.write("""
次回は以下の内容を学びます：
- レイアウト（`st.columns`, `st.expander`, `st.sidebar`）
- 状態管理（`st.session_state`）
- ファイル入力（`st.file_uploader`）
""") 