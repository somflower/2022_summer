import random

num = int(input("리스트의 원소 수를 입력하시오: "))
Total = []
Bigger10 = []
Smaller10 = []

for _ in range(num):
    randN = random.randint(1, 20)
    if Total.count(randN) == 0 :
        Total.append(randN)

for i in Total :
    if i > 10 :
        Bigger10.append(i)
    else :
        Smaller10.append(i)

print("생성된 데이터:", Total)
print("10초과 데이터:", Bigger10)
print("10이하 데이터:", Smaller10)

if Total.count(10) == 1 :
    print("10은 인덱스 %d에 있다." % Total.index(10))
else :
    print("10이 없다.")
