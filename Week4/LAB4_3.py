num = int(input())
binary = []
#insert이용해 list의 제일 앞에 넣어주기

while num>0 :
    binary.insert(0, num%2)
    num = int(num / 2)

for i in binary :
    print(i, end = "")


"""while num>0 :
    binary.append(num%2)
    num = int(num / 2)

for i in binary[-1::-1] :
    print(i, end = "")"""

