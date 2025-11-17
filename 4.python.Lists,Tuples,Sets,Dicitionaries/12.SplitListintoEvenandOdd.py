lists=[int(h) for h in input("Give the list=").split()]
a=[]
b=[]
for i in lists:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(f"Even:{a} , Odd:{b}")