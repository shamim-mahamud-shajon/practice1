#A function that extends the behaviour of another function without changing the base function

def my_decorator(func):
    def wrapper():
        print("Assalamualikum")
        func()
       # print("after calling main function")
    return wrapper
@my_decorator
def greet():
    print("Hello everyone")

greet()