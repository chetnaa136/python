x=10
y=20
z=30
# and operator
print(x>y and y>z)
print(x>y and y<z)
print(x<y and y>z)
print(x<y and y<z)

#or operator
print(x>y or y>z)
print(x>y or y<z)
print(x<y or y>z)
print(x<y or y<z)

print(not(x>y or y>z))
print(not(x>y or y<z))
print(not(x<y or y>z))
print(not(x<y or y<z))


