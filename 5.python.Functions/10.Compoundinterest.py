def Compound(a,b,c):
    for i in range(1,c+1):
       e=a+((a*b)/100)  
       a=e
#       print(e)
    return e


principle=int(input("give the Amount="))
interest=int(input("Give the Amount="))
time=int(input("Give the Time="))


print(Compound(principle,interest,time))
