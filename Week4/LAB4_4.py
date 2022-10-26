import random
key = random.randint(1,100)

print("숫자를 맞혀 보세요.(1~100)")
num = int(input())

while num!= key:
    if(num>key):
        print("숫자가 너무 큽니다.")
    elif(num<key):
        print("숫자가 너무 작습니다.")
    num = int(input())

print("정답입니다. 입력한 숫자는", key,"입니다.")