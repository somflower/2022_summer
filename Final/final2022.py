#모듈
import math
def isPrime(x) :
    flag = 1

    for i in range(2, x):
        if x % i == 0 :
            flag = 0
            break
    if flag == 1 :
        return 1
    else:
        return 0

def toPower(x) :
    return 2**x