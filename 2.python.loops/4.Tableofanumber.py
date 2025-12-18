Num=int(input("Give the number of table="))
for i in range (Num,Num+1):
    print(f"Table of {i}")
    for j in range (1,11):
        print(f"{Num} x {j} = {Num*j}",end=" ")
print()
i=1
while i<=10:
    print(f"{Num} X {i} = {Num*i}")
    i+=1
