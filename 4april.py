# greatest among 3 values
# first approach
x=int(input("enter first value"))
y=int(input("enter second value"))
z=int(input("enter third value"))
# if x>y and x>z:
#     print(f'{x} is greater than {y} and {z}')
# elif y>x and y>z:
#     print(f'{y} is greater than {x} and {z}')
# else:
#     print(f'{z} is greater than {x} and {y}')
# second approach
# l=[x,y,z]
# print(max(l))
# third approach 
if x>y:
    if x>z:
        print(f'{x} is greater than {y} and {z}')
elif y>x:
    if y>z:
        print(f'{y} is greater than {x} and {z}')
else:
    print(f'{z} is greater than {y} and {x}')
