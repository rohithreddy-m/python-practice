# List=[[1,2,3],
#       [4,5,6], 
#       [7,8,9]
#       ]
List=[[1,2,3,4,5],
      [6,7,8,9,1],
      [6,7,8,9,1],
      [5,4,3,2,1],
      [9,8,7,6,5]
         ]
a=[]
for i in range(len(List)):
    if i%2==0:
        for j in range(i+1):
            a.append(List[i-j][j]) 
    else:
        for j in range(i,-1,-1):
            a.append(List[i-j][j])
for i in range(len(List)):
    if i%2==0:
        n=1
        for j in range(len(List)-1,i,-1):
            a.append(List[i+n][j]) 
            n+=1 
    else:
        n=1
        for j in range(i+1,len(List)):
            a.append(List[len(List)-n][j]) 
            n+=1              
            
print(a)