def count_freq(lis):
    for i in range(len(lis)):
        if i == lis.index(lis[i]): 
            count = 0
            for j in range(len(lis)):
                if lis[i] == lis[j]:
                    count += 1
            print(lis[i], "appeared", count, "times")

lis = [1, 1, 2, 2, 3, 3, 4, 4]
count_freq(lis)
