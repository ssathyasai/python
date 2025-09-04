def perfect(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    sum_div = sum(div)

    if n == sum_div:
        print("Perfect Number")
    else:
        print("Not a perfect Number")


n = int(input("Enter the number: "))
perfect(n)
