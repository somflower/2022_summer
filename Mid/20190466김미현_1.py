x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

if x1 > y1 :
    v1 = x1 - y1
else :
    v1 = y1 - x1

if x2 > y2 :
    v2 = x2 - y2   
else :
    v2 = y2 - x2

result = (v1**2 + v2**2)**(1/2)

print("점 (%d, %d)와 점 (%d, %d)의 거리는 %.2f이다." % (x1, x2, y1, y2, result))