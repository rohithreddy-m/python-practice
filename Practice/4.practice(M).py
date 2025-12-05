List=[
    [1,2,3,4,1,4,3],
    [1,2,3,4,1,4,3],
    [1,2,3,4,1,4,3],
    [1,2,3,2,5,6,5],
    [1,2,3,2,5,6,5],
    [1,2,3,2,5,6,5],
    [1,2,3,4,5,3,4]
      ]
a=[]
v=len(List)-1
for i in range(len(List)):
    a.append(List[i][i])
for i in range(len(List)):
    a.append(List[i][v])
    v-=1
print(a) 