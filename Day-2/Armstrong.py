def arm(n):
    temp=n
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum+r**3
        temp//=10
    if(n==sum):
        print("Arm strong")
    else:
        print("Not arm strong")
n=int(input())
arm(n)