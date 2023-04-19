# (1) list에 자료 저장하기
lst = []  # 빈 list 만들기
for i in range(10) : # 0~9
    r = random.randint(1,10) # 난수 발생
    lst.append(r) # 난수 저장

print('lst =', lst) # 난수 출력

# (2) list에 자료 참조하기
for i in range(10) : #0~9
    print(lst[i] * 0.25) # 난수 * 0.25


# 구구단 출력 : range() 함수 이용

# (1) 바깥쪽 반복문
for i in range(2, 10) :
    print('~~~ {}단 ~~~'.format(i))

    # (2) 안쪽 반복문
    for j in range(1, 10) :

        print('%d * %d = %d'%(i, j, i*j))




#문장과 단어 추출 예
string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = [] # 문장 저장 # 값이 많으니 리스트를 만든다
words = [] # 단어 저장

# (1) 문단 -> 문장
for sen in string.split(sep = "\n") :
    sents.append(sen)#sents 문장을 저장하기 위한 변수 #뒤에 append로 추가 for문에 있는 sen을 가져온다
    # (2) 문장 -> 단어
    for word in sen.split() :
        words.append(word) # 끝나면 위로 올라간다 (for)문으로 주소는, 서울시, 입니디.
print('문장 :', sents)
print('문장수 :', len(sents))
print('단어 :', words)
print('단어수 :', len(words))



#연습문제
while True :
    weight = int(input('짐의 무게는 얼마입니까?'))
    if weight == 0:
        break;
    if weight >= 10 :
        price = (weight // 10) * 10000
        print('수수료는 ' + format(price, '3,d')+ '입니다')
    else :
        print('수수료는 없습니다')




multiLine = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
words = []
sents = []
for sent in multiLine.split('\n') :
    sents.append(sent)
    for word in sent.split(' ') :
        words.append(word)
        print(word)
print('단어 개수 : ', len(words))



multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
cnt = 0
doc = []
word = []
for line in multiline.split("\n"):
    doc.append(line)
    for w in line.split():
        word.append(w)
        print(w)
        cnt += 1

print('단어수 : ', cnt)
print(doc)
print(word)