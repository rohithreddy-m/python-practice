def PoweroftheNumber(Base,Exponent):
    if Exponent==0:
        return 1
    return Base*PoweroftheNumber(Base,Exponent-1)
    
Base=int(input("Give the Base="))
Exponent=int(input("Give the Exponent="))
print(PoweroftheNumber(Base,Exponent))