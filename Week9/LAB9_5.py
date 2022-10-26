list1 = []
"""for i in range(1, 11): 
    if i % 2 == 0 :
        list1.append(i)
    else :
        list1.append(-1)"""

[list1.append(i) if i % 2 == 0 else list1.append(-1) for i in range(1, 11)]


print(list1)