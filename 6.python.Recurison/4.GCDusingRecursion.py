def GCD(Num1,Num2,count=None):
    if count is None:
        count=min(Num1,Num2)
    if Num1%count==0 and Num2%count==0:
        return count
    return GCD(Num1,Num2,count-1)     
        
Num1=int(input("Gvie the Number1="))
Num2=int(input("Gvie the Number2="))
print(GCD(Num1,Num2))