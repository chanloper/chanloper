import random
from flask import Flask, render_template, request
app = Flask(__name__)

# 초기 무승부, 승리, 패배 초기화
draw = 0
win = 0
lose = 0

# home 페이지 라우트 처리


@app.route('/')
def home():
    # 초기화한 무승부/승/패 기록을 HTML에 렌더링하여 전달
    return render_template('index.html', win=win, lose=lose, draw=draw)


def play(user_choice):
    global draw, win, lose
    # 가위바위보 게임을 진행하는 함수
    # 사용자가 '/play' 경로에 POST 요청을 보낼때 호출됨.
    # 사용자의 선택과 컴퓨터의 랜덤 선택을 비교하여 게임 결과를 계산하고, index.html 템플릿에 결과를 반영하여 보여줌.
    choices = ['바위 ✊', '가위 ✌️', '보 ✋']
    computer_choice = random.choice(choices)

    reult = ""
    if user_choice not in choices:
        result = "유효 값이 아닙니다."
    elif user_choice == computer_choice:
        draw += 1
        result = "비겼습니다."
    elif (user_choice == "바위 ✊" and computer_choice == "가위 ✌️") or (user_choice == "보 ✋" and computer_choice == "바위 ✊") or (user_choice == "가위 ✌️" and computer_choice == "보 ✋"):
        win += 1
        result = "유저 승리!"
    else:
        lose += 1
        result = "컴퓨터 승리!"

    return result, user_choice, computer_choice


@app.route('/play', methods=['POST'])
def play_game():
    # 사용자가 선택한 값 가져오기
    user_choice = request.form.get('choice')
    result, user_choice, computer_choice = play(user_choice)
    # index.html 템플릿에 렌더링하여 사용자 선택, 컴퓨터 선택, 게임 결과 전달
    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result, win=win, draw=draw, lose=lose)


if __name__ == '__main__':
    app.run(debug=True)
