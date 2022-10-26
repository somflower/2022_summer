num = 18
for i in range(2,num):
    if num % i == 0:
        print("소수가 아니다")
        break
else:
    print("소수이다")