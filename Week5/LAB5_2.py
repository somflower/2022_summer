def BMI(height, weight) :
    return weight/(height*height)
def result_print(result) :
    print("당신의 체지방지수는 %.2f입니다." % result)
    if result >= 30 :
        print("당신은 고도비만입니다.")
    elif result >= 25 :
        print("당신은 경도비만입니다.")
    elif result >= 23 :
        print("당신은 과체중입니다.")
    elif result >= 18.5 :
        print("당신은 정상입니다.")
    else:
        print("당신은 저체중입니다.")

h = float(input("키를 m단위로 입력: "))
w = float(input("몸무게를 kg단위로 입력: "))

result = BMI(h, w)
result_print(result)