def fact_of_num(n):
    fact=1
    if(n==0 or n==1):
            return 1
    else:
        while(n>0):
            fact=fact*n
            n=n-1
    return fact
n=int(input("Enter the number:"))
print(fact_of_num(n))
        