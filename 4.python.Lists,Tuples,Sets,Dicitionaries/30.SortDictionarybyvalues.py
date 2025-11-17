n=int(input("Give the number of times="))
d={}
for i in range (n):
    key=input("Give the key=")
    value=int(input("Give the value="))
    d[key]=value
print(d)
d=dict(sorted(d.items(), key=lambda item:item[1]))
print(d)