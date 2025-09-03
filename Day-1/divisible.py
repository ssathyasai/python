def divisible(n):
    if(n%5==0 and n%11==0):
        print("Number is divisible by 5 & 11")
    else:
        print("Not divisible by 5 & 11")
n=int(input("Enter a number"))
divisible(n)