from abc import ABC, abstractmethod

class Animal(ABC):
    def display(self):
        return "this is normal method"
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

d = Dog()
print(d.sound())
c = Cat()
print(c.sound())