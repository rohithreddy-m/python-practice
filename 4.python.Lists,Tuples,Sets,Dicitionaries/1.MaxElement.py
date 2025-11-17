l=input("Give the list=").split()
lists=[int(items) for items in l]
print(lists)
a=lists[0]
for i in lists :
    if i > a:
        a=i
print(a)