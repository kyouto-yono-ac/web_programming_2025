import streamlit as st

# カウンターの初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

# カウントアップボタン
if st.button('カウントアップ'):
    st.session_state.count += 1

# カウンターの表示
st.write(f"現在のカウント: {st.session_state.count}")

# リセットボタン
if st.button('リセット'):
    st.session_state.count = 0 