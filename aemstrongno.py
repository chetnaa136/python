# q.1 no.of digits in the no
# every single digit number is an armstrong number
# n=int(input("enter any number"))
# count=0
# while n>0:
#     n=n//10
#     count=count+1
# print(count)
# by using length function
# n=input("enter number")
# print(len(n))
# sum of each powered digit
# n=int(input("enter number"))
# digit=int(input("enter any digit"))
# sum=0
# while n>0:
#     x=n%10
#     sum=sum+x**digit
#     n=n//10
# print(sum)
# n=int(input(("enter any number:")))
# x=m=n
# digit_count=0
# sum=0
# while n>0:
#     digit_count=digit_count+1
#     n=n//10
# print(digit_count,x)
# y=0
# while x>0:
#     y=x%10
#     sum=sum+y**digit_count
#     x//10
# print(sum,x)
# if sum==m:
#     print('given number {} is an armstrong number'.format(m))
# else:
#     print('not an armstrong number')
# string palindrome
s=input('enter a string')
# l=s[::-1]
# if l==s:
#     print("its a palindrome")
# else:
#     print("its a plaindrome")
l=0
r=len(s)-1
div=len(s)/2
if (len(s)%2==0):
    while l<=div and r>=div:
        if s[l]==s[r]:
            l=l+1
            r=r-1
        else:
            print('not a palin')

i