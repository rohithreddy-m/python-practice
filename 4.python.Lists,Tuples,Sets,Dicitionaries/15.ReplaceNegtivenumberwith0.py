lists=[int(t) for t in input("Give the lists=").split()]
print(lists)
a=[]
for i in lists:
    if i <0:
        i=0
    a.append(i)
print(a)