List=[[1,2,3,4,2,6,7,1,1,1,1,1,1,2,3,5,6,7],
      [5,6,7,8,3,4,5,1,1,1,1,1,1,2,3,5,6,7],
      [9,8,9,1,0,1,9,1,1,1,1,1,1,2,3,5,6,7],
      [9,8,9,1,0,1,9,1,1,1,1,1,1,2,3,5,6,7],
      [9,8,9,1,0,1,9,1,1,1,1,1,1,2,3,5,6,7],
      [9,8,9,1,0,1,9,1,1,1,1,1,1,2,3,5,6,7],
      [9,8,9,1,0,1,9,1,1,1,1,1,1,2,3,5,6,7],
    ]
a=[] 
j=0
u=0
if len(List)==1:
    for i in range(len(List[0])):
        a.append(List[0][i])
elif len(List)==2:
    for i in range(len(List[0])):
        a.append(List[i%2][i])
else:
    while u<len(List[0]):
        if j ==0:
            for i in range(len(List)):
                if u<len(List[0]):
                    a.append(List[i][u])
                    u+=1
            j=len(List)
            g=u-1
        elif j==len(List):
            for i in range (j-2,0,-1):
                if  u<len(List[0]):
                    a.append(List[i][u])
                    u+=1
            j=0
            g=u-1
print(a)
