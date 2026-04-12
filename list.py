#List is a collection which is ordered and changeable. Allows duplicate members.

a = [ "shamim", 23, 3.1416, False, "valo" ]
print(a)
print(a[1:3])

a[1:3] = ["ami", "ekhon"]
print(a)

#insert at particular index
a.insert(2, "nei")
print(a)

#insert at the end
a.append("nei")
print(a)

#removes first occurance of any instance
a.remove("nei");
print(a)

#removes specified index
a.pop(3)
print(a)
#del a[0]

#range(start, stop, step)
for i in range(len(a)):
    print(a[i],  end = " ")
print('\n')
#list comprehension
b = [x for x in range(5, 10) ]
print(b)
b.sort(reverse= True)
print(b)
