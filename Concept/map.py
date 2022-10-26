#list(map(함수, 리스트 등 데이터))
def two_times(x) :
    return x * 2

print(list(map(two_times, [1, 2, 3, 4, 5, 6])))

print(list(map(lambda x : x*2, [1, 2, 3, 4, 5, 6])))
