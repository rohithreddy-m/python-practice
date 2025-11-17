def RAT(Number):
    for i in range(1,Number+1):
        j=1
        while j<=i:
            print("*",end="")
            j+=1
        print()
Number=int(input("Give the Number="))
RAT(Number)