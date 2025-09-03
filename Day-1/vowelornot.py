def vowelornot(char):
    vowels=['a','e','i','o','u']
    if(char in vowels):
        return "vowels"
    else:
        return "consonant"
char=input("Enter a character:" )
print(vowelornot(char))
