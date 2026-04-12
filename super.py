class Parent:
    def show(self):
        print("This is parent")

class Child(Parent):
    def show(self):
        super().show()   # call parent method
        print("This is child")

c = Child()
c.show()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()