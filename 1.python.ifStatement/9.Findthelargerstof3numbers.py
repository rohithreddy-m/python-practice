number1=int(input("Give the first value ="))
number2=int(input("Give the second value ="))
number3=int(input("Give the third value ="))
#if number1>number2:
#   if number1>number3: 
#     print(f"{number1} is largerst Number")
#elif number2>number3:
#    if number2>number1:
#      print(f"{number2} is largerst Number")
#else:
#    print(f"{number3}is largerst Number")
if number1>number2 and number1>number3:
    print(f"{number1} is Largerst Number")
elif number2>number3 and number2>number1:
      print(f"{number2} is Largerst Number")
elif number3>number1 and number3>number2:
    print(f"{number3} is Largerst Number")