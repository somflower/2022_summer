class Student(object) :
    def __init__(self, name, department, id, gender):
        self.name = name
        self.department = department
        self.id = id
        self.__gender = gender
    def goSchool(self, id) :
        if int(id) % 2 == 0 :
            print("짝수 주 대면수업")
        else : print("홀수 주 대면수업")
    def getgender(self) :
        return self.__gender

ddwu = Student("동덕", "컴퓨터학과", "20220021", "여자")
print("ddwu는 "+ddwu.department+" "+ddwu.id+"번 이름은 "+ddwu.name+"입니다.")
ddwu.goSchool(ddwu.id)
print(ddwu.getgender())#가시성