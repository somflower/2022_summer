#filter 예시
#filter의 함수는 조건문같은 역할을 함
#list(filter(함수, 리스트 등 데이터))
def positive(x) :
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x : x>0, [1, -3, 2, 0, -5, 6])))