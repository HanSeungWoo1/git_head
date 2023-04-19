def bank_account(bal) : # outer
    balance = bal # 잔액

    def getBalance() : # balance 확인 : getter()
        return balance

    def deposit(money) : # balance += money : setter()
        nonlocal balance
        balance += money

    def withdraw(money) : # balance -= money : setter()
        # 조건 : balance >= money
        nonlocal balance
        if balance >= money :
            balance -= money
        else :
            print("출금액이 잔액보다 커서 출금되지 않았습니다.")

    return getBalance, deposit, withdraw


# 잔액 입력
bal = int(input('개설할 계좌 입금액 : '))
# 외부 함수 호출
getBalance, deposit, withdraw = bank_account(bal)
#잔액확인
print("현재 계좌 잔액은 {}원 입니다.".format(getBalance()))

# 계좌입금
money = int(input('입금액을 입력하세요: ')).deposit(money)
print("{}원 입금후 잔액은 {}원 입니다.".format(money, getBalance()))