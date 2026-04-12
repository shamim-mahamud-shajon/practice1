class Person:
    def __init__(self, name):
        self.name = name

    def show(self):   # instance method
        print(self.name)

p = Person("Shamim")
p.show()

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def total(cls):
        return cls.count

p1 = Person()
p2 = Person()

print(Person.total())

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 4))