def voweconstcount(str):
    vowels=['a','e','i','o','u']
    vowels_count,consonant_count=0,0
    for i in str:
        if(i in vowels):
            vowels_count+=1
        else:
            consonant_count+=1
    print("No of the vowels ",vowels_count," consonants ",consonant_count)
char=input("Enter a String:" )
voweconstcount(char)
