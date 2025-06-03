import streamlit as st

st.title("第8回 演習: ToDoリストアプリ - 解答例")
st.caption("タスクの追加・完了チェック・削除ができるシンプルなToDoリストを作成しましょう。")

st.markdown("---")
st.subheader("演習: ToDoリスト")
st.write("**課題**: タスクの追加・完了チェック・削除ができるシンプルなToDoリストを作成する。")

# ToDoリストの初期化
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# タスク追加機能
st.subheader("新しいタスクを追加")
new_task = st.text_input("タスクを入力してください", placeholder="例: レポートを書く")

if st.button("タスクを追加"):
    if new_task:
        st.session_state.todo_list.append({"task": new_task, "done": False})
        st.success(f"「{new_task}」を追加しました！")
        st.rerun()
    else:
        st.error("タスクを入力してください")

# ToDoリスト表示
st.subheader("📝 ToDoリスト")

if not st.session_state.todo_list:
    st.info("まだタスクがありません。新しいタスクを追加してみましょう！")
else:
    # 完了・未完了の統計
    total_tasks = len(st.session_state.todo_list)
    completed_tasks = sum(1 for item in st.session_state.todo_list if item["done"])
    
    st.write(f"**タスク数**: {total_tasks} 件 | **完了**: {completed_tasks} 件 | **残り**: {total_tasks - completed_tasks} 件")
    
    # 各タスクの表示
    for i, item in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            # チェックボックスで完了状態を管理
            is_done = st.checkbox(
                item["task"], 
                value=item["done"], 
                key=f"checkbox_{i}"
            )
            
            # 完了状態が変更された場合
            if is_done != item["done"]:
                st.session_state.todo_list[i]["done"] = is_done
                st.rerun()
        
        with col2:
            # 削除ボタン
            if st.button("🗑️ 削除", key=f"delete_{i}"):
                st.session_state.todo_list.pop(i)
                st.success("タスクを削除しました")
                st.rerun()

# 一括操作
if st.session_state.todo_list:
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("全て完了にする"):
            for item in st.session_state.todo_list:
                item["done"] = True
            st.success("全てのタスクを完了にしました！")
            st.rerun()
    
    with col2:
        if st.button("完了済みタスクを削除"):
            st.session_state.todo_list = [item for item in st.session_state.todo_list if not item["done"]]
            st.success("完了済みタスクを削除しました")
            st.rerun()

st.markdown("---")
st.success("✅ ToDoリストアプリの解答例です。st.session_stateでデータを管理し、ユニークなkeyでウィジェットを識別しています。")

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