import random

choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)

print(computer_choice)

draw = 0
win = 0
lose = 0

# 가위 바위 보 부분 세밀화
# game start
while True:
    user_choice = input("가위,바위,보 중 하나를 선택하세요 : ")
    if user_choice != computer_choice:
        print("유효한 입력이 아닙니다.")
    elif user_choice == computer_choice:
        draw += 1
        print(f"사용자 : {user_choice}, 컴퓨터: {computer_choice}"),
        print("비겼습니다.")
    elif (user_choice == '주먹' and computer_choice == '가위') or (user_choice == '보' and computer_choice == '바위') or (user_choice == '가위' and computer_choice == '보'):
        win += 1
        print(f"사용자 : {user_choice}, 컴퓨터: {computer_choice}"),
        print("사용자 승리!")
    else:
        lose += 1
        print(f"사용자 : {user_choice}, 컴퓨터: {computer_choice}"),
        print("컴퓨터 승리!")
    # 사용자와 컴퓨터가 낸 가위,바위,보 등을 화면에 출력해주어야 함

    user_choice = input("다시 하시겠습니까? (y/n): ")
    if user_choice == 'n':
        print(f"승 :{win} 패 :{lose} 무승부 : {draw}")
        break
    elif user_choice == 'y':
        choices = ['가위', '바위', '보']
        computer_choice = random.choice(choices)
        print(computer_choice)
