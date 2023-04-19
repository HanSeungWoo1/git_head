# (1) 입력 자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

# (2) 변수 초기화
vmax = vmin = dataset[0]

# (3) 최댓값 / 최솟값 구하기
for i in dataset:
    if vmax < i:   # 잘 알아두기
        vmax = i   # 잘 알아두기
    if vmin > i:   # 잘 알아두기
        vmin = i   # 잘 알아두기

# (4) 결과 출력
print('max =', vmax, 'min =', vmin)


# (1) 오름차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) : # 1 ~ n-1
    for j in range(i+1, n) : # i+1 ~ n
        if dataset[i] > dataset[j] :
            tmp = dataset[i]        #잘 알아두기 바꾸는거
            dataset[i] = dataset[j] #잘 알아두기 바꾸는거
            dataset[j] = tmp        #잘 알아두기 바꾸는거
        print(dataset) # 각 회전 정렬 내용

print(dataset) # [1, 2, 3, 4, 5]

# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) : # 1 ~ n-1
    for j in range(i+1, n) : # i+1 ~ n
        if dataset[i] < dataset[j] :
            tmp = dataset[i]        #잘 알아두기 바꾸는거
            dataset[i] = dataset[j] #잘 알아두기 바꾸는거
            dataset[j] = tmp        #잘 알아두기 바꾸는거
        print(dataset) # 각 회전 정렬 내용

print(dataset) # [5, 4, 3, 2, 1]
