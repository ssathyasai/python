def cal_result(s):
    visited=[]
    for i in s:
        if(i not in visited):
            visited.append(i)
    return visited

def cal_result2(s):
    check=cal_result(s) 
    for i in check:
        k=s.count(i)
        print(i,end="")
        print(k,end="")
s=input("Enter the input string:")
cal_result2(s)
