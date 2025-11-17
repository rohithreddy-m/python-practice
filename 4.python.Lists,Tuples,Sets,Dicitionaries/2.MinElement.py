lists=[int(i) for i in input("Give the list=").split()]
print(lists)
a=lists[0]
for i in lists :
    if i < a:
        a=i 
print(a)