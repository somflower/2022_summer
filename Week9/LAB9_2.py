list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list3 = []

for i in list1 :
    (lambda x : list2.append(x) if x%2 == 0 else list3.append(x))(i) 

print("원래 리스트", list1)
print("짝수 리스트", list2)
print("홀수 리스트", list3)