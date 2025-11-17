def BT(Numbers):
    j=2
    b=2
    for i in range(1,Numbers+1):
        a=(Numbers*2)-j
        print("*"*i + " "*(a)+("*"*i))
        j+=2
    for k in range(Numbers-1,0,-1):
        print("*"*k+" "*(b)+("*"*k))
        b+=2

Number=int(input("Give the number="))
BT(Number)