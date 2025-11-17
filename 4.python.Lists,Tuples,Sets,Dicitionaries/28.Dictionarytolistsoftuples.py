d={}
t=[]
n=int(input("how many times ="))
for i in range(n) :
    key = input("Give the Key =")
    value=int(input("Give the value="))
    d[key]=value
print(d)
c=list(d.items())
print(c)
e=[(i,j) for i,j in d.items()]
print(e)
'''for i,j in d.items():
     t.extend([i,j])
print(t)'''