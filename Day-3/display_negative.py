def add(lis,n):
    for i in range(n):
        k=int(input())
        lis.append(k)
    return lis
def display_nega(lis2):
    lis3=[]
    for i in lis2:
        if(i<0):
            lis3.append(i)
    return lis3
n=int(input())
lis=[]
lis2=add(lis,n)
for i in lis2:
    print(i,end=" ")
print("\n Negative elements in list:")
lis4=display_nega(lis2)
for i in lis4:
    print(i,end=" ")