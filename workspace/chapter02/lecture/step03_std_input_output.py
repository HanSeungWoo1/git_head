# (1) 문자형 숫자 입력
num = input("숫자 입력 : ")             # 숫자 입력 : 100
print('num type : ', type(num)) # <class 'str'>     #num type : <class 'str'>
print('num = ', num)                # num = 100
print('num = ', num*2)              # num = 100100


# (2) 문자형 숫자를 정수형으로 변환
num1 = int( input("숫자 입력 : "))   # str -> int  숫자입력 : 100
#(형변환)
print('num1 = ', num1*2)        #num1 = 200

# (3) 문자형 숫자를 실수형으로 변환
num2 = float(input("숫자 입력 : ")) # str -> float(형변환) 숫자입력 : 200
result = num1 + num2 # 실수 = 정수 + 실수
print('result = ', result)          # result = 300.0



#(1) value 인수
print("value =", 10+20+30+40+50)    #value = 150

#(2) sep 인수 : 값과 값을 특수문자로 구분
print("010","1234","5678", sep="-")  #010-1234-5678

#(3) end 인수
print("value=", 10, end = ", ")
print("value=", 20)     # value = 10, value = 20



#
print("안녕하세요! 다음 질문에 답하고 이야기를 완성하세요.")

sto1 = input("동물을 입력하세요 : ")
sto2 = input("이름을 입력하세요 : ")
sto3 = input("형용사를 입력하세요(00(이)고): ")
sto4 = input("색을 입력하세요(00색): ")
sto5 = input("형용사를 입력하세요: ")
sto6 = input("명사를 입력하세요: ")
sto7 = input("명사를 입력하세요: ")
sto8 = input("명사를 입력하세요: ")
sto9 = input("형용사를 입력하세요(00은): ")
sto10 = input("색을 입력하세요: ")
sto11 = input("명사를 입력하세요: ")
print("다음은 여러분이 만든 이야기입니다.")

print("저의 반려동물은",sto1 ,"이며 이름은",sto2 ,"입니다.")
print(sto3 ,"(이)고",sto4 ,"이며",sto5 ,"니다.")
print(sto2 ,"은(는)",sto6 ,sto7 ,sto8 ,"을(를) 먹습니다.")
print("가장 좋아하는 장난감은",sto9 ,sto10 ,sto11 ,"입니다.")



# (4) format() 함수 인수 : format(value, "format")
print("원주율=", format(3.14159, "8.3f") )
print("금액=", format(10000, "10d") )
print("금액=", format(125000, "3,d"))

# (5) 양식문자 인수 : print( "%양식문자" %(값) )
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price))

#(6) 외부 상수 인수
print("이름 : {}, 나이 : {}, data={}".format(name,age,price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age,name,price))

#(7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query) # member 테이블에서 uid가 hong인 레코드 검색