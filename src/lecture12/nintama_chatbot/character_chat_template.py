import streamlit as st
import random
import os
import google.generativeai as genai

st.title("忍たま乱太郎キャラクター紹介")
st.write("あなたの好みに沿って、あなたにおすすめのキャラクターを紹介します！")

# Gemini API設定（チャット機能のため）
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    chat_available = True
except:
    chat_available = False
    st.warning("⚠️ Gemini APIが設定されていないため、チャット機能は利用できません。")

# --- 入力セクション ---
st.header("あなたの好みを教えてください！")
# 1. 好きなキャラクターのタイプ
character_type = st.multiselect(
    "好きなキャラクターのタイプを選んでください (複数選択可):",
    ["元気", "真面目", "しっかり者", "陰気", "ツンデレ", "お調子者", "マイペース","天然", "おおらか", "その他"]
)

# 2. 好きなキャラクターの見た目
appearance_features = st.multiselect(
    "好きなキャラクターの見た目を選んでください (複数選択可):",
    ["可愛い", "かっこいい", "美人", "元気系", "ミステリアス系", "おっとり系", "その他"]
)

# 3. 好きなキャラクターの一人称
first_person_options = [ "私", "僕", "俺", "敬語の時は一人称が変わる"]
relationship = st.selectbox(
    "好きなキャラクターの一人称を選んでください:",
    first_person_options
)

# 4. 好きなキャラクターの年齢
age_range = st.slider("好きなキャラクターの年齢を選んでください:", min_value=10, max_value=30, value=15, step=1, format="年齢: %d")

# --- キャラクター紹介ロジックセクション ---
if "character_introduction_done" not in st.session_state:
    st.session_state.character_introduction_done = False

if st.button("キャラクターを紹介"):
    st.session_state.character_introduction_done = True

if st.session_state.character_introduction_done:
    st.header("あなたにおすすめのキャラクター")

    all_fields_filled = True  # 初期化
    if not character_type:
        st.warning("好きなキャラクターのタイプを1つ以上選択してください。")
        all_fields_filled = False
    if not appearance_features:
        st.warning("好きなキャラクターの見た目を選択してください。")
        all_fields_filled = False
    if not relationship:
        st.warning("好きなキャラクターの一人称を選択してください。")
        all_fields_filled = False

    if all_fields_filled:
        # ▼ここから折りたたみ（デフォルトで閉じる）
        with st.expander("あなたの好みまとめ", expanded=False):
            st.write(f"- **好きなキャラクターのタイプ:** {', '.join(character_type)}")
            st.write(f"- **好きなキャラクターの見た目:** {appearance_features}")
            st.write(f"- **好きなキャラクターの一人称:** {relationship}")
            st.write(f"- **好きなキャラクターの年齢:** {age_range}歳")
        # ▲ここまで折りたたみ

        st.subheader("📝 おすすめキャラクター")
        recommendations = []

        # キャラクターごとに条件を定義
        characters = [
            {
                "name": "猪名寺 乱太郎（いなでら らんたろう）",
                "type": ["元気", "おおらか"],
                "appearance": ["可愛い", "元気系"],
                "first_person": ["私"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳／保健委員会所属\n「忍たま乱太郎」の主人公。\n家は先祖代々由緒正しいヒラ忍者。一流の忍者を目指して、忍術学園に入学。\nぼさぼさ頭で、ひどい乱視のためメガネをかけている。\n足が速く、100ｍ10秒で走ることができる。絵を描くのも得意。素直で元気！\n「乱・きり・しん」三人組のまとめ役。",
                "image": "rantarou.webp"
            },
            {
                "name": "摂津のきり丸（せっつのきりまる）",
                "type": ["元気", "その他"],
                "appearance": ["かっこいい"],
                "first_person": ["俺","敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳／図書委員会所属\n戦で家を焼かれ家族をなくしたが、アルバイトをしながらたくましく生きている。\n忍術学園の長期休みには、土井先生の家でお世話になっている。\n小銭が大好きで、「タダ」「安い」という言葉に弱い。",
                "image": "kirimaru.webp"
            },
            {
                "name": "福富 しんべヱ（ふくとみ しんべえ）",
                "type": ["おおらか"],
                "appearance": ["可愛い"], 
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】10歳／用具委員会所属\n堺の大貿易商「福富屋」の息子で、おっとり・のんびりした性格。\n大の食いしん坊で、遠くの食べ物のにおいも嗅ぎ分けることができる。\n走ることは苦手だが、硬い髪と石頭、粘着力のある鼻水で仲間のピンチを救うこともある。",
                "image": "sinbee.webp"
            },
            {
                "name": "黒木 庄左エ門（くろき しょうざえもん）",
                "type": ["真面目"],
                "appearance": ["可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳／学級委員長委員会所属\nクラスでは一番成績が良く、いつも冷静沈着。\n実家は、京都洛北の炭屋さん。\n元気なおじいちゃんと、幼い弟がいる。",
                "image": "syouzaemo.webp"
            },
            {
                "name": "二廓 伊助（にのくるわ いすけ）",
                "type": ["真面目","その他"],
                "appearance": ["その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。火薬委員会所属。\n出身は河内の国。\n実家は染め物屋さん。とても気がつく性格で、掃除が大好き。",
                "image": "isuke.jpg"
            },
            {
                "name": "山村 喜三太（やまむら きさんた）",
                "type": ["天然","元気"],
                "appearance": ["その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。用具委員会所属。\n相模の国出身。風魔（ふうま）流忍術学校からの転校生。ナメクジが大好きで、壺に入れてペットにしている。",
                "image": "kisanta.webp"
            },
            {
                "name": "皆本 金吾（みなもと きんご）",
                "type": ["しっかり者","元気"],
                "appearance": ["かっこいい"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。体育委員会所属。\n相模の国出身。お侍の家の出身で、剣術師範	（けんじゅつしはん）の戸部先生を尊敬している。まっすぐな性格。喜三太と同室。",
                "image": "kingo.webp"
            },
            {
                "name": "加藤 団蔵（かとう だんぞう）",
                "type": ["しっかり者"],
                "appearance": ["かっこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。会計委員会所属。\n近江の国出身。しっかり者だが、字が汚いのが悩みのタネ。\n父の飛蔵（とびぞう）は馬借（ばしゃく）の親方をしていて、団蔵も馬術が得意。",
                "image": "danzou.webp"
            },
            {
                "name": "佐竹 虎若（さたけ とらわか）",
                "type": ["マイペース","元気"],
                "appearance": ["可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。生物委員会所属。\n火縄銃が大好きで、山田先生から火縄銃を習うために忍術学園に入学した。\n父は佐武村の鉄砲隊の首領。",
                "image": "torawaka.jpg"
            },
            {
                "name": "笹山 兵太夫（ささやま へいたゆう）",
                "type": ["マイペース","元気"],
                "appearance": ["可愛い","かっこいい"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。作法委員会所属。\nカラクリが大好きで、三治郎といっしょの部屋は仕掛けやワナがいっぱいのカラクリ部屋になっている。ちょっぴり強情な面も!? ",
                "image": "heidayuu.jpg"
            },
            {
                "name": "夢前 三治郎（ゆめさき さんじろう）",
                "type": ["元気","おおらか"],
                "appearance": ["可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年は組】\n10歳。生物委員会所属。\n優しくて明るい性格で、いつもニコニコ笑顔。カラクリが大好き。\n山伏（やまぶし）の父と修行をしているため、走るのが得意。乱太郎に続き、2番目に速く走れる。",
                "image": "sanjirou.jpg"
            },
            {
                "name": "土井 半助（どい はんすけ）",
                "type": ["真面目","その他"],
                "appearance": ["かっこいい"],
                "first_person": ["私"],
                "age_min": 20,
                "age_max": 27,
                "desc": "【一年は組】\n25歳。教科担当教師／火薬委員会顧問\n山田先生の紹介で忍術学園の先生になり、現在一年は組の教科担当教師をしている。\nは組の生徒達に振り回されることが多く、胃を痛めることもしばしば。\n幼い頃に家族を失った過去があり、同じ境遇のきり丸とは家族のような深い絆で結ばれている。練り物が苦手。",
                "image": "hansuke.webp"
            },
            {
                "name": "山田 伝蔵（やまだ でんぞう）",
                "type": ["しっかり者","その他"],
                "appearance": ["かっこいい","その他"],
                "first_person": ["私"],
                "age_min": 26,
                "age_max": 30,
                "desc": "【一年は組】\n46歳。実技担当教師。\n忍たまたちへの愛がいっぱいの父親みたいな先生。\n印地打ちや火縄銃など忍術の腕は抜群！特に変装には自信があり、女装姿のときは「伝子」と呼ばれないと振り向かない。\n忍術学園に単身赴任中で、なかなか実家に帰れないことが悩み。",
                "image": "denzou.webp"
            },
            {
                "name": "今福 彦四郎（いまふく ひこしろう）",
                "type": ["真面目","しっかり者"],
                "appearance": ["可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年い組】\n10歳。学級委員長委員会所属。\n一年い組のまとめ役だが、ちょっと頼りない一面もあり学級委員長であることを不安に思うこともしばしば",
                "image": "hikosirou.webp"
            },
            {
                "name": "黒門 伝七（くろかど でんしち）",
                "type": ["真面目", "しっかり者", "ツンデレ"],
                "appearance": ["かっこいい", "美人"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年い組】\n10歳。作法委員会所属。\n秀才で、プライドが高い。いつも左吉と行動をともにしている。\n成績優秀な一年い組に所属していることを誇りに思っている。",
                "image": "densiti.webp"
            },
            {
                "name": "任暁 佐吉（にんぎょう さきち）",
                "type": ["真面目","しっかり者", "ツンデレ"],
                "appearance": ["かっこいい"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年い組】\n10歳。会計委員会所属。\n成績優秀だが、うぬぼれが強い。伝七とは仲良しでもあり、良きライバル。\n実戦に強い「は組」をライバル視している。",
                "image": "sakiti.webp"
            },
            {
                "name": "上之島 一平（うえのしま いっぺい）",
                "type": ["真面目","おだやか"],
                "appearance": ["おっとり系", "可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年い組】\n10歳。生物委員会所属。\nい組にはめずらしく、おとなしくておだやかな性格。\n伝七・左吉のケンカの仲裁役をすることがおおい。",
                "image": "ippei.jpg"
            },
            {
                "name": "鶴町 伏木蔵（つるまち ふしきぞう）",
                "type": ["おおらか", "陰気", "その他"],
                "appearance": ["可愛い", "ミステリアス系"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年ろ組】\n10歳。保健委員会所属。\nマイペースな性格で、『スリルとサスペンス～』が口ぐせ。\nタソガレドキ忍者の雑渡昆奈門になついている。\nたまに、名探偵伏木蔵モードが発動する。",
                "image": "fusikizou.webp"
            },
            {
                "name": "二ノ坪 怪士丸（にのつぼ あやかしまる）",
                "type": ["真面目","陰気"],
                "appearance": ["ミステリアス系", "その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年ろ組】\n10歳。図書委員会所属。\nおとなしくてまじめな性格。冷静な頭脳派で、日陰ぼっこがすき。",
                "image": "ayakasimaru.jpg"
            },
            {
                "name": "初島 孫次郎（はつしま まごじろう）",
                "type": ["マイペース", "陰気"],
                "appearance": ["ミステリアス系", "おっとり系"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年ろ組】\n10歳。生物委員会所属。\n同室の平太と一緒に行動することが多く、マイペースな性格なので平太をよく翻弄する。",
                "image": "magojirou.jpg"
            },
            {
                "name": "下坂部 平太（しもさかべ へいた）",
                "type": ["陰気", "その他"],
                "appearance": ["ミステリアス系", "かわいい"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【一年ろ組】\n10歳。用具委員会所属。\n人一倍怖がりなため、一人で行動するのが苦手。\n小さなことでも、すぐにビビってしまうし、チビってしまう。",
                "image": "heita.jpg"
            },
            {
                "name": "池田 三郎次（いけだ さぶろうじ）",
                "type": ["真面目", "しっかり者", "ツンデレ"],
                "appearance": ["かっこいい"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【二年生】\n二年い組　11歳／火薬委員会\n何かと乱太郎たち一年生をからかったりジャマしたりする。根はまじめなしっかり者。",
                "image": "saburouji.webp"
            },
            {
                "name": "川西 左近（かわにし さこん）",
                "type": ["真面目", "おおらか", "ツンデレ"],
                "appearance": ["可愛い"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【二年生】\n二年い組　11歳／保健委員会\n三郎次といっしょに一年生にからんでくるけど、やさしい一面も持っている。困っている人を放っておけない。",
                "image": "sakon.webp"
            },
            {
                "name": "能勢 久作（のせ きゅうさく）",
                "type": ["真面目", "その他"],
                "appearance": ["可愛い"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【二年生】\n二年い組　11歳／図書委員会\n性格はきちょうめん。キッチリしていて、ガンコで融通がきかないところがある。\nときどき、キレてしまうことも…。",
                "image": "kyuusaku.webp"
            },
            {
                "name": "時友 四郎兵衛（ときとも しろべえ）",
                "type": ["天然", "マイペース" ,"おおらか"],
                "appearance": ["可愛い", "おっとり系", "その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【二年生】\n二年は組　11歳／体育委員会\nおだやかでまじめな性格。のほほんとした顔と、やさしい話し方が特徴。",
                "image": "sirobee.webp"
            },
            {
                "name": "羽丹羽 石人（はにわ せきと）",
                "type": ["真面目", "マイペース" ,"おおらか"],
                "appearance": ["可愛い", "おっとり系", "その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 13,
                "desc": "【二年生】\n二年は組　11歳／火薬委員会\nまじめで物腰柔らかな性格。カワタレドキ城に仕える父の言いつけで忍術を学ぶことになり、忍術学園に編入した。",
                "image": "sekito.webp"
            },
            {
                "name": "伊賀崎 孫兵（いがさき まごへい）",
                "type": [ "マイペース" ,"その他"],
                "appearance": ["かっこいい", "美人"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年い組／生物委員会\n生物が大好きで危険なペットをたくさん飼っているが、そのペットたちが逃げ出して騒動になることがよくある。\n特に毒ヘビのジュンコとはいつも一緒。万が一噛まれたときに傷口を焼いて治療するため、左腕に「火縄」を巻いている。",
                "image": "magohei.webp"
            },
            {
                "name": "神崎 左門（かんざき さもん）",
                "type": [ "元気" ,"その他"],
                "appearance": ["元気系", "その他"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年ろ組／会計委員会\n決断力のある方向オンチ。\n無鉄砲で、どんなに失敗しても自分の決断を信じきる、一本気な性格。",
                "image": "samon.webp"
            },
            {
                "name": "次屋 三之助（つぎや さんのすけ）",
                "type": [ "マイペース" ,"天然"],
                "appearance": ["元気系", "その他"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年ろ組／体育委員会\n知らないうちに迷っている、無自覚な方向オンチ。\n左門とコンビで、よく行方不明になる。物に動じない、ひょうひょうとした性格。",
                "image": "sannosuke.webp"
            },
            {
                "name": "富松 作兵衛（とまつ さくべえ）",
                "type": [ "真面目" ,"しっかり者"],
                "appearance": ["かっこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年ろ組／用具委員会\n世話の焼ける左門と三之助が迷子になってはぐれないようにいつも面倒を見ている。\n責任感の強いしっかりもの。心配性な一面もある。",
                "image": "sakubee.webp"
            },
            {
                "name": "浦風 藤内（うらかぜ とうない）",
                "type": [ "真面目" ,"天然"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年は組／作法委員会\n自主トレや予習を進んで行う、まじめな性格。予習することに固執するあまり、空回りすることも・・・。",
                "image": "tounai.webp"
            },
            {
                "name": "三反田 数馬（さんたんだ かずま）",
                "type": [ "おおらか" ,"その他"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["僕"],
                "age_min": 10,
                "age_max": 14,
                "desc": "【三年生】\n12歳　三年は組／保健委員会\n影が薄いことがなやみで、存在を忘れられることが多い。そのせいか、不運に見舞われることも多々あるが、影の薄さが忍者に向いていることにまだ気付いていない・・・",
                "image": "kazuma.webp"
            },
            {
                "name": "平滝夜叉丸（たいらのたきやしゃまる）",
                "type": ["お調子者" ,"元気"],
                "appearance": ["美人", "かっこいい"],
                "first_person": ["私"],
                "age_min": 11,
                "age_max": 15,
                "desc": "【四年生】\n13歳　四年い組／体育委員会\n自分のことが大好きで、うぬぼれが強すぎるのが難点。教科・実技も学年で一番だと思い込んでいる。\n得意武器は戦輪（せんりん）で、「輪子ちゃん」とよんでいる。",
                "image": "takiyasyamaru.webp"
            },
            {
                "name": "綾部 喜八郎（あやべ きはちろう）",
                "type": ["マイペース" ,"天然"],
                "appearance": ["美人", "可愛い"],
                "first_person": ["僕"],
                "age_min": 11,
                "age_max": 15,
                "desc": "【四年生】\n13歳　四年い組／作法委員会\nマイペースでひょうひょうとしている。罠を仕掛けるのが得意で、「天才トラパー」の異名を持つ。\n愛用の用具は踏鋤で、「踏子ちゃん」と呼んでいる。",
                "image": "kihatirou.webp"
            },
            {
                "name": "田村 三木ヱ門（たむら みきえもん）",
                "type": ["お調子者" ,"元気"],
                "appearance": ["美人", "可愛い"],
                "first_person": ["私"],
                "age_min": 11,
                "age_max": 15,
                "desc": "【四年生】\n13歳　四年ろ組／会計委員会\n忍術学園のアイドルと豪語し、過激な武器である石火矢やカノン砲などを得意武器としている。\n火縄銃の使い手である照星を尊敬している。また、似たもの同士の滝夜叉丸とは、ライバル関係。",
                "image": "mikiemon.webp"
            },
            {
                "name": "浜 守一郎（はま しゅいちろう）",
                "type": ["おおらか" ,"元気"],
                "appearance": ["元気系", "かこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 11,
                "age_max": 15,
                "desc": "【四年生】\n13歳　四年ろ組／用具委員会\n家は先祖代々マツホド城忍者で、幼少期に耳の遠い祖父から忍術の知識を学んでいた。そのせいで、大きな声でしゃべってしまう癖がある。\nおやじギャグに対する笑いの沸点が低い。忍術学園には編入生として入ってきた。\n得意武器は、南蛮鉤	（なんばんかぎ）。",
                "image": "syuitirou.webp"
            },
            {
                 "name": "斉藤 タカ丸（さいとう たかまる）",
                "type": ["おおらか" ,"しっかり者"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["僕", "敬語の時は一人称が変わる"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【四年生】\n15歳　四年は組／火薬委員会\n代々忍者の家柄で、父親の斉藤幸隆は人気のカリスマ髪結い師。元髪結い師ということもあり、くの一からは注目される存在。\n忍術学園には編入生として入ってきた。",
                "image": "takamaru.webp"
            },
            {
                "name": "久々知 兵助（くくち へいすけ）",
                "type": ["真面目" ,"しっかり者", "天然"],
                "appearance": ["美人", "かっこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 12,
                "age_max": 16,
                "desc": "【五年生】\n14歳　五年い組／火薬委員会委員長代理\n頭が良く、成績優秀。豆腐が大好物で、豆腐に詳しく、豆腐小僧と呼ばれている。\n家は山守で、体幹を鍛えるために豆腐を落とさないように鍛練をしていた。\n得意武器は、寸鉄（すんてつ）。",
                "image": "heisuke.webp"
            },
            {
                "name": "尾浜 勘右衛門（おはま かんえもん）",
                "type": ["しっかり者" , "天然"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 12,
                "age_max": 16,
                "desc": "【五年生】\n14歳　忍術学園　五年い組／学級委員長委員会\n性格は天然ボケで巻き込まれ型。特徴的な髪の毛がトレードマーク。\n得意武器は、万力鎖（まんりきぐさり）で同室である久々知の得意武器が接近戦向きのため、それを補うために守備範囲の広い武器を選んだ。",
                "image": "kanemon.webp"
            },
            {
                "name": "不破 雷蔵（ふわ らいぞう）",
                "type": ["真面目" , "おおらか"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["僕"],
                "age_min": 12,
                "age_max": 16,
                "desc": "【五年生】\n14歳　五年ろ組／図書委員会\n穏やかで面倒見が良く、後輩たちに慕われている。\nまじめで優秀だが、優柔不断さが弱点。\n得意技は、印地（いんじ）。",
                "image": "raizou.webp"
            },
            {
                "name": "鉢屋 三郎（はちや さぶろう）",
                "type": ["お調子者" , "その他"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["私"],
                "age_min": 12,
                "age_max": 16,
                "desc": "【五年生】\n14歳　五年ろ組／学級委員長委員会\n成績優秀。特に変装に関しては、忍術学園で一、二を争う達人。\n普段は雷蔵の顔に変装していて、素顔はわからない。\n得意武器は、鏢刀（ひょうとう）。",
                "image": "saburou.webp"
            },
            {
                "name": "竹谷 八左ヱ門（たけや はちざえもん）",
                "type": ["元気" , "おおらか"],
                "appearance": ["元気系", "かっこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 12,
                "age_max": 16,
                "desc": "【五年生】\n14歳　五年ろ組／生物委員会委員長代理\n明るく、責任感が強い。「いったん生き物を飼ったら、最後まで面倒を見るのが人として当然」がモットー。\n得意武器は、微塵（みじん）。",
                "image": "hatizaemon.webp"
            },
            {
                "name": "潮江 文次郎（しおえ もんじろう）",
                "type": ["元気" , "真面目","しっかり者","その他"],
                "appearance": ["元気系", "かっこいい"],
                "first_person": ["俺", "敬語の時は一人称が変わる"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年い組／会計委員会委員長\n「ギンギン、ギ〜ン」が口ぐせの熱い性格で、常に鍛練を欠かさない。\n留三郎とは「犬猿の仲」。重さ10キロの鉄製そろばんを使っている。\n得意武器は、袋鎗（ふくろやり）。",
                "image": "monjirou.webp"
            },
            {
                "name": "立花 仙蔵（たちばな せんぞう）",
                "type": [ "真面目", "しっかり者"],
                "appearance": ["美人", "かっこいい"],
                "first_person": ["私"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年い組／作法委員会委員長。\n学園一クールな優等生だが、怒るとこわい。火薬や火器の扱いが得意。\nしんべヱ・喜三太といっしょに行動すると、なぜか振り回されてしまう結果に…。\n得意武器は、宝禄火矢（ほうろくひや）。",
                "image": "sezou.webp"
            },
            {
                "name": "中在家 長次（なかざいけ ちょうじ）",
                "type": [ "真面目", "しっかり者", "おおらか"],
                "appearance": ["その他", "かっこいい"],
                "first_person": ["私"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年ろ組／図書委員会委員長\n学園一無口で無表情。笑っているときは逆に不気味で怖い。一年生の時に鍛練のしすぎで、顔に傷を負ってしまってから笑えなくなってしまった。\n得意武器は、縄鏢（じょうひょう）。",
                "image": "tyouji.webp"
            },
            {
                "name": "七松 小平太（ななまつ こへいた）",
                "type": [ "元気", "その他"],
                "appearance": ["元気系"],
                "first_person": ["私"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年ろ組／体育委員会委員長\n「いけいけどんどーん!!」と細かいことは気にしない豪快な性格で、並外れた体力の持ち主。たまに調子にのりすぎてしまうことも…。\n得意武器は、苦無（くない）。",
                "image": "koheita.webp"
            },
            {
                "name": "善法寺 伊作（ぜんぽうじ いさく）",
                "type": [ "おおらか", "その他"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["僕"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年は組／保健委員会委員長\n穏やかで優しい性格で、ケガ人を見ると放っておけない。薬草に詳しい。\n不運に見舞われることが多く、所属している保健委員会は「不運委員会」とよばれることも。\nあらゆるものを武器として活用する、乱定剣を得意とする。",
                "image": "isaku.webp"
            },
            {
                "name": "食満 留三郎（けま とめざぶろう）",
                "type": [ "元気", "しっかり者"],
                "appearance": ["かっこいい"],
                "first_person": ["俺"],
                "age_min": 13,
                "age_max": 17,
                "desc": "【六年生】\n15歳　六年は組／用具委員会委員長。\n戦うのが大好きな武闘派で、潮江とはライバル。\n伊作と同室であり、何かと不運に巻き込まれるが、「同室じゃないか」と受け入れてしまう。\n得意武器は鉄双節棍。",
                "image": "tomesaburou.webp"
            },
            {
                "name": "小松田 秀作（こまつだ しゅうさく）",
                "type": [ "お調子者", "天然", "おおらか", "マイペース"],
                "appearance": ["可愛い", "おっとり系"],
                "first_person": ["僕"],
                "age_min": 14,
                "age_max": 20,
                "desc": "【忍術学園関係者】\n忍術学園　事務員\n忍術学園の出入りチェックにはきびしく、入門票と出門票のサイン確認は欠かさない！だけど、ドジを踏んだり、失敗したりすることが多い。\n忍者になるのが夢。（忍者3級は持っている）",
                "image": "syuusaku.webp"
            },
            {
                "name": "山田 利吉（やまだ りきち）",
                "type": [ "真面目", "しっかり者"],
                "appearance": ["かっこいい", "美人"],
                "first_person": ["私"],
                "age_min": 16,
                "age_max": 25,
                "desc": "【忍術学園関係者】\n山田先生のひとり息子。フリーの売れっ子忍者として大活躍している。\n山田先生が家に帰ってこず、忍術学園に来ることもしばしば。\n小さいころから土井先生を慕っている。",
                "image": "rikiti.webp"
            },
            {
                "name": "雑渡 昆奈門（ざっと こんなもん）",
                "type": [ "お調子者", "しっかり者"],
                "appearance": ["かっこいい","その他"],
                "first_person": ["私"],
                "age_min": 25,
                "age_max": 30,
                "desc": "【タソガレドキ城】\nタソガレドキ忍軍忍び組頭。\nとても優秀な忍者で部下の信頼もあつい。\n合戦場で、敵味方の区別なくケガの手当てをしてくれた伊作に恩義を感じて以来、忍たまには好意的。\n若い頃、尊奈門の父を助けたことがある。",
                "image": "zatto.webp"
            },
            {
                "name": "諸泉 尊奈門（もろいずみ そんなもん）",
                "type": [ "真面目", "しっかり者", "おおらか", "元気"],
                "appearance": ["可愛い","おっとり系"],
                "first_person": ["私"],
                "age_min": 15,
                "age_max": 23,
                "desc": "【タソガレドキ城】\n雑渡昆奈門の忠実な部下で、若い忍者。\n土井先生をライバル視していて勝負を挑むが、ことごとく文房具で撃退されてしまう。",
                "image": "sonnamon.webp"
            }
        ]

        for char in characters:
            if (
                any(t in character_type for t in char["type"]) and
                any(a in appearance_features for a in char["appearance"]) and
                any(r == relationship for r in char["first_person"]) and
                char["age_min"] <= age_range <= char["age_max"]
            ):
                recommendations.append(char)

        def get_related_characters(target_char, all_chars):
            # desc内の括弧内のグループ名
            char_group = target_char["desc"].split("【")[1].split("】")[0]
            related = []
            # 1. グループ名一致
            for related_char in all_chars:
                if (
                    char_group in related_char["desc"]
                    and related_char["name"] != target_char["name"]
                    and related_char not in related
                ):
                    related.append(related_char)
            return related

        # 🎯 課題: この関数を完成させてください！
        def create_character_prompt(char):
            """
            キャラクター固有のプロンプトを作成する関数
            
            Args:
                char (dict): キャラクター情報の辞書
                    - name: キャラクター名
                    - type: 性格のリスト
                    - appearance: 見た目のリスト
                    - first_person: 一人称のリスト
                    - desc: 詳細説明
            
            Returns:
                str: Gemini APIに送信するプロンプト文字列
            """
            # TODO: ここに実装してください！
            
            
            return ""

        if not recommendations:
            st.info("あなたの好みに合うキャラクターが見つかりませんでした。ランダムで3人紹介します！")
            random_chars = random.sample(characters, min(3, len(characters)))
            for i, char in enumerate(random_chars):
                st.markdown(f"### {i+1}. {char['name']}")
                if "image" in char:
                    image_path = os.path.join(os.getcwd(), char["image"])
                    if os.path.exists(image_path):
                        st.image(image_path, width=200)
                    else:
                        st.write("画像が見つかりませんでした。")
                else:
                    st.write("画像が見つかりませんでした。")
                st.markdown(char["desc"].replace('\n', '<br>'), unsafe_allow_html=True)
                

                # 関連人物を折りたたみセクションで表示
                related_characters = get_related_characters(char, characters)
                if related_characters:
                    with st.expander("関連人物", expanded=False):
                        for related_char in related_characters:
                            st.markdown(f"#### {related_char['name']}")
                            if "image" in related_char:
                                image_path = os.path.join(os.getcwd(), related_char["image"])
                                if os.path.exists(image_path):
                                    st.image(image_path, width=150)
                                else:
                                    st.write("画像が見つかりませんでした。")
                            st.markdown(related_char["desc"].replace('\n', '<br>'), unsafe_allow_html=True)
                st.write("---")
        else:
            for i, char in enumerate(recommendations):
                st.markdown(f"### {i+1}. {char['name']}")
                if "image" in char:
                    image_path = os.path.join(os.getcwd(), char["image"])
                    if os.path.exists(image_path):
                        st.image(image_path, width=200)
                    else:
                        st.write("画像が見つかりませんでした。")
                else:
                    st.write("画像が見つかりませんでした。")
                st.markdown(char["desc"].replace('\n', '<br>'), unsafe_allow_html=True)
                
                # チャット開始ボタン
                if chat_available:
                    chat_key = f"chat_active_{char['name']}"
                    if st.button(f"💬 {char['name']}とチャットを開始する", key=f"btn_recommend_{i}"):
                        st.session_state[chat_key] = True
                        st.rerun()
    
                    # チャット機能を表示
                    if st.session_state.get(chat_key, False):
                        st.markdown(f"#### 💬 {char['name']}とのチャット")
                        
                        # メッセージ履歴の初期化（キャラクター別）
                        messages_key = f"messages_{char['name']}"
                        if messages_key not in st.session_state:
                            st.session_state[messages_key] = []

                        # 過去のメッセージを表示
                        for message in st.session_state[messages_key]:
                            with st.chat_message(message["role"]):
                                st.markdown(message["content"])

                        # ユーザー入力
                        prompt = st.chat_input(f"{char['name']}にメッセージを送る...", key=f"input_recommend_{i}")
                        if prompt:
                            # ユーザーメッセージを表示
                            with st.chat_message("user"):
                                st.markdown(prompt)
                            
                            # ユーザーメッセージを履歴に追加
                            st.session_state[messages_key].append({"role": "user", "content": prompt})
                            
                            # AI応答を生成・表示
                            with st.chat_message("assistant"):
                                try:
                                    # キャラクター設定を含むプロンプトを作成
                                    character_prompt = create_character_prompt(char)
                                    
                                    # 会話履歴を含む完全なプロンプト
                                    full_prompt = character_prompt + "\n\n【現在の会話】\n"
                                    for msg in st.session_state[messages_key][-5:]:  # 直近5件
                                        role = "ユーザー" if msg["role"] == "user" else "キャラクター"
                                        full_prompt += f"{role}: {msg['content']}\n"
                                    full_prompt += f"\nキャラクター:"
                                    
                                    response = model.generate_content(full_prompt)
                                    print(full_prompt)
                                    st.markdown(response.text)
                                    
                                    # AI応答を履歴に追加
                                    st.session_state[messages_key].append({
                                        "role": "assistant", 
                                        "content": response.text
                                    })
                                except Exception as e:
                                    st.error(f"エラーが発生しました: {str(e)}")
                                    st.write("もう一度お試しください。")
                        
                        # チャット終了ボタン
                        if st.button(f"チャット終了", key=f"end_recommend_{i}"):
                            st.session_state[chat_key] = False
                            st.rerun()

                # 関連人物を折りたたみセクションで表示
                related_characters = get_related_characters(char, characters)
                if related_characters:
                    with st.expander("関連人物", expanded=False):
                        for related_char in related_characters:
                            st.markdown(f"#### {related_char['name']}")
                            if "image" in related_char:
                                image_path = os.path.join(os.getcwd(), related_char["image"])
                                if os.path.exists(image_path):
                                    st.image(image_path, width=150)
                                else:
                                    st.write("画像が見つかりませんでした。")
                            st.markdown(related_char["desc"].replace('\n', '<br>'), unsafe_allow_html=True)
                st.write("---")

    st.success("キャラクターの紹介が完了しました！") 