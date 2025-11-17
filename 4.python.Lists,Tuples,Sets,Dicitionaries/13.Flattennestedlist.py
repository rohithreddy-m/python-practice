lists=str([1,[2,3],[4,[5]]])
a=[]
for i in lists:
    if i.isdigit():
        a.append(i)
a=[int(r) for r in a]        
print(a)