class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
        print self.age

ob = Person('vineet', 20)
ob.birthday()