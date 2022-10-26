print("구구단 몇 단을 계산할까요?(1~9)")
num = int(input())
print("구구단", num, "단을 계산합니다.")

while num != 0:
    for j in range(1,10):
        print(num,"*",j,"=", num*j)
    print("구구단 몇 단을 계산할까요?(1~9)")
    num = int(input())
    print("구구단", num, "단을 계산합니다.")
print("구구단 게임을 종료합니다.")