list1 = [1, 2, 3, 4, 5, 6, 7]

print(list1[ : ])#생략
print(list1[ : : ])#생략
print(list1[-50 : 50]) #범위 초과
print(list1[0 : 7 : 1])#생략 안하고 쓰기

print("=" * 21)
print(list1[0 : 6])#증가값 생략
print(list1[0 : 6 : 1])
print(list1[ : 6 : 1])
print(list1[ : 6])#증가값 생략

print("=" * 21)
print(list1[2 : 7])#증가값 생략
print(list1[2 : 7 : 1])
print(list1[2 : : 1])
print(list1[2 : ])#증가값 생략

print("=" * 21)
print(list1[0 : 7 : 2])
print(list1[ : : 2])

#리버스 인덱스
print("=" * 21)
print(list1[-7 : : 1])
print(list1[-7 : -1 : 1])
print(list1[-7 : 0 : 1])
print(list1[-7 : 1 : 1])
print(list1[-7 : 2 : 1])
#어떻게 해야 끝까지 출력하지..? 흠

#거꾸로 출력
print("=" * 21)
print(list1[ : : -1])
print(list1[-1 : : -1])
print(list1[-1 : -8 : -1])