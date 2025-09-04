def perfect(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    sum_div = sum(div)

    if n == sum_div:
        return True
    else:
        return False

n=int(input())
for i in range(1,n+1):
    if(perfect(i)):
        print(i,end=" ")