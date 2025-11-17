lists= input("Give the List=").split()
l=[]
for i in lists:
    if i not in l:
        l.append(i)
print(l)