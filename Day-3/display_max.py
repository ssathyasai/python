def cal_sec_max(lis):
    lis.sort()
    n=len(lis)
    return lis[n-2]
lis=[2,1,33,4,19,24]
print("The second largest element in list is :",cal_sec_max(lis))