def input_gender(i):
    gender = input("성별을 입력하세요(%d번)"% i)
    return gender

def get_jeju():
    answer = input("여름 휴가 장소를 제주도를 선호합니까?")
    return answer

def gender_jeju(g, a, fy, fn, my, mn):
    if g == "female" :
        if a == "yes" :
            fy = fy + 1
        elif a == "no" :
            fn = fn + 1
    if g == "male" :
        if a == "yes" :
            my = my + 1
        elif a == "no" :
            mn = mn + 1

    return fy, fn, my, mn

def total_jeju(*args) :
    print(args[0])
    if args[0] == "yes" :
        args[1] = args[1] + 1
    return args[1]

def print_result(fn) :
    print("제주도를 선호하지 않는 여성 응답자 수:", fn)

cnt = 0
fy = 0
fn = 0
my = 0
mn = 0

for i in range(1, 6) :
    g = input_gender(i)
    a = get_jeju()
    fy, fn, my, mn = gender_jeju(g, a, fy, fn, my, mn)
    total_jeju(a, cnt)

print("-"*20)


