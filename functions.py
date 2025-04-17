# anonymous function jiska naam nhi hota usko lambda function bolte hai
def leap(x):
    if (x%4==0 and x%100!=0)or x%400==0:
        print(f'{x} is a leap year')
    else:
        print(f'{x} is not a leap year')

y=int(input("enter the year"))
leap(y)