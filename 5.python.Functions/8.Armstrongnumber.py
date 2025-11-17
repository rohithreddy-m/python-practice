def Armstrong(Num):
    b=0
    for i in str(Num):
        i=int(i)
        a=i**s
        b+=a
    if Num==b:
        print("Yes")
    else:
        print("No")
Num=int(input("Give the Number="))
global s
s=len(str(Num))
Armstrong(Num)
