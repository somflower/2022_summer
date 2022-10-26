list1 = [1, 2, 3] #패킹
a, b, c = list1 #언패킹
print(list1, a, b, c)

a, b, c, d, e = list1 #언패킹 에러, 변수개수 많아서
a, b = list1 #언패킹 에러, 변수개수 적어서
