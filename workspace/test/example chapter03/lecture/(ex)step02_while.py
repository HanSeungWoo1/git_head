 # (1) 카운터와 누적변수
 cnt = tot = 0 # 변수 초기화
 while cnt < 5 : # True : loop 수행
     cnt += 1  #카운터 변수 (cnt = cnt + 1)
     tot += cnt # 누적변수 : tot = tot + cnt
     print(cnt,tot)


# [실습] 1~100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = [] # 빈 list

while cnt < 100:    # 100회 반복
    cnt += 1    # 카운터
    if cnt % 3 == 0:
        tot += cnt # 누적변수
        dataset.append(cnt) #cnt추가

print('1~100 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)


# 무한 루프(loop)
numData = [] #빈 list

while True :
    num = int (input("숫자 입력 : "))

    if num % 10 == 0 : # exit 조건식
        print("프로그램 종료")
        break
    else :
        print(num)
        numData.append(num) #list추가

        # 실무에선 True문 잘써라~~!!


# (3) 0~1 사이 난수 실수
import random
r=random.random()
print('r=', r)

# [실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True:
    r = random.random()
    print(r)
    if r < 0.01:
        break # loop exit
    else:
        cnt += 1

print('난수 개수 =',cnt)



