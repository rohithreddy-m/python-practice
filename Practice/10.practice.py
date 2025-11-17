units=int(input("Give the Uints="))
if units<=500:
    print(f"you units less then 500. you didnot Nide to pay")
elif units<=750:
    print(f"you{(units-500)*3} is you wat pay. ")
elif units<=1000:
    print(f"you {(250)*3+((units-750)*6)} is you want to pay")