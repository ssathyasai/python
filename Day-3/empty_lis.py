def add(lis,n):
    for i in range(n):
        k=int(input())
        lis.append(k)
    return lis
n=int(input())
lis=[]
lis2=add(lis,n)
for i in lis2:
    print(i,end=" ")