from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print(p.x)
print(p.y)

from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

s = Student("Shamim", 22)

print(s.name)
print(s.age)