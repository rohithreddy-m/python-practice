Num1=int(input("Give the first number="))
Num2=int(input("Give the second number="))
if Num1>Num2 :
    if Num1%Num2==0 :
      print(f"{Num1} is Divisible by {Num2}.")
    else :
      print(f"{Num1} is Not Divisible by {Num2}.")
elif Num2>Num1 :
    if Num2%Num1==0 :
        print(f"{Num2} is Divisible by {Num1}")
    else:
        print(f"{Num2} is Not Divisible by {Num1}")
elif Num1==Num2:
    print("Both Numbers are same ")