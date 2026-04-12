def hello():
    print("hello world")

hello()

def ok(name):
    return "Hello " + name + ", I am your boss"
print(ok("shamim"))
print(ok("amin"))

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#The *args parameter allows a function to accept any number of positional arguments.
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#The **kwargs parameter allows a function to accept any number of keyword arguments.
#Inside the function, kwargs becomes a dictionary containing all the keyword arguments

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#recursion

def even() :
     for i in range(1, 11) :
         if i%2 == 0 : print(i)

even()