#(1) 함수 정의
def calc_func(a,b): #외부함수
    #변수선언 : 자료저장
    x = a # 10
    y = b # 20

    def plus(): #내부함수
        p = x + y
        return p

    def minus(): #내부함수
        m = x - y
        return m
    return plus,minus()

