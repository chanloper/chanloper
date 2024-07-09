import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """
    홈 페이지 렌더링 함수.
    사용자가 '/' 경로에 접속할 때 호출됨.
    index.html 템플릿을 렌더링하여 보여줌.
    """
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    """
    가위바위보 게임을 진행하는 함수.
    사용자가 '/play' 경로에 POST 요청을 보낼 때 호출됨.
    사용자의 선택과 컴퓨터의 랜덤 선택을 비교하여 게임 결과를 계산하고,
    index.html 템플릿에 결과를 반영하여 보여줌.
    """
    choices = ['바위 ✊', '가위 ✌️', '보 ✋']
    computer_choice = random.choice(choices)

    # 사용자가 선택한 값 가져오기
    user_choice = request.form.get('choice')

    # 게임 결과 초기화
    result = ""

    # 사용자 선택이 유효한지 확인하고 게임 결과 계산
    if user_choice not in choices:
        result = "유효한 값이 아닙니다."
    elif user_choice == computer_choice:
        result = "비겼습니다."
    elif (user_choice == "바위 ✊" and computer_choice == "가위 ✌️") or (user_choice == "보 ✋" and computer_choice == "바위 ✊") or (user_choice == "가위 ✌️" and computer_choice == "보 ✋"):
        result = "사용자 승리!"
    else:
        result = "컴퓨터 승리!"

    # index.html 템플릿 렌더링하여 사용자 선택, 컴퓨터 선택, 게임 결과 전달
    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)


if __name__ == '__main__':
    app.run(debug=True)
