#모듈 연습
def add(n1, n2) :
    return n1 + n2
def sub(n1, n2) :
    return n1 - n2
def mul(n1, n2) :
    return n1 * n2
def div(n1, n2) :
    return n1 / n2

#모듈도 독립적으로 실행 가능
#print(add(4,5)) --> 가능은 하지만 잘 안씀
#다른 곳에서 모듈 실행시 원치않는 결과 나올 수 있기 때문에
#그때는 아래처럼 수행하면 된다.
if __name__ == "__main__":#내가 메인이면 실행, 다른곳에서 실행돼서 모듈되면 실행X
    print(add(4,5))
