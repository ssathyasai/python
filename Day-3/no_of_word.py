def count_wordd(str):
    word_count=1
    for i in str:
        if(i==" "):
            word_count+=1
    return word_count
str=input("Enter the string:")
print("NO Of word in the string is ",count_wordd(str))