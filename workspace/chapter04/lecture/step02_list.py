# (1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[:i]) # i 전까지


# (1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)

for i in lst :
    print(lst[i-1:]) # i 전까지


# (2) 단일 list 색인
x = list(range(1, 11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2]) # 홀수 색인
print(x[1::2]) # 1부터 시작 하는 짝수 색인



# (1) 단일 리스트 객체 생성 # 다루는 방법을 잘 알아놓아라
a = ['a', 'b', 'c']

# (2) 중첩 리스트 객체 생성
b = [10, 20, a, 5, True, '문자열'] # 서로 다른 자료형
print(b[0]) # 10
print(b[2]) # ['a', 'b', 'c'] -> 중첩 list
print(b[2][0]) # a -> 중첩 list 1번 원소
print(b[2][1:]) # ['b', 'c'] -> 중첩 list 2번 이후 원소
print(a)



# (1) 단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(len(num)) # 4

# (2) 리스트 원소 추가
num.append('five') # 추가 #업엔드는 추가 리무브는 삭제 알아두기
print(num) # ['one', 'two', 'three', 'four', 'five']
#추가는 삽입과 다르게 맨뒤에 붙는다
# (3) 리스트 원소 삭제
num.remove('five') #삭제
print(num)

# (4) 리스트 원소 수정
num[3] = '4' # 수정
print(num)

# (5) 리스트 원소 삽입
num.insert(0, 'zero') # 삽입
print(num)
#삽입은 추가와 다르게 위치지정해서 넣을 수 있다


# (1) 리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y  # new object
print(z) #[1, 2, 3, 4, 1.5, 2.5]

# (2) 리스트 확장
x.extend(y)  # x 확장
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# (3) 리스트 추가
x.append(y) # x 추가
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# (4) 리스트 두 배 확장
lst = [1, 2, 3, 4] # list 생성
result = lst * 2 # 각 원소 연산 안됨
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]


result = [1,2,3,4,1,2,3,4]
# (1) 리스트 정렬
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]
result.sort() # 오름차순 정렬
print(result) # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse = True) # 내림차순 정렬
print(result) # [4, 4, 3, 3, 2, 2, 1, 1]

# (2) 리스트 요소 검사
import random
r = [] # 빈 list
for i in range(5) : # 5개의 숫자를 가지고
     r.append(random.randint(1,5))

print(r)
if 4 in r :
    print('있음')
else :
    print('없음')


# 리스트 내포 예

#형식1) 변수 = [실행문   for   ]
x = [2, 4, 1, 5, 7]

lst = [ i ** 2   for i in x] # x변량에 제곱 계산
print(lst) # [4, 16, 1, 25, 49]

# 형식2) 변수 = [실행문 for if]
# 1~10 -> 2의 배수 추출 -> i*2 -> list 저장
num = list(range(1,11))

lst2 = [ i*2 for i in num if i % 2 ==0 ]
print(lst2)


# (1) 원소가 한 개인 경우
t = (10, )
print(t)

# (2) 원소가 여러 개인 경우
t2 = (1, 2, 3, 4, 5, 3)
print(t2)

# (3) 튜플 색인
print(t2[0], t2[1:4], t2[-1])

# (4) 수정 불가
# t2[0] = 10 # error

# (5) 요소 검사
if 6 in t2 :
    print("6 있음")
else :
    print("6 없음")
