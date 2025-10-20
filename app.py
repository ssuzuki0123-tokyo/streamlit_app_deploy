import streamlit as st
st.title("サンプルアプリ②: 少し複雑なアプリ")

# マークダウン形式で、見出しレベル4:#### 最大6、#の数が小さいほど大きく太く表示される
st.write("#### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("#### 動作モード2: BMI計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

# radio()メソッドを使ってラジオボタンを表示
# ラジオボタンとは、複数の選択肢の中からいずれかを選べるパーツ
    # 第一引数に指定したテキストは、ラジオボタンのラベルとして上部に表示される
    # 第二引数にリストで指定した各要素が、ラジオボタンの選択肢として表示される
selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI計算"]
)

# divider()メソッドで区切り線を表示
st.divider()

# ラジオボタンの選択によって表示を分岐
if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数をカウントしたいテキストを入力してください。")
    text_count = len(input_message)

else:
    height = st.text_input(label="身長(cm)を入力してください。")
    weight = st.text_input(label="体重(kg)を入力してください。")

# button()メソッドで表示されたボタンが押された場合に、if文の中の処理が実行される
# error()メソッドでエラーメッセージを表示
if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")
        else:
            st.error("カウント対象となるテキストを入力してから実行ボタンを押してください。")
    
    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height)/100)**2),1)
                st.write(f"BMI: {bmi}")
            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")
        else:
            st.error("身長と体重をどちらも入力してください。")