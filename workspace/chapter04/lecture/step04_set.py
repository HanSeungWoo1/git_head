# (1) 중복 불가
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)  # 3 중복이 안되니 중복뺴니 '3'

# (2) 요소 반복

for d in s :
    print(d, end=' ') # 1,3,5 <- 's'

print()

# (3) 집합관련 함수
s2 = {3, 6}
print(s.union(s2)) # 합집합 (전부)   # {1, 3, 5, 6} # 용어 알아두기
print(s.difference(s2)) # 차집합 (빼다) 3,6중 둘중하나 빼 # {1, 5} # 용어 알아두기
print(s.intersection(s2)) # 교집합  # {3}  # 용어 알아두기


# (4) 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7) # 원소 추가
print(s3) #

s3.discard(3) # 원소 삭제
print(s3) #


# 중복 원소를 갖는 리스트
gender = ['남','여','남','여']

# 중복 원소 제거 set!!
sgender = set(gender) # list -> set
lgender = list(sgender) # set -> list # 리스트로 변환 인덱스를 사용하기위해
print(lgender)

print(lgender[1])