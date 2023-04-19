
# 1. 변수, 메모리 주소, 자료형
var1 = "Hello python" #문자열
print(var1) #Hello python
print(id(var1)) #주소를 출력해라 _id 주소 #2306349222064

var1 = 100 #숫자
print(var1) #100
print(id(var1)) #140713685806984
print(type(var1))# 타입이뭐냐? 어떤타입이냐 #<class 'int'>

var2 = 150.25 #실수
print(var2) #150.25
print(id(var2)) #2306348334800
print(type(var2)) #<class 'float'>

var3 = True # True or false만 들어갈 수 있다 #boolean = yes,no
print(var3) #True
print(id(var3)) #140713684278120
print(type(var3)) #<class 'bool'>

#어떤 타입이냐 뭐가 중요하냐 알고
#주소는 아무의미 없음 큰의미없음



# 2. 예약어 확인
import keyword #모듈 임포트
python_keyword = keyword.kwlist #140713684278120
print(python_keyword) #<class 'bool'>
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  [ ] 대괄호 = 리스트

print(type(python_keyword)) # <class 'list'>
print(len(python_keyword)) #35 #몇개냐~~? 할떈 len함수


var1 = "Hello python"
print(var1) #Hello python
print( type(var1) ) #<class 'str'>

var1 = 100
print(var1) #100
print( type(var1) ) #<class 'int'>

var2 = 150.25
print( type(var2) ) #<class 'float'>

var3 = True
print( type(var3) ) #<class 'bool'>

#실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a+b
print('add = ', add)  # add = 30

#정수 -> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)  # add2 = 30.0

#논리형 -> 정수
print(int(True)) # 1
print(int(False)) # 0



