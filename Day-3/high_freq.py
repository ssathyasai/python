s = input("Enter string: ")
max_count = 0
char_max = ''
for i in s:
    count = s.count(i)
    if count > max_count:
        max_count = count
        char_max = i
print(char_max, "occurs", max_count, "times")
