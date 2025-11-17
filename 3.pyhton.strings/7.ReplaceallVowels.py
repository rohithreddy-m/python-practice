Name=input("Give the String=")
a=""
b="aeiouAEIOU"
for i in Name:
    if i in b :
        a+="*"
    else :
        a+=i
print(a)