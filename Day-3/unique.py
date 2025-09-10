def dis_unique(lis):
    exist=[]
    c=0
    for i in lis:
        if(i in exist):
            c+=1
            continue
        else:
            exist.append(i)
    print("No.of Duplicates in list are :",c)
    return exist
lis=[1,1,2,2,3,3,4,4]
print(dis_unique(lis))
