def calfactor(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
n=int(input("Enter the Number:"))
calfactor(n)
