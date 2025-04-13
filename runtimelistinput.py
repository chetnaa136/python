x=eval(input("enter any data"))
# eval ka use runtime mein as it is datatype ko save karne k liye use karte hai
print(x)
print(type(x))
l1=[]
for i in x:
    y=i+5
    l1.append(y)
print(l1)