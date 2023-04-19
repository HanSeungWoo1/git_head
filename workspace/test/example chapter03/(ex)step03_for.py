multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
words = []
sents = []
for sent in multiline.split('\n') :
    sents.append(sent)
    for word in sent.split(' ') :
        words.append(word)
        print(word)
print('단어 개수 : ', len(words))

# multiline.split
# sent.split