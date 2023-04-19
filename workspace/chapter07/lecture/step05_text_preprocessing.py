# re 모듈관련 함수 import
from re import findall, sub

# 텍스트
texts = ['우리나라 대한민국, 우리나라%$만세','비아그&라 500GRAM 정력 최고!',
         '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박','나는 홍길동']

# 단계1: 소문자 변경
texts_re1 = [t.lower() for t in texts]
print('texts_re1 :', texts_re1=1)

# 단계2: 숫자 제거
texts_re2 = [sub("[0-9]", '', text)for text in texts_re1]
print('texts_re:',texts_re2)

# 단계3: 문장부호 제거
texts_re3 = [sub('[,.?!:;])']