class Animal :
    def __init__(self, name) :
        self.name = name
    def talk(self) :
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal) :
    def talk(self) :
        return "Woof! Woof!"

class Cat(Animal) :
    def talk(self) :
        return "Meow!"

animals = [Cat("가을"), Cat("알콩"), Dog("두나")]
for animal in animals:
    print(animal.name + "의 소리 " + animal.talk())