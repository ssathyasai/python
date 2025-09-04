def week_day(day):
    if(day==1):
        return "monday"
    elif(day==2):
        return "Tuesday"
    elif(day==2):
        return "Wednesday"
    elif(day==2):
        return "Thursday"
    elif(day==2):
        return "Friday"
    elif(day==2):
        return "Satday"
    elif(day==2):
        return "Sunday"
    else:
        return "invalid"
day=int(input("Enter the day Number:"))
print("The Day is ",week_day(day))