number=int(input("Give the Number="))
j=1
k=1
for i in range (1,number+1):
    k=k+i
    for r in range (j,k):
        print(r,end=" ")
    print()
    j=k
    