def Diamond(Number):
    j=1
    i=Number
    while j<=(Number*2)-1 :
        if j<=Number:
            print(" "*(Number-j)+("*")*((2*j)-1))
            j+=1
        elif j>Number and i>=1:
            print(" "*(Number-i)+("*")*((2*i)-1))
            i-=1
        else :
            j=(Number*2)+1
Number=int(input("Give the Number="))
Diamond(Number)