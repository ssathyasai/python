def fib(n):
    a,b=0,1
    for i in range(1,n+1):
        temp=a+b
        print(temp,end=" ")
        a=b
        b=temp
n=int(input())
fib(n)
