import streamlit as st

st.title("第7回 Streamlit 状態管理演習 - テンプレート")
st.caption("st.session_state を使ってToDoリストを作成しましょう。")

st.markdown("---")

# 状態の初期化 (ToDoリストがセッション状態になければ作成)
# st.session_state に 'todo_items' というキーがあるか確認し、なければ空のリスト [] で初期化してください。
# 同様に、入力フィールド用に 'new_todo_input' というキーを空文字列 "" で初期化してください。
# if "todo_items" not in st.session_state:
#     st.session_state.todo_items = []
# if "new_todo_input" not in st.session_state:
#     st.session_state.new_todo_input = ""

# ToDoを追加する関数
# st.session_state.new_todo_input の値を st.session_state.todo_items リストに追加する関数を作成してください。
# 追加後、st.session_state.new_todo_input を空文字列に戻して入力フィールドをクリアしましょう。
# 入力が空の場合は警告を出すようにしても良いでしょう。
def add_new_item_template():
    # ここにコードを記述してください
    pass # Replace with your code
    
# ToDoを削除する関数 (発展課題用)
# リストのインデックスを受け取り、st.session_state.todo_items から該当項目を削除する関数を作成してください。
def remove_item_template(index_to_remove):
    # ここにコードを記述してください
    pass # Replace with your code

st.markdown("**演習2.1 & 2.2: ToDo入力・追加ボタン・リスト表示**")
st.write("新しいToDoを入力し、リストに追加・表示します。")

# ToDo入力フィールド
# st.text_input() を使って入力フィールドを作成してください。
# key='new_todo_input' と on_change=add_new_item_template を設定して、入力確定時にToDoが追加されるようにしましょう。
# st.text_input("新しいToDoを入力:", key="new_todo_input", on_change=add_new_item_template, placeholder="例: 状態管理をマスターする")

# ToDoを追加ボタン
# st.button() を使ってボタンを作成してください。
# on_click=add_new_item_template を設定して、ボタンクリック時にもToDoが追加されるようにしましょう。
# keyを設定すると、入力フィールドのkeyと衝突するのを避けられます。
# st.button("ToDoを追加", on_click=add_new_item_template, key="add_todo_button_template")

st.subheader("現在のToDoリスト")
# st.session_state.todo_items リストの内容を画面に表示してください。
# リストが空の場合は「ToDoはまだありません」と表示しましょう。
# リストの各項目を st.write() などで表示します。
# 各項目の横に削除ボタンを配置するために、st.columns() を使うと良いでしょう。
# if not st.session_state.todo_items:
#     st.info("ToDoはまだありません。追加してみましょう！")
# else:
#     for i, item in enumerate(st.session_state.todo_items):
#         col_item, col_button = st.columns([0.8, 0.2])
#         with col_item:
#             st.write(f"{i+1}. {item}")
#         with col_button:
            # 演習2.3 (発展): 削除ボタンの追加
            # st.button() を使って削除ボタンを作成してください。
            # key は f"remove_todo_template_{i}" のようにインデックスを含めて一意にしてください。
            # on_click=remove_item_template と args=(i,) を設定して、ボタンクリック時に remove_item_template 関数が実行され、インデックスが渡されるようにしましょう。
            # st.button("削除", key=f"remove_todo_template_{i}", on_click=remove_item_template, args=(i,), type="secondary")

# デバッグ用にセッション状態を表示 (オプション)
# チェックボックスを作り、ONの時に st.session_state の内容を表示してみましょう。
# st.write(st.session_state) や st.json(st.session_state.to_dict()) を使います。
# if st.checkbox("現在のst.session_stateを表示", key="show_session_state_todo_template"):
#     # ここにコードを記述してください
#     pass # Replace with your code

st.markdown("---")
st.info("状態管理演習のテンプレートファイルです。コメントに従ってコードを記述してください。") 