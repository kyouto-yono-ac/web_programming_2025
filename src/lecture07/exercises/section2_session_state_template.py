import streamlit as st

st.title("第7回 Streamlit 状態管理演習 - テンプレート")
st.caption("st.session_state を使って今日の気分を記録しましょう。")

st.markdown("---")
st.subheader("演習: 今日の気分記録アプリ")
st.write("**課題**: ボタンで気分を選択し、`st.session_state` で履歴を保持するアプリを作成する。")

# ここに演習のコードを記述してください
# ヒント: st.session_state でリストを初期化し、st.button() で気分を追加


st.markdown("---")
st.info("💡 気分ボタンを押すたびに履歴が蓄積され、アプリを再実行しても保持されることを確認してください。") 