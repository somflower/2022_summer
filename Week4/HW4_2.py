import random
#randrange -> 0부터 n-1까지
num1 = random.randint(1,100)
num2 = random.randint(1,100)
cnt = 0
correct = 0

print("<<덧셈 문제 연습 게임>>")
print("-----------------------")

while correct!=5:
    print(num1, "+", num2, "=", end = " ")
    answer = int(input())
    if(answer==num1+num2):
        print("맞았다.")
        correct = correct + 1
    else:
        print("틀렸다.")
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    cnt = cnt + 1

print("시도횟수 :", cnt)