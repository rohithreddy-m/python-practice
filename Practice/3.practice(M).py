List=[[1, 2, 3, 4, 5],
      [1, 2, 3, 7, 6], 
      [1, 2, 5, 9, 0],
      [1, 2, 5, 9, 2],
      [1, 2, 5, 9, 0],
      [1, 2, 5, 9, 0],
      ]
b=[]
a=len(List)
if a%2==0:
   c=a//2
   b.append(List[c-1])
   b.append(List[c])
else:
   c=a//2
   b.append(List[c])
print(b)