import final2022
num = int(input("양의 정수 입력: "))
print("-"*20)
if final2022.isPrime(num) == 1 :
    print(str(num)+"은 소수이다.")
else :
    print(str(num)+"은 소수가 아니다.")

print("2의 "+str(num)+"승은 "+ str(final2022.toPower(num))+"이다.")

