lists=[int(i) for i in input("Give the list=").split()]
#lists.sort()
#print(lists[-2])
a=lists[0]
for i in lists :
    if i > a :
        a=i
print(a)
b=float('-inf')
for i in lists :
    if i==a:
        continue
    elif  i>b:
          b=i
print(b)
