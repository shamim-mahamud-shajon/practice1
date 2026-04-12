#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
a= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(a)
print(a["brand"])
x = a.get("model")
print(x)
a = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

x = a.values()
print(x);
x = a.keys()
print(x)

#remove
a.pop("year")
for x, y in a.items():
  print(x, y)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
  print(x)

  for y, z in obj.items():
    print(y + ':', z)
