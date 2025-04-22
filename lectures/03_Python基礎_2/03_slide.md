---
marp: true
theme: default
paginate: true
header: "大妻女子大学 社会情報学部 WebプログラミングI"
footer: "第3回：Python基礎 (2): 制御構造と関数"
size: 16:9
style: |
  section {
    font-size: 25px;
  }
  h1 {
    font-size: 32px;
  }
  h2 {
    font-size: 28px;
  }
  code {
    font-size: 18px; /* コードのフォントサイズ調整 */
  }
  pre code {
    font-size: 16px; /* コードブロック内のフォントサイズ調整 */
    line-height: 1.2; /* 行間調整 */
  }
  table {
    font-size: 20px; /* テーブルのフォントサイズ調整 */
  }

---

<!-- _class: lead -->
# 第3回 Python基礎 (2)
## 制御構造と関数

大妻女子大学 社会情報学部 WebプログラミングI
担当：余野
出席認証コード: 3343
授業資料: https://x.gd/NoqkC (大学のアカウントでgoogleにログインしていることが必要)

---

## 本日の流れ

1.  **前回の復習**
2.  **条件分岐 (if文)**
3.  **繰り返し (forループ)**
4.  **繰り返し (whileループ)**
5.  **ネストした制御構造**
6.  **関数 (def 基本)**
7.  **関数 (詳細 - 引数, Docstring)**
8.  **総合演習**
9.  **まとめと次回予告**

**目標:** if, for, while, def を使いこなし、プログラムの流れを自在に操る！

---

## 1. 前回の復習

- **変数:** 値を入れておく箱 (`x = 10`)
- **データ型:** `int`, `float`, `str`, `list`, `bool`
- **演算:** 算術(`+`, `-`, `*`, `/`, `%`, `**`), 比較(`==`, `!=`, `<`, `>`), 論理(`and`, `or`, `not`)
- **文字列操作:** 連結(`+`), 繰り返し(`*`), インデックス(`[ ]`), スライス(`[:]`), メソッド(`.upper()`, `.replace()`...)
- **リスト操作:** インデックス(`[ ]`), スライス(`[:]`), 追加(`.append()`), 変更(`fruits[i]=...`), 削除(`.remove()`, `del`, `.pop()`)
- **タプル:** 変更不可のリスト (`()`, `,`)
- **入出力:** `input()`, `print()`
- **型変換:** `int()`, `float()`, `str()`

---

## 2. 条件分岐 (if文) - 復習

**特定の条件に応じて処理を変えたい**

```python
if 条件式1:
    # 条件式1がTrueの処理
elif 条件式2:
    # 条件式1がFalseで、条件式2がTrueの処理
else:
    # すべての条件がFalseの処理
```
- 比較演算子 (`==`, `!=`, `<`, `>`...) と論理演算子 (`and`, `or`, `not`) で条件を作る。
- インデントが重要！

---

## if文の例 - 復習

**例: 点数による評価**
```python
score = 75

if score >= 80:
    print("優")
elif score >= 60:
    print("良")
elif score >= 0:
    print("可")
else:
    print("無効な点数です") # 負の点数など
```
**▶ 演習: `03_lecture.ipynb` で試してみよう！**

---

## 3. 繰り返し処理 (forループ) - 復習

**リストの要素や、決まった回数だけ処理を繰り返したい**

```python
# リストの要素を順に処理
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 0から4まで繰り返す (計5回)
for i in range(5):
    print(i)

# break (中断) と continue (スキップ)
for i in range(10):
    if i == 5:
        break # ループを抜ける
    if i % 2 == 0:
        continue # 次の繰り返しへ
    print(i) # 1, 3 が出力される
```
**▶ 演習: `03_lecture.ipynb` で試してみよう！**

---

## 4. 繰り返し処理 (whileループ) - 新登場！

**特定の条件が満たされている間、処理を繰り返したい**
(繰り返しの回数が事前に分からない場合に便利)

**基本的な形:**
```python
while 条件式:
    # 条件式がTrueの間、実行される処理
    # ...
    # 注意: ループ内で条件式がいつかFalseになるようにする！
```

**例: カウンタ変数を使う**
```python
count = 0
while count < 5:
    print(f"現在のカウント: {count}")
    count += 1 # カウントを増やす (忘れると無限ループ！)
print("ループ終了")
```

---

## whileループ: `break` と 無限ループ注意

- `while` ループでも `break` で中断できる。
- 条件式が常に `True` になってしまうと **無限ループ** に陥る。
  (プログラムが止まらなくなるので注意！)

**例: 特定の入力があるまで繰り返す**
```python
while True: # わざと無限ループにして...?
    user_input = input("終了するには 'exit' と入力: ")
    if user_input == "exit":
        break # 'exit' が入力されたらループを抜ける
    print(f"入力された文字: {user_input}")

print("プログラム終了")
```
**▶ 演習: `03_lecture.ipynb` で試してみよう！**

---

## 5. ネストした制御構造

**制御構造の中に、さらに制御構造を入れることができる (入れ子)**

- `if` の中に `for` や `while`
- `for` や `while` の中に `if`

**例: リストの数値から偶数だけ表示**
```python
numbers = [1, 5, 2, 8, 3, 10, 7]

for num in numbers: # 外側のループ
    if num % 2 == 0: # 内側の条件分岐
        print(f"偶数発見: {num}")
```

複雑な処理も組み合わせで実現できる！
**▶ 演習: `03_lecture.ipynb` で試してみよう！**

---

## 6. 関数 (def) - 基本の復習

**処理をまとめて再利用可能にする**

```python
def 関数名(引数1, 引数2, ...):
    # 関数の中で行う処理
    # ...
    return 戻り値 # 戻り値
```
- **引数:** 関数に渡す情報
- **戻り値:** 関数が返す結果 (`return` がないと `None` を返す)
- **スコープ:** 関数内の変数は基本的に外から見えない (ローカル変数)

**例: 合計を計算**
```python
def calculate_sum(a, b):
    total = a + b
    return total

result = calculate_sum(5, 3)
print(result) # 8
```

---

## 7. 関数 (詳細) - 引数の指定方法

**デフォルト引数:** 引数に初期値を設定できる。
呼び出し時に省略すると、その初期値が使われる。
```python
def greet(name="ゲスト"):
    print(f"こんにちは、{name}さん！")

greet("山田") # こんにちは、山田さん！
greet()      # こんにちは、ゲストさん！ (省略時はデフォルト値)
```

**キーワード引数:** 引数名を指定して値を渡せる。
順序を気にしなくて良い、意味が分かりやすくなる。
```python
def describe_pet(pet_name, animal_type="犬"):
    print(f"私のペットは{animal_type}の{pet_name}です。")

describe_pet(pet_name="ポチ")             # 私のペットは犬のポチです。
describe_pet(pet_name="タマ", animal_type="猫") # 私のペットは猫のタマです。
describe_pet(animal_type="ハムスター", pet_name="コロ") # キーワード引数なら順序逆でもOK
```

---

## 7. 関数 (詳細) - Docstring (ドキュメンテーション文字列)

**関数が何をするものか説明する文字列**

- `def` 文の直下に `"""説明文"""` (トリプルクォート) で書く。
- 関数を使う人 (将来の自分も含む！) が理解しやすくなる。
- `help()` 関数や、開発ツールで表示される。

```python
def calculate_sum(a, b):
    """二つの数値を受け取り、その合計を返す関数。

    Args:
        a (int or float): 一つ目の数値。
        b (int or float): 二つ目の数値。

    Returns:
        int or float: 二つの数値の合計。
    """
    total = a + b
    return total

# Docstringを表示してみる
help(calculate_sum)
# print(calculate_sum.__doc__)
```
**▶ 良い習慣として書くようにしよう！**

---

## 8. 総合演習

**`03_exercises.ipynb` を使って、今日学んだことをフル活用！**

- **演習内容 (例):**
    - 数値リストを受け取り、偶数だけを抽出して新しいリストを返す関数を作る (for, if, def, return)。
    - ユーザーに繰り返し数値を入力させ、合計が100を超えたら終了するプログラム (while, break, input, int)。
    - デフォルト引数やキーワード引数を使った関数を定義・呼び出し。
    - 作成した関数に Docstring を付ける。

**`if`, `for`, `while`, `def` を組み合わせて、少し複雑な課題に挑戦！**

---

## 9. まとめ

- **条件分岐 (if文):** `if`, `elif`, `else`
- **繰り返し (forループ):** `for ... in ...`, `range()`, `break`, `continue`
- **繰り返し (whileループ):** `while 条件式:`, `break`, 無限ループ注意
- **ネスト構造:** 制御構造の入れ子で複雑な処理
- **関数 (def):**
    - 基本: `def 関数名(引数): ... return 戻り値`
    - 詳細: デフォルト引数 (`arg="default"`), キーワード引数 (`func(arg=value)`), Docstring (`"""説明"""`)

これらを使いこなせば、より構造化された、読みやすいプログラムが書けます！

---

## 次回予告

**第4回: Streamlit基本 (1): テキストとデータ表示**

いよいよ Web アプリケーションフレームワーク **Streamlit** の登場です！

- `st.write()` 以外にも、様々なテキストやデータを表示する方法を学びます。
    - `st.markdown()`
    - `st.dataframe()`
    - `st.table()`
    - `st.metric()`

