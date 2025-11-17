string=input("Give the string=")
string=string.replace(" ","")
for i in string:
    if string.count(i) == 1 :
        print(i,end="")
    
    
