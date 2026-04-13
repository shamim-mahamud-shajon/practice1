# try:
#     x = int(input("Enter number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("Result:", 10 / x)

try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Program finished")