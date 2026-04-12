class student:
    def __init__(self, name, age):
        print(f"{name} is {age} years old")
    def attendance(self):
        print("present")

s = student("shamim", 23)
t = student("abir", 25)
s.attendance()
t.attendance()
