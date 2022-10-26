F = int(input("화씨 온도를 입력하세요: "))

print(round((lambda x : (x-32)/1.8)(F),2))