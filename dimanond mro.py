class A:
    def display(self):
        return("Hello from A")
    def show(self):
        return("Show from A")

class B:
    def display(self):
        return("Hello from B")

    def show(self):
        return("Show from B")
class C(A,B):
    # def display(self):
    #     return ("Hello from C")

    def show(self):
        return("Show from C")

obj = C()
print(obj.display())

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

obj = D()
obj.show()