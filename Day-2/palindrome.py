n=int(input("Enter a number:"))

def palindrome(n):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
if(n==palindrome(n)):
    print("Palindrome")
else:
    print("Not a Palindrome")
