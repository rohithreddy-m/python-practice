String=input("Give the string=")
String1=""
for i in String:
    if i not in "aeiouAEIOU":
        String1+=i
print(String1)