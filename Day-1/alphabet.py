def identify(alpha):
    if(alpha.isalpha()):
        return "alphabet"
    else:
        return "Not a alphabet"
alpha=input("Enter a alphabet:")
print(identify(alpha))
