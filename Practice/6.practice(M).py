List=[
    [1,2,3,1], 
    [1,2,2,4],
    [1,4,3,4],
    [1,4,3,4],
    [1,4,3,4],
    [1,4,3,4],
    [1,4,3,4],
    [6,2,3,4]
    ]
    # [1,8,3,4,5,9,7]
    # [1,10,10,4,11,11,7]
    # [1,2,3,12,12,6,2]
     
a=[]
for i in range(len(List)):
    if i==0 or i%2==0:
        for j in List[i]:
            a.append(j)
    else:
            List[i].reverse()
            a.extend(List[i])
print(a) 