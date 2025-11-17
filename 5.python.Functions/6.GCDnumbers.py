def GCD(Num1,Num2):
    for i in range (Num1,0,-1):
        if Num1%i==0:
            if Num2%i==0:
                print(i)
                break
Num1,Num2=map(int, input("give the Numbers=").split())            
GCD(Num1,Num2)