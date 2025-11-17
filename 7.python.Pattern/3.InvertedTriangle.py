def IV(Number):
    j=1
    while j<=Number:
        for i in range (Number+1,j,-1):
            print("*",end="")
        j+=1
        print()
Number=int(input("Give the Numbe="))
IV(Number)