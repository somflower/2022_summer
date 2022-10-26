print("당신이 태어난 연도를 입력하세요.")
year = int(input())
age = 2020 - year + 1

if 20 <= age <= 26 :
    print("대학생 입니다.")
elif 17 <= age :
    print("고등학생 입니다.")
elif 14 <= age:
    print("중학생 입니다.")
elif 8 <= age :
    print("초등학생 입니다.")
else :
    print("학생이 아닙니다.")
