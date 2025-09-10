def char_occur(str):
    c = input("Enter the character you want to find occurrence: ")
    k = 0
    for i in str:
        if i == c:
            k += 1
    print(f"{c} occurs {k} times")
    
s = input("Enter the string: ")
char_occur(s)
