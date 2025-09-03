a=int(input("Enter the customer number:"))
name=input("Enter customer name:")
pre_mon=int(input("Enter the Present month reading:"))
last_mon=int(input("Enter the Last month reading:"))
tu=pre_mon-last_mon
bill=tu*3.8
print("consumer number:{}".format(a))
print("consumer Name:{}".format(name))
print("Present month reading:{}".format(pre_mon))
print("Last month reading:{}".format(last_mon))
print("Total units:{}".format(tu))
print("current bill:{}".format(bill))

