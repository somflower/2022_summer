#map 예시
def abs_func(x) :
    if (x > 0) : return x
    else : return -x

nums = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
result = map(abs_func, nums)
print(result)#map의 오브젝트 값 출력됨
print(list(result))#혹은 result = list(map(abs_func, nums))
#list대신 tuple형식, 기타 등... 사용 가능
#그치만 tuple형식은 변경이 불가능해서 list많이 사용

#filter test
#map과 filter의 차이
print(list(map(lambda x : x%2 == 0, [1, 2, 3, 4, 5, 6])))
print(list(filter(lambda x : x%2 == 0, [1, 2, 3, 4, 5, 6])))

#zip
print(list(zip([1, 2, 3], [4, 5, 6, 7, 8])))