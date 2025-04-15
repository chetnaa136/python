x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
z=int(input("enter number 3:"))
p=int(input("enter number 4:"))
h=max(x,y,z,p)
print(h)
while True:
    if h%x==0 and h%y==0 and h%z==0 and h%p==0:
        lcm=h
        break
    h=h+1
print(f'lcm of given values {x},{y},{z} and {p} is {h} ')
    