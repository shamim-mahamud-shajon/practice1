#Tuple items are ordered, unchangeable, and allow duplicate values.

a = ("hello" , "how", "are", "you", 54, True)
print(a)
print(a[-1])

b = ("hello bai", )
a += b
print(a)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red, blue) = fruits

print(green)
print(tropic)
print(red)
print(blue)

for i in range(len(a)):
    print(a[i], end = " ")
