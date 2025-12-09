List=[[1,2,3],
      [4,5,6], 
      [7,8,9]
      ]
# List=[[1,2,3,4,5],
#       [6,7,8,9,1],
#       [6,7,8,9,1],
#       [5,4,3,2,1],
#       [9,8,7,6,5]
#          ]
a=[] 
b=0 
if b==0 or b%2==0:
    for j in range(len(List[0])):
        for i in range(j,-1,-1): 
            a.append(List[j-i][i])
    for j in range(len(List)+1):
        n=1
        for i in range(len(List)-1,j,-1):
            a.append(List[j+n][i])
            n+=1 
    b+=1
print(a)