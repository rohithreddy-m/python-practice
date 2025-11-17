def LCM(Num1,Num2):
    s=1
    while True:
        a=Num1*s
        if a%Num2==0:
            print(a)
            break
        s+=1
Num1,Num2=map(int,  input("give the Number=").split())
LCM(Num1,Num2)