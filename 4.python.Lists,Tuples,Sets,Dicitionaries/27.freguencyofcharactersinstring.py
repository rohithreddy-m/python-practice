String=input("Give the string=")
d={}
a=len(String)
#for i in String:
#   d.update({i:String.count(i)})
for i in String:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)