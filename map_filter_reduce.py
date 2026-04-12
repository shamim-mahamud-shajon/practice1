#lambda function :
sq = lambda x : x * x
print(sq(7))

#map(function, iterable)

#map: apply functions to all the items

#def add(nums) :
#    return  nums + 1
a = [1, 23, 6, 99, 4, 8]

result = list(map(lambda n : n+2, a))

print(result)

#filter : select specific items:

result = list(filter(lambda n : n%2 == 0, a))

print(result)

#reduce : Combine all into one value
from functools import reduce
sum = reduce(lambda x, y : x + y, a)

print(sum)