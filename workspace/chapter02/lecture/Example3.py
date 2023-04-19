#이것도 정답
con = input("첫번째 단어: ")
spo = input("두번째 단어: ")
exp = input("세번째 단어: ")

print("첫번째 단어: ",con)
print("두번째 단어: ",spo)
print("세번째 단어: ",exp)
print("="*30)
addr = con[0]+spo[0]+exp[0]
print("약자 : ",addr)


#완답
word1 = input("첫번째 단어: ")
word2 = input("두번째 단어: ")
word3 = input("세번째 단어: ")

addr = word1[0] + word2[0] + word3[0]
print("="*15)
print('약자 : ' + addr)