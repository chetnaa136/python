# same as set but is used to freeze any collection
# its immutable
l=[2,3,4,5]
x=frozenset(l)
print(x)
print(type(x))
# functions same as set
# methods different than set reduced methods

print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(id(x))
# methods