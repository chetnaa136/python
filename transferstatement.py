# x=int(input("enter number 1:"))
# y=int(input("enter number 2:"))
# z=int(input("enter number 3:"))
# p=int(input("enter number 4:"))
# h=max(x,y,z,p)
# print(h)
# while True:
#     if h%x==0 and h%y==0 and h%z==0 and h%p==0:
#         lcm=h
#         break
#     h=h+1
# print(f'lcm of given values {x},{y},{z} and {p} is {h} ')
# break pass and continue
# x=int(input("enter number 1:"))
# y=int(input("enter number 2:"))
# if x>y:
#     pass
# print("hello")
# n=10
# i=0
# while i<=10:
#     if i==5:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
mv=min(x,y)
for i in range(1,mv):
    if x%i==0 and y%i==0:
        hcf=i
print(hcf)