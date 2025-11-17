lists=[int(s) for s in input("Give the lists=").split()]
count=0
a=[]
for i in range (max(lists)+1):
    if i in lists:
        a.append(i)
print(a)
'''       a.insert(count,i) 
       count+=1
    if len(lists)==len(a):
        break
print(a)'''