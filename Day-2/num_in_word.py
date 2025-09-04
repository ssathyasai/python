lis = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

n = int(input("Enter a number: "))
temp = n

while temp > 0:
    digit = temp % 10              
    print(lis[digit],end=" ")            
    temp = temp // 10              
