import random
lotto = []

for i in range(5):
    for j in range(6):
        num = random.randint(1,45)
        if lotto.count(num) == 0:
            lotto.append(num)
    print(lotto)
    lotto = []
#count함수, lotto.count(num)==0, 기존의 list에서 해당 숫자가 있는 지 확인
#if in 사용도 가능
