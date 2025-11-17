lists1=[int(x) for x in input("Give the lists1=").split()]
lists2=[int(x) for x in input("Give the lists2=").split()]
lists3=[int(x) for x in input("Give the lists3=").split()]
lists=lists1+lists2+lists3
print(lists)
a=[]
for i in lists:
    if i not in a:
        a.append(i)
print(a)
 