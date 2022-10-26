def game369(num):
    if "3" in str(num) or "6" in str(num) or "9" in str(num):
        return "짝"
    else:
        return i


for i in range(1, 100):
    print(game369(i), end = " ")