#reduce와 람다식 사용
from functools import reduce
print(reduce(lambda x, y : x * y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))