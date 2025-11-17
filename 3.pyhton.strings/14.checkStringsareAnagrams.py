string1=input("Give the string=").lower()
string2=input("Give the string=").lower()
count=0
if len(string1)!=len(string2):
    print("Not Anagrams")
else :
    for i in string1:
       if string1.count(i)==string2.count(i):
          count+=1
    if len(string2)==count:
        print("Anagrams")
    else:
        print("Not Anagrams")