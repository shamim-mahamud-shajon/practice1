#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unordered, unchangeable, and do not allow duplicate values.
a = {"beta", "gama", "alpha", "sigma", }
print(a)

a.add("hello")
print(a)

b = ["ami", "ekhn", "kaj", "kori"]

a.update(b)
print(a)

a.remove("ekhn")
print(a)

#delete random item
x = a.pop()
print(x)
print(a)

#for i in a:
#    print(i)

