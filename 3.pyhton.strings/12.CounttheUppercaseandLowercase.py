String=input("Give the string=")
uppercount=0
lowercount=0
for i in String:
    if i.isupper():
        uppercount+=1
    elif i.islower():
        lowercount+=1
print(f"UpperCase Letters = {uppercount}")
print(f"lowerCase Letters = {lowercount}")