import streamlit as st

# アプリのタイトル
st.title("シンプルなToDoリスト (解答例)")
st.write("やるべきことをリストにして管理しましょう。")

# ---------------------------------------------------------------------------
# ToDoリストと入力値をst.session_stateで管理
# ---------------------------------------------------------------------------
if "todo_list" not in st.session_state:
    st.session_state.todo_list = [
        {"task": "Streamlitの基本を復習する", "done": True, "id": "task_0"},
        {"task": "新しい演習テーマに挑戦する", "done": False, "id": "task_1"},
        {"task": "GitHubにコードをプッシュする", "done": False, "id": "task_2"}
    ] # タスクIDも追加して管理しやすくする

if "new_task_input" not in st.session_state:
    st.session_state.new_task_input = ""

# ---------------------------------------------------------------------------
# コールバック関数
# ---------------------------------------------------------------------------
def add_todo_item():
    """新しいタスクをリストに追加するコールバック関数"""
    task_name = st.session_state.new_task_input
    if task_name: # 入力があれば
        # ユニークなIDを生成 (ここでは単純な連番とするが、より堅牢な方法も検討可)
        new_id = f"task_{len(st.session_state.todo_list)}"
        st.session_state.todo_list.append({"task": task_name, "done": False, "id": new_id})
        st.session_state.new_task_input = "" # 入力フィールドをクリア

def toggle_task_done(task_id):
    """指定されたIDのタスクの完了状態を切り替える"""
    for item in st.session_state.todo_list:
        if item["id"] == task_id:
            item["done"] = not item["done"]
            break
    # st.experimental_rerun() # 状態変更を即時反映 (今回はボタンでのみ操作するため不要な場合も)

def delete_task_item(task_id):
    """指定されたIDのタスクを削除する"""
    st.session_state.todo_list = [item for item in st.session_state.todo_list if item["id"] != task_id]
    # st.experimental_rerun() # 即時反映

# ---------------------------------------------------------------------------
# UI要素の配置
# ---------------------------------------------------------------------------

# タスク入力と追加ボタン (st.formを使うとEnterキーでも追加しやすくなる)
with st.form(key="add_task_form", clear_on_submit=True):
    st.text_input(
        "新しいタスクを入力してください", 
        key="new_task_input", 
        placeholder="例: 牛乳を買う"
    )
    submit_button = st.form_submit_button(label="タスクを追加", on_click=add_todo_item) # on_clickでコールバック指定

st.divider() # 区切り線

# ToDoリストの表示
st.subheader("現在のToDoリスト")
if not st.session_state.todo_list:
    st.info("タスクはまだありません。新しいタスクを追加しましょう！")
else:
    # 未完了タスクと完了タスクを分けて表示することもできる
    # pending_tasks = [item for item in st.session_state.todo_list if not item["done"]]
    # done_tasks = [item for item in st.session_state.todo_list if item["done"]]

    for item in st.session_state.todo_list:
        task_id = item["id"]
        task_description = item["task"]
        is_done = item["done"]

        col1, col2, col3 = st.columns([0.08, 0.72, 0.2]) # レイアウト調整用

        with col1:
            # 完了チェックボックス
            st.checkbox(
                label="", # ラベルは空にしてタスク名と別に表示
                value=is_done, 
                key=f"done_cb_{task_id}", 
                on_change=toggle_task_done, 
                args=(task_id,)
            )
        with col2:
            if is_done:
                st.markdown(f"<span style='text-decoration: line-through; color: grey;'>{task_description}</span>", unsafe_allow_html=True)
            else:
                st.markdown(task_description)
        
        with col3:
            # 削除ボタン
            st.button(
                "削除", 
                key=f"delete_btn_{task_id}", 
                on_click=delete_task_item, 
                args=(task_id,)
            )
    st.caption(f"合計タスク数: {len(st.session_state.todo_list)}")

# デバッグ用: session_stateの中身を表示 (開発中のみ)
# st.sidebar.subheader("デバッグ情報")
# st.sidebar.json(st.session_state.to_dict())

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「シンプルなToDoリスト」の解答例です。
    - `st.session_state` を使ってタスクリストを永続化します。
    - タスクは辞書のリスト (`{"task": ..., "done": ..., "id": ...}`) として管理されます。
    - `st.form` と `st.text_input`, `st.form_submit_button` で新しいタスクを追加できます。
    - 各タスクは `st.checkbox` で完了状態を切り替え、`st.button` で削除できます。
    - コールバック関数 (`on_click`, `on_change`) を活用して状態を更新します。
    - `st.columns` でレイアウトを整えています。
    - `st.markdown` で完了タスクに取り消し線を表示しています。
    """
)
st.sidebar.warning(
    "ウィジェットの `key` は、各要素を一意に識別するために非常に重要です。"
    "特にループ内で動的にウィジェットを生成する場合、IDなどを使ってユニークなキーを割り当てましょう。"
) 