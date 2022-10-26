sNum = input("학번 입력(9자리): ")

if len(sNum) != 9 :
    print("학번 입력 오류")
else :
    if sNum[2] == "2" :
        if sNum[3] == "2" :
            print("1학년이군요.")
        elif sNum[3] == "1" :
            print("2학년이군요.")
        elif sNum[3] == "0" :
            print("3학년이군요.")
    elif sNum[2] == "1" :
        if sNum[3] == "9" :
            print("4학년이군요.")
        elif sNum[3] == "8" :
            print("5학년이군요.")
        elif sNum[3] == "7" :
            print("6학년이군요.")

    if int(sNum[8]) % 2 == 0 :
        print("%s는 짝수 주에 등교합니다." % sNum)
    else :
        print("%s는 홀수 주에 등교합니다." % sNum)
