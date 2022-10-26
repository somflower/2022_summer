list1 = []

print(list1)

list1.append(1)
list1.append('2')
list1.append([3])
print(list1)

list1.extend([5, 6, 7])
print(list1)

list1.insert(3, 4)
print(list1)

list1.remove([3])
print(list1)

del list1[4]
print(list1)

print(list1)
print(list1.pop())
print(list1)

#print(list1.remove[5])

print(list1)
print(list1.index(1))