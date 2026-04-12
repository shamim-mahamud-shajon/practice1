if 5 > 2:
         print("five is big", end = " ")

print('I "am" shamim')

x = "shamim"
print(type(x))
y = 9
print(x, y)

z = "vat khabo"

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is not " + x)

a = """char chor korbe churi vaiyar goru,
regemege vaiyar goru korlo mar shuru,
pran milk candyr shad sobai ter je pelo,
jei khabe sei hobe asol hero,
pran milk candy, pran milk candy,
ya ya yoooooooooooooo
"""

#print(a)

if "goru" in a:
    print("we have our own cow")


a = "hello welcome hello"
#print(a[:4])
print(a.replace("hello", "mofiz"))
print(a.upper())
b = "mofiz"
c = "abul"
d = b + c
print(d)

#f-strings
x = "aladin"
y = f"today is a {x} day"
print(y)


#range(start, stop, step)
x = range(2, 6)
for i in x:
    print(i, end = " ")