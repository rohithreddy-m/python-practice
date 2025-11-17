Num=int(input("Give the Number="))
total=1
for Sum in range (2,Num+1):
    total+=Sum
    print(f"{total-Sum} + {Sum}.The Sum of Numbers{total}")
total=1
Sum=2
while Sum<=Num:
    total+=Sum
    print(f"{total-Sum} +{Sum}. The Sum of Number{total}")
    Sum+=1