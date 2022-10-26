def average(*args):
    nums = []
    print("매개변수로 전달된 값: ", end="")
    for n in args:
        print(n, end=" ")
        nums.append(n)
        print()
    return sum(nums)/len(nums)

print("평균: ", average(1, 2, 3, 4, 5))
print("-" * 40)
print("평균: ", average(30, 10, 20))
