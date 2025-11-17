lists=[int(i) for i in input("Give the lists=").split()]
b=set(lists)
print(lists)
c=[]
for i in b:
    a=lists.count(i)
    print(f"{i}:{a} ",end=",")