def leap(year):
    if(year%4==0 or year%400==0):
        return "leap"
    else:
        return "not Leap Year"
y=int(input("Enter the year:"))
print(leap(y))