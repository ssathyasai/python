n = int(input("Enter a number: "))

for i in range(2, n):   
    con= 0
    for j in range(1, i+1):   
        if i % j == 0:
            con += 1
    if con == 2:  
        print(i, end=" ")
