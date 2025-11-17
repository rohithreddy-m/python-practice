def Factorial(s):
    a=1
    for i in range (1,s+1):
        a*=i
    return a
    
f=int(input("Give the Number="))
print(Factorial(f))
