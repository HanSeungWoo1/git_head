#숫자 맞히기 게임

import random

# 변수 정의하기
guesses = 0 # 시도 횟수 기록하기
numMin = 1  # 범위 시작 숫자
numMax = 100 # 범위 끝 숫자
userInput ="" # 사용자 입력 저장하기

randNum = random.randint(numMin, numMax) # 1~100
while randNum != userInput:
    # 사용자 답 입력받기
    userInput = int(input("예상 숫자: "))
    #시도 횟수 1회 늘리기
    guesses = guesses + 1
    if userInput < randNum:
        print("작습니다. 다시 입력하세요.")
    elif userInput > randNum:
        print("너무 큽니다. 다시 입력하세요. ")
    else:
        print("정답입니다! 시도 횟수:", guesses, "번")

print("즐거우셨나요? 또 만나요!")