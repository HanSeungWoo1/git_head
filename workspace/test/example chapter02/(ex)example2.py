su = 5
dan = 800
print("su 주소 :",id(su))
print("dan 주소 :",id(dan))
print("금액 =",su*dan)


#이것도 정답
su = 5
dan = 800
price = su * dan
print("su 주소:",id(su))
print("dan 주소 :",id(dan))
print("금액 =",price)