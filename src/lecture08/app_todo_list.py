import streamlit as st

st.title("第8回 演習: ToDoリストアプリ")
st.caption("タスクの追加・完了チェック・削除ができるシンプルなToDoリストを作成しましょう。")

st.markdown("---")
st.subheader("演習: ToDoリスト")
st.write("**課題**: タスクの追加・完了チェック・削除ができるシンプルなToDoリストを作成する。")

# ここに演習のコードを記述してください
# ヒント: st.session_state でリスト管理、st.text_input でタスク入力、st.button で追加・削除


st.markdown("---")
st.info("💡 st.session_state でタスクリストを管理し、ユニークなkeyを使ってウィジェットを区別しましょう。") 