def Reverse(Num):
    b=0
    while Num>0:
        a=Num%10
        b=b*10+a
        Num//=10
    print(b)
Num=int(input("Give the Number="))
Reverse(Num)