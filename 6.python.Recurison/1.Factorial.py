def Factorial(Num):
    if Num==0 :
        return 1
    a=Num*Factorial(Num-1)
    return a

print(Factorial(5))