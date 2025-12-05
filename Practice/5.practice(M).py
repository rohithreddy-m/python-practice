List=[
    [1,2,3,1,5,6,7],
    [1,2,2,4,3,6,7],
    [1,4,3,4,5,5,7],
    [6,2,3,4,5,6,7],
    [1,8,3,4,5,9,7],
    [1,10,10,4,11,11,7],
    [1,2,3,12,12,6,2]
     ]
b=[]
l=len(List)//2
r=len(List)//2
m=len(List)//2
for i in range(len(List[0])):
    if i<=m:
        b.append(List[i][l])
        if r !=l:
            b.append(List[i][r])
        r+=1
        l-=1
    elif i > m:
        if l==-1 and r==len(List):
            l+=1 
            r-=1   
        r-=1
        l+=1
        b.append(List[i][l])
        if l != r:
            b.append(List[i][r])
print(b)