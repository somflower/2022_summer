import random
rps_dic = {1 : '가위', 2 : '바위', 3 : '보'}
match_table = {'가위' : '보', '바위' : '가위', '보' : '바위'}
#사용자 입력
player = input("가위, 바위, 보 입력: ")

#컴퓨터 random 출력
key = random.randint(1,3)
if rps_dic.get(key) :
    print("컴퓨터:", rps_dic[key])

#결과 확인
if player == rps_dic[key] :
    print("비겼습니다.")
elif match_table[player] == rps_dic[key] :
    print("이겼습니다.")
else :
    print("졌습니다.")