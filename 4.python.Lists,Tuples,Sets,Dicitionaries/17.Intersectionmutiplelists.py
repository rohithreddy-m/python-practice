lists1=[int(r) for r in input("Give the lists1=").split()]
lists2=[int(r) for r in input("Give the lists2=").split()]
lists3=[int(r) for r in input("Give the lists3=").split()]
lists=max(lists1+lists2+lists3)
print(lists)
a=[]
for i in range(lists+1):
    if i in lists1 and i in lists2 and i in lists3:
        a.append(i)
print(a)