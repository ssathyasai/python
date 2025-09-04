def sum_of_n(n):
    sum=0
    i=0
    while(i<=n):
        i=i+1
        sum=sum+i
    return sum
n=int(input("Enter last number upto you want to find sum:"))
print(sum_of_n(n))
