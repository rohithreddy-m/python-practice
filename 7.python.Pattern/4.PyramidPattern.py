def Pyramid(Number):
    for i in range(1,Number+1):
        print(" "*(Number-i)+("*")*((2*i)-1))
Number=int(input("Give the Number="))
Pyramid(Number)