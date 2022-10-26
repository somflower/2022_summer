word = {'CS' : 'Computer science', 
        'IT' : 'Information Technology', 
        'IoT' : 'Internet of Things', 
        'HAND' : 'Have A Nice Day', 
        'thx' : 'Thanks', 
        'BBL' : 'Be Back Later'}

enter = input("번역할 문장을 입력하시오: ")

cut = enter.split(" ")
for i in cut :
    if i in word :
        print(word[i])
    else :
        print(i)
#입력받은 것이 문장일 경우도 고려하기
#CS is IoT같은 ......