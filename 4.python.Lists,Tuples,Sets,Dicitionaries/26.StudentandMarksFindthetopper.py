d={}
A=int(input("give the Marks of A="))
B=int(input("give the Marks of B="))
C=int(input("give the Marks of C="))
d["A"]=A
d["B"]=B
d["C"]=C
m=0
for i,j in d.items():
    if j >=m:
        n=i
        m=j
print(n,m)
