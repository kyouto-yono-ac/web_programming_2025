import streamlit as st
import random

# アプリのタイトル
st.title("おみくじアプリ (解答例)")
st.write("今日の運勢を占ってみましょう！下のボタンを押してください。")

# おみくじの結果データ
# 各結果は「名前」「メッセージ」「画像ファイルパス」「アニメーション(任意)」を持つ辞書
fortune_results = [
    {"name": "大吉", 
     "message": "🎉 おめでとうございます！今日は最高の1日になるでしょう！何事も積極的にチャレンジ！", 
     "image": "images/omikuji/daikichi.png",
     "animation": "balloons"},
    {"name": "中吉", 
     "message": "✨ なかなか良い運勢です！小さな幸せがたくさん見つかるかも。笑顔を忘れずに！", 
     "image": "images/omikuji/chukichi.png"},
    {"name": "小吉", 
     "message": "👍 まずまずの日です。油断せず、コツコツ努力を続けると良い結果に繋がります。", 
     "image": "images/omikuji/shokichi.png"},
    {"name": "吉",   
     "message": "😊 平穏で穏やかな一日になりそうです。周囲への感謝の気持ちを大切に。", 
     "image": "images/omikuji/kichi.png"},
    {"name": "末吉", 
     "message": "🌱 これまでの努力が少しずつ報われ始める兆し。焦らず、じっくりと進みましょう。", 
     "image": "images/omikuji/suekichi.png"},
    {"name": "凶",   
     "message": "😥 少し注意が必要な日。予期せぬトラブルに気をつけて、慎重な行動を心がけましょう。", 
     "image": "images/omikuji/kyo.png"},
    {"name": "大凶", 
     "message": "☔️ 今日は無理せず、静かに過ごすのが吉。嵐が過ぎ去るのを待ち、明日に備えましょう。", 
     "image": "images/omikuji/daikyo.png",
     "animation": "snow"}
]

# セッション状態で前回のおみくじ結果を保持 (任意、表示を固定するため)
if "last_fortune" not in st.session_state:
    st.session_state.last_fortune = None

# おみくじを引くボタン
if st.button("⛩️ おみくじを引く！ ⛩️", help="クリックして今日の運勢を占う"):
    # ランダムに結果を選択
    selected_result = random.choice(fortune_results)
    st.session_state.last_fortune = selected_result # 結果をセッションに保存
    
    # アニメーション（あれば）
    if "animation" in selected_result:
        if selected_result["animation"] == "balloons":
            st.balloons()
        elif selected_result["animation"] == "snow":
            st.snow()

# 前回引いた結果があれば表示 (ボタンを押すたびに変わるのを防ぐためセッション利用)
if st.session_state.last_fortune:
    result_to_display = st.session_state.last_fortune
    
    st.header(f"今日のあなたの運勢は...「{result_to_display['name']}」です！")

    # 画像表示
    # 画像ファイルは src/lecture08/images/omikuji/ に配置想定
    try:
        full_image_path = result_to_display["image"]
        st.image(full_image_path, caption=result_to_display["name"], width=300)
    except FileNotFoundError:
        st.warning(f"画像ファイル ({full_image_path}) が見つかりません。ダミー画像を表示します。")
        st.image("https://via.placeholder.com/300x300/CCCCCC/FFFFFF?Text=Image+Not+Found", caption="画像準備中")
    except Exception as e:
        st.error(f"画像表示中にエラーが発生しました: {e}")
    
    # メッセージのスタイル分け
    if result_to_display["name"] in ["大吉", "中吉"]:
        st.success(result_to_display["message"])
    elif result_to_display["name"] in ["凶", "大凶"]:
        st.error(result_to_display["message"])
    else:
        st.info(result_to_display["message"])
else:
    st.info("ボタンを押しておみくじを引いてください。")

st.sidebar.header("このアプリについて")
st.sidebar.success(
    """
    これは「おみくじアプリ」の解答例です。
    - ボタンを押すと、ランダムに運勢、メッセージ、関連画像を表示します。
    - `random.choice()` を使って、事前に定義した運勢結果のリストからランダムに一つを選びます。
    - 結果は辞書のリストとして定義されています。
    - `st.image` で画像を表示し、結果に応じて `st.balloons()` や `st.snow()` のアニメーションを実行します。
    - メッセージは運勢の良し悪しに応じて `st.success`, `st.info`, `st.error` で色分けしています。
    - `st.session_state` を使って、最後に引いたおみくじの結果を保持し、ボタンクリック時のみ更新・表示するようにしています。
    """
)
st.sidebar.markdown("--- ")
st.sidebar.caption(
    "画像ファイル (例: `daikichi.png`) は、`src/lecture08/images/omikuji/` "
    "フォルダ内に配置することを想定しています。"
    "これらの画像はご自身でご用意いただくか、教員から提供されたものを使用してください。"
) 