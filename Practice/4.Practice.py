Alphbet=input("Give the Alphbet=").lower()
if Alphbet in "aieou":
    print("Vowel")
elif Alphbet.isalpha() :
     print("Consonant")
else :
    print("invalid input")