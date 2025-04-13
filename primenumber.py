n=int(input("enter a number"))
m=1
count=0
while(m<=n):
    if n%m==0:
        count=count+1
        m=m+1
    else:
        m=m+1
if count>2:
    print(f'{n} is not a prime number')
else:
    print(f'{n} is a prime number')
