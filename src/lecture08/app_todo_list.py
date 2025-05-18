import streamlit as st

# アプリのタイトル
st.title("シンプルなToDoリスト")

st.write("やるべきことをリストにして管理しましょう。")

# ---ここからコードを書いてみましょう---

# TODO: st.session_state を使ってToDoリストを初期化する
# ヒント: if "todo_list" not in st.session_state:
#           st.session_state.todo_list = [] # 例: タスク名を文字列で格納するリスト
#           # または、st.session_state.todo_list = [{"task": "最初のタスク", "done": False}, ...] のように辞書のリストも可

# TODO: 新しいタスクを追加するコールバック関数を定義する (任意)
# def add_todo_item():
#     new_task_name = st.session_state.new_task_input # 入力ウィジェットのキーを指定
#     if new_task_name: # 空でなければ追加
#         st.session_state.todo_list.append({"task": new_task_name, "done": False}) # 辞書形式の場合
#         # st.session_state.todo_list.append(new_task_name) # 文字列形式の場合
#         st.session_state.new_task_input = "" # 入力欄をクリア

# TODO: タスク入力用の st.text_input と追加ボタン (st.button) を配置する
#       ボタンには上記のコールバック関数を on_click で指定する、またはボタンが押されたら直接処理する
# st.text_input("新しいタスクを入力してください", key="new_task_input", on_change=add_todo_item) # on_changeで追加する場合
# if st.button("タスクを追加"): # ボタンで追加する場合
#     # add_todo_item() を直接呼び出すか、ここでタスク追加ロジックを記述
#     pass

# TODO: ToDoリストの項目を表示する
# st.subheader("現在のToDoリスト")
# if not st.session_state.get("todo_list", []):
#     st.info("タスクはまだありません。新しいタスクを追加しましょう！")
# else:
#     for i, item in enumerate(st.session_state.todo_list):
#         # TODO: 各タスクの完了状態を管理する st.checkbox を配置する
#         #       チェックボックスの値を st.session_state 内のタスクの状態と同期させる
#         #       ユニークなkeyを指定することが重要 (例: f"done_checkbox_{i}")
#         # is_done = st.checkbox(item["task"], value=item["done"], key=f"done_checkbox_{i}") # 辞書形式の場合
#         # if is_done != item["done"]:
#         #     st.session_state.todo_list[i]["done"] = is_done
#         #     st.experimental_rerun() # 状態変更を即時反映するためにリラン

#         # TODO: (発展) タスクを削除するボタンを配置する
#         #       ボタンが押されたら、該当するタスクをリストから削除する
#         #       ここでもユニークなkey (例: f"delete_button_{i}") とコールバック関数が役立つ
#         # if st.button("削除", key=f"delete_button_{i}"):
#         #     del st.session_state.todo_list[i]
#         #     st.experimental_rerun()

#         # 表示の工夫: 完了したタスクは取り消し線を引くなど
#         # if item["done"]:
#         #     st.markdown(f"- ~~{item['task']}~~ (完了)")
#         # else:
#         #     st.write(f"- {item['task']}")
        pass # このpassは上記TODO実装時に削除

# ---ここまで---

st.sidebar.header("ヒント")
st.sidebar.info(
    """
- `st.session_state` を使って、ページが再読み込みされてもリストの状態を保持します。
- 新しいタスクは `st.text_input` で入力し、`st.button` でリストに追加します。
- タスクの追加や削除にはコールバック関数を使うと便利です。
- 各タスクの完了状態は `st.checkbox` で管理します。チェックボックスの状態変更を `st.session_state` に反映させる必要があります。
- (発展) 各タスクに削除ボタンを付け、リストから項目を削除する機能を実装してみましょう。
- `st.experimental_rerun()` を使うと、状態変更を即座に画面に反映できます。
"""
)
st.sidebar.warning(
    "`st.session_state` を使う場合、ウィジェットの `key` 引数を適切に設定することが非常に重要です。"
    "特にループ内で動的にウィジェットを生成する場合は、各ウィジェットにユニークなキーを割り当ててください。"
) 