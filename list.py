#string,integer and tuple are immutable in nature.
my_list=[1,2,3,4,'sdfgh','erty']
# in-built functions
a=[1,2,3,4,'Neeraj']
print(len(a))
print(id(a))
print(type(a))
b=[1,2,3,4,5,6]
print(max(b))
print(min(b))
print(sum(b))
print(type(b))
# id is system dependant hence everyone will get different addresses.
print(len(b))
print(id(b))
#empty list bhi hoti hai
#empty list ko dekh sakte hai pr empty string nhi dekh sakte hai.
x=[]
print(type(x))