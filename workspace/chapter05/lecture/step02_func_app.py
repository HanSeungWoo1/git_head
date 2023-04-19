from statistics import mean, variance
from math import sqrt

dataset = [2, 4,5,6,1,8]

# (1) 산술평균
def Avg(data):
    avg = mean(data)
    return avg

print('산술평균 =', Avg(dataset)) # 산술평균 = 3

# (2) 분산/표준편차
def var_sd(data):
    avg=Avg(data) # 함수 호출

    #list 내포
    diff = [ (d-avg)**2 for d in data]

    var = sum(diff) / (len(data) -1)
    sd = sqrt(var)

    return var, sd

# (3) 함수 호출
v, s = var_sd(dataset)
print('분산 =',v)
print('표준편차 =',s)


# 피타고라스 정리
def pytha (s, t) :
    a = s**2 - t**2
    b = 2 * s * t
    c = s ** 2 + t ** 2
    print("3변의 길이 : ",a,b,c)

pytha(2, 1) # s, t의 인수는 양의 정수를 갖는다.



# 단계 1 : 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n):
    result = []
    for i in range (n):
        r = random.randint(0, 1)
        if(r == 1) :
            result.append(1) #앞면
        else:
            result.append(0) #뒷면

    return result

print(coin(10))



# 단계 2 : 몬테카를로 시뮬레이션 함수 정의
def montaCoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0] # coin 함수 호출

    result = cnt / n # 누적 결과를 시행 횟수(n)로 나눈다.
    return result


# 단계 3 : 몬테카를로 시뮬레이션 함수 호출
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))