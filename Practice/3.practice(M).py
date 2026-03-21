List=[[1,  2,  3, 4,    5],
      [7,  6,  8, 9,   10], 
      [11, 12, 15, 19, 20],
      [1,  22,  5,  9,  2],
      [1,  23,  5,  9,  0],
      [1,  2,  45,  9,  0],
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