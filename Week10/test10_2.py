class Person(object) :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self) :
        print("나의 이름은 %s 이고 나이는 %d이다." % (self.name, self.age))

class Employee(Person) :#Person으로부터 상속받음
    def __init__(self, name, age, gender, salary, hire_date) :
        #부모클래스 다 적고 추가적인거 적어줌
        #부모클래스의 생성자를 가져와야 함
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date
    def about_me(self) :#오버라이딩, 재정의
        super().about_me()#안써줘도 됨, 여기서는 쓰여서 썼음
        print("나의 급여는 %d원이고 입사일은 %s이다." % (self.salary, self.hire_date))
    def do_wort(self) :
        print("열심히 일하자.")

aPerson = Employee("홍길동", 35, "남자", 50000, "2021-03-34")
aPerson.about_me()        

