Number1=int(input("Give the Frist Number="))
Number2=int(input("Give the Second Number="))
Count=0
Num1=1
Num2=1
if Number1==Number2:
    print(f"{Number1} and {Number2} is Equvale.So the LCM is {Number1}")
else :
    while Count<1:
        Malitipul=Number1*Num1       
        if  Malitipul%Number2==0:
            print(f"The LCM of {Number1} and {Number2} = {Malitipul}")
            Count=1
        Num1+=1
        