"""for i in range(1, 31) :
    if i%2==0 or i%3==0:
        print(i)"""

result = [i for i in range(1, 31) if i % 2 == 0 or i % 3 == 0]
print(result)