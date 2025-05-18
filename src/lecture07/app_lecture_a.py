import streamlit as st
import pandas as pd # 発展課題で使用

st.title("第7回 Streamlit総合演習 - 解答例")
st.caption("レイアウト、状態管理、フォーム、ファイルアップロードの解答例です。")

st.markdown("---")

st.header("1. レイアウト機能 演習セクション - 解答例")
st.write("st.sidebar, st.columns, st.expander を使った例です。")

# 演習1.1: サイドバー (st.sidebar)
st.sidebar.title("自己紹介入力")
user_name = st.sidebar.text_input("お名前を入力してください:", value="大妻 花子", key="layout_name")
user_id = st.sidebar.text_input("学籍番号を入力してください:", value="XXYYZZ", key="layout_id")
if user_name and user_id:
    st.sidebar.success(f"名前: {user_name}\n学籍番号: {user_id}")
else:
    st.sidebar.info("サイドバーから名前と学籍番号を入力してください。")

# 演習1.2: カラムレイアウト (st.columns)
st.subheader("好きなものを2列で紹介")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**好きな動物**")
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="ネコ", use_column_width=True)
    st.write("猫は自由気ままで可愛らしいです。")

with col2:
    st.markdown("**好きな食べ物**")
    # Dog image as placeholder for food
    st.image("https://static.streamlit.io/examples/dog.jpg", caption="イヌ (例: こちらも可愛い)", use_column_width=True)
    st.write("お寿司やラーメンが好きです。")

# 演習1.3: エキスパンダー (st.expander)
st.subheader("詳細情報")
with st.expander("ここをクリックして詳細を表示"):
    st.write("エキスパンダーは、通常は隠しておきたい補足情報や詳細設定を表示するのに便利です。")
    st.warning("この情報はエキスパンダー内にあります。")
    st.image("https://static.streamlit.io/examples/owl.jpg", caption="フクロウもいます")

st.markdown("---")

st.header("2. 状態管理 (`st.session_state`) 演習セクション - 解答例")
st.write("簡単なToDoリストを作成して、`st.session_state` の使い方を学びましょう。")

# 状態の初期化 (ToDoリストがセッション状態になければ作成)
if "todo_items" not in st.session_state:
    st.session_state.todo_items = ["Streamlitの基本を学ぶ", "レイアウト機能を試す"]
if "new_todo_input" not in st.session_state: # 入力フィールド用のキーも初期化
    st.session_state.new_todo_input = ""

def add_new_item():
    if st.session_state.new_todo_input: # keyを使ってアクセス
        st.session_state.todo_items.append(st.session_state.new_todo_input)
        st.success(f"ToDo「{st.session_state.new_todo_input}」を追加しました")
        st.session_state.new_todo_input = "" # 追加後、入力フィールドをクリア
    else:
        st.warning("ToDo内容を入力してください。")

def remove_item(index_to_remove):
    if 0 <= index_to_remove < len(st.session_state.todo_items):
        removed = st.session_state.todo_items.pop(index_to_remove)
        st.info(f"ToDo「{removed}」を削除しました")
        # st.experimental_rerun() # 即時反映させたい場合に必要

# 演習2.1: ToDo入力と追加ボタン
st.text_input("新しいToDoを入力:", key="new_todo_input", on_change=add_new_item, placeholder="例: 状態管理をマスターする")
st.button("ToDoを追加", on_click=add_new_item, key="add_todo_button")

# 演習2.2: ToDoリストの表示
st.subheader("現在のToDoリスト")
if not st.session_state.todo_items:
    st.info("ToDoはまだありません。追加してみましょう！")
else:
    for i, item in enumerate(st.session_state.todo_items):
        col_item, col_button = st.columns([0.8, 0.2])
        with col_item:
            st.write(f"{i+1}. {item}")
        with col_button:
            # 演習2.3 (発展): 削除ボタンの追加
            st.button("削除", key=f"remove_todo_{i}", on_click=remove_item, args=(i,), type="secondary")

# デバッグ用にセッション状態を表示 (オプション)
if st.checkbox("現在のst.session_stateを表示", key="show_session_state_todo"):
    st.json(st.session_state.to_dict()) # .to_dict() で辞書として表示

st.markdown("---")

st.header("3. フォーム (`st.form`) 演習セクション - 解答例")
st.write("アンケートフォームを作成し、複数の入力を一度に処理する方法を学びましょう。")

# 演習3.1: アンケートフォームの作成
with st.form(key="survey_sample_form_answered"):
    st.subheader("簡単なアンケート")
    s_name = st.text_input("お名前:", value="山田 太郎")
    s_email = st.text_input("メールアドレス:", value="yamada.taro@example.com")
    s_fav_food_options = ["", "寿司", "ラーメン", "カレー", "焼肉", "イタリアン", "その他"]
    s_fav_food = st.selectbox("好きな食べ物は？", options=s_fav_food_options, index=2) # ラーメンを選択状態に
    s_feedback = st.text_area("ご意見・ご感想 (任意):", value="Streamlitは楽しく学べます！")
    
    s_submitted_button = st.form_submit_button("アンケートを送信する")

    if s_submitted_button:
        all_filled = True
        if not s_name: 
            st.warning("お名前を入力してください。")
            all_filled = False
        if not s_email: 
            st.warning("メールアドレスを入力してください。")
            all_filled = False
        if not s_fav_food:
            st.warning("好きな食べ物を選択してください。")
            all_filled = False
        
        if all_filled:
            st.success("アンケートへのご協力、ありがとうございました！")
            st.markdown("**送信内容:**")
            st.write(f"- お名前: {s_name}")
            st.write(f"- メールアドレス: {s_email}")
            st.write(f"- 好きな食べ物: {s_fav_food}")
            if s_feedback:
                st.write(f"- ご意見: {s_feedback}")
            else:
                st.write("- ご意見: (未記入)")
            st.balloons()
        else:
            st.error("未入力の項目があります。ご確認ください。")

st.markdown("---")

st.header("4. ファイルアップロード (`st.file_uploader`) 演習セクション - 解答例")
st.write("画像ファイルまたはCSVファイルをアップロードして、その情報を表示してみましょう。")

# 演習4.1: ファイルアップローダーの設置
uploaded_file_data = st.file_uploader(
    "ここにファイルをアップロード (画像 or CSV)", 
    type=["png", "jpg", "jpeg", "gif", "csv"],
    accept_multiple_files=False, # Falseに設定
    key="file_uploader_main"
)

if uploaded_file_data is not None:
    st.success(f"ファイル「{uploaded_file_data.name}」がアップロードされました！")
    st.write("**ファイル情報:**")
    st.write(f"- ファイル名: {uploaded_file_data.name}")
    st.write(f"- ファイルタイプ: {uploaded_file_data.type}")
    st.write(f"- ファイルサイズ: {uploaded_file_data.size} バイト")

    # 演習4.2: アップロードされたファイルの種類に応じて処理を分岐
    if uploaded_file_data.type.startswith("image/"):
        st.subheader("アップロードされた画像:")
        st.image(uploaded_file_data, caption=f"{uploaded_file_data.name}", use_column_width=True)
    elif uploaded_file_data.type == "text/csv":
        st.subheader("アップロードされたCSV (先頭5行):")
        # 発展課題: Pandasを使ってCSVを読み込み表示
        try:
            df = pd.read_csv(uploaded_file_data)
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
            st.info("エラーが発生した場合でも、ファイル情報自体は上記に表示されています。CSVの内容が正しいかご確認ください。")
    else:
        st.warning("対応していないファイルタイプです。画像(png, jpg等)またはCSVファイルをアップロードしてください。")
else:
    st.info("まだファイルはアップロードされていません。")

st.markdown("---")
st.success("全ての演習セクションの解答例を確認しました！") 