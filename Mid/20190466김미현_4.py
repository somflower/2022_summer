sentence = input("문장을 입력하시오: ")
dic = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}

for i in sentence :
    if i == dic.keys() :
        i = dic.values()
