num1=100
num2=20

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)

# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <= 10
print(log_result)

log_result = num1 >= 50 #관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1>=50)
print(log_result)


# (1) 변수에 값 할당 (=)
i = tot = 10 # i = 10; tot = 10
i += 1 # i = i+1
tot += i # tot = tot + i
print(i,tot)

# 같은 줄에 중복 출력
print('출력1', end=', ') # end ='구분자'
print('출력2')

v1, v2 = 100,200

#(2) 변수 교체

v2, v1 = v1, v2
print(v1, v2) # 200 100

# (3) 패킹(packing) 할당
lst = [1, 2, 3,4, 5]
v1, *v2 = lst
print(v1,v2) # 1[2,3,4,5]

*v1, v2 = lst
print(v1,v2) # [1,2,3,4]5