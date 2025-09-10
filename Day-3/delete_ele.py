def delete_py(lis):
    pos=int(input("\nEnter the Element you want to remove based on position :"))
    lis2=[]
    k=len(lis)
    for i in range(k):
        if(i==pos):
            continue
        else:
            lis2.append(i)
    return lis2
lis=[1,2,3,4,5]
for i in lis:
    print(i,end=" ")
lis3=delete_py(lis)
print("*** removing element from the list:")
print("After removing element the list is ")
for i in lis3:
    print(i,end=" ")
