a = 5.5
print(type(a))
print(isinstance(a, int))

#implicit conversion

a_int = 1
b_float = 2.0
c = a_int + b_float
print(c)

#explicit conversion

a = 3.14

print(int(a))

price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
print("The total is: " + str(total)  + "$")

#convert to octal

a = 57
oct_a = oct(a)
print(oct_a)
print(int(oct_a, 8))


print(
    chr(68),
    chr(65),
    chr(84),
    chr(65),
    chr(67),
    chr(65),
    chr(77),
    chr(80),
)