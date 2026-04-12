#[expression for item in iterable]
numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(squares)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#{key: value for item in iterable}
numbers = [1, 2, 3, 4]

square_dict = {x: x**2 for x in numbers}
print(square_dict)

even_square = {x: x**2 for x in numbers if x % 2 == 0}
print(even_square)