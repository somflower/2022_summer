def Adult(x) :
    if x >= 19 :
        return x


ages = [24, 29, 20, 18, 13, 54, 10]
adult = []

print("성년 리스트:", list(filter(Adult, ages)))