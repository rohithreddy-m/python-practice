def Fibonacci(Num):
    a=0
    b=1
    if Num==1:
        return a
    elif Num==2:
        return b
    else:
        for i in range (3,Num+1):
            c=a+b
            a=b
            b=c
        return c
Num=int(input("Give the Number="))
print(Fibonacci(Num))
