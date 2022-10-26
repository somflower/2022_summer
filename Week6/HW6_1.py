import random
rps_dic = {1: '가위', 2: '바위', 3: '보'}
match_table = {'가위': '보', '바위': '가위', '보': '바위'}
name_list = []
winVSlose = []
#name_list = ["홍길동"]
#winVSlose = [[0, 0, 0,], [0, 0, 0]]

#도전자 이름
name = input("도전자 이름 : ")
if name_list.count(name) == 0:
    name_list.append(name)
    winVSlose.append([0, 0, 0])#리스트 안에 리스트 추가

while name != "":
    #사용자 입력
    player = input("가위, 바위, 보 입력: ")

    #컴퓨터 random 출력
    key = random.randint(1, 3)
    if rps_dic.get(key):
        print("컴퓨터:", rps_dic[key])

    for i in range(len(name_list)) :
        if name == name_list[i] :
            idx = i

    #결과 확인
    if player == rps_dic[key]:
        winVSlose[idx][1] += 1
        print("비겼습니다.")
    elif match_table[player] == rps_dic[key]:
        print("사람 승!")
        winVSlose[idx][0] += 1
    else:
        print("컴퓨터 승!")
        winVSlose[idx][2] += 1

    for i in range(len(name_list)) :
        print(name_list[i] + " : " + str(winVSlose[i][0]) + "승", str(winVSlose[i][1]) + "무", str(winVSlose[i][2]) +"패")

    #도전자 이름
    name = input("도전자 이름 : ")
    if name_list.count(name) == 0:
        name_list.append(name)
        winVSlose.append([0, 0, 0])