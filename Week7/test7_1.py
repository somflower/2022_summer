from typing import Type
from unittest import result


for i in range(10) :
    try :
        result = 10 / i
    except ZeroDivisionError :
        print("Not divided by 0")
    else :
        print(10 / i)

n = input("어떤 수 입력: ")

try :
    n = int(n)
    result2 = 10 % n
except TypeError:
    print("자료형이 숫자가 아니군요")#16라인 없을때
except ValueError as e:
    print(e)
    print("숫자가 아닌 다른 자료형을 입력하였군요")#a
except :
    print("다른 기타 예외 사항")#0
else :
    print(result2)
finally :
    print("다른 것 합시다")