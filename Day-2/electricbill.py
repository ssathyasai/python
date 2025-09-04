def cal_bill(units):
    cbill = 0
    if units > 300:
        cbill += (units - 300) * 7.5
        units = 300
    if units > 200:
        cbill += (units - 200) * 6.30
        units = 200
    if units > 100:
        cbill += (units - 100) * 5.10
        units = 100
    if units > 50:
        cbill += (units - 50) * 3.75
        units = 50
    if units > 0:
        cbill += units * 3.0
    return cbill


a = input("Enter the customer number: ")
name = input("Enter customer name: ")
pre_mon = int(input("Enter the Present month reading: "))
last_mon = int(input("Enter the Last month reading: "))

tu = pre_mon - last_mon

bill = cal_bill(tu)

print("***Electricity Bill***")
print("Consumer Number : {}".format(a))
print("Consumer Name   : {}".format(name))
print("Present Reading : {}".format(pre_mon))
print("Last Reading    : {}".format(last_mon))
print("Total Units     : {}".format(tu))
print("Current Bill    : {:.2f}".format(bill))
