def count(str):
    alpa_count,spl_count,digit_count=0,0,0
    for i in str:
        if(i.isalpha()):
            alpa_count+=1
        elif(i.isdigit()):
            digit_count+=1
        else:
            spl_count+=1
    print("Alphabets count ",alpa_count," special symbol count ",spl_count," digit count ",digit_count)
str=input("Enter string:")
print("**********calculating Digits ,Alphabets,Symbols in the string*******")
count(str)