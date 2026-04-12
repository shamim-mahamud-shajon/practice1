class base:
    def function1(self):
        print("I am function1")

    def function2(self):
        print("I am function2")

#single inheritance
class child:
    def function3(self):
        print("I am function3")

    def function4(self):
        print("I am function4")


a = child()

#multilevel inheritance
class c(child):
    def function5(self):
        print("I am function5")

a = c

#multiple inheritance
class d(base, child):
    def function6(self):
        print("I am function6")

a = d

