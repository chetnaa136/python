# positional argument
# def add(x,y):
#     print(f'value of x is:{x}')
#     print(f'value of y is:{y}')
#     return x+y
# z=add(5,7)
# print(z)
# keyword argument
# def add(x,y):
#     print(f'value of x is:{x}')
#     print(f'value of y is:{y}')
#     return x+y
# p=int(input("enter 1st value:"))
# q=int(input("enter 2nd value:"))
# z=add(x=p,y=q)
# print(z)
# code for error
# def add(x,y):
#     print(f'value of x is:{x}')
#     print(f'value of y is:{y}')
#     return x+y
# p=int(input("enter 1st value:"))
# q=int(input("enter 2nd value:"))
# z=add()
# print(z)
# error ko band karne k liye,we use default arguments
# DEFAULT ARGUMENT
# def add(x=0,y=0):
    # print(f'value of x is:{x}')
    # print(f'value of y is:{y}')
    # return x+y
# p=int(input("enter 1st value:"))
# q=int(input("enter 2nd value:"))
# z=add()
# print(z)
# case3:
# z=add(6)
# print(z)
# VARIABLE-LENGTH ARGUMENT
# *-->select all
# isme variable ka number varied hota hai
# data ko store karega tuple format mein
# def add(*n):
    # print(n)
    # print(type(n))
# p=int(input("enter 1st value:"))
# q=int(input("enter 2nd value:"))
# z=add(2,3,4,5,6,7,8,9)
# print(z)
# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# z=add(2,3,4,5,6,7,8,9)
# print(z)
# def add(*n):
#     print(n)
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#     return sum
# n=eval(input("enter all values"))
# z=add(n)
# print(z)
# keyword variable-length argument
# recommended is kwargs stands for keyword arguemnets as per documentation\
# *-->is tuple
# **-->is dictionary
# def showdetail(**n):
#     print(n)
#     print(type(n))
#     for i,j in n.items():
#         print(f'my {i} is{j}')
# showdetail(name="Neeraj",age=56)
# args and kwargs