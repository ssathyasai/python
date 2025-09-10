def count_char(str1,):
    c=0
    for i in str:
        c=c+1
    return c
def comapare(str1,str2):
    print("Are the strings Equal:",(str1==str2))
    print("is str1 is grater than str2:",(str1>=str2))
    print("is str1 is lesser than str2::",(str1<=str2))
    print("IS st1 not equal to str2:",(str1!=str2))
def con_cat(str1,str2):
    str3=str1+str2
str=input("Enter a string1:")
str1=input("Enter a string2:")
print("Length of the string :",count_char(str))
print("*****comparing strings")
comapare(str,str1)
print("********concating********")
print(con_cat(str,str1))
