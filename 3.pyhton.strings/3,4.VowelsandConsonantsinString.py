Name=input("Give the String =").lower()
Count_Vowels=0
Count_Consonants=0
for i in Name:
    if i in "aeiou":
        Count_Vowels+=1
    if  i.isalpha() and i not in "aeiou":
        Count_Consonants+=1
print(f"There are {Count_Vowels} Vowels.")
print(f"There are {Count_Consonants} Consonants.")