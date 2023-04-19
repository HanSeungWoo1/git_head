# 함수 정의
def bank_account(bal) :
    balance = bal # 잔액 초기화(1000)
num = int(input("최초 계좌의 잔액을 입력하세요 :"))

    def getBalance(): #잔액확인(getter)
        return balance

    def deposit(money) : #입금하기(setter)