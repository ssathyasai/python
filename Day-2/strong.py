def fact_of_num(n):
    fact=1
    if(n==0 or n==1):
            return 1
    else:
        while(n>0):
            fact=fact*n
            n=n-1
    return fact
def strong(n):
    temp=n
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum+fact_of_num(r)
        temp//=10
    if(n==sum):
        print("Strong Number")
    else:
        print("Not Strong Number")
n=int(input())
strong(n)