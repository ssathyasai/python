def arm(n):
    temp=n
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum+r**3
        temp//=10
    if(n==sum):
        return True
    else:
        return False
n=int(input())
for i in range(n):
    if arm(i):
        print(i,end=" ")