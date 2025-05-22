import streamlit as st

st.title("第7回 Streamlit 状態管理演習 - 解答")
st.caption("st.session_state を使ってToDoリストを作成しましょう。")

st.markdown("---")

# 状態の初期化 (ToDoリストがセッション状態になければ作成)
# st.session_state に 'todo_items' がなければ空のリストで初期化
if "todo_items" not in st.session_state:
    st.session_state.todo_items = ["Streamlitの基本を学ぶ", "レイアウト機能を試す"]
# 入力フィールド用のキー 'new_todo_input' がなければ空文字列で初期化
if "new_todo_input" not in st.session_state:
    st.session_state.new_todo_input = ""

# ToDoを追加する関数
def add_new_item_ans():
    # st.session_state.new_todo_input に入力があればリストに追加
    if st.session_state.new_todo_input:
        st.session_state.todo_items.append(st.session_state.new_todo_input)
        st.success(f"ToDo「{st.session_state.new_todo_input}」を追加しました")
        # 追加後、入力フィールドをクリアするためにキーの値を更新
        st.session_state.new_todo_input = ""
    else:
        st.warning("ToDo内容を入力してください。")

# ToDoを削除する関数
def remove_item_ans(index_to_remove):
    # 指定されたインデックスがリストの範囲内であれば削除
    if 0 <= index_to_remove < len(st.session_state.todo_items):
        removed = st.session_state.todo_items.pop(index_to_remove)
        st.info(f"ToDo「{removed}」を削除しました")
        # st.experimental_rerun() # 削除後即時反映させたい場合にコメント解除

st.markdown("**演習2.1 & 2.2: ToDo入力・追加ボタン・リスト表示**")
st.write("新しいToDoを入力し、リストに追加・表示します。")

# ToDo入力フィールドと追加ボタン
# key と on_change を使って、入力確定時に関数 add_new_item_ans() を実行
st.text_input("新しいToDoを入力:", key="new_todo_input", on_change=add_new_item_ans, placeholder="例: 状態管理をマスターする")
# 追加ボタン。on_click で関数 add_new_item_ans() を実行
st.button("ToDoを追加", on_click=add_new_item_ans, key="add_todo_button_ans")

st.subheader("現在のToDoリスト")
# st.session_state.todo_items に項目があればリストを表示
if not st.session_state.todo_items:
    st.info("ToDoはまだありません。追加してみましょう！")
else:
    # リストの各項目をループ処理
    for i, item in enumerate(st.session_state.todo_items):
        # 各項目と削除ボタンを横に並べるためにカラムを使用
        col_item, col_button = st.columns([0.8, 0.2])
        with col_item:
            st.write(f"{i+1}. {item}")
        with col_button:
            # 演習2.3 (発展): 削除ボタンの追加
            # ボタンのkeyは一意になるようにインデックスiを含める
            # on_click で remove_item_ans() を実行し、argsでインデックスiを渡す
            st.button("削除", key=f"remove_todo_ans_{i}", on_click=remove_item_ans, args=(i,), type="secondary")

# デバッグ用にセッション状態を表示 (オプション)
# チェックボックスがONの場合のみセッション状態を表示
if st.checkbox("現在のst.session_stateを表示", key="show_session_state_todo_ans"):
    # st.session_state全体または特定のキーを表示
    # st.write(st.session_state)
    st.json(st.session_state.to_dict()) # 辞書形式で見やすく表示

st.markdown("---")
st.success("状態管理演習の解答例です。") 