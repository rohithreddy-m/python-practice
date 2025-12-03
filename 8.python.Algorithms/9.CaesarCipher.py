def CC(shfit,String):
    b=""
    A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in String:
        j=0
        if i in A:
            while i!=A[j]:
                j+=1
            n=(j+shfit)%26
            b=b+A[n] 
        else:
            b=b+i           
    return b         
shfit=int(input("give the Number="))
String=input("Give the String=").upper()
print(CC(shfit,String))