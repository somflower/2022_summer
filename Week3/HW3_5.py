key = [3, 6]
arr = []

num = int(input("내 번호 입력(10 ~ 99): "))
arr.append(num//10)
arr.append(num%10)

print("당첨번호는 36 입니다.")

if (arr[0]==key[0] and arr[1]==key[1]) or (arr[0]==key[1] and arr[1]==key[0]) :
    print("피자10판 당첨")
elif arr[0]==key[0] or arr[0]==key[1] or arr[1]==key[0] or arr[1]==key[1] :
    print("치킨5마리 당첨")
else :
    print("꽝입니다.")