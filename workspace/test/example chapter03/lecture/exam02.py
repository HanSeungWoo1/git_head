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





multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
words = []
sents = []
for sent in multiline.split('\n'):
    sents.append(sent)
    for word in sent.split(' '):
        words.append(word)
        print(word)
print('단어 개수 :', len(words))