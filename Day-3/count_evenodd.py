def count_even(lis):
    count_even=0
    count_odd=0
    for i in lis:
        if(i%2==0):
            count_even+=1
        else:
            count_odd+=1
    print("Even numbers in list are  ",count_even,"\nOdd numbers in the list are ",count_odd)
lis=[1,2,3,4,5,6,7,8,9]
count_even(lis)