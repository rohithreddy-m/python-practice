def Perfect(Num):
    a=0
    for i in range(1,Num):
        if Num%i==0:
            a=a+i
    if a==Num:
        return "Yes"
    else:
        return "No"
Num=int(input("Give the Number="))
print(Perfect(Num))