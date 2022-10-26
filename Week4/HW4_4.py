def func(num):
    list = []
    binary = ""

    while num>0 :
        list.insert(0, num%2)
        num = int(num / 2)

    for i in list:
        binary = binary + str(i)
    
    return binary

num = int(input())
print(func(num))