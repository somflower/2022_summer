#클래스 연습
class SoccerPlayer(object) :
    def __init__(self, name, position, back_number) :#생성자
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_number) :
        print("선수의 등번호를 변경한다: From %d to %d" %(self.back_number, new_number))
        self.back_number = new_number

ddwu = SoccerPlayer("동덕", "MF", 10)
print(ddwu.name)
#print(ddwu.back_number)
ddwu.change_back_number(11)