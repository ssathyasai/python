a,b=map(int,input("Enter two numbers seperated by space:").split(" "))
try:
    c=a//b
except:
    print("Arithemetic error can divided by 0")
else:
    print("A divided by B is:",c)
finally:
    print("Done division performed")
