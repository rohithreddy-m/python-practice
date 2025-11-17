Number=int(input("Give the Income="))
if Number <= 250000:
    print("You Don't want to pay")
elif Number <= 500000:
    print(f"You Want to Pay={(5/100)*(Number-250000):.2f}")
elif Number <= 1000000:
    print(f"You Want to Pay={((5/100)*(250000))+((20/100)*(Number-500000)):.2f}")
else :
    print(f"{((5/100)*(250000))+((20/100)*(500000))+((30/100)*(Number-1000000)):.2f}")