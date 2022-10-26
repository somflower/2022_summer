s = {1, 2, 3}
s2 = {1, 2, 4, 5}

print(s|s2)
print(s&s2)
print(s-s2)
print(s2-s)


print(s)
s.add(4)
s.remove(1)
print(s)
s.update([1,5,6,7])
print(s)
s.clear()
print(s)

t = (1, 2, 3)
print(t)
#t[0]= 5
print(t[0])