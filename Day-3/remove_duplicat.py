def count_dupl(lis):
    dup_count=0
    for i in lis:
            if(lis[i]==lis[i+1]):
                dup_count+=1
    return dup_count
lis=[1,1,2,2,3,3,4,4]
print("NO.Of duplicates in the list are ",count_dupl(lis))