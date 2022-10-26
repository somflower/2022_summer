#키워드 인수
def f1(a, b):
    print(a,b)

#디폴트 인수
def f2(a = 0, b = 0):
    print(a,b)

#가변 인수
def f3(*args):
    print(args)

#키워드 가변 인수
def f4(**kwargs):
    print(kwargs)
    print("{a}".format(**kwargs))
    print("{b}".format(**kwargs))
    print("{c}".format(**kwargs))


f1(b = 10, a = 3)
f2()
f2(10)

f3(1,2,3,4,5)

f4(a=10,b=20,c=30)