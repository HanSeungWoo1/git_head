
num1 = 100 # 피연산자1
num2 = 20 # 피연산자2

add = num1 + num2 # 덧셈
print('add=', add)      #add= 120
sub = num1 - num2 # 뺄셈
print(sub)              # 80
mul = num1 * num2 # 곱셈
print(mul)              # 2000
div = num1 / num2 # 나눗셈
print(div)              # 5.0
div2 = num1%num2 # 나머지 계산
print(div2)             # 0
square = num1**2 # 제곱 계산
print(square)           # 10000




num1 = 100 # 피연산자1
num2 = 20 # 피연산자2
# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)          # false
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)          # true

# (2) 크기비교
bool_result = num1 > num2 # num1 값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1 값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2 값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2 값이 크거나 같은지 비교
print(bool_result)


num1 = 100 # 피연산자1
num2 = 20 # 피연산자2
# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <=10 # 두 관계식이 같은지 판단
print(log_result)      # false(0)
log_result = num1 >= 50 or num2 <=10 # 두 관계식 중 하나라도 같은지 판단
print(log_result)     # true(1)

log_result = num1 >= 50 #관계식 판단
print(log_result)
log_result = not(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정
print(log_result)


# (1) 변수에 값 할당(=)
i = tot = 10 # i = 10; tot = 10
i += 1 # i = i + 1
tot += i # tot = tot + i
print(i, tot)

# 알아두기
# i += 1  # i = i + 1  알
# i -= 1 # i = i - 1   아
# i *= 1 # i = i * 1   두
# i /= 1 # i = i / 1   기


# 같은 줄에 중복 출력
print('출력1', end=' , ') # end = '구분자'
print('출력2')            # 출력1 , 출력2

v1 , v2 = 100, 200
v2 , v1 = v1 , v2
print(v1, v2) # 200 100             # 200 100

# (3) 패킹(packing) 할당
lst = [1, 2, 3, 4, 5]
v1 , *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]      # 1 [2, 3, 4, 5]


v1 ,v12 ,*v3 = lst
print(v1 ,v12, v3) #1,2[3,4,5]

*v1 , v2 = lst
print(v1,v2) # [1, 2, 3, 4] 5       # [1,2,3,4]5