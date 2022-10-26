s = {1, 2, 3, 4, 5, 1, 2, 3}
print(s)

s.add(10)#순서 X
print(s)

#s.remove(20)#없어서 에러
s.discard(20)
print(s)

t = {9, 8, 5, 3, 1}
print(s.union(t))
#print(s + t)#에러
print(s.difference(t))
print(t.difference(s))